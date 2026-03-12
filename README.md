
# 🍎 VisionTeacher AI – GitLab Developer Copilot

**VisionTeacher AI** is an AI-powered assistant for learning programming and analyzing software projects.

By combining **Google Gemini AI** with **GitLab repositories**, the system analyzes code, explains errors, and generates structured GitLab issues to guide debugging and learning.

The goal of the project is to transform raw code errors into **clear, structured development tasks**.

---

# 🚀 Project Goal

Many beginner developers struggle with:

- understanding programming errors  
- debugging complex code  
- organizing tasks when fixing problems  

VisionTeacher AI helps solve this by turning code analysis into **structured actionable steps**, making debugging easier to understand and follow.

---

# ✨ Core Features

## 🔍 GitLab Repository Intelligence

The system connects to GitLab repositories and analyzes project structure using the **GitLab REST API**.

It can inspect:

- repository structure  
- file organization  
- project architecture  

---

## 📸 Multimodal Code Analysis

Users can upload:

- code screenshots  
- error messages  
- text files  
- PDF documents  

Gemini AI analyzes the content and explains the issue.

---

## 🤖 Gemini AI Engine

VisionTeacher AI uses **Google Gemini Flash models** for:

- code reasoning  
- debugging explanations  
- structured improvement suggestions  

---

## 📋 Automatic Issue Generator

The system converts analysis results into **GitLab-style issue checklists**.

Example output:

- [ ] Fix syntax error in `main.py`  
- [ ] Add error handling for API requests  
- [ ] Improve variable naming  
- [ ] Refactor duplicated logic  

This helps transform debugging into a **step-by-step development workflow**.

---

## ⚡ FastAPI Backend

The backend is built using **FastAPI**, providing:

- asynchronous request handling  
- fast API responses  
- lightweight architecture  

---

# 🔄 How It Works

1️⃣ User submits:

- code snippet  
- screenshot  
- file  
- or GitLab repository URL  

2️⃣ Backend processes the input.

3️⃣ Repository structure is fetched from GitLab (if provided).

4️⃣ Gemini AI analyzes the content.

5️⃣ The system generates structured suggestions and improvement tasks.

---

# 🛠 Tech Stack

**Language**

Python 3.10+

**AI Engine**

Google Gemini API (`google-genai`)

**Framework**

FastAPI

**Integration**

GitLab REST API

**Environment**

`.env` secure environment variables

---

# 📂 Project Structure

```
VisionTeacher-AI
│
├── assets
│   └── visionteacher-demo.png
│
├── backend
│   ├── main.py
│   ├── prompts.py
│   ├── gitlab_utils.py
│   └── requirements.txt
│
├── frontend
│   └── index.html
│
├── .env.example
└── README.md
```

---

# 📥 Installation

## 1️⃣ Clone the repository

```bash
git clone https://github.com/InfoSchoolUz/VisionTeacher-AI.git
cd VisionTeacher-AI
```

---

## 2️⃣ Install dependencies

```bash
pip install -r backend/requirements.txt
```

---

## 3️⃣ Configure environment variables

Create a `.env` file in the root directory.

```
GEMINI_API_KEY=your_gemini_api_key
GITLAB_TOKEN=your_gitlab_token
MODEL_ID=gemini-2.5-flash
```

---

## 4️⃣ Run the backend server

```bash
cd backend
uvicorn main:app --reload
```

Server will start at:

```
http://127.0.0.1:8000
```

---

# 📖 API Endpoints

## GET /health

Checks system and model status.

Example response:

```
{
  "ok": true,
  "model": "gemini-2.5-flash"
}
```

---

## POST /analyze

Submits data for AI analysis.

Supported inputs:

- text  
- code files  
- screenshots  
- GitLab repository URLs  

---

# 📸 Demo

<p align="center">
  <img src="assets/visionteacher-demo.png" width="900">
</p>

---

# 🌍 Future Improvements

Possible future enhancements:

- real-time AI coding assistant  
- voice explanations for code errors  
- automated learning exercises  
- deeper GitLab project integration  

VisionTeacher AI explores how AI tools can improve programming workflows and learning experiences.
