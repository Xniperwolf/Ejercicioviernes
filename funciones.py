def asientoaelegir():
            while True:
            try:
                asientoelegido = int(input("Ingrese asiento a elegir (12 asientos): "))
                for x in bus:
                    if asientoelegido in x[bus] and x[bus] == 0:
                        bus[x[asientoelegido]] = "$"
                        print("Asiento elegido con éxito")
                        break
                    else:
                        if asientoelegido in bus:
                            print("Asiento ya ocupado, elija otro.")
            except:
                print("Ingrese un número entero")