# Importar las clases de los modelos de animales

from Modelo_caballo import caballo
from Modelo_caiman import caiman
from Modelo_pez import pez
from Modelo_escarabajo import escarabajo
from Modelo_pato import pato
# Codigo principal
while True:
    print("1. caballo")
    print("2. caiman")
    print("3. pez")
    print("4. escarabajo")
    print("5. pato")
    print("6. Salir")
    opcion = int(input("Seleccione el tipo de animal para saber el dato (1-6): "))
    match opcion:
        case 1:
            print("=== caballo ===")
            caballo = caballo("caballo", 5, "Pradera", "Herbívoro", "Grande", "Marrón")
            caballo.imprimir_datos()
        case 2:
            print("\n=== caiman ===")
            caiman = caiman("caiman", 8, "Río", "Carnívoro", "Grande", "Verde")
            caiman.imprimir_datos()
        case 3:
            print("\n=== pez ===")
            pez = pez("pez", 2, "agua", "carnivoro", "pequeño", "gris, rojo")
            pez.imprimir_datos()
        case 4:
            print("\n=== escarabajo ===")
            escarabajo = escarabajo("escarabajo", 1, "tierra", "herbivoro", "pequeño", "negro")
            escarabajo.imprimir_datos()
        case 5:
            print("\n=== pato ===")
            pato = pato("pato", 3, "agua", "omnivoro", "mediano", "blanco")
            pato.imprimir_datos()
        case 6:
            print("saliendo...")
            break