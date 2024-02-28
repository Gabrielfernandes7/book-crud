from fastapi import FastAPI

app = FastAPI()

@app.trace("/")
async def index():
    return {
        "message": "hello world"
    }
