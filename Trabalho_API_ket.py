from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel
from typing import Dict

app = FastAPI(
    title="API de Cadastro de Alunos",
    description="API para realizar as quatro operações básicas (CRUD) para alunos.",
    version="1.0.0"
)

# Modelo de dados do aluno usando Pydantic
class Aluno(BaseModel):
    nome: str
    idade: int
    turma: int

# "Banco de dados" em memória (um dicionário Python)
db_alunos: Dict[int, Aluno] = {
    1: Aluno(nome="Ketlhyn Klebber", idade=17, turma=204),
    2: Aluno(nome="Larissa Thaiza", idade=16, turma=204),
    3: Aluno(nome="Micheli Ferreira", idade=16, turma=204),
}

# --- ENDPOINTS DA API ---

@app.get("/")
def read_root():
    """Endpoint raiz da API."""
    return {"message": "Bem-vindo à API Alunos! Acesse /docs para a documentação interativa."}

@app.get("/alunos")
def pegar_todos_alunos():
    """Retorna todos os alunos cadastrados."""
    return db_alunos

@app.get("/alunos/{id}")
def pegar_aluno_por_id(id: int):
    """Retorna um aluno específico pelo seu Id."""
    if id not in db_alunos:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Aluno não encontrado")
    return db_alunos[id]

@app.post("/alunos/{id}", status_code=status.HTTP_201_CREATED)
def criar_aluno(id: int, aluno: Aluno):
    """Cria um novo aluno com um id específico."""
    if id in db_alunos:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail="Esse aluno já existe")
    
    db_alunos[id] = aluno
    return {"message": "Aluno cadastrado com sucesso!", "Id": id, "aluno": aluno}

@app.put("/alunos/{id}")
def atualizar_aluno(id: int, aluno: Aluno):
    """Atualiza as informações de um aluno existente."""
    if id not in db_alunos:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Aluno não encontrado")
    
    db_alunos[id] = aluno
    return {"message": "Cadastro do aluno atualizado com sucesso!", "aluno": aluno}

@app.delete("/alunos/{id}")
def deletar_aluno(id: int):
    """Deleta o cadastro de um aluno."""
    if id not in db_alunos:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Aluno não encontrado")
    
    del db_alunos[id]
    return {"message": "Aluno deletado com sucesso!"}