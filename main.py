from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Welcome to the FastAPI application!"}

@app.get("/health")
def health_check():
    return {"status": "healthy"}

@app.get("/api/v1/users/me")
def get_user():
    return {
        "id": 1,
        "username": "johndoe",
        "email": "abc@ex.com"
    }