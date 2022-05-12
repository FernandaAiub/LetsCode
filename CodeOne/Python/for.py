for variavel in range(10):
    print(variavel)

for variavel in range(1, 10):
    print(variavel)

for variavel in range(1, 12, 3):
    print(variavel)

# A função range para no número anterior ao parâmetro de parada
# Na função range é possível passar de um a três parâmetros:
# Um parâmetro: conta de 0 ao número anterior ao parâmetro dado
# Dois parâmetros: conta do primeiro parâmetro ao número anterior ao parâmetro dado
# Três parâmetros: conta do primeiro parâmetro ao número anterior ao parâmetro dado na contagem, contando de x em x, sendo x o terceiro parâmetro (no exemplo acima o resultado retornado seria 1, 4, 7, 10)

soma = 0

for i in range(1, 4):
    nota = float(input(f"Informe sua nota {i}: "))

    soma = soma + nota

print("Sua média é:", soma/3)
