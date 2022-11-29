precoAntigo = float(input("Qual o antigo preço do jogo? "))

if precoAntigo < 20.00:
    porcentagem = 5

elif 20.00 < precoAntigo < 80.00:
    porcentagem = 10

elif precoAntigo > 80.00:
    porcentagem = 15

porcentagem = porcentagem / 100.0
aumento = porcentagem * precoAntigo
precoNovo = precoAntigo + aumento

if precoNovo < 40.00:
    print(precoNovo)
    print("O jogo é barato")

if 40.00 < precoNovo < 80.00:
    print(precoNovo)
    print("O jogo é normal")

if 81.00 < precoNovo < 120.00:
    print(precoNovo)
    print("O jogo é caro")

if precoNovo > 120.00:
    print(precoNovo)
    print("O jogo é muito caro")
