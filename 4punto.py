
candidato1 = 0
candidato2 = 0
candidato3 = 0


for i in range(2500000):
    voto = int(input("Ingrese el número del candidato por el cual votó: "))
    
   
    if voto == 1:
        candidato1 += 1
    elif voto == 2:
        candidato2 += 1
    elif voto == 3:
        candidato3 += 1


if candidato1 > candidato2 and candidato1 > candidato3:
    print("El ganador es el candidato 1 con un total de", candidato1, "votos")
elif candidato2 > candidato1 and candidato2 > candidato3:
    print("El ganador es el candidato 2 con un total de", candidato2, "votos")
elif candidato3 > candidato1 and candidato3 > candidato2:
    print("El ganador es el candidato 3 con un total de", candidato3, "votos")
else:
    print("Hubo un empate entre dos o más candidatos.")
