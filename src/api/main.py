from fastapi import FastAPI

app = FastAPI(title="AI Personal Finance Manager")

@app.get("/")
def home():
    return {"message": "AI Personal Finance Manager API is running"}
