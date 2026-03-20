from fastapi import FastAPI

app=FastAPI()

@app.get("/") 
def hello_word(
    q:str,
    sort: bool=False
    ):
    return {"q":q, "sort":sort}