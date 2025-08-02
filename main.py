from fastapi import FastAPI

app = FastAPI()

@app.get("/")  


def hello():
    return {'message':'Hello World!'}

@app.get('/about')

def about():
    return {'message': 'This is what happens when you create another endpoint called about'}