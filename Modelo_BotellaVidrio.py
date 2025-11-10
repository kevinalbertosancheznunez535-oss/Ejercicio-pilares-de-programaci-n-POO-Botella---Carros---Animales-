from Modelo_Botella import Botella
# Clase hija 2 - Botella de Vidrio
class BotellaVidrio(Botella):
    def __init__(self, material, capacidad, forma, diseño, tapa, grabados):
        super().__init__(material, capacidad, forma, diseño, tapa, grabados)

    def contener_liquidos(self):
        print("La botella de vidrio puede contener bebidas frías o calientes.")

    def cierre_hermetico(self):
        print("Tiene un cierre hermético con corcho o tapa metálica.")

    def manejo(self):
        print("Debe manejarse con cuidado para evitar rupturas.")

    def compatibilidad_con_bebidas_calientes_frias(self):
        print("Es compatible con bebidas frías y calientes sin afectar su estructura.")

    def reutilizacion(self):
        print("Puede ser reutilizada muchas veces sin perder calidad.")

    def transparencia_nivel(self):
        print(f"Nivel de transparencia: transparente")