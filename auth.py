from fastapi import APIRouter

auth_router = APIRouter(prefix='/auth')

@auth_router.get('/register')
async def register():
    return {
        "message": "Sign Up"
    }


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
