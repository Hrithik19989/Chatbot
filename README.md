===============================================================================
                        RAG DOCUMENT Q&A SYSTEM
===============================================================================

A smart chatbot that reads your PDF documents and answers questions about them
using AI technology. Simply upload your documents and start asking questions!

===============================================================================
                             WHAT IT DOES
===============================================================================

This application helps you:
  - Upload PDF documents to create a knowledge base
  - Ask questions about the content in your documents
  - Get accurate AI-powered answers instantly
  - Handle multiple documents at once
  - Search through large amounts of text quickly

Perfect for: Research papers, company documents, manuals, books, reports

===============================================================================
                          WHAT YOU'LL NEED
===============================================================================

Before starting, make sure you have:
  1. Python 3.8 or newer installed on your computer
  2. A Google API Key (free to get - instructions below)
  3. A modern web browser (Chrome, Firefox, Safari, Edge)
  4. About 500MB of free disk space

===============================================================================
                        GETTING STARTED
===============================================================================

STEP 1: Download the Project
-----------------------------
  - Download or clone this project to your computer
  - Unzip it to a folder you can easily find
  - Open a terminal/command prompt in that folder

STEP 2: Set Up Python Environment
----------------------------------
  Windows users:
    python -m venv venv
    venv\Scripts\activate

  Mac/Linux users:
    python3 -m venv venv
    source venv/bin/activate

  You should see (venv) appear at the start of your terminal line

STEP 3: Install Required Software
----------------------------------
  Run this command:
    pip install -r requirements.txt

  This will install all necessary components (takes 2-5 minutes)

STEP 4: Get Your Google API Key
--------------------------------
  1. Visit: https://makersuite.google.com/app/apikey
  2. Sign in with your Google account
  3. Click the "Create API Key" button
  4. Copy the key that appears

STEP 5: Configure Your API Key
-------------------------------
  1. Create a new file named: .env
  2. Put it in the main project folder
  3. Add this line to the file:
     GOOGLE_API_KEY=paste_your_key_here
  4. Save and close the file

  Important: Keep this key private! Never share it online.

===============================================================================
                         RUNNING THE APPLICATION
===============================================================================

You need to start TWO servers - one for the backend, one for the frontend

TERMINAL 1 - Start the Backend Server
--------------------------------------
  1. Open a terminal in the project folder
  2. Activate your virtual environment (see Step 2 above)
  3. Run this command:
     uvicorn main:app --reload --host 0.0.0.0 --port 8000

  You should see:
     "Application startup complete"
     "Uvicorn running on http://0.0.0.0:8000"

TERMINAL 2 - Start the Frontend Server
---------------------------------------
  1. Open a NEW terminal window
  2. Go to the frontend folder:
     cd frontend
  3. Run this command:
     python -m http.server 8080

  You should see:
     "Serving HTTP on :: port 8080"

OPEN YOUR BROWSER
-----------------
  Go to: http://localhost:8080

  You should see the RAG Document Q&A interface!

===============================================================================
                         HOW TO USE THE APP
===============================================================================

UPLOADING DOCUMENTS
-------------------
  1. Look for the "Upload Documents" section
  2. Either:
     - Drag and drop PDF files into the box, OR
     - Click "Browse Files" and select PDFs
  3. Click "Upload & Process Documents"
  4. Wait for the success message

  Supported files: PDF only
  File size: Up to 10MB recommended

ASKING QUESTIONS
----------------
  1. Type your question in the "Ask Questions" text box
  2. Click "Ask Question" or press Enter
  3. Wait a few seconds for the AI to process
  4. Read the answer in the "Response" section

  Tips for better answers:
    - Be specific in your questions
    - Ask one question at a time
    - Reference document topics directly
    - Use complete sentences

EXAMPLE QUESTIONS
-----------------
  "What is the main topic of this document?"
  "Summarize the key findings in chapter 3"
  "What are the recommendations mentioned?"
  "Explain the methodology used in the study"

===============================================================================
                        PROJECT FILE STRUCTURE
===============================================================================

Your project folder contains:

chatbot/
  |
  |-- main.py                    (Backend server code)
  |-- gemini_rag_chatbot.py      (AI chatbot logic)
  |-- requirements.txt           (List of required software)
  |-- .env                       (Your API key - create this)
  |-- README.md                  (This file)
  |
  |-- frontend/
      |-- index.html             (Web interface)

DEPLOYING TO THE INTERNET
Want to make your app accessible online? Deploy it to Render for FREE!
WHAT YOU'LL NEED

GitHub account (free)
Render account (free, no credit card needed)
Your project code pushed to GitHub
About 30-45 minutes

STEP 1: Prepare Your Project Files
Create these new files in your main project folder:

Create "runtime.txt":
python-3.11.0
Create "Procfile" (no file extension):
web: uvicorn main:app --host 0.0.0.0 --port $PORT
Add to end of "requirements.txt":
gunicorn==21.2.0
Create ".gitignore":
pycache/
*.py[cod]
venv/
.env
.venv
*.log
chromadb/

STEP 2: Update Code for Production
Update main.py - Find the CORS section and replace with:
import os
FRONTEND_URL = os.getenv("FRONTEND_URL", "*")
app.add_middleware(
CORSMiddleware,
allow_origins=[""] if FRONTEND_URL == "" else [FRONTEND_URL],
allow_credentials=True,
allow_methods=["GET", "POST", "PUT", "DELETE", "OPTIONS"],
allow_headers=[""],
expose_headers=[""]
)
Update frontend/index.html - Find this line:
const API_BASE_URL = 'http://localhost:8000';
Replace with:
const API_BASE_URL = window.location.hostname === 'localhost'
? 'http://localhost:8000'
: 'https://YOUR-BACKEND-URL.onrender.com';
STEP 3: Push to GitHub
Install Git if needed: https://git-scm.com/downloads
Run these commands in your project folder:
git init
git add .
git commit -m "Prepare for deployment"
Create repository on GitHub:

Go to https://github.com
Click "+" → "New repository"
Name: rag-chatbot
Keep it Public
Click "Create repository"

Push your code:
git remote add origin https://github.com/YOUR_USERNAME/rag-chatbot.git
git branch -M main
git push -u origin main
STEP 4: Deploy Backend to Render
Create Render account:

Visit: https://render.com
Sign up with GitHub (easiest)
Verify your email

Deploy backend:

Click "New +" → "Web Service"
Connect to GitHub and select your repository
Configure:
Name: rag-chatbot-backend
Region: Choose closest to you
Branch: main
Runtime: Python 3
Build Command: pip install -r requirements.txt
Start Command: uvicorn main:app --host 0.0.0.0 --port $PORT
Instance Type: Free
Add Environment Variables:
GOOGLE_API_KEY = your_actual_api_key
FRONTEND_URL = *
PYTHON_VERSION = 3.11.0
Click "Create Web Service"
Wait 5-10 minutes for deployment
Copy your backend URL (like: https://rag-chatbot-backend.onrender.com)

Test backend:
Visit: https://your-backend-url.onrender.com
Should see: {"status": "API is running"}
STEP 5: Deploy Frontend to Render
Update frontend code with backend URL:

Edit frontend/index.html
Replace YOUR-BACKEND-URL with actual URL from Step 4
Save file

Push changes:
git add frontend/index.html
git commit -m "Add production backend URL"
git push
Deploy frontend:

In Render dashboard, click "New +" → "Static Site"
Select same GitHub repository
Configure:
Name: rag-chatbot-frontend
Branch: main
Root Directory: (leave blank)
Build Command: (leave blank)
Publish Directory: ./frontend
Click "Create Static Site"
Wait 2-3 minutes
Copy your frontend URL

Update backend CORS:

Go to backend service in Render
Click "Environment"
Update FRONTEND_URL to your frontend URL
Save (backend will auto-redeploy)

STEP 6: Test Your Deployed App
Visit your frontend URL and test:
✓ Page loads correctly
✓ Upload a small PDF
✓ Ask a question
✓ Verify answer appears
Check browser console (F12) for any errors
IMPORTANT NOTES FOR DEPLOYED APP
Cold Starts:

Free Render services sleep after 15 minutes of inactivity
First request after sleep takes 30-60 seconds to wake up
Subsequent requests are fast
This is normal for free tier

Limitations:

750 hours per month (enough for one service always running)
512 MB RAM
Services may be slower than local
Large PDFs may timeout

If Something Goes Wrong:

Check Render logs: Service → Logs tab
Verify environment variables are set correctly
Check CORS settings match frontend URL
Ensure backend shows "Live" status

UPGRADING TO PAID (Optional)
If you need:

No cold starts (instant responses)
More memory for large PDFs
Faster processing
Higher reliability

Consider Render paid plan ($7/month):

Always-on service
2GB RAM
Better performance

YOUR DEPLOYED URLS
After deployment, save these:
Backend API:  https://.onrender.com
Frontend App: https://.onrender.com
Share your frontend URL with anyone to let them use your app!
===============================================================================
FUTURE IMPROVEMENTS
Planned features:

Support for Word documents and text files
Multiple language support
Conversation history
Document management (delete, view uploaded docs)
Export answers to PDF
User authentication
Advanced search filters
Custom domain support
Usage analytics

===============================================================================
                          TROUBLESHOOTING
===============================================================================

PROBLEM: Backend won't start
-----------------------------
  Check these:
    - Is port 8000 already in use? Close other apps.
    - Is your API key correctly set in the .env file?
    - Did all packages install? Run: pip install -r requirements.txt again
    - Check for error messages in the terminal

PROBLEM: Frontend shows blank page
-----------------------------------
  Try this:
    - Make sure backend is running first (Terminal 1)
    - Check you're using: http://localhost:8080
    - Try a different browser
    - Check browser console (F12) for error messages

PROBLEM: "Connection refused" error
------------------------------------
  Solutions:
    - Verify backend is running on port 8000
    - Visit http://localhost:8000 directly to test backend
    - Restart both servers
    - Check your firewall isn't blocking localhost

PROBLEM: File upload fails
---------------------------
  Check:
    - File is a PDF (not Word doc or image)
    - File isn't corrupted - try opening it first
    - File size isn't too large (under 10MB is best)
    - PDF contains actual text (not just scanned images)

PROBLEM: No answer appears
---------------------------
  Possible causes:
    - Documents weren't uploaded successfully - try again
    - Your Google API key has no remaining quota
    - Question is too vague - be more specific
    - Check backend terminal for error messages

PROBLEM: "Rate limit exceeded"
-------------------------------
  What to do:
    - Wait a few minutes before trying again
    - You've made too many requests too quickly
    - Free API keys have usage limits per minute

===============================================================================
                        TECHNICAL DETAILS
===============================================================================

HOW IT WORKS
------------
  1. You upload a PDF document
  2. The system extracts all text from the PDF
  3. Text is split into smaller chunks
  4. Each chunk is converted to a "vector" (numerical representation)
  5. Vectors are stored in a database
  6. When you ask a question:
     - Your question is also converted to a vector
     - System finds most relevant document chunks
     - AI generates an answer using those chunks

TECHNOLOGIES USED
-----------------
  Backend:
    - FastAPI: Web server framework
    - Google Gemini: AI language model
    - ChromaDB: Vector database for storing documents
    - PyMuPDF: PDF text extraction tool

  Frontend:
    - HTML: Page structure
    - CSS: Styling and design
    - JavaScript: Interactive features

API ENDPOINTS
-------------
  GET  /           - Check if server is running
  POST /upload     - Upload PDF documents
  POST /query      - Ask a question
  GET  /stats      - View database statistics

===============================================================================
                      SAFETY AND SECURITY
===============================================================================

IMPORTANT SECURITY NOTES
------------------------
  1. Never share your .env file or API key publicly
  2. Don't commit .env to GitHub or version control
  3. Current setup allows ALL websites to connect (development only)
  4. For production use:
     - Restrict CORS to specific domains
     - Add user authentication
     - Use HTTPS instead of HTTP
     - Set up proper rate limiting

DATA PRIVACY
------------
  - Your documents are processed locally on your computer
  - Only text content is sent to Google for AI processing
  - Documents are stored in your local database
  - No data is shared with third parties

===============================================================================
                         GETTING HELP
===============================================================================

If you're stuck:
  1. Read this README carefully
  2. Check the Troubleshooting section above
  3. Look at error messages in your terminal
  4. Search for the error message online
  5. Open an issue on GitHub with:
     - What you were trying to do
     - What error you got
     - Your operating system
     - Python version

===============================================================================
                        FUTURE IMPROVEMENTS
===============================================================================

Planned features:
  - Support for Word documents and text files
  - Multiple language support
  - Conversation history
  - Document management (delete, view uploaded docs)
  - Export answers to PDF
  - User authentication
  - Advanced search filters

===============================================================================
                            LICENSE
===============================================================================

MIT License - Free to use, modify, and distribute

===============================================================================
                         CONTRIBUTING
===============================================================================

Want to improve this project?
  - Fork the repository
  - Make your changes
  - Test thoroughly
  - Submit a pull request
  - Describe what you changed and why

===============================================================================

                        Happy Document Chatting!

              Questions? Feedback? Open an issue on GitHub!

===============================================================================

## Performance Considerations

- PDF processing and embedding generation are performed asynchronously
- Batch processing is used for embedding generation and vector storage
- Rate limiting is implemented to prevent API abuse

## Acknowledgements

- [FastAPI](https://fastapi.tiangolo.com/)
- [Google Gemini](https://ai.google.dev/)
- [Pinecone](https://www.pinecone.io/)
- [PyPDF2](https://pypdf2.readthedocs.io/)


# System Architecture

## Overview
This RAG-based chatbot uses a modern tech stack to provide accurate, 
context-aware responses to user queries based on uploaded PDF documents.

## Architecture Diagram

┌─────────────┐
│   User      │
│  (Browser)  │
└──────┬──────┘
       │
       │ HTTPS
       ▼
┌──────────────────┐
│   Frontend       │
│  (HTML/CSS/JS)   │
│  Static Site     │
└──────┬───────────┘
       │
       │ REST API
       ▼
┌──────────────────┐
│   Backend        │
│  FastAPI Server  │
│  Python 3.11     │
└──────┬───────────┘
       │
       ├─────────────┐
       │             │
       ▼             ▼
┌──────────┐   ┌─────────────┐
│ ChromaDB │   │ Google      │
│ Vector   │   │ Gemini API  │
│ Database │   │ (AI Model)  │
└──────────┘   └─────────────┘

## Component Details

### Frontend Layer
- **Technology**: Vanilla HTML, CSS, JavaScript
- **Hosting**: Render Static Site
- **Features**:
  - File upload with drag-and-drop
  - Real-time query interface
  - Response display with formatting
  - Error handling and user feedback

### Backend Layer
- **Framework**: FastAPI
- **Language**: Python 3.11
- **Hosting**: Render Web Service
- **Responsibilities**:
  - PDF text extraction (PyMuPDF)
  - Document chunking
  - API request handling
  - Vector database operations
  - AI model integration

### Vector Database
- **Technology**: ChromaDB
- **Purpose**: Store document embeddings for similarity search
- **Features**:
  - Automatic embedding generation
  - Semantic search
  - Metadata storage

### AI Model
- **Provider**: Google Gemini
- **Model**: gemini-pro (or gemini-1.5-flash)
- **Usage**:
  - Generate embeddings for documents
  - Generate contextual responses
  - Natural language understanding

## Data Flow

### Upload Flow
1. User uploads PDF via frontend
2. Frontend sends file to backend /upload endpoint
3. Backend extracts text using PyMuPDF
4. Text is chunked into smaller segments
5. Gemini API generates embeddings for chunks
6. Embeddings stored in ChromaDB with metadata
7. Success response sent to frontend

### Query Flow
1. User enters question in frontend
2. Frontend sends query to backend /query endpoint
3. Backend generates embedding for query
4. ChromaDB performs similarity search
5. Top relevant chunks retrieved
6. Context + query sent to Gemini API
7. AI generates response using retrieved context
8. Response with sources sent to frontend
9. Frontend displays answer and sources

## Security Measures
- API keys stored in environment variables
- CORS configuration for frontend-backend communication
- Input validation on all endpoints
- HTTPS encryption in production
- No sensitive data in client-side code

## Scalability Considerations
- Stateless backend design
- Vector database for efficient retrieval
- Async operations for better performance
- Rate limiting on API endpoints
- Caching for frequently accessed data

# User Guide - RAG Document Q&A System

## Getting Started

### Accessing the Application
Visit the live application at: [https://chatbot-f.onrender.com/]

The application works on:
- Desktop browsers (Chrome, Firefox, Safari, Edge)
- Mobile browsers (iOS Safari, Android Chrome)
- Tablets

## Features Overview

### 1. Document Upload
Upload PDF documents to create your knowledge base.

**How to Upload:**
1. Look for the "Upload Documents" section on the left
2. Either:
   - **Drag and drop** PDF files into the dashed box
   - Click **"Browse Files"** button to select files
3. You'll see selected files listed below
4. Click **"Upload & Process Documents"**
5. Wait for the green success message

**Tips:**
- Only PDF files are supported
- Maximum file size: 10MB recommended
- Multiple files can be uploaded at once
- Files with selectable text work best (not scanned images)

### 2. Asking Questions
Query your uploaded documents using natural language.

**How to Ask Questions:**
1. Look for the "Ask Questions" section on the right
2. Type your question in the text box
3. Either:
   - Click **"Ask Question"** button
   - Press **Enter** key (Shift+Enter for new line)
4. Wait a few seconds for processing
5. View the answer in the "Response" section below
   
