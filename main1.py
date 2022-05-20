from fastapi import FastAPI
from typing import Optional
from pydantic import BaseModel

class Item(BaseModel):
    name: str
    description: Optional[str] = None
    price: float
    tax: Optional[float] = None

app = FastAPI()

@app.post("/items/")
async def create_item(item: Item):
    item_dict = item.dict()
    if item.tax:
        price_with_tax = item.price+item.tax
        item_dict.update({"Price with Tax": price_with_tax})
    return item_dict

#@app.post("/items/{item_id}")
#async def create_item(item_id: int, item: Item):
#    return {"Item ID":item_id, **item.dict()}