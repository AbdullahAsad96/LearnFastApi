from fastapi import FastAPI

app=FastAPI()

posts ={
        "title":'here you get all post related to your feed',
        "description":'These all afe posts are scure and authentic',
        "age":22
    }


@app.get("/") 
async def home():
    return {"message":" Thank God i run my fast api app" }

@app.get("\lists")
def getlist():
    return list
@app.get("/")
def getposts():
    return {1,2,3,4,"Hello G"}
#python -m uvicorn app:app --reload