from fastapi import FastAPI, Query, Path, Body
from enum import Enum
from typing import Optional, List
from pydantic import BaseModel, Field

app=FastAPI()

class Item(BaseModel):
    name: str
    # num: int
    desc: str or None = Field(None, title="Desciption", max_length=100)
    price: int or None = Field(..., gt=0, description="price")
    tax: int or None = None

@app.put("/items/{item_id}")
async def update_item(item_id: int, item :Item=Body()):
    results = {"item_id": item_id, "item": item}
    return results

