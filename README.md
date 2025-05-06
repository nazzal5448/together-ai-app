# 🖼️ Together AI FastAPI Image Generation Service

This is a lightweight FastAPI-based microservice for generating AI-powered images using [Together AI](https://www.together.ai/) models. It's designed to integrate seamlessly with automated content workflows such as [n8n](https://n8n.io/) and is currently deployed on [Render](https://render.com).

## 🔧 Features

- Accepts text prompts via a POST API endpoint.
- Generates base64-encoded images using Together AI.
- Optimized for integration with n8n automation workflows.
- FastAPI + `uvicorn` for quick, lightweight deployment.

## 🚀 Use Case

This service powers the **image generation step** of a fully automated content creation pipeline in n8n. The workflow:

1. Researches trending topics using LLMs.
2. Writes social media posts for LinkedIn, Facebook, and X.
3. **Calls this FastAPI service to generate platform-specific images.**
4. Publishes the content automatically.

> 💡 The entire process is free and hands-off — ideal for solo creators and marketing teams.

## 🛠️ Tech Stack

- **FastAPI** – API framework.
- **Uvicorn** – ASGI server.
- **Together AI API** – For diffusion model-based image generation.
- **Render** – Deployment platform.

## 📦 Installation

Make sure you have Python 3.8+ installed.

```bash
git clone https://github.com/nazzal5448/together-ai-app.git
cd together-ai-app
pip install -r requirements.txt
````

## 🧪 Running Locally

```bash
uvicorn main:app --host 0.0.0.0 --port 8000 --reload
```

## 📝 Example API Request

**Endpoint:** `POST /generate-images`

**Request JSON:**

```json
{
  "prompt": "a futuristic robot working in a lush green office"
}
```

**Response:**

```json
{
  "b64_json": "<base64_encoded_image>"
}
```

## 🌐 Deployment (Render)

This app is deployed as a **web service** on [Render](https://render.com). Render handles deployment directly from GitHub, so any pushes to `main` trigger a redeploy.

## 🔐 Environment Variables

Set the following environment variable either locally or on Render:

* `TOGETHER_API_KEY` – Your Together AI API key.

## 📄 License

MIT – Free to use and modify.

---

### ✨ Credits

Developed by [Nazzal](https://nazzalkausar.com) as part of an automated AI content creation project using n8n, Groq LLMs, and Together AI.


