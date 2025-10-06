from fastapi import FastAPI
from pydantic import BaseModel
from typing import Literal

app = FastAPI()

#Schemas:
class Jogador(BaseModel):
    id: int | None = None
    nome: str
    sexo: Literal['masculino', 'feminino', 'outro'] = 'outro'
    idade: int
    categoria: Literal['iniciante', 'intermediario', 'avancado'] = 'iniciante'

class Partida(BaseModel):
    id: int | None = None
    nome: str
    data: str
    local: str
    tipo: Literal['mista', 'especifica'] = 'mista'
    categoria: Literal['iniciante', 'intermediario', 'avancado'] = 'iniciante'
    situacao: Literal['nova', 'em_adesao', 'encerrada'] = 'nova'

class Incricao(BaseModel):
    status: Literal['pendente', 'aprovada', 'rejeitada'] = 'pendente'    

####################################################################################

#Partidas:
@app.get('/partidas', response_model=list[Partida])
def list_partidas(partida: Partida):
    return partida

@app.get('/partidas/{id}', response_model = Partida)
def detail_partida(id: int):
    return Partida

@app.post('/partida', status_code= 201)
def create_partida(partida: Partida):
    return partida



#Jogadores:
@app.get('/jogadores', response_model=list[Jogador])
def list_jogadores(jogador: Jogador):
    return jogador

@app.get('/jogadores/{id}', response_model= Jogador)
def detail_jogador(id: int):
    return Jogador

@app.post('/jogadores', status_code=201)
def create_jogador(jogador: Jogador):
    return jogador

@app.delete('/jogadores', status_code=204)
def delete_jogador(id: int):
    print("Deletaando jogador com id: {id}")
    return None