import requests
from fastapi import FastAPI
from pydantic import BaseModel
import base64
import json
from fastapi.middleware.cors import CORSMiddleware


class RequestInfo(BaseModel):
    encodeddata:str
    

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins="*",
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

def do_request(gheaders, data):
    url = "https://www.youtube.com/miniapp_cloudsaves?authuser=0"


    response = requests.request("POST", url, headers=gheaders, data=data)
    print(response)
    return(response.status_code)


@app.post("/do-request/")
async def create_item(request: RequestInfo):
    datos = base64.b64decode(request.encodeddata).decode("utf-8")
    datos = json.loads(datos)
    return {"status":do_request(datos["gameheaders"], datos["gameinfo"])}