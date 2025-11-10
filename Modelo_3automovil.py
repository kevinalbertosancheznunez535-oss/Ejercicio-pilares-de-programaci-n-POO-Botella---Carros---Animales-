from Modelo_2vehiculo import Vehiculo
# Clase hija 1 - Automóvil
class Automovil(Vehiculo):

    def tipo_seguridad(self):
        print("El automóvil tiene frenos ABS y bolsas de aire frontales.")

    def funcionamiento(self):
        super().arranque()
        super().sistema_direccion()
        super().climatizacion()
        super().luces()