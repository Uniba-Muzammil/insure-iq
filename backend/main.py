from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api import upload

app = FastAPI(
    title="InsureIQ API",
    description="Insurance Financial Analyzer Backend",
    version="1.0.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(upload.router, prefix="/api/v1", tags=["upload"])

@app.get("/")
def root():
    return {"message": "InsureIQ backend is running"}