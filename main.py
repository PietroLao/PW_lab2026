from fastapi import FastAPI,Request, Form
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from typing import Annotated
from pydantic import Field, BaseModel

class Product(BaseModel):
    name:Annotated[str, Field(min_length=3, max_length=30)]
    price: Annotated[float, Field(gt=0)]
    location: Annotated[str, Field(min_length=3, max_length=30)]

app=FastAPI()

app.mount("/static",StaticFiles(directory="static"),name="static")
templates=Jinja2Templates(directory="./templates")

products_list=[
    {"name":"Pietro", "price":"10", "location":"italy"},
    {"name":"giovi", "price":"10001", "location":"french"},
    {"name":"andre", "price":"200", "location":"german"},
    {"name":"troia", "price":"2000", "location":"italy"}    
]

@app.get("/", response_class=HTMLResponse) 
def home(request: Request):  # sourcery skip: inline-immediately-returned-variable
    """Render the home page
    """
    text= {
        "title": "Home Page",
        "content": 'Welcome to the home page!'
        
    }
    dictionary={"key1":"value1","key2":"value2"}
    context={"text":text , "sequence":["A","B","C"],"dictionary":dictionary}
    return templates.TemplateResponse(
        request=request, 
        name="home.html",
        context=context
    )

   

@app.get("/products", response_class=HTMLResponse) 
def products(request: Request):

    return templates.TemplateResponse(
        request=request, 
        name="products.html",
        context={"products_list":products_list}
    )

@app.get("/product_form", response_class=HTMLResponse)
def add_product(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="product_form.html"
    )

@app.post("/insert_product", response_class=HTMLResponse)
def insert_product(
    request: Request,
    product: Annotated[Product, Form()]
):
    products_list.append(product.model_dump())
    return templates.TemplateResponse(
        request=request,
        name="success.html",
        context={"product":product}
    )

@app.post("/insert_product_json")
def insert_product_json(
    product: Product
):
    print(product)
    
    








"""
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
