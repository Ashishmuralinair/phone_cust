import uvicorn
from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware
from pymongo import MongoClient
from contextlib import asynccontextmanager

app = FastAPI()

origins = ["http://localhost", "http://localhost:8000"]

app.add_middleware(CORSMiddleware, allow_origins=origins, allow_credentials=True, allow_methods=['*'],
                   allow_headers=['*'])


@asynccontextmanager
async def lifespan(app: FastAPI):
    app.mongo_client = MongoClient("mongodb://localhost:27017/")
    app.database = app.mongo_client["customer_stats"]
    yield
    app.mongo_client.close()

@app.get("/")
def hello_function():
    return "Hello"

if __name__ == "__main__":
    uvicorn.run(app,host="127.0.0.1",port=8080)



