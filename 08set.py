from fastapi import FastAPI
from pydantic import BaseModel
from typing import Literal

app = FastAPI()

#Schemas:
class Partida(BaseModel):
    id: int | None = None
    nome: str
    data: str
    local: str
    categoria: Literal['p', 'a', 's'] = 'a'

# GET /partidas -> List[Partida] --- 200 (OK)
# Parametros:
# Query: categoria (http://galeravolei.com/partidas?categoria=P)

@app.get('/partidas', response_model=list[Partida])
def list_partidas(categoria: str | None = None):
    return ['Patro#01']

# GET /partidas/[id] --> Partida
@app.get('/partidas/{id}', response_model = Partida)
def detail_partida(id: int):
    return Partida(id=1, nome='Patro01', local='Patro Beach', categoria='a')

@app.post('/partida', status_code= 201)
def create_partida(partida: Partida):
    return partida