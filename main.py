# main.py

import os
import fitz  # PyMuPDF
from fastapi import FastAPI, UploadFile, File, HTTPException
from pydantic import BaseModel, Field
from typing import List, Dict, Optional
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title="RAG Chatbot API")

# Load environment variables
from dotenv import load_dotenv
load_dotenv()

# Import RAGChatbot
from gemini_rag_chatbot import RAGChatbot

# Get API key
api_key = os.getenv("GOOGLE_API_KEY")
if not api_key:
    raise ValueError("GOOGLE_API_KEY not found. Make sure it's set in your .env file.")

# Initialize chatbot
print("Initializing RAG Chatbot...")
chatbot = RAGChatbot(google_api_key=api_key)
print("Chatbot initialized successfully.")

# Add CORS middleware BEFORE defining routes
#app.add_middleware(
#    CORSMiddleware,
 #   allow_origins=["*"],  # Allow all origins for development
  #  allow_credentials=True,
   # allow_methods=["*"],
    #allow_headers=["*"],
#)

# Pydantic Models
class QueryRequest(BaseModel):
    query: str = Field(..., examples=["What is Project Nautilus?"])

class RetrievedDoc(BaseModel):
    content: str
    metadata: Dict
    distance: float
    id: str

class QueryResponse(BaseModel):
    query: str
    answer: str  # Changed from 'response' to 'answer' to match frontend
    retrieved_docs: List[RetrievedDoc]

# API Endpoints
@app.get("/")
async def read_root():
    """Health check endpoint."""
    return {"status": "API is running"}

@app.post("/upload")  # Changed from /add-file to /upload
async def upload_files(files: List[UploadFile] = File(...)):
    """
    Upload multiple files and add them to the knowledge base.
    """
    uploaded_files = []
    errors = []
    
    for file in files:
        if not (file.filename.lower().endswith('.pdf') or file.filename.lower().endswith('.txt')):
            errors.append(f"{file.filename}: Unsupported file type")
            continue
        
        try:
            file_bytes = await file.read()
            
            if file.filename.lower().endswith('.pdf'):
                doc = fitz.open(stream=file_bytes, filetype="pdf")
                full_text = "".join(page.get_text() for page in doc)
                doc.close()
                content_source = full_text
            else:  # .txt file
                content_source = file_bytes.decode('utf-8')
            
            if not content_source.strip():
                errors.append(f"{file.filename}: No text content found")
                continue
                
            doc_id = chatbot.add_document(content_source, metadata={'source_file': file.filename})
            uploaded_files.append({"filename": file.filename, "document_id": doc_id})
        
        except Exception as e:
            errors.append(f"{file.filename}: {str(e)}")
    
    if not uploaded_files and errors:
        raise HTTPException(status_code=400, detail="; ".join(errors))
    
    return {
        "message": f"Successfully uploaded {len(uploaded_files)} file(s)",
        "uploaded_files": uploaded_files,
        "errors": errors if errors else None
    }

@app.post("/query", response_model=QueryResponse)  # Changed from /chat to /query
async def query_documents(request: QueryRequest):
    """
    Query the knowledge base with a question.
    """
    if not request.query.strip():
        raise HTTPException(status_code=400, detail="Query cannot be empty.")
    
    try:
        result = chatbot.chat(request.query)
        # Ensure the response has 'answer' key instead of 'response'
        return {
            "query": result.get("query", request.query),
            "answer": result.get("response", result.get("answer", "")),
            "retrieved_docs": result.get("retrieved_docs", [])
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error: {str(e)}")

@app.get("/stats")
async def get_stats():
    """Get knowledge base statistics."""
    return chatbot.get_collection_stats()