from fastapi import FastAPI, Query, Path, Body
from enum import Enum
from typing import Optional, List, Set, Dict, Union, Literal
from pydantic import BaseModel, Field, HttpUrl, EmailStr

# from pydantic import EmailStr

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


# class Item(BaseModel):
#     name: str = Field(None)
#     description: str = Field(None)
#     price: float = Field(0)
#     tax: float = Field(0)

#     class Config:
#         json_schema_extra = {
#             "example": {
#                 "name": "Foo",
#                 "description": "A very nice Item",
#                 "price": 16.25,
#                 "tax": 1.67,
#             }
#         }


# @app.put("/items/{item_id}")
# async def update_item(
#     item_id: int,
#     item: Item,
#     # item: Item = Body(
#     #     ...,
#     #     # example={"name": "foo", "desc": "nice desc", "price": 10, "tax": 20},
#     #     examples={
#     #         "normal": {
#     #             "summary": "A normal example",
#     #             "description": "A __normal__ item works _correctly_",
#     #             "value": {
#     #                 "name": "Foo",
#     #                 "description": "A very nice Item",
#     #                 "price": 16.25,
#     #                 "tax": 1.67,
#     #             },
#     #         },
#     #         "converted": {
#     #             "summary": "An example with converted data",
#     #             "description": "FastAPI can convert price `strings` to actual `numbers` automatically",
#     #             "value": {"name": "Bar", "price": "16.25"},
#     #         },
#     #         "invalid": {
#     #             "summary": "Invalid data is rejected with an error",
#     #             "description": "Hello youtubers",
#     #             "value": {"name": "Baz", "price": "sixteen point two five"},
#     #         },
#     #     },
#     #     embed=True,
#     #     type=Dict,
#     # ),
# ):
#     results = {"item_id": item_id, "item": item}
#     return results


# from uuid import UUID
# from datetime import datetime, timedelta, time


# @app.put("/items/{item_id}")
# async def read_items(
#     item_id: UUID,
#     start_date: datetime or None = Body(None),
#     end_date: datetime or None = Body(None),
#     repeat_at: time or None = Body(None),
#     process_after: timedelta or None = Body(None),
# ):
#     start_process = start_date + process_after
#     duration = end_date - start_process
#     return {
#         "item_id": item_id,
#         "start_date": start_date,
#         "end_date": end_date,
#         "repeat_at": repeat_at,
#         "process_after": process_after,
#         "start_process": start_process,
#         "duration": duration,
#     }

# # Cookie and header params
# from fastapi import Cookie, Header


# @app.get("/items")
# async def read_items(
#     cookie_id: str or None = Cookie(None),
#     accept_encoding: str or None = Header(None),
#     sec_ch_ua: str or None = Header(None),
#     user_agent: str or None = Header(None),
#     x_token: List[str] or None = Header(None),
# ):
#     return {
#         "cookie_id": cookie_id,
#         "Accept-Encoding": accept_encoding,
#         "sec-ch-ua": sec_ch_ua,
#         "User-Agent": user_agent,
#         "X-Token values": x_token,
#     }


# # Response Model
# from pydantic import EmailStr
# from typing import Literal


# class Item(BaseModel):
#     name: str
#     description: str or None = None
#     price: float
#     tax: float = 10.5
#     tags: List[str] = []


# @app.post("/items/", response_model=Item)
# async def create_item(item: Item):
#     return item


# class UserBase(BaseModel):
#     username: str
#     email: EmailStr
#     full_name: str or None = None


# class UserIn(UserBase):
#     password: str


# class UserOut(UserBase):
#     pass


# @app.post("/user/", response_model=UserOut)
# async def create_user(user: UserIn):
#     return user


# items = {
#     "foo": {"name": "Foo", "price": 50.2},
#     "bar": {"name": "Bar", "description": "The bartenders", "price": 62, "tax": 20.2},
#     "baz": {"name": "Baz", "description": None, "price": 50.2, "tax": 10.5, "tags": []},
# }


# # excludes fields from response which are not set
# @app.get("/items/{item_id}", response_model=Item, response_model_exclude_unset=True)
# async def read_item(item_id: Literal["foo", "bar", "baz"]):
#     return items[item_id]


# @app.get(
#     "/items/{item_id}/name",
#     response_model=Item,
#     response_model_include={"name", "description"},
# )
# async def read_item_name(item_id: Literal["foo", "bar", "baz"]):
#     return items[item_id]


# @app.get("/items/{item_id}/public", response_model=Item, response_model_exclude={"tax"})
# async def read_items_public_data(item_id: Literal["foo", "bar", "baz"]):
#     return items[item_id]


# Extra Models


class UserBase(BaseModel):
    username: str
    email: EmailStr
    full_name: str or None = None


class UserIn(UserBase):
    password: str


class UserOut(UserBase):
    pass


class UserInDB(UserBase):
    hashed_password: str


def fake_password_hasher(raw_password: str):
    return f"supersecret{raw_password}"


def fake_save_user(user_in: UserIn):
    hashed_password = fake_password_hasher(user_in.password)
    user_in_db = UserInDB(**user_in.dict(), hashed_password=hashed_password)
    print("User 'saved'.")
    return user_in_db


@app.post("/user/", response_model=UserOut)
async def create_user(user_in: UserIn):
    user_saved = fake_save_user(user_in)
    return user_saved


class BaseItem(BaseModel):
    description: str
    type: str


class CarItem(BaseItem):
    type: str or "car"


class PlaneItem(BaseItem):
    type: str or "plane"
    size: int


items = {
    "item1": {"description": "All my friends drive a low rider", "type": "car"},
    "item2": {
        "description": "Music is my aeroplane, it's my aeroplane",
        "type": "plane",
        "size": 5,
    },
}


@app.get("/items/{item_id}", response_model=Union[PlaneItem, CarItem])
async def read_item(item_id: Literal["item1", "item2"]):
    return items[item_id]


class ListItem(BaseModel):
    name: str
    description: str


list_items = [
    {"name": "Foo", "description": "There comes my hero"},
    {"name": "Red", "description": "It's my aeroplane"},
]


@app.get("/list_items/", response_model=List[ListItem])
async def read_items():
    return list_items


@app.get("/arbitrary", response_model=Dict[str, float])
async def get_arbitrary():
    return {"foo": 1, "bar": "2"}
