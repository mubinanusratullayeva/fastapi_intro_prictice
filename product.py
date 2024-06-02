from typing import List
from fastapi import APIRouter, status, HTTPException
from fastapi.encoders import jsonable_encoder

from db.models import Product
from db.database import ENGINE, Session
from schemas import ProductModel


product_router = APIRouter(prefix='/products')
session = Session(bind=ENGINE)

# @product_router.get('/')
# async def product_list(status_code=status.HTTP_200_OK):
#     products = Session.query(Product).all()
#     context = [
#         {
#             "id": product.id,
#             "name": product.name,
#             "description": product.description,
#             "category_id": product.category_id,
#         }
#         for product in products
#     ]
#     return jsonable_encoder(context)


items = []

@product_router.get("/", response_model=List[ProductModel])
async def read_items():
    return items

@product_router.post("/", response_model=ProductModel)
async def create_item(item: ProductModel):
    items.append(item)
    return item

@product_router.put("/{item_id}", response_model=ProductModel)
async def update_item(item_id: int, item: ProductModel):
    items[item_id] = item
    return item

@product_router.delete("/{item_id}")
async def delete_item(item_id: int):
    del items[item_id]
    return {"message": "Item deleted"}