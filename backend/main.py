from fastapi import FastAPI
from typing import List
from starlette.middleware.cors import CORSMiddleware
from db import session
from model import UserTable

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/api/hoge")
def index():
    return {"message": "hoge"}

@app.get("/users")
def read_users():
    users = session.query(UserTable).all()
    return users
