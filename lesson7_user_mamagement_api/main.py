from fastapi import FastAPI
from entity import User

app = FastAPI()
users = []

# used to get all users
# success code: 200 OK
# response all users
@app.get('/users', tags=['Users'], status_code=200)
def get_all_users():
    return {'users' : users}

# used to create a users
# success code: 201 Created
# response user information
@app.post('/users', tags=['Users'], status_code=201)
def create_a_user(user: User):
    users.append(user)
    return user

# used to update the specific user
# success code: 200 OK
# response the update data
@app.put('/users/{user_id}', tags=['Users'], status_code=200)
def update_a_user(user_id, update_user):
    return None

# used to delete the specific user
# success code: 204 No Content
# response no content
@app.delete('/users/{user_id}', tags=['Users'], status_code=204)
def delete_a_user(user_id):
    return None