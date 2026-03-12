# VisionTeacher AI

AI Coding Tutor • README Writer • GitLab Task Generator

VisionTeacher AI is an AI-powered developer assistant designed for hackathons and educational use.
It helps developers and students analyze code, generate GitLab issues, understand projects, and improve software quality using Google's Gemini AI.

The application integrates **FastAPI**, **Gemini API**, and **GitLab API** to provide intelligent code analysis and project insights.

---

# Features

### AI Code Analysis

Upload source code or project files and receive explanations, improvements, and bug suggestions.

### GitLab Repository Analysis

Provide a GitLab repository URL and the system will analyze the repository structure.

### GitLab Issue Generator

Automatically generate GitLab issue checklists for improving a project.

### README Generator

Generate structured project documentation automatically.

### Diagram & Image Analysis

Upload diagrams or screenshots and get AI explanations.

---

# How It Works

VisionTeacher AI connects several components:

User Input
↓
FastAPI Backend
↓
GitLab API (repository structure)
↓
Gemini AI Analysis
↓
AI-generated insights and recommendations

The system sends structured prompts to Gemini AI and returns developer-friendly responses.

---

# Tech Stack

Backend

* Python
* FastAPI

AI

* Google Gemini API

Integration

* GitLab API

Frontend

* HTML
* JavaScript
* CSS

---

# Project Structure

visionteacher-ai

backend/

* main.py
* prompts.py
* requirements.txt
* .env

frontend/

* index.html
* app.js
* style.css

README.md

---

# Installation

Clone the repository

```bash
git clone <your-gitlab-repository>
cd visionteacher-ai
```

Install dependencies

```bash
pip install -r backend/requirements.txt
```

Create `.env` file

```
GEMINI_API_KEY=your_gemini_api_key
GITLAB_TOKEN=your_gitlab_token
MODEL_ID=gemini-2.5-flash
```

Run the backend server

```bash
cd backend
python -m uvicorn main:app --reload --port 8000
```

Open the frontend

```
frontend/index.html
```

---

# Usage

Select a task type:

* Bug Fix
* Code Explanation
* Generate GitLab Issues
* Write README
* Analyze Image or Diagram

Then:

1. Enter a question or task
2. Optionally upload a file
3. Optionally provide a GitLab repository URL
4. Click **Analyze**

VisionTeacher AI will return AI-generated insights.

---

# Why VisionTeacher AI

Developers often spend time reviewing code, writing documentation, and organizing issues.

VisionTeacher AI automates these tasks using AI to help:

* Students learn programming faster
* Developers analyze code quicker
* Teams organize GitLab projects better

---

# Future Improvements

* Pull Request AI review
* Full repository code analysis
* Automatic GitLab issue creation
* AI architecture diagram generator

---

# License

MIT License

---

# Author

Azamat Madrimov
Informatics & IT Teacher
Uzbekistan

Built for AI and developer productivity.
