# 🧩 Task Builder - Full Stack Web App

A simple yet powerful task manager built using **FastAPI** (Python backend) and **HTML/CSS/JavaScript** (frontend). It allows users to add, delete, and view tasks with a clean UI.

---

## 📁 Project Structure

task-builder/
├── backend/
│ ├── main.py
│ ├── models.py
│ ├── database.py
│ ├── schemas.py
│ ├── crud.py
│ └── requirements.txt
└── frontend/
├── index.html
├── style.css
└── script.js

yaml
Copy
Edit

---

## 🔧 Backend Setup (FastAPI + SQLite)

### 1. Navigate to the backend folder
```bash
cd backend
2. Create a virtual environment
bash
Copy
Edit
python -m venv .venv
3. Activate the environment
Windows (PowerShell):

bash
Copy
Edit
.venv\Scripts\Activate.ps1
Linux/macOS:

bash
Copy
Edit
source .venv/bin/activate
4. Install required packages
bash
Copy
Edit
pip install fastapi uvicorn sqlalchemy pydantic
Optional: Save dependencies

bash
Copy
Edit
pip freeze > requirements.txt
5. Run the FastAPI server
bash
Copy
Edit
uvicorn main:app --reload
6. Access your API
http://127.0.0.1:8000

Docs: http://127.0.0.1:8000/docs

🎨 Frontend Setup
1. Open frontend/index.html in your browser
The page includes a responsive UI to:

Add new tasks

View all tasks

Delete tasks

Displays task creation time

🚀 How to Run Everything From Scratch
Clone the repo:

bash
Copy
Edit
git clone https://github.com/your-username/task-builder.git
Setup backend as shown above.

Open the frontend:

bash
Copy
Edit
cd frontend
start index.html
Or right-click and open index.html in any browser.

🌐 API Endpoints
Method	Endpoint	Description
GET	/tasks	Get all tasks
POST	/tasks	Add a new task
DELETE	/tasks/{id}	Delete a task

👤 Author
Srivamsi Magapu
📌 LinkedIn
💻 GitHub

📄 License
This project is open-source and free to use under the MIT License.
