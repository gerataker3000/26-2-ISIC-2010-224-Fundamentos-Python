def dinerito(dinero,loqueGaste):
    print("dinero", dinero)
    print("lo que gaste", loqueGaste)
    print("Lo que mq euda",dinero-loqueGaste)

def mensaje_amor_reutilizado_de_mi_ex(nombreDeLaSupesta ="Querida", loQueGaste=10,saldo = 1500000):
    print("Buenos días ",nombreDeLaSupesta)
    print("Ya saque el loQueGaste para la noche fue",loQueGaste)
    print("Tu ponte linda y ya sabes qué hacer, te amo")
    dinerito(saldo,loQueGaste)
    print("================ MENSAJE FINALIZADO DEL INGE TA SOLITIO =====================")
    print("")

def caliInge(cali1,calif2):
    return (cali1+calif2)/2


calificacionFinal = caliInge(90,70)
print(calificacionFinal)
print(caliInge(85,70))


# mensaje_amor_reutilizado_de_mi_ex("Elizabeth olsen", 1000)
# mensaje_amor_reutilizado_de_mi_ex("Scarlett Johansson")
# mensaje_amor_reutilizado_de_mi_ex()
