#Como estuvo tu dia

repetir = 0

while repetir == 0:
    dia = int(input("Como estuvo tu dia del 1 al 10?: "))
    if dia >= 7:
        print("Tuviste un buen dia amigo")
    elif dia < 7 and dia >= 4:
        print("Tuviste un dia regular, mañana sera mejor")
    elif dia < 4:
        print("Tuviste un mal dia, pero las cosas van a mejorar")
    repetir = int(input("Quieres repetir el programa? Si(0) No(1)"))

print("Fin del programa")