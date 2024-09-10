from fastapi import FastAPI, Query, Path, Body
from enum import Enum
from typing import Optional, List, Set, Dict
from pydantic import BaseModel, Field, HttpUrl

app = FastAPI()

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

# class Image(BaseModel):
#     name: str
#     # url: str = Field(..., pattern="^www")
#     url: HttpUrl

# class Item(BaseModel):
#     name:str or None
#     desc: str or None
#     price: int or None = Field(..., gt=0, description="price")
#     tax: int or None = None
#     # tags: List[str]=["sdlk"]
#     tags: Set[str]=set(["sdlk", "sdlk", "sdlk"])
#     # image: Image or None
#     image: List[Image] or None


# @app.put("/items/{item_id}")
# async def update_item(*, item_id: int, item :Item):
#     results = {"item_id": item_id, "item": item}
#     return results


# class Offer(BaseModel):
#     name: str
#     description: str or None = None
#     price: float
#     items: List[Item]

# @app.post("/offers")
# async def create_offer(offer: Offer = Body(..., embed=True)):
#     return offer


# @app.post("/images/multiple")
# async def create_multiple_images(images: List[Image]):
#     return images


# @app.post("/blah")
# # async def create_some_blahs(blahs: Dict[str, float]):
# async def create_some_blahs(blahs: Dict[int, float]):
#     return blahs

# class Item(BaseModel):
#     name: str
#     desc: str or None = None
#     price: float or None = None
#     tax: float or None

#     class Config:
#         schema_extra ={
#             "example":{
#                 "name": "Foo",
#                 "desc": "nice desc",
#                 "price": 90.0,
#                 "tax": 12.2
#             }
#         }


class Item(BaseModel):
    name: str = Field(None)
    description: str = Field(None)
    price: float = Field(0)
    tax: float = Field(0)

    class Config:
        json_schema_extra = {
            "example": {
                "name": "Foo",
                "description": "A very nice Item",
                "price": 16.25,
                "tax": 1.67,
            }
        }


@app.put("/items/{item_id}")
async def update_item(
    item_id: int,
    item: Item,
    # item: Item = Body(
    #     ...,
    #     # example={"name": "foo", "desc": "nice desc", "price": 10, "tax": 20},
    #     examples={
    #         "normal": {
    #             "summary": "A normal example",
    #             "description": "A __normal__ item works _correctly_",
    #             "value": {
    #                 "name": "Foo",
    #                 "description": "A very nice Item",
    #                 "price": 16.25,
    #                 "tax": 1.67,
    #             },
    #         },
    #         "converted": {
    #             "summary": "An example with converted data",
    #             "description": "FastAPI can convert price `strings` to actual `numbers` automatically",
    #             "value": {"name": "Bar", "price": "16.25"},
    #         },
    #         "invalid": {
    #             "summary": "Invalid data is rejected with an error",
    #             "description": "Hello youtubers",
    #             "value": {"name": "Baz", "price": "sixteen point two five"},
    #         },
    #     },
    #     embed=True,
    #     type=Dict,
    # ),
):
    results = {"item_id": item_id, "item": item}
    return results
