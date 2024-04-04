"main.py"

import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from core_api.routers import expenses, accounts

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(expenses.router)
app.include_router(accounts.router)


if __name__ == "__main__":
    uvicorn.run(
        "__main__:app",
        host="127.0.0.1",
        port=8000,
        reload=True,
    )
