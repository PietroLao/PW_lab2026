from fastapi import FastAPI

app=FastAPI()

@app.get("/") 
def hello_word(
    q:str,
    sort: bool=False
    ):
    return {"q":q, "sort":sort}

@app.get("/home")
def homepage():
    return "Welcome to the home page!"

@app.get("/{username}")
def username_webpage(
    username:str
    ):
    return f"This is the webpage of {username}."

@app.get("/{username}/orders/{order_id}")
def order_webpage(
    username:str,
    order_id:int,
    sort: bool=False
):
    return f" Order {order_id} for user {username}. Sorted: {sort}"

