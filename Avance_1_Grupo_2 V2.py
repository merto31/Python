# 6 Avance_1_Grupo_12
#   KENDALL ELIAS QUIRÓS PANIAGUA
#   ANA SABRINA JIMENEZ BARQUERO
#   JOSE ANDRES RIVERA HERRERA


from colorama import init, Fore, Back, Style

init()

precioventa = 0
cantidadhuevos = 0
gastosmantenimeinto = 0
gastosdeagua = 0

while True:
    print(Fore.YELLOW + "=== MENÚ DE OPCIONES ===" + Style.RESET_ALL)
    print("1. Incluir")
    print("2. Consultar")
    print("3. Modificar")
    print("4. Borrar")
    print("5. Salir")

    opcion = input(Fore.BLUE + "Seleccione una opción (1-5): \r\n " + Style.RESET_ALL )

    if opcion == "1":
        print(Fore.GREEN +"Elegiste la opción: Incluir datos"+ Style.RESET_ALL)
        precioventa = int(input("¿Cuál es el precio de venta de los huevos por unidad? \r\n"))
        cantidadhuevos = int(input("¿Cuál fue la cantidad de huevos producidos esta semana? \r\n"))
        gastosmantenimeinto = int(input("¿Cuántos fueron los gastos por mantenimiento? \r\n"))
        gastosdeagua = int(input("¿Cuánto fue el gasto de agua? \r\n"))
        print(Fore.GREEN + "Datos incluidos correctamente." + Style.RESET_ALL )

    elif opcion == "2":
        print(Fore.GREEN +"Has elegido consultar datos."+ Style.RESET_ALL)
        if precioventa != 0 and cantidadhuevos != 0:
            resultadoventa = precioventa * cantidadhuevos
            totalgastos = gastosmantenimeinto + gastosdeagua
            print(f"Para el día de hoy tienes: {cantidadhuevos} huevos")
            print(f"Se espera recibir {resultadoventa} colones por la venta de estos huevos")
            print(f"El monto total de gastos es de: {totalgastos} colones")
        else:
            print(Fore.RED + "Primero debes incluir los datos en la opción 1." + Style.RESET_ALL)

    elif opcion == "3":
        print(Fore.GREEN +"Has elegido modificar datos."+ Style.RESET_ALL)
        precioventa = int(input("Nuevo precio de venta: \r\n"))
        cantidadhuevos = int(input("Nueva cantidad de huevos: \r\n"))
        gastosmantenimeinto = int(input("Nuevos gastos de mantenimiento: \r\n"))
        gastosdeagua = int(input("Nuevo gasto de agua: \r\n"))

    elif opcion == "4":
        print(Fore.GREEN +"Has elegido borrar datos."+ Style.RESET_ALL)
        precioventa = 0
        cantidadhuevos = 0
        gastosmantenimeinto = 0
        gastosdeagua = 0
        print(Fore.GREEN +"Datos borrados correctamente."+ Style.RESET_ALL)

    elif opcion == "5":
        print(Fore.YELLOW +"Saliendo del programa. ¡Adiós!")
        break

    else:
        print(Fore.RED + "Opción no válida. Por favor, seleccione una opción del 1 al 5." + Style.RESET_ALL)