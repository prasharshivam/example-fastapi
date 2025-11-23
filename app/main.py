from typing import Optional, List
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from random import randrange
from . import models, schemas , utils
from .database import engine, get_db
from .routers import post, user,auth, vote
from .config import settings







# models.Base.metadata.create_all(bind=engine)

app = FastAPI()
origins = ["https://www.google.com","https://www.youtube.com","http://localhost","http://localhost:8000"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)




##moving this database connection code to database.py as this is no more required here, since we are using sqlalchemy ORM now    

# while True:
#     try:
#         conn = psycopg2.connect(host='localhost', database='fastapi', user='postgres', password='Shivambharti@123', cursor_factory=RealDictCursor)
#         cursor = conn.cursor()
#         print("Database connection was successful")
#         break
#     except Exception as error:
#         print("Connecting to database failed")
#         print("Error:", error)
#         time.sleep(2)

# my_posts = [{"title": "title of post 1", "content": "content of post 1", "id": 1},
#             {"Networth": "over 5 Trillion", "content": "I am the wealthiest person  ", "id": 2}]

# def find_post(id: int):
#     for p in my_posts:
#         if p['id'] == id:
#             return p

# def find_index_post(id: int):
#     for i, p in enumerate(my_posts):
#         if p['id'] == id:
#             return i

app.include_router(post.router)
app.include_router(user.router)
app.include_router(auth.router)
app.include_router(vote.router)


@app.get("/")
async def root():
    return {"data": "Welcome to my API!!!"}

    

