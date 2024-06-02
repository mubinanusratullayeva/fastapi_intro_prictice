from fastapi import APIRouter, status, HTTPException

from werkzeug import security

from db.database import Session, ENGINE
from db.models import User
from schemas import RegisterModel


auth_router = APIRouter(prefix='/auth')

@auth_router.get('/register')
async def register():
    return {
        "message": "Sign Up"
    }


@auth_router.get('/register')
async def register_post(user: RegisterModel):
    email = Session.query(User).filter(User.email == user.email).first()
    username = Session.query(User).filter(User.username == user.username).first()
    if username or email is not None:
        return HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="this user is already exist")


    new_user = User(
        username=username,
        email=user.email,
        password=security.generate_password_hash(user.password),
        is_staff=user.is_staff,
        is_active=user.is_active
    )
    


@auth_router.get('/login')
async def login():
    return {
        "message": "Sign In"
    }


@auth_router.get('/logout')
async def logout():
    return {
        "message": "Sign Out"
    }
