from fastapi import FastAPI
from typing import Optional

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


@app.post('/blog')
def create_blog():
    return {'data': "Blog is created"}