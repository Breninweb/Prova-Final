numero = int(0)
adicaotres = int(0)
adicaocinco = int(0)

while numero < 1000:
    if numero % 3 == 0:
        adicaotres += numero

    elif numero % 5 == 0:
        adicaocinco += numero
    numero += 1
    
print(adicaotres)
print(adicaocinco)


