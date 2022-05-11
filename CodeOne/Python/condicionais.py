# > ESTRUTURAS CONDICIONAIS

idade = 18

if idade >= 18:
    print("Você é maior de idade.")
else:
    print("Você é menor de idade.")

"""
  Imagine que você queira imprimir "Aprovada(o)" caso o estudante tenha uma média superior ou igual a 7, e "Reprovada(o)", caso a média seja inferior a 7.
"""

media = float(input("Informe a média do estudante: "))

if media >= 7:
    print("Você foi aprováda(o)!")
elif media >= 5:
    print("Você ficou de recuperação!")
else:
    print("Você foi reprovada(o).")

# Para uso de duas condições conjuntamente:

media = float(input("Informe a média do estudante: "))
presenca = float(input("Informe a presença do estudante: "))

if media >= 7 and presenca >= 75:
    print("Você foi aprovada(o)!")
    print("Parabéns!")
else:
    print("Você foi reprovada(o).")
    print("Tente novamente!")

# O operador and é usado quando duas comparações devem ser verdadeiras para atender a condição e o operador or é utilizado quando apenas uma das comparações precisa ser verdadeira para que a condição seja atendida.
