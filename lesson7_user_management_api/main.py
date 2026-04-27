from fastapi import FastAPI, HTTPException, Query
from fastapi.responses import JSONResponse
from entity import User
import copy
import re

app = FastAPI()
users = []

# used to get all users
# success code: 200 OK
# response all users
@app.get('/users', tags=['Users'], status_code=200)
def get_all_users(sort_by: str = Query(default=None)):
    users_dict = [user.model_dump(exclude=['id']) for user in users]
    if sort_by is None:
        return JSONResponse(content=users_dict, headers={"Success-Code-Header":"200_OK"})
    
    if sort_by not in ['mail', 'phone', 'name']:
        raise HTTPException(status_code=400, detail='Bad request')
    
    sorted_users_dict = sorted(users_dict, key=lambda user: user.get(sort_by, 0))
    return JSONResponse(content=sorted_users_dict, headers={"Success-Code-Header":"200_OK"})

# used to get the specific user by phone number
# success code: 200 OK
#  response the specific user
@app.get('/users/{user_phone}', tags=['Users'], status_code=200)
def get_a_user_by_phone(user_phone:str):
    # Check if phone input is fake.
    if user_phone == '0123456789' or len(set(user_phone)) == 1 or not bool(re.match(r"^0\d{9}$", user_phone)):
        raise HTTPException(status_code=400, detail='There some thing wrong with the input phone number, please check it')
    
    for db_user in users:
        if user_phone == db_user.phone:
            return JSONResponse(content=db_user.model_dump(exclude=['id']), headers={"X-Custom-Header": f"{db_user.phone}"})
    # return error if user not found
    raise HTTPException(status_code=404, detail='User Not Found')
    
# used to create a users
# success code: 201 Created
# response user information
@app.post('/users', tags=['Users'], status_code=201)
def create_a_user(user: User):
    # check if user phone has been registered.
    if any(user.phone == db_user.phone for db_user in users):
        raise HTTPException(status_code=409, detail='User phone has been registered, please give another.')
     # check if user mail has been registered.
    if any(user.mail == db_user.mail for db_user in users):
        raise HTTPException(status_code=409, detail='User mail has been registered, please give another.')

    # add user when success
    users.append(user)
    return JSONResponse(content=user.model_dump(exclude=['id']), headers={"X-Custom-Header": f"{user.phone}"})

# used to update the specific user
# success code: 200 OK
# response the update data
@app.put('/users/{user_phone}', tags=['Users'], status_code=200)
def update_a_user(user_phone: str, update_user: User):
    if not user_phone == update_user.phone:
        raise HTTPException(status_code=409, detail='Incorrect action.')
    
    for user in users:
        if user_phone == user.phone:
            user.__dict__.update(update_user.__dict__)
            return user
    
    raise HTTPException(status_code=404, detail='User Not Found')

# used to delete the specific user
# success code: 204 No Content
# response no content
@app.delete('/users/{user_phone}', tags=['Users'], status_code=204)
def delete_a_user(user_phone: str):
    global users
    users = [user for user in users if user.phone != user_phone]
    return None