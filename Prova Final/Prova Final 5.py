def primeiraMatriz():
    matriz = [
        [0, 0, 0],
        [0, 0, 0],
        [0, 0, 0]
    ]
    for linha in range(3):
        for coluna in range(3):
            matriz[linha][coluna] = int(input("Escolha um número: "))


    for linha in range(3):
        print(matriz[linha])

    return matriz


print(primeiraMatriz())


def listaPalavras():
    palavras = []

    for word in range(5):
        palavras1 = str(input("Escreva uma palavra: "))
        palavras.append(palavras1)

    return palavras


print(listaPalavras())


def ultimaLista():
    lista = []

    for numero in range(5):
        numero1 = int(input("Escolha um número: "))
        lista.append(numero1)

    print(lista)

    return lista


print(ultimaLista())
