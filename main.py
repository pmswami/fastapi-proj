from fastapi import (
    FastAPI,
    Query,
    Path,
    Body,
    status,
    Form,
    File,
    UploadFile,
    HTTPException,
    Request,
    Depends,
)
from fastapi.exception_handlers import (
    http_exception_handler,
    request_validation_exception_handler,
)
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse, PlainTextResponse
from fastapi.encoders import jsonable_encoder
from starlette.exceptions import HTTPException as StarletteHTTPException
from starlette.responses import HTMLResponse
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


# # Extra Models
# class UserBase(BaseModel):
#     username: str
#     email: EmailStr
#     full_name: str or None = None


# class UserIn(UserBase):
#     password: str


# class UserOut(UserBase):
#     pass


# class UserInDB(UserBase):
#     hashed_password: str


# def fake_password_hasher(raw_password: str):
#     return f"supersecret{raw_password}"


# def fake_save_user(user_in: UserIn):
#     hashed_password = fake_password_hasher(user_in.password)
#     user_in_db = UserInDB(**user_in.dict(), hashed_password=hashed_password)
#     print("User 'saved'.")
#     return user_in_db


# @app.post("/user/", response_model=UserOut)
# async def create_user(user_in: UserIn):
#     user_saved = fake_save_user(user_in)
#     return user_saved


# class BaseItem(BaseModel):
#     description: str
#     type: str


# class CarItem(BaseItem):
#     type: str or "car"


# class PlaneItem(BaseItem):
#     type: str or "plane"
#     size: int


# items = {
#     "item1": {"description": "All my friends drive a low rider", "type": "car"},
#     "item2": {
#         "description": "Music is my aeroplane, it's my aeroplane",
#         "type": "plane",
#         "size": 5,
#     },
# }


# @app.get("/items/{item_id}", response_model=Union[ Item, CarItem])
# async def read_item(item_id: Literal["item1", "item2"]):
#     return items[item_id]


# class ListItem(BaseModel):
#     name: str
#     description: str


# list_items = [
#     {"name": "Foo", "description": "There comes my hero"},
#     {"name": "Red", "description": "It's my aeroplane"},
# ]


# @app.get("/list_items/", response_model=List[ListItem])
# async def read_items():
#     return list_items


# @app.get("/arbitrary", response_model=Dict[str, float])
# async def get_arbitrary():
#     return {"foo": 1, "bar": "2"}


# # Response status codes
# @app.post("/items/", status_code=status.HTTP_201_CREATED)
# async def create_item(name: str):
#     return {"name": name}


# @app.delete("/items/{pk}", status_code=status.HTTP_204_NO_CONTENT)
# async def delete_item(pk: str):
#     print("pk", pk)
#     return pk


# @app.get("/items/", status_code=status.HTTP_302_FOUND)
# async def read_items_redirect():
#     return {"hello": "world"}


# # Form Fields
# @app.post("/login/")
# async def login(username: str = Form(...), password: str = Body(...)):
#     print("password", password)
#     return {"username": username}


# @app.post("/login-json/")
# async def login_json(username: str = Body(...), password: str = Body(...)):
#     print("password", password)
#     return {"username": username}


# # Request Files
# @app.post("/files/")
# async def create_file(
#     files: bytes or None = File(None, description="A file read as bytes")
# ):
#     if files:
#         return {"file_sizes": len(files)}
#     else:
#         return {"message": "No Files attached"}


# # @app.post("/files/")
# # async def create_file(
# #     files: List[bytes] = File(..., description="A file read as bytes")
# # ):
# #     return {"file_sizes": [len(file) for file in files]}


# @app.post("/uploadfile/")
# async def create_upload_file(
#     file: UploadFile or None = File(None, description="A file read as UploadFile")
# ):
#     if file:
#         return {"filename": file.filename}
#     else:
#         return {"message": "No file is attached"}


# # @app.post("/uploadfile/")
# # async def create_upload_file(
# #     files: List[UploadFile] = File(..., description="A file read as UploadFile")
# # ):
# #     return {"filename": [file.filename + " " + str(file.size) for file in files]}


# # Request Forms and Files
# @app.post("/files/")
# async def create_file(
#     file: bytes = File(...),
#     fileb: UploadFile = File(...),
#     token: str = Form(...),
#     hello: str = Body(...),
# ):
#     return {
#         "file_size": len(file),
#         "token": token,
#         "fileb_content_type": fileb.content_type,
#         "hello": hello,
#     }


# # Handling errors
# items = {"foo": "The Foo Wrestlers"}


# # @app.get("/items/{item_id}")
# # async def read_item(item_id: str):
# #     if item_id not in items:
# #         raise HTTPException(
# #             status_code=404,
# #             detail="Item not found",
# #             headers={"X-Error": "There goes my error"},
# #         )
# #     return {"item": items[item_id]}


# class UnicornException(Exception):
#     def __init__(self, name: str):
#         self.name = name


# @app.exception_handler(UnicornException)
# async def unicorn_exception_handler(request: Request, exc: UnicornException):
#     return JSONResponse(
#         status_code=418,
#         content={"message": f"Oops! {exc.name} did something. There goes a rainbow..."},
#     )


# # @app.get("/unicorns/{name}")
# # async def read_unicorns(name: str):
# #     if name == "yolo":
# #         raise UnicornException(name=name)
# #     return {"unicorn_name": name}


# @app.exception_handler(RequestValidationError)
# async def validation_exception_handler(request, exc):
#     return PlainTextResponse(str(exc), status_code=400)


# # @app.get("/validation_items/{item_id}")
# # async def read_validation_items(item_id: int):
# #     if item_id == 3:
# #         raise HTTPException(status_code=418, detail="Nope! I don't like 3.")
# #     return {"item_id": item_id}


# @app.exception_handler(RequestValidationError)
# async def validation_exception_handler(request: Request, exc: RequestValidationError):
#     return JSONResponse(
#         status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
#         content=jsonable_encoder({"detail": exc.errors(), "blahblah": exc.body}),
#     )


# class Item(BaseModel):
#     title: str
#     size: int


# @app.post("/items/")
# async def create_item(item: Item):
#     return item


# @app.exception_handler(StarletteHTTPException)
# async def custom_http_exception_handler(request, exc):
#     print(f"OMG! An HTTP error!: {repr(exc)}")
#     return await http_exception_handler(request, exc)


# @app.exception_handler(RequestValidationError)
# async def validation_exception_handler(request, exc):
#     print(f"OMG! The client sent invalid data!: {exc}")
#     return await request_validation_exception_handler(request, exc)


# @app.get("/blah_items/{item_id}")
# async def read_items(item_id: int):
#     if item_id == 3:
#         raise HTTPException(status_code=418, detail="Nope! I don't like 3.")
#     return {"item_id": item_id}


# # Path operations
# class Item(BaseModel):
#     name: str
#     description: str or None = None
#     price: float
#     tax: float or None = None
#     tags: Set[str] = set()


# class Tags(Enum):
#     items = "items"
#     users = "users"


# @app.post(
#     "/items/",
#     response_model=Item,
#     status_code=status.HTTP_201_CREATED,
#     tags=[Tags.items],
#     summary="Create an Item-type item",
#     # description="Create an item with all the information: "
#     # "name; description; price; tax; and a set of "
#     # "unique tags",
#     response_description="The created item",
# )
# async def create_item(item: Item):
#     """
#     Create an item with all the information:

#     - **name**: each item must have a name
#     - **description**: a long description
#     - **price**: required
#     - **tax**: if the item doesn't have tax, you can omit this
#     - **tags**: a set of unique tag strings for this item
#     """
#     return item


# @app.get("/items/", tags=[Tags.items])
# async def read_items():
#     return [{"name": "Foo", "price": 42}]


# @app.get("/users/", tags=[Tags.users])
# async def read_users():
#     return [{"username": "PhoebeBuffay"}]


# @app.get("/elements/", tags=[Tags.items], deprecated=True)
# async def read_elements():
#     return [{"item_id": "Foo"}]


# class Item(BaseModel):
#     name: str or None = None
#     description: str or None = None
#     price: float or None = None
#     tax: float = 10.5 or 0
#     tags: List[str] = []


# items = {
#     "foo": {"name": "Foo", "price": 50.2},
#     "bar": {
#         "name": "Bar",
#         "description": "The bartenders",
#         "price": 62,
#         "tax": 20.2,
#     },
#     "baz": {
#         "name": "Baz",
#         "description": None,
#         "price": 50.2,
#         "tax": 10.5,
#         "tags": [],
#     },
# }


# @app.get("/items/{item_id}", response_model=Item)
# async def read_item(item_id: str):
#     return items.get(item_id)


# @app.put("/items/{item_id}", response_model=Item)
# def update_item(item_id: str, item: Item):
#     update_item_encoded = jsonable_encoder(item)
#     items[item_id] = update_item_encoded
#     return update_item_encoded


# @app.patch("/items/{item_id}", response_model=Item)
# def patch_item(item_id: str, item: Item):
#     stored_item_data = items.get(item_id)
#     if stored_item_data is not None:
#         stored_item_model = Item(**stored_item_data)
#     else:
#         stored_item_model = Item()
#     update_data = item.dict(exclude_unset=True)
#     updated_item = stored_item_model.copy(update=update_data)
#     items[item_id] = jsonable_encoder(updated_item)
#     return updated_item


# # function based Dependencies
# async def hello():
#     return "world"


# async def common_parameters(
#     q: str or None = None, skip: int = 0, limit: int = 100, blah: str = Depends(hello)
# ):
#     return {"q": q, "skip": skip, "limit": limit, "hello": blah}


# @app.get("/items/")
# async def read_items(commons: dict = Depends(common_parameters)):
#     return commons


# @app.get("/users/")
# async def read_users(commons: dict = Depends(common_parameters)):
#     return commons


# class based dependencies
fake_items_db = [{"item_name": "Foo"}, {"item_name": "Bar"}, {"item_name": "Baz"}]


class CommonQueryParams:
    def __init__(self, q: str or None = None, skip: int = 0, limit: int = 100):
        self.q = q
        self.skip = skip
        self.limit = limit


@app.get("/items/{item_id}")
async def read_items(commons: CommonQueryParams = Depends()):
    response = {}
    if commons.q:
        response.update({"q": commons.q})
    items = fake_items_db[commons.skip : commons.skip + commons.limit]
    response.update({"items": items})
    return response
