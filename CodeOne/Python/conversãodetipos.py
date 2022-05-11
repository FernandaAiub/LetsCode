# CONVERSÃO DE TIPOS

# A soma de duas strings vai concatená-las.

numero1 = "10"
numero2 = "20"

print(numero1 + numero2)
# O resultado da operação acima é 1020 pois ambos os números são strings
# Python não permite a soma de um int com uma str, então caso um dos números fosse int, a função print retornaria um erro

# Transformando uma string em número inteiro

idade = "27"

print(idade, type(idade))

idade_inteira = int(idade)

print(idade_inteira, type(idade_inteira))

"""
  Assim como existe uma função que transforma algo em número inteiro 'int()', existem funções que transformam algo em outros tipos de dados:
  str()
  float()
  bool()
"""

altura = float(input("Informe a sua altura: "))
# O input sempre irá tratar o dado digitado como texto, então é necessário fazer a conversão para um tipo numérico quando você for pedir um dado do usuário que tenha que ser tratado como número

print(altura, type(altura))
