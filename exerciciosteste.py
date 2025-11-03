# 1. Classificação de Idade
# Peça a idade do usuário e classifique-o de acordo com a tabela:
# Menor de 12 anos → Criança
# Entre 12 e 17 anos → Adolescente
# 18 anos ou mais → Adulto

def classificar_idade(idade):
    if idade < 12 and idade >= 1:
        return 'Criança'
    elif idade >= 12 and idade <= 17:
        return 'Adolescente'
    elif idade >= 18 and idade <= 100:
        return 'Adulto'
    else:
        return 'Idade Inválida' 

# 2. Maior de Dois Números
# Solicite dois números ao usuário e exiba o maior deles. Caso sejam iguais, informe isso.

def comparar_numeros(numero1, numero2):
    if numero1 > numero2:
        return f'{numero1} é maior que {numero2}'
    elif numero1 == numero2:
        return f'{numero1} é igual a {numero2}'
    else:
        return f'{numero1} é menor que {numero2}'

# 3. Verificação de Vogal ou Consoante
# Peça ao usuário para digitar uma letra e informe se é uma vogal (a, e, i, o, u) ou consoante.

def comparar_vogal_consoante(letra):
    if letra == 'a' or letra == 'e' or letra == 'i' or letra == 'o' or letra == 'u':
        return f'A letra digitada é uma vogal'
    else:
        return f'A letra digitada é uma consoante'
    
# 4. Comparação de Senhas
# Solicite ao usuário que defina uma senha e, em seguida, peça para confirmá-la. Caso as senhas sejam iguais, exiba “Acesso permitido”, senão, exiba “Senhas não coincidem”.

def comparar_senhas(senha, senhaconfirmada):
    if(senha == senhaconfirmada):
        return 'Acesso permitido!'
    else:
        return 'Acesso negado!'
    
# 5. Cálculo de Média e Aprovação
# Peça ao usuário para digitar três notas e calcule a média. Se a média for maior ou igual a 7, o aluno está aprovado, caso contrário, está reprovado.

def calcular_media(nota1, nota2, nota3):
    media = (nota1 + nota2 + nota3) / 3
    if media >= 7 and media <= 10:
        return f'O aluno está aprovado com média: {media}!'
    elif media < 7 and media >= 0:
        return f'O aluno está reprovado com média: {media}!'
    else:
        return f'Média inválida!'
    
# 6. Escreva um programa que leia 3 números inteiros e imprima na tela os valores em ordem decrescente

def numeros_ordem_decrescente(numero1, numero2, numero3):
    listaDeNumeros = [numero1, numero2, numero3]
    return f'A lista dos números em ordem decrescente é: {sorted(listaDeNumeros,reverse=True)}'









    
    




    

