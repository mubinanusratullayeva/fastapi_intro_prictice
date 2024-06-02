from typing import Optional
from pydantic import BaseModel


class RegisterModel(BaseModel):
    id: Optional[int]
    username: str
    email: str
    password: str
    is_staff: Optional[bool]
    is_active: Optional[bool]

    # class Config:
    #     orm_mode = True
    #     schema_extra = {
    #         "example": {"Base example"}
    #     }


class OrderModel(BaseModel):
    id: Optional[int]
    user_id: int
    product_id: int


class CategoryModel(BaseModel):
    id: Optional[int]
    name: str


class ProductModel(BaseModel):
    id: Optional[int]
    name: str
    description: str
    price: float    
    category_id: Optional[int]
