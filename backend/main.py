from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    return {"message": "InsureIQ backend is running"}