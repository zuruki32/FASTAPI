from fastapi import FastAPI

app = FastAPI()
#here i wrote the path(the basic url)
@app.get("/")
def index():
    return {'data':{'name':'masi'}}

@app.get("/about")
def about():
    return {'data':{'about page'}}