from enum import Enum
from typing import Optional

from fastapi import FastAPI
from pydantic import BaseModel
from pydantic.error_wrappers import flatten_errors


class ModelName(str, Enum):
    title = "title"
    rank = "rank"
    description = "No description"

class Item(BaseModel):
    name: str
    description: Optional[str] = None
    price: float
    tax: Optional[float] = None


app = FastAPI()


@app.get("/movies/{movie_id}")
async def get_movie(movie_id: int):
    return {"movie_id": movie_id}


@app.get("/models/{model_name}")
async def get_something(model_name: ModelName):
    if model_name == ModelName.title:
        return {"model_name": model_name, "message": "it is title"}
    if model_name == ModelName.rank:
        return {"model_name": model_name, "message": "it is rank"}
    if model_name == ModelName.description:
        return {"model_name": model_name, "message": "it is description"}


@app.post("/items/")
async def create_item(item: Item):
    return {"response": item}


@app.post("/new_items/{item_id}")
async def create_new_item(item_id: int, item: Item):
    return {"item_id": item_id, "response": item}
