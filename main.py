from fastapi import FastAPI,Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates




app=FastAPI()
templates=Jinja2Templates(directory="./templates")


@app.get("/", response_class=HTMLResponse) 
def home(request: Request):  # sourcery skip: inline-immediately-returned-variable
    """Render the home page
    """
    text= {
        "title": "Home Page",
        "content": 'Welcome to the home page!'
        
    }
    
    context={"text":text , "sequence":["A","B","C"]}
    return templates.TemplateResponse(
        request=request, 
        name="home.html",
        context=context
    )
   
"""
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

"""
