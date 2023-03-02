repetir = 0 

while repetir == 0:
    
    libro = input("Que libro esta buscando? ")
    id = int(input("Diga el ID del libro: "))
    precio = float(input("Cual es el precio? "))
    envio = (input("El envio es gratis?(Si) o (No) "))

    if envio == "Si":
       print(f"""
            Nombre: {libro}
            Id: {id}
            Precio: {precio}
            Envio gratis: {envio}
            \n Gracias por su compra

       """)
    

    else:
        print(f"Lo siento pero el libro de {libro} no tiene envio gratis")

    repetir = int(input("Desea repetir el programa? Si(0) No(1)"))

print("Fin del programa")