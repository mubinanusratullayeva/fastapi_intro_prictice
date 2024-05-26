from fastapi import APIRouter

model_router = APIRouter(prefix='/models')

@model_router.get('/')
async def default_model():
    return{
        "message": "Learning Centre"
    }


@model_router.get('/about-us')
async def aboutUs_model():
    return{
        "message": "Students can learn many variety of foreign languages with us"
    }


@model_router.get('/contact')
async def contact_model():
    return{
        "message": "You can contact us via our course email: learningcentre@email.com"
    }