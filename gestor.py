from gasto import Gasto
from ingreso import Ingreso

#
class GestorGastos:
    def __init__(self):
        self.movimientos = []

    def agregar(self, movimiento):
        self.movimientos.append(movimiento)

    def saldo_total(self):
        return sum(m.importe() for m in self.movimientos)
    
