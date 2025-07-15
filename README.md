<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0"/>
  <title>Task Builder - Setup Guide</title>
  <style>
    body {
      font-family: Arial, sans-serif;
      background: #f4f6f9;
      color: #333;
      line-height: 1.6;
      padding: 20px;
    }
    .container {
      max-width: 900px;
      margin: auto;
      background: white;
      padding: 30px;
      border-radius: 10px;
      box-shadow: 0 0 20px rgba(0,0,0,0.1);
    }
    h1, h2 {
      color: #2c3e50;
    }
    code, pre {
      background: #eee;
      padding: 5px 10px;
      display: inline-block;
      border-radius: 5px;
      font-family: Consolas, monospace;
    }
    .codeblock {
      background: #272822;
      color: #f8f8f2;
      padding: 15px;
      border-radius: 8px;
      overflow-x: auto;
    }
    button {
      background: #2980b9;
      color: white;
      padding: 10px 16px;
      margin-top: 10px;
      border: none;
      border-radius: 5px;
      cursor: pointer;
    }
    button:hover {
      background: #1e6a8a;
    }
  </style>
</head>
<body>
  <div class="container">
    <h1>📝 Task Builder - Full Stack App</h1>
    <p>A full stack task manager built with FastAPI backend and HTML/CSS/JS frontend.</p>

    <h2>📁 Project Structure</h2>
    <pre class="codeblock">
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
    </pre>

    <h2>🚀 Backend Setup (FastAPI)</h2>
    <ol>
      <li>Open terminal and navigate to <code>backend/</code> folder:</li>
      <pre class="codeblock">cd backend</pre>

      <li>Create a virtual environment:</li>
      <pre class="codeblock">python -m venv .venv</pre>

      <li>Activate the environment (Windows PowerShell):</li>
      <pre class="codeblock">.venv\Scripts\Activate.ps1</pre>

      <li>Install dependencies:</li>
      <pre class="codeblock">pip install fastapi uvicorn sqlalchemy pydantic</pre>

      <li>Run the server:</li>
      <pre class="codeblock">uvicorn main:app --reload</pre>

      <li>Visit <a href="http://127.0.0.1:8000" target="_blank">http://127.0.0.1:8000</a> in your browser.</li>
    </ol>

    <h2>🎨 Frontend Setup</h2>
    <ol>
      <li>Open <code>index.html</code> in a browser.</li>
      <li>Ensure backend is running on <code>http://127.0.0.1:8000</code>.</li>
      <li>Use the interface to add/view/delete tasks.</li>
    </ol>

    <h2>👨‍💻 Author</h2>
    <p><strong>Srivamsi Magapu</strong> — <a href="https://www.linkedin.com/in/srivamsimagapu" target="_blank">LinkedIn Profile</a></p>

    <button onclick="alert('Happy Building! 🎉')">Click to Start!</button>
  </div>
</body>
</html>
