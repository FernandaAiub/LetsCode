# > FUNÇÕES

# 1. O que são funções e por que utilizá-las?

# Funções que já utilizamos anteriormente...

"""print()  # - Imprime uma mensagem (int, float, str, bool) no console (terminal, cmd)
input()  # - Retorna um dado informado pelo usuário (entrada padrão) e pode receber uma string
len()  # - Recebe uma lista e retorna o tamanho dessa lista
max()  # - Retorna o maior valor de uma lista"""

# 2. Criação de Funções

# Função Inicial


def saudacao():
    print("Seja bem-vinda(o)!")
    print("Olá, é um prazer ter você fazendo parte desse curso!")


saudacao()
saudacao()
saudacao()

# Função com parâmetro


def saudacao(nome, curso):
    print(f"Seja bem-vinda(o), {nome}!")
    print(f"Olá, é um prazer ter você fazendo parte do curso de {curso}!")


saudacao("Fernanda", "Python")
saudacao("Augusto", "JavaScript")

# Função com parâmetros default


def saudacao(nome, curso="Python"):
    print(f"Seja bem-vinda(o), {nome}!")
    print(f"Olá, é um prazer ter você fazendo parte do curso de {curso}!")


saudacao("Fernanda", "C++")

# Funções com retorno


def soma(num1, num2):
    return num1 + num2
# Depois do return nada mais que esteja dentro da função será executado
# O return deve ser o último passo na função


resultado = soma(5, 7)

print("O resultado da soma é:", resultado)


def calculadora(num1, num2, operacao="+"):
    if operacao == "+":
        return num1 + num2
    elif operacao == "-":
        return num1 - num2
    elif operacao == "*":
        return num1 * num2
    elif operacao == "/":
        return num1 / num2
    elif operacao == "//":
        return num1 // num2
    elif operacao == "**":
        return num1 ** num2


resultado = calculadora(10, 20, "-")
print(resultado)

resultado = calculadora(10, 20, "**")
print(resultado)
