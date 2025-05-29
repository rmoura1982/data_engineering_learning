# Tipos de Dados (principais)

# int: número inteiro
idade = 42
print(idade, type(idade))  # saída: 42 <class 'int'>

# float: número decimal
altura = 1.75
print(altura, type(altura))  # saída: 1.75 <class 'float'>

# str: texto
nome = "Rodrigo"
print(nome, type(nome))  # saída: Rodrigo <class 'str'>

# datetime: data e hora
from datetime import datetime
agora = datetime.now()
print(agora, type(agora))  # saída: 2025-05-29 14:23:45.123456 <class 'datetime.datetime'>

#############################################################################################
# Estruturas de Dados

# list: sequência mutável (pode mudar)
lista = [1, 2, 3]
print(lista, type(lista))  # saída: [1, 2, 3] <class 'list'>

# tuple: sequência imutável (não pode mudar)
tupla = (1, 2, 3)
print(tupla, type(tupla))  # saída: (1, 2, 3) <class 'tuple'>

# dict: estrutura chave-valor
dicionario = {"nome": "Rodrigo", "idade": 42}
print(dicionario, type(dicionario))  # saída: {'nome': 'Rodrigo', 'idade': 42} <class 'dict'>

# set: coleção de elementos únicos e não ordenados
conjunto = {1, 2, 3}
print(conjunto, type(conjunto))  # saída: {1, 2, 3} <class 'set'>

#############################################################################################
# Estruturas de Controle

# Condicional simples
idade = 20
if idade >= 18:
    print("Maior de idade")       # saída: Maior de idade
else:
    print("Menor de idade")

# Laço for com lista
frutas = ["maçã", "banana", "laranja"]
for fruta in frutas:
    print(fruta)
    # saída:
    # maçã
    # banana
    # laranja

# Laço while com contador
contador = 0
while contador < 3:
    print("Contador:", contador)
    contador += 1
    # saída:
    # Contador: 0
    # Contador: 1
    # Contador: 2

#############################################################################################
# Funções

# Função comum (sem args e kwargs)
def saudacao(nome):
    print("Olá,", nome)

saudacao("Rodrigo")  # saída: Olá, Rodrigo

# Função com *args (vários valores)
def somar(*args):
    print("Soma:", sum(args))

somar(1, 2, 3)  # saída: Soma: 6

# Função com **kwargs (vários pares chave-valor)
def exibir_info(**kwargs):
    for chave, valor in kwargs.items():
        print(f"{chave}: {valor}")

exibir_info(nome="Rodrigo", idade=42)
# saída:
# nome: Rodrigo
# idade: 42

#############################################################################################
# Módulos e Pacotes

# Importação comum de um módulo
import math
print(math.sqrt(16))  # saída: 4.0

# Importação específica de uma função
from math import sqrt
print(sqrt(25))  # saída: 5.0

#############################################################################################
# Tratamento de Erros (pricipais)

# Blocos try e except
try:
    resultado = 10 / 0  # isso causará um erro
except Exception as erro:
    print("Ocorreu um erro:", erro)

# saída: Ocorreu um erro: division by zero

#############################################################################################
# Manipulação de Arquivos

# Escrevendo em um arquivo
with open("exemplo.txt", "w") as f:
    f.write("Olá, Rodrigo!")

# Lendo o conteúdo do arquivo
with open("exemplo.txt", "r") as f:
    conteudo = f.read()
    print(conteudo)

# saída: Olá, Rodrigo!

#############################################################################################
# Orientação a Objetos (POO)

# Definindo uma classe
class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

# Criando um objeto da classe
p1 = Pessoa("Rodrigo", 42)

# Acessando os atributos
print(p1.nome)   # saída: Rodrigo
print(p1.idade)  # saída: 42

#############################################################################################
