#Trabalho em grupo, criando API.

from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel, Field
from typing import Dict
from itertools import count

app = FastAPI(
    title="API de Tarefas (To-Do List)",
    description="API para realizar operações CRUD em tarefas.",
    version="1.0.0"
)

# Modelo de dados da tarefa usando Pydantic

class Tarefa(BaseModel):
    titulo: str = Field(..., min_length=3, description="Título da tarefa (mínimo 3 caracteres)")
    descricao: str = Field("", description="Descrição opcional da tarefa")
    concluida: bool = Field(default=False, description="Status da tarefa")
    
# Banco de dados em memória (dicionário)

db_tarefas: Dict[int, Tarefa] = {}

# Gerador automático de IDs

id_counter = count(1)

# ENDPOINTS DA API

@app.get("/")
def read_root():
   
    """Endpoint raiz da API."""
   
    return {"message": "Bem-vindo à API de Tarefas! Acesse /docs para testar os endpoints."}

@app.post("/tarefas", status_code=status.HTTP_201_CREATED)
def criar_tarefa(tarefa: Tarefa):
   
    """Cria uma nova tarefa com ID gerado automaticamente."""
   
    tarefa_id = next(id_counter)
    db_tarefas[tarefa_id] = tarefa
    return {"id": tarefa_id, **tarefa.dict()}

@app.get("/tarefas")
def listar_tarefas():
   
    """Lista todas as tarefas cadastradas."""
   
    return [{"id": id, **tarefa.dict()} for id, tarefa in db_tarefas.items()]

@app.get("/tarefas/{id}")
def obter_tarefa(id: int):
   
    """Obtém uma tarefa específica pelo ID."""
   
    if id not in db_tarefas:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Tarefa não encontrada")
    return {"id": id, **db_tarefas[id].dict()}

@app.put("/tarefas/{id}")
def atualizar_tarefa(id: int, tarefa_atualizada: Tarefa):
   
    """Atualiza os dados de uma tarefa existente."""
   
    if id not in db_tarefas:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Tarefa atualizada")
    db_tarefas[id] = tarefa_atualizada
    return {"id": id, **tarefa_atualizada.dict()}

@app.delete("/tarefas/{id}", status_code=status.HTTP_204_NO_CONTENT)
def deletar_tarefa(id: int):
   
    """Deleta uma tarefa pelo ID."""
   
    if id not in db_tarefas:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Tarefa deletada")
   
    del db_tarefas[id]

    return{"message": "tarefa deletada com sucesso!"}
