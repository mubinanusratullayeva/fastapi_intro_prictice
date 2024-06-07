from fastapi import APIRouter, status, HTTPException

from werkzeug import security

from db.database import Session, ENGINE
from db.models import User
from schemas import RegisterModel


auth_router = APIRouter(prefix='/auth')

session = Session(bind=ENGINE)

@auth_router.get('/register')
async def register():
    return {
        "message": "Sign Up"
    }


@auth_router.get('/register')
async def register_post(user: RegisterModel):
    username = session.query()


# @auth_router.get('/login')
# async def login():
#     return {
#         "message": "Sign In"
#     }
#
#
# @auth_router.get('/logout')
# async def logout():
#     return {
#         "message": "Sign Out"
#     }
