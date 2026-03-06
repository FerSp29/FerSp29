ombre_cajero = "Cajero El Gran Riwi"
print(f"Bienvenido a {nombre_cajero} ")

claveaunth= 7023
intentos = 3
Saldo = 1000
autenticado = False

while intentos > 0:
    Contraseña = int(input(f"Digite su contraseña (intentos restantes {intentos}): "))

    if Contraseña == claveaunth:
        print("La Contraseña es correcta, bienvenido")
        autenticado = True
        break
    else: 
        intentos -= 1
        print("La contraseña que se ingreso no es correcta.")

    if intentos == 0 and not autenticado:
        print("Ha agotado sus inetentos disponibles, su cuenta ha sido bloqueada")

        
while autenticado:
        print("\n1 Consultar Saldo")
        print("\n2 Retirar monto")
        print("\n3 Depositar monto")
        print("\n4 Salir")
        opcion = input("Elija una opcion de lo que desea hacer:")

        if opcion == "1":
            print(f"Su saldo es: ${Saldo}")

        elif opcion == "2":
            retiro = float(input("¿Cuanto desea retirar?:"))
            if retiro > Saldo:
                print("El Saldo es insuficiente.")
            elif retiro <= 0:
                print("El monto es invalido")
            else:
                Saldo -= retiro
                print(f"El retiro fue exitoso. El Saldo restante es: ${Saldo} ")

        elif opcion == "3":
            deposito = float(input("¿Cuanto desea depositar?: "))
            if deposito <= 0:
                print("El monto no es valido")
            else:
                Saldo += deposito
                print(f"El deposito ha sido exitoso. Su nuevo saldo es: ${Saldo}")

        elif opcion == "4":
            print("Gracias por usar el cajero, vuelva pronto, Adios")
            break
        else:
            print("La opcion no es valida")
