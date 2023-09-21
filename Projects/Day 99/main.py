from fastapi import FastAPI
from typing import Optional
from pydantic import BaseModel
import uvicorn 

app = FastAPI()


@app.get('/blog')
def index(limit : Optional[int] = 10, published : Optional[bool] = False, sort : Optional[str] = None):
    if published:
        return {'data':f'{limit} published blogs from Data Base'}
    else:
        return {'data':f'{limit} blogs from Data Base'}


@app.get('/blog/unpublished')
def unpublished():
    return {"data": "all unpublished blog"}

@app.get('/blog/{id}')
def show(id: int):
    return {'data':id}


@app.get('/blog/{id}/comments')
def comments(id: int):
    return {'data': {'comments' : {'other'}}}

class Blog(BaseModel):
    title : str
    body : str
    published : Optional[bool]

@app.post('/blog')
def create_blog(requset : Blog):
    return {'data': f"Blog is created with {requset.title} as TITLE and {requset.body} as BODY"}


if __name__ == '__main__':
    uvicorn.run(app, host="127.0.0.1", port=9000)