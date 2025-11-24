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
