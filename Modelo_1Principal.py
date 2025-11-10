from Modelo_2vehiculo import Vehiculo
from Modelo_3automovil import Automovil
from Modelo_4van import Van
from Modelo_5volqueta import Volqueta

#=== Programa principal ===
while True:
    print("\n=== MENÚ DE VEHÍCULOS ===")
    print("1. Automóvil")
    print("2. Van")
    print("3. Volqueta")
    print("4. Salir")
    opcion = input("Seleccione la opcion(1-4): \n")
    
    match opcion:
        case "1":
            auto = Automovil()
            print("\n--- INGRESAR DATOS DEL AUTOMÓVIL ---")
            auto.ingresar_datos()
            auto.imprimir_datos()
            auto.tipo_seguridad()
            auto.funcionamiento()

        case "2":
            van = Van()
            print("\n--- INGRESAR DATOS DE LA VAN ---")
            van.ingresar_datos()
            van.imprimir_datos()
            van.tipo_seguridad()
            van.funcionamiento()

        case "3":
            volqueta = Volqueta()
            print("\n--- INGRESAR DATOS DE LA VOLQUETA ---")
            volqueta.ingresar_datos()
            volqueta.imprimir_datos()
            volqueta.tipo_seguridad()
            volqueta.funcionamiento()

        case "4":
            print("Saliendo....")
            break