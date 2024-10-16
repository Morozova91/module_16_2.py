# Задача "Аннотация и валидация":
from fastapi import FastAPI, Path
from typing import Annotated

app = FastAPI()

# 2.Создайте маршрут к главной странице - "/". По нему должно выводиться сообщение "Главная страница".
@app.get("/")
async def welcome() -> dict:
    return {"message": "Главная страница"}
# 3.Создайте маршрут к странице администратора - "/user/admin".
# По нему должно выводиться сообщение "Вы вошли как администратор".
@app.get("/user/admin")
async def admin() ->dict:
    return {"message" : "Вы вошли как администратор"}

#4. Валидация по id

@app.get("/user/{user_id}")
def users(user_id: int = Path(ge=1, le=100, description='Enter User ID', examples='1')) ->dict:
    return {"message": f"Вы вошли как пользователь № {user_id}"}
# 5. Валидация по username / age
@app.get('/user/{username}/{age}')
async def user(username:Annotated[str, Path(ge=5, le=20, description='Enter username', examples='juk')],
               age:int= Path(ge=18, le=120,description="Enter age", examples='24'))-> set[str]:
      return {f'Информация о пользователе. Имя: {username}, Возраст: {age}'}