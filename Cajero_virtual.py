 #sistema cajero automatico-version en clase 
saldo = 1500 #saldo inicial 
print("=" * 35)
print(" Bienvenido al cajero virtual")
print("=" * 35)

#OPCIONES 
print("\n ¿que desea hacer?")
print("1, consultar saldo")
print("2, retirar dinero")
print("3, salir")
print("4, depositar dinero")
print("-" * 35)
opcion = input("elige una opcion: ")

#validacion de datos 
if opcion not in ("1", "2", "3", "4"):
    print("opcion no valida, por favor elige 1, 2, 3 o 4")
elif opcion =="1":
    print(f"\ntu saldo actual es: ${saldo}")
elif opcion == "2":
    monto = input("¿cuanto deseas retirar? $")
    if not monto.isdigit():
        print("debes ingresar un numero valido")
    else:
        monto = int(monto)
        if monto <= 0:
            print("el monto debe ser mayor a cero")
        elif monto > saldo:
            print(f"saldo insuficiente. solo tienes ${saldo}")
        else:
            saldo = saldo - monto 
            print(f"retiro exitoso. Nuevo saldo: ${saldo}")
elif opcion == "3":
    print("\ngracias por usar el cajero. Hasta luego")

    #opcion 4: depositar dinero  
elif opcion == "4":
    monto_texto = input("¿ cuanto deseas depositar? $")
    if not monto_texto.isdigit():
        print("debes de ingresar un numero valido")
    else:
        monto = int(monto_texto)
        if monto <= 0:
            print("el monto debe ser mayor a cero.")
        else:
            saldo += monto
            print(f"\nDeposito exitoso. Nuevo saldo: ${saldo}")

