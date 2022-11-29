import random

matriz = []

for i in range(4):
    listaLinhas = []
    for j in range(3):
        real = round(random.uniform(1.0, 9.0), 1)
        listaLinhas.append(real)

    matriz.append(listaLinhas)

for i in range(4):
    print(matriz[i])

soma = sum(matriz[i % 2 == 0])
media = [sum(matriz[1]) + sum(matriz[3]) / 3]

for i in range(3):
    matrizSomas = sum(matriz[0] + matriz[1])

matrizNova = [matriz[0] + matriz[1]]

print(f'soma dos elementos das colunas ímpares: {soma}')
print(f'média aritmética da segunda e quarta coluna: {media}')
print(f'valores da terceira coluna pela soma dos valores das colunas 1 e 2. : {matrizNova}')
for i in range(4):
    print(matriz[i])