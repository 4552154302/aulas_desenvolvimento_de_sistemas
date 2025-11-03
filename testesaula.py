import unittest

from exerciciosteste import *

class TestesExemplos(unittest.TestCase):

    def testar_classificar_idade(self):
     self.assertEqual(classificar_idade (10), 'Criança')
     self.assertEqual(classificar_idade (15), 'Adolescente')
     self.assertEqual(classificar_idade (34), 'Adulto')
     self.assertEqual(classificar_idade (150), 'Idade Inválida')

    def testar_comparador_numeros(self):
       self.assertEqual(comparar_numeros(10, 13), '10 é menor que 13')
       self.assertEqual(comparar_numeros(22, 17), '22 é maior que 17')
       self.assertEqual(comparar_numeros(33, 33), '33 é igual a 33')

    def testar_comparar_vogal_consoante(self):
       self.assertEqual(comparar_vogal_consoante('a'), 'A letra digitada é uma vogal')
       self.assertEqual(comparar_vogal_consoante('b'), 'A letra digitada é uma consoante')

    def testar_comparar_senhas(self):
       self.assertEqual(comparar_senhas(123, 123), 'Acesso permitido!')
       self.assertEqual(comparar_senhas('abc', 'def'), 'Acesso negado!')

    def testar_calcular_media(self):
       self.assertEqual(calcular_media(8, 8, 8), 'O aluno está aprovado com média: 8.0!')
       self.assertEqual(calcular_media(3, 3, 3), 'O aluno está reprovado com média: 3.0!')
       self.assertEqual(calcular_media(11, 11, 11), 'Média inválida!')

    def testar_numeros_ordem_decrescente(self):
       self.assertEqual(numeros_ordem_decrescente(5, 7, 6), 'A lista dos números em ordem decrescente é: 567')
     
if __name__ == "__main__":

    unittest.main()



