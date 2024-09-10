from fastapi import FastAPI, Query, Path, Body
from enum import Enum
from typing import Optional, List, Set,Dict
from pydantic import BaseModel, Field, HttpUrl

app=FastAPI()

# class Item(BaseModel):
#     name: str
#     # num: int
#     desc: str or None = Field(None, title="Desciption", max_length=100)
#     price: int or None = Field(..., gt=0, description="price")
#     tax: int or None = None

# @app.put("/items/{item_id}")
# async def update_item(item_id: int, item :Item=Body()):
#     results = {"item_id": item_id, "item": item}
#     return results

class Image(BaseModel):
    name: str
    # url: str = Field(..., pattern="^www")
    url: HttpUrl

class Item(BaseModel):
    name:str or None
    desc: str or None
    price: int or None = Field(..., gt=0, description="price")
    tax: int or None = None
    # tags: List[str]=["sdlk"]
    tags: Set[str]=set(["sdlk", "sdlk", "sdlk"])
    # image: Image or None
    image: List[Image] or None


@app.put("/items/{item_id}")
async def update_item(*, item_id: int, item :Item):
    results = {"item_id": item_id, "item": item}
    return results


class Offer(BaseModel):
    name: str
    description: str or None = None
    price: float
    items: List[Item]

@app.post("/offers")
async def create_offer(offer: Offer = Body(..., embed=True)):
    return offer


@app.post("/images/multiple")
async def create_multiple_images(images: List[Image]):
    return images


@app.post("/blah")
# async def create_some_blahs(blahs: Dict[str, float]):
async def create_some_blahs(blahs: Dict[int, float]):
    return blahs