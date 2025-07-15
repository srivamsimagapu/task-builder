# 📝 Task Builder - Full Stack App

A simple task manager app with FastAPI backend and HTML/CSS/JavaScript frontend.

---

## 🔧 Project Setup Instructions

### Backend (FastAPI)

1. **Navigate to backend folder:**
   ```bash
   cd backend
Create a virtual environment:

bash
Copy
Edit
python -m venv .venv
Activate the virtual environment:

Windows (PowerShell):

bash
Copy
Edit
.\.venv\Scripts\Activate.ps1
Install dependencies:

bash
Copy
Edit
pip install fastapi uvicorn sqlalchemy pydantic
Run the FastAPI server:

bash
Copy
Edit
uvicorn main:app --reload
Access the API at: http://127.0.0.1:8000

Frontend
Open index.html in a browser.

The app connects to the backend at http://127.0.0.1:8000 for CRUD operations.

📁 Project Structure
pgsql
Copy
Edit
task-builder/
├── backend/
│   ├── main.py
│   ├── models.py
│   ├── database.py
│   ├── schemas.py
│   ├── crud.py
│   └── .venv/
└── frontend/
    ├── index.html
    ├── style.css
    └── script.js
📦 Features
Add / View / Delete tasks

Backend API with FastAPI + SQLite

Frontend with HTML/CSS/JS

🧠 Author
Srivamsi Magapu – LinkedIn

vbnet
Copy
Edit
