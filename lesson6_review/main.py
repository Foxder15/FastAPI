# To build an API with FastAPI, import FastAPI library
from fastapi import FastAPI

# create FastAPI object.
app = FastAPI()

# Note that: 
# Automactic docs - data validation - async/await - Fast to build is the key features of FastAPI

class User():
    def __init__(self, name, password):
        self.name = name
        self.password = password
    
def load_data():
    with open('users.txt', 'r') as f:
        return [User(line.split(',')[0], line.split(',')[1].strip()) for line in f]

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
def get_user_by_id(user_id):
    users = load_data()
    return users[int(user_id)]

