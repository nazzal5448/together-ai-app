from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List
from main import generate

app = FastAPI()


origins = [
    "http://localhost",
    "http://localhost:5678"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,  
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Request model
class ImageGenerationRequest(BaseModel):
    prompts: List[str] 

@app.get("/")
def home():
    return {"response": "Together AI FastAPI app is running!"}

@app.post("/generate-images")
def generate_images(request: ImageGenerationRequest):
    try:
        if not request.prompts or len(request.prompts) < 1:
            raise ValueError("At least one prompt is required.")

        images_b64 = generate(request.prompts)

        if not isinstance(images_b64, list) or len(images_b64) != len(request.prompts):
            raise ValueError("Image generation failed or returned incorrect number of images.")

        return {
            "images_b64": images_b64
        }

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Image generation failed: {str(e)}")
