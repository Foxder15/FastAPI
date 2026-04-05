from fastapi import FastAPI

# create app object of FastAPI
main = FastAPI()

# routing for my API.
@main.get("/")
def mainPage():
  return {'message':'hello', 'status':200}

@main.get("/about")
def mainPage2():
  return {'message':'My name is Duy, Im an AI engineer.', 'status':200}

# to run this: uvicorn main:fastAPI object --reload