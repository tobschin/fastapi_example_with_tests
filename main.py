from fastapi import FastAPI

app = FastAPI()

from pydantic import BaseModel

class Foo(BaseModel):
    val1: str
    val2: list
@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}

@app.post("/")
async def post(foo: Foo):
    return {
    "val1" : foo.val1.upper(),
    "val2" : list(map(lambda x: str.upper(x), foo.val2))
    }

