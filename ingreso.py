from movimiento import Movimiento
from datetime import date

# Clase de Ingreso que hereda de Movimiento
class Ingreso(Movimiento):
    def __init__(self, concepto: str, cantidad: float, fecha: date):
        super().__init__(concepto, fecha)
        self.cantidad = cantidad

    def importe(self):
        return self.cantidad # Definimos que el gasto tiene importe positivo