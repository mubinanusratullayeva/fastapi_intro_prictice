from fastapi import APIRouter, status, HTTPException
from fastapi.encoders import jsonable_encoder

from db.models import Product
from db.database import ENGINE, Session


product_router = APIRouter(prefix='/products')
session = Session(bind=ENGINE)

@product_router.get('/')
async def product_list(status_code=status.HTTP_200_OK):
    products = Session.query(Product).all()
    context = [
        {
            "id": product.id,
            "name": product.name,
            "description": product.description,
            "category_id": product.category_id,
        }
        for product in products
    ]
    return jsonable_encoder(context)
