#1.

def primos_no_intervalo(a, b):
    primos = []
    for num in range(a, b + 1):
        if eh_primo(num):
            primos.append(num)
    return primos

def main():
    a = int(input("Digite o início do intervalo: "))
    b = int(input("Digite o fim do intervalo: "))
    lista_primos = primos_no_intervalo(a, b)
    print(f"Números primos entre {a} e {b}: {lista_primos}")

if __name__ == "__main__":
    main()

#2

def mostrar_lista(lista):
    print("Nossa lista de frutas:")
    print(lista)
    print(" ")

def remover_fruta(lista, fruta):
    if fruta in lista:
        print(f"Removendo a primeira ocorrência do elemento '{fruta}'...")
        lista.remove(fruta)

    else:
        print(f"A fruta '{fruta}' não está na lista!")

def ordenar_lista(lista, reverso=False):
    lista.sort(reverse=reverso)
    print("Lista ordenada com sucesso!")

def main():
    lista_frutas = ["banana", "uva", "banana", "maça", "laranja"]
    mostrar_lista(lista_frutas)
    remover_fruta(lista_frutas, "banana")
    ordenar_lista(lista_frutas)
    print(lista_frutas)
    print("\nFim!")

if __name__ == "__main__":
    main()

#3

def ler_numero(posicao):
    return int(input(f"Digite o {posicao}º número: "))

def somar_tres_numeros(a, b, c):
    return a + b + c

def main():
    digito_um = ler_numero(1)
    digito_dois = ler_numero(2)
    digito_tres = ler_numero(3)
    soma = somar_tres_numeros(digito_um, digito_dois, digito_tres)
    print("A soma dos números é:", soma)

if __name__ == "__main__":

    main()

#4
def palindromo(Texto):
    Texto = Texto.replace(" ", "").lower()  
    return Texto == Texto[::-1]
print(palindromo("Micheli"))  
print(palindromo("Ana"))  

#5
def frequencia_palavras(texto):
    texto = texto.lower()            
    palavras = texto.split()        
    freq = {}                        

    for p in palavras:              
        if p in freq:
            freq[p] += 1              
        else:
            freq[p] = 1              

    return freq

#Teste: 5 e 6 
import unittest

def palindromo(texto):

    texto = texto.replace(" ", "").lower()
    return texto == texto[::-1]

def frequencia_palavras(texto):

    texto = texto.lower()
    palavras = texto.split()

    freq = {}

    for p in palavras:

        if p in freq:
            freq[p] += 1

        else:
            freq[p] = 1

    return freq

class TesteFuncoes(unittest.TestCase):

    def test_palindromos(self):
        self.assertTrue(palindromo("A sacada da casa"))
        self.assertTrue(palindromo("Ana"))
        self.assertTrue(palindromo("Ovo"))

    def test_nao_palindromos(self):
        self.assertFalse(palindromo("Lari"))
        self.assertFalse(palindromo("Lua"))

    def test_frequencias(self):
        frase = "A lua é linda, linda é a lua"
        resultado = frequencia_palavras(frase)
        esperado = {
            'a': 2,
            'lua': 2,
            'é': 2,
            'linda': 1,
            'linda': 1,
        }

        self.assertEqual(resultado, esperado)

    def test_frase_simples(self):
        frase = "ooi ooi"
        resultado = frequencia_palavras(frase)
        esperado = {'ooi': 2}
        self.assertEqual(resultado, esperado)

if __name__ == "__main__":
    unittest.main()

#6

def media_lista(lista):
    if not lista:
        return None
    soma = sum(lista)
    quantidade = len(lista)
    return soma / quantidade

print("\n--- 6. Média dos Elementos ---")
lista_numeros = [10, 20, 30, 40]
print(f"Média de {lista_numeros}: {media_lista(lista_numeros)}") # Deve retornar 100 / 4 = 25.0
print(f"Média de lista vazia: {media_lista([])}") # Deve retornar None
