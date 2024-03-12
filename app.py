# 1. Importar libreria
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Text, Optional
from datetime import datetime
from uuid import uuid4 as uuid

# 2. Apliccion FastAPI
app = FastAPI()

posts = [
    {
        "title": "Cybersecurity",
        "author": "Kevinn Mitnick",
        "content": "Techniques about hacking"
    },
    {
        "title": "Using FastAPI in python",
        "author": "Unknown",
        "content": "Tutorial about how to use FastAPI"
    },
    {
        "title": "Hello World",
        "author": "Angel",
        "content": "How to make your first program"
    },
    {
        "id": "4",
        "title": "Prueba FastAPI",
        "author": "Angel",
        "content": "Test a new item in the API"
    }
]

# Post Model
class Post(BaseModel):
    id: Optional[str]
    title: str
    author: str
    content: Text
    created_at: datetime = datetime.now()

# 3. Crear Endpoint
@app.get('/')
async def read_root():
    return {'Welcome': 'Welcome to my REST API'}

@app.get('/posts')
async def get_posts():
    return posts

@app.post('/posts')
def save_post(post: Post):
    post.id = str( uuid() )
    posts.append(post.model_dump())
    return posts[-1]

@app.get('/posts/{post_id}')
def get_post(post_id: str):
    for post in posts:
        if post["id"] == post_id:
            return post
    return HTTPException(status_code=404, detail="Post not found")

# 4. Ejecutar la app
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, port=8000)