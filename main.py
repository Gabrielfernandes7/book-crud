import uvicorn
from fastapi import FastAPI
from app import model

app = FastAPI()

if __name__ == "__main__":
    uvicorn.run(app)