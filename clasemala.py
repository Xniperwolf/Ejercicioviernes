import os
import time
import csv
os.system("cls")
filasbus = 6
columnasbus = 6
bus = [['x' for x in range(columnasbus)] for x in range(filasbus)]

ventaspasajeros = []

descmenor18 = 0.2
descmayor65 = 0.15
tarifaentrada = 9500


while True:
    print("Bienvenido al programa de reserva BUS")
    print("--------------------------------------")
    time.sleep(2)

    print("1. Mostrar asientos disponibles")
    print("2. Comprar asiento")
    print("3. Mostrar ventas realizadas")
    print("4. Generar CSV ventas")
    print("5. Salir")

    while True:
        try:
            opc = int(input("Ingrese opción: "))
            if opc in (1,2,3,4,5):
                break
            else:
                print("ERROR! Ingrese una opción válida")
        except:
            print("Debe ser un número entero.")
            break

    if opc == 1:
        print("ASIENTOS:")
        print("---------------")
        for fila in bus:
            print(fila)


    elif opc == 2:
 
        while True:
            nombrepasajero = input("Ingrese nombre de pasajero: ")
            if len(nombrepasajero) >= 3 and nombrepasajero.isalpha():
                break
            else:
                print("Error, ingrese un nombre válido")

        while True:
            try:
                edad = int(input("Ingrese edad: "))
                if edad > 0 and edad < 120:
                    break
                else:
                    print("ERROR! Ingrese una edad entre 0 y 120")
            except:
                print("ERROR! Ingrese un número entero.")

        while True:
            try:
                numerotelefono = int(input("Ingrese número de teléfono: "))
                if len(str(numerotelefono)) == 9:
                    break
                else:
                    print("Ingrese un número de teléfono válido (9 números)")
            except:
                print("Ingrese un número entero.")
        
        
        while True:
            try:
                filaalegeir = int(input("Ingrese fila de asiento a elegir: "))
                columnaaelegir = int(input("Ingrese columna de asiento a elegir: "))
                if bus[filaalegeir-1][columnaaelegir-1]=="O":
                    bus[filaalegeir-1][columnaaelegir-1] = 'X'
                    print("Ha elegido el asiento correctamente")
                    break
                else:
                    print("El asiento está ocupado")
            except:
                print("Ingrese valores numéricos")

        clientebus = {"Nombre": nombrepasajero, "Edad": edad, "Telefono": numerotelefono, "Fila": filaalegeir, "Columna": columnaaelegir}
        ventaspasajeros.append(clientebus)



        print("Su edad es: ",edad)
        if edad < 18:
            preciomenores18 = tarifaentrada*0.2
            print("Su precio a pagar al ser menor de edad es de un 20%, debe pagar: ",preciomenores18)
        else:
            print("Existe descuento para menores de 18 y mayores de 65")

        if edad > 65:
            precioterceraedad = tarifaentrada*0.15
            print("Al ser tercera edad, el descuento es de 15%, y su precio a pagar es de: ", precioterceraedad)

    
    elif opc == 3:
        if len(ventaspasajeros) == 0:
            print("Lista vacía, ingrese un libro en la opción 1")
        else:
            print("Lista de ventas: ")
        for x in ventaspasajeros:
            print(f"Nombre: {x['Nombre']}, Edad: {x['Edad']}, Telefono: {x['Telefono']}, Fila: {x['Fila']}, Columna: {x['Columna']}")
            time.sleep(2)
    
    
    elif opc == 4:
        if len(ventaspasajeros) == 0:
            print("Lista vacía, agregue venta.")

        else:
            with open("asientobuses.csv", "w", newline="") as archivo:
                escritor = csv.DictWriter(archivo, ["Nombre","Edad","Telefono","Fila","Columna"])
                escritor.writerows(ventaspasajeros)
                print("Archivo creado con éxito!")

    else:
        print("Muchas gracias por ocupar el servicio de bus.")
        break
    
        