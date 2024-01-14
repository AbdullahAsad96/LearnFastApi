from fastapi import FastAPI

app=FastAPI()

posts ={
        "title":'here you get all post related to your feed',
        "description":'These all afe posts are scure and authentic',
        "age":22
    }

@app.get("/") 
def home():
    return {"message":" Thank God i run my fast api app" }

@app.get("\posts")
def getpost():
    return posts
    