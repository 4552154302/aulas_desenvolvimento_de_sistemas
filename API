Criação API

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

Testes 

#testes unitarios do trabalho


import unittest
from fastapi.testclient import TestClient


from trabalhoEmGrupo import *

class TestesTarefa(unittest.TestCase):

        @classmethod
        def setUpClass(self):
                self.client = TestClient(app)
   
        def setUp(self):
               db_tarefas.clear()
   
    # 1. Testes de criação de tarefa
   
        def test_criar_tarefa_sucesso(self):
                response = self.client.post(url="/tarefas", json={"titulo": "Estudar Python", "descricao": "Revisar FastAPI"})
                self.assertEqual(response.status_code, 201)
                dados = response.json()
                self.assertIn("id", dados)
                self.assertEqual(dados["titulo"], "Estudar Python")
                self.assertFalse(dados["concluida"])


        def test_criar_tarefa_sem_titulo(self):
                resposta = self.client.post("/tarefas", json={"descricao": "Sem título"})
                self.assertEqual(resposta.status_code, 422)


        def test_criar_tarefa_titulo_curto(self):
                resposta = self.client.post("/tarefas", json={"titulo": "Oi"})
                self.assertEqual(resposta.status_code, 422)



    # 2. Testes de listagem de tarefas
   
        def test_listar_tarefas_vazio(self):
                resposta = self.client.get("/tarefas")
                self.assertEqual(resposta.status_code, 200)
                self.assertEqual(resposta.json(), [])


        def test_listar_tarefas_com_dados(self):
                self.client.post("/tarefas", json={"titulo": "Tarefa 1"})
                self.client.post("/tarefas", json={"titulo": "Tarefa 2"})
                resposta = self.client.get("/tarefas")
                self.assertEqual(resposta.status_code, 200)
                self.assertEqual(len(resposta.json()), 2)



    # 3. Testes de busca por ID
 
        def test_obter_tarefa_por_id_existente(self):
                resposta= self.client.post("/tarefas", json={"titulo": "Nova tarefa"})
                tarefa_id =  resposta.json()["id"]
                resposta_busca = self.client.get(f"/tarefas/{tarefa_id}")
                self.assertEqual(resposta_busca.status_code, 200)
                self.assertEqual(resposta_busca.json()["id"], tarefa_id)


        def test_obter_tarefa_por_id_inexistente(self):
                resposta = self.client.get("/tarefas/999")
                self.assertEqual(resposta.status_code, 404)



    # 4. Testes de atualização
   
        def test_atualizar_tarefa_sucesso(self):
                resposta = self.client.post("/tarefas", json={"titulo": "Antiga"})
                tarefa_id = resposta.json()["id"]


                resposta_update = self.client.put(f"/tarefas/{tarefa_id}", json={"titulo": "Atualizada", "descricao": "Nova", "concluida": True})
                self.assertEqual(resposta_update.status_code, 200)
                dados = resposta_update.json()
                self.assertEqual(dados["titulo"], "Atualizada")
                self.assertTrue(dados["concluida"])


        def test_atualizar_tarefa_inexistente(self):
                resposta = self.client.put("/tarefas/999", json={"titulo": "Nada", "descricao": "", "concluida": False})
                self.assertEqual(resposta.status_code, 404)


 
    # 5. Testes de deleção
   
        def test_deletar_tarefa_sucesso(self):
                resposta = self.client.post("/tarefas", json={"titulo": "Apagar"})
                tarefa_id = resposta.json()["id"]
                resposta_delete = self.client.delete(f"/tarefas/{tarefa_id}")
                self.assertEqual(resposta_delete.status_code, 204)


        # Verifica se foi realmente removida
                resposta_busca = self.client.get(f"/tarefas/{tarefa_id}")
                self.assertEqual(resposta_busca.status_code, 404)


        def test_deletar_tarefa_inexistente(self):
                resposta = self.client.delete("/tarefas/999")
                self.assertEqual(resposta.status_code, 404)




if __name__ == "__main__":
    unittest.main()
