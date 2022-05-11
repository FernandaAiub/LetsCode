numero_sorteado = 18

numero_escolhido = int(input("Informe um número entre 1 e 99: "))

while numero_escolhido != numero_sorteado:
    print("Você errou o número, tente novamente!")
    numero_escolhido = int(input("Informe um número entre 1 e 99: "))

print("Parabéns! Você acertou!")

# Exemplo 2: estrutura com contador

contador = 0

while contador < 5:
    print(contador)
    contador = contador + 1
