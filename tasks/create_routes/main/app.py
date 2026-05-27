
import os

from fastapi import FastAPI
import uvicorn

app = FastAPI()


@app.post("/")
async def index():
    return "Hello this is home page."


@app.post("/login")
async def login(
    id: str,
    password: str
):
    if id == password:
        return True
    else:
        return False




if __name__ == "__main__":

    uvicorn.run(
        app=app,
        host=os.getenv("APP_HOST", "0.0.0.0"),
        port=int(os.getenv("APP_PORT", "3000")),
    )