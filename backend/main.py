import os
import requests
from fastapi import FastAPI, File, Form, UploadFile
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from dotenv import load_dotenv
from google import genai
from google.genai import types

from prompts import SYSTEM_PROMPT, build_user_prompt

load_dotenv()

app = FastAPI(title="VisionTeacher AI for GitLab Hackathon")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ENV variables
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY", "")
GITLAB_TOKEN = os.getenv("GITLAB_TOKEN", "")
MODEL_ID = os.getenv("MODEL_ID", "gemini-2.5-flash")

client = genai.Client(api_key=GEMINI_API_KEY)


# -----------------------------
# HEALTH CHECK
# -----------------------------
@app.get("/health")
def health():
    return {"ok": True, "model": MODEL_ID}


# -----------------------------
# GITLAB REPO ANALYZER
# -----------------------------
def get_gitlab_repo_files(project_path):
    url = f"https://gitlab.com/api/v4/projects/{project_path}/repository/tree"

    headers = {
        "PRIVATE-TOKEN": GITLAB_TOKEN
    }

    r = requests.get(url, headers=headers)

    if r.status_code != 200:
        return []

    return r.json()


# -----------------------------
# MAIN ANALYSIS ENDPOINT
# -----------------------------
@app.post("/analyze")
async def analyze(
    task: str = Form(...),
    user_text: str = Form(""),
    repo_url: str = Form(""),
    file: UploadFile | None = File(default=None),
):
    try:

        parts = [
            types.Part.from_text(text=SYSTEM_PROMPT),
            types.Part.from_text(text=build_user_prompt(task, user_text)),
        ]

        # FILE ANALYSIS
        if file is not None:
            content = await file.read()
            mime_type = file.content_type or "application/octet-stream"

            if mime_type.startswith("text/"):
                decoded = content.decode("utf-8", errors="ignore")
                parts.append(types.Part.from_text(text=decoded))
            else:
                parts.append(
                    types.Part.from_bytes(
                        data=content,
                        mime_type=mime_type,
                    )
                )

        # GITLAB REPO ANALYSIS
        if repo_url:
            project_path = repo_url.replace("https://gitlab.com/", "").replace("/", "%2F")
            repo_files = get_gitlab_repo_files(project_path)

            parts.append(
                types.Part.from_text(
                    text=f"GitLab repository structure:\n{repo_files}"
                )
            )

        # GEMINI REQUEST
        response = client.models.generate_content(
            model=MODEL_ID,
            contents=[types.Content(role="user", parts=parts)],
        )

        text = response.text if hasattr(response, "text") else "No response text returned."

        return JSONResponse({"ok": True, "result": text})

    except Exception as e:
        return JSONResponse({"ok": False, "error": str(e)}, status_code=500)