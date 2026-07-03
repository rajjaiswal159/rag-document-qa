from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def home():
    return {"message": "Document QA API is running"}