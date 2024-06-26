from fastapi import FastAPI

from auth import auth_router
from product import product_router

app = FastAPI(
    title="Users App"
)
app.include_router(auth_router)
app.include_router(product_router)


@app.get('/')
async def intro():
    return {
        "messages":"Hello World"
    }
