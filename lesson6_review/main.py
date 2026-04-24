# To build an API with FastAPI, import FastAPI library
from fastapi import FastAPI, Path, HTTPException
from entity import User
from pydantic import BaseModel
import uuid

# Create Base Model:
class PostUser(BaseModel):
    name: str
    password: str

# create FastAPI object.
app = FastAPI()

# Note that: 
# Automactic docs - data validation - async/await - Fast to build is the key features of FastAPI
con = f'users.txt'

def load_data():
    with open(con, 'r') as f:
        return [User(line.split(',')[0], line.split(',')[1].strip(), line.split(',')[2].strip()) for line in f]
    
def add_data(data):
    with open(con, 'a') as f:
        f.write(data)

def save_data(data):
    with open(con, 'w') as f:
        f.writelines(data)

# routing my API
@app.get("/users")
def get_main_page():
    # By default, when you return list, dict or Python object -> convert to json.
    # behind the back, Python use JSONResponse - set content-type header: application/json.
    return load_data()

# Serializtion:
# The process when API convert your return object to json.
# Return a dict: Becomes a JSON Object {}.
# Return a list: Becomes a JSON Array [].
# Return a str: Becomes a JSON String "".
# Return a Pydantic Model: Becomes a JSON Object {}.

@app.get('/users/{user_id}')
def get_user_by_id(user_id = Path(..., description='ID of the user'), example='1c1ef692-3e58-11f1-a0e2-d85ed3d279b0'):
    users = load_data()
    for user in users:
        if user_id == user.id:
            return user
    raise HTTPException(status_code=404, detail='User not found')

# Path, Query: used for adding metadata nad validation rule to path/query params.
# It sets validaiton rule like numeric constraints (min/max value), regex patterns, min/max length, description - title of documentation. 
# ... : the Ellipsis, means required.

@app.post('/users')
def create_user(user: PostUser):
    store_user = User(uuid.uuid1(), user.name, user.password)
    add_data(f"{store_user.id},{store_user.name},{store_user.password}\n")
    return store_user

@app.put('/users/{user_id}')
def update_user(user_id: str, user: PostUser):
    users = load_data()
    for data_user in users:
        if data_user.id == user_id:
            update_user = User('NOT', user.name, user.password)
            data_user.name = update_user.name
            data_user.password = update_user.password
            break

    users_str = [f'{user.id},{user.name},{user.password}\n' for user in users]
    save_data(users_str)
    return data_user

@app.delete('/users/{user_name}')
def delete_user(user_name: str):
    users = load_data()
    for user in users:
        if user.name == user_name:
            users.remove(user)
            break
    users_str = [f'{user.id},{user.name},{user.password}\n' for user in users]
    save_data(users_str)
    return user

