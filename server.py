from fastapi import FastAPI
from constants import *
import uvicorn

app = FastAPI()


@app.get("/")
def load_homepage():
    return {"home_page_contents": HOMEPAGE}


if __name__ == "__main__":
    uvicorn.run("server:app", host="127.0.0.1", port=8000, reload=True)
