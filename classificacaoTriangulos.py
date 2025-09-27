# Solicita ao usuário três valores para os segmentos e converte para float
r1 = float(input("Primeiro segmento: "))
r2 = float(input("Segundo Segmento: "))
r3 = float(input("Terceiro Segmento: "))

# Verifica se os segmentos podem formar um triângulo usando a regra da desigualdade
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print("Os seguimentos acima podem formar um TRIANGULO!")

    # Se todos os lados forem iguais, é um triângulo equilátero
    if r1 == r2 == r3:
        print("EQUILATERO")

    # Se todos os lados forem diferentes, é um triângulo escaleno
    elif r1 != r2 != r3 != r1:
        print("ESCALENO")

    # Caso contrário, dois lados são iguais — é isósceles
    else:
        print("ISÓCELES")

# Caso os segmentos não formem um triângulo, exibe a mensagem de erro
else:
    print("Os segmentos acima NÃO pode formar um TRIANGULO!")
