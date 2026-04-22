# To build an API with FastAPI, import FastAPI library
from fastapi import FastAPI, Path, HTTPException
from entity import User
from pydantic import BaseModel

# Create Model:


# create FastAPI object.
app = FastAPI()

# Note that: 
# Automactic docs - data validation - async/await - Fast to build is the key features of FastAPI
    
def load_data():
    with open('users.txt', 'r') as f:
        return [User(line.split(',')[0], line.split(',')[1].strip(), line.split(',')[2].strip()) for line in f]

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


