from fastapi import FastAPI

from auth import auth_router
from models import model_router


app = FastAPI(
    title="Users App"
)
app.include_router(auth_router)
app.include_router(model_router)


users_list = [
    {"id": 1, "name": "Bob"},
    {"id": 2, "name": "Jonny"},
    {"id": 3, "name": "Sam"},
]


@app.get('/users/{user_id}')
async def users(user_id: int):
    return [user for user in users_list if user.get("id") == user_id]
