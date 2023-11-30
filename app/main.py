from typing import Union

from fastapi import FastAPI

# app.memo, because docker pwd is the parent directory of app directory
from app.memo import memo_router  

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return{"item_id": item_id, "q": q}

# uvicorn uses app, so add the memo_router to app
app.include_router(memo_router)

