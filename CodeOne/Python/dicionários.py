# > DICIONÁRIOS

# Criando dicionários

dicionario = {}
dicionario = dict()
dicionario = {"nome": "Fernanda", "idade": 33, "altura": 1.70}

print(dicionario)
print(dicionario["idade"])

# Adicionando elementos em um dicionário

dicionario["programador"] = True

print(dicionario)

dicionario["altura"] = 1.66
# se a chave já existir no dicionário, ela será sobrescrita ao tentar adicionar um novo elemento na mesma chave

print(dicionario)

# Iterando sobre um dicionário

for chave in dicionario:
    print(chave, dicionario[chave])

# Testando a existência de uma chave

print("peso" in dicionario)
print("altura" in dicionario)
