import os
from fastapi import FastAPI

'''Creating FastAPI instance. This will be the main point of interaction to create your API.'''
app = FastAPI()

'''/ is a path operation function. '''
@app.get("/")

#If you are using third party libraries that tell you to call them with await, like:
#results = await some_library()
#Then, declare your path operation functions with async def like:

async def root():
    '''http://127.0.0.1:8000/docs to access Swaggewr UI'''
    '''http://127.0.0.1:8000/redoc to access alternative Swagger UI'''
    return {"message": "Hello World"}

#If you are using a third party library that communicates with something (a database,
# an API, the file system, etc) and doesn't have support for using await, (this is
# currently the case for most database libraries), then declare your path operation
# functions as normally, with just def, like:

#def root():
#    '''http://127.0.0.1:8000/docs to access Swaggewr UI'''
#    '''http://127.0.0.1:8000/redoc to access alternative Swagger UI'''
#    return {"message": "Hello World"}

#Notes: If your application (somehow) doesn't have to communicate with anything else and wait for it to respond, use async def.
#If you just don't know, use normal def.

'''Path Parameters: Get an Item by ID'''

#@app.get("/items/{item_id}")
#async def read_item(item_id):
#    return {"item_id":item_id}

'''While disabled above function there will be an error as HttpError for try conversion is not available'''

'''Here we have passed item_id as a parameter & this is interacting to my function as argument'''
'''TEST URL: http://127.0.0.1:8000/items/foo'''

####################################################################
'''Path parameters with types'''
#Hence only integer as ID would be taken or there is an exception.
@app.get("/items/{item_id}")
async def read_item1(item_id: int):
    return {"Item_ID":item_id}

'''To get current User details'''
@app.get("/users/me")
async def read_user_me():
    return {"User ID":"the current user"}


'''To get any specific user details through user ID'''
@app.get("/users/{user_id}")
async def read_user(user_id: str):
    return {"user_id":user_id}

