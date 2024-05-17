# Importa las librerias necesarias
import requests
from fastapi import FastAPI
from pydantic import BaseModel
import base64
import json
from fastapi.middleware.cors import CORSMiddleware


#Crea una clase para que fastapi pueda recibirlo sin mayor dificultad
class RequestInfo(BaseModel):
    encodeddata:str

# Crea el objeto de la app, contiene todo lo necesario para iniciar la api, el middleware funciona para salirse de problemas con los sitios externos
app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins="*",
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
#Se encarga de hacer la peticion
def do_request(gheaders, data):
    url = "https://m.youtube.com/miniapp_cloudsaves?authuser=0"


    response = requests.request("POST", url, headers=gheaders, data=data)
    print(response)
    return(response.status_code)


@app.post("/do-request/")
async def create_item(request: RequestInfo):
    datos = base64.b64decode(request.encodeddata).decode("utf-8")
    datos = json.loads(datos)
    return {"status":do_request(datos["gameheaders"], datos["gameinfo"])}
