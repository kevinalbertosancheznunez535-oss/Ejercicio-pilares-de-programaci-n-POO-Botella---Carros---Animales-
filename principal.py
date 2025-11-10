from Modelo_BotellaPlastica import BotellaPlastica
from Modelo_BotellaVidrio import BotellaVidrio
# Programa principal
while True:
    print("1. Botella Plástica")
    print("2. Botella de Vidrio")
    print("3. Salir")
    opcion = int(input("Seleccione el tipo de botella para saber el dato (1-3): "))
    match opcion:
        case 1:
            print("=== Botella Plástica ===")
            plastica = BotellaPlastica("Plástico", "600ml", "Cilíndrica", "Moderno", "Rosca", "Sin grabado")
            plastica.imprimir_datos()
            plastica.contener_liquidos()
            plastica.cierre_hermetico()
            plastica.reutilizacion()
            plastica.transparencia()
        case 2:
            print("\n=== Botella de Vidrio ===")
            vidrio = BotellaVidrio("Vidrio", "1L", "Recta", "Clásico", "Corcho", "Logo grabado")
            vidrio.imprimir_datos()
            vidrio.contener_liquidos()
            vidrio.cierre_hermetico()
            vidrio.reutilizacion()
            vidrio.transparencia_nivel()
        case 3:
            print("saliendo...")
            break