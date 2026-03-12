const analyzeBtn = document.getElementById("analyzeBtn");
const resultEl = document.getElementById("result");

analyzeBtn.addEventListener("click", async () => {
  const task = document.getElementById("task").value;
  const userText = document.getElementById("userText").value;
  const repoUrl = document.getElementById("repoUrl").value.trim();
  const fileInput = document.getElementById("fileInput");

  const formData = new FormData();
  formData.append("task", task);
  formData.append("user_text", userText);
  formData.append("repo_url", repoUrl);

  if (fileInput.files.length > 0) {
    formData.append("file", fileInput.files[0]);
  }

  resultEl.textContent = "Loading...";

  try {
    const res = await fetch("http://127.0.0.1:8000/analyze", {
      method: "POST",
      body: formData,
    });

    const data = await res.json();

    if (!data.ok) {
      resultEl.textContent = `Error: ${data.error}`;
      return;
    }

    resultEl.textContent = data.result;
  } catch (err) {
    resultEl.textContent = `Connection error: ${err.message}`;
  }
});