from gasto import Gasto
from ingreso import Ingreso

# Clase GestorGastos donde gestionamos los métodos de agregar y eliminar movimientos
# y de listar el saldo total
class GestorGastos:
    def __init__(self):
        self.movimientos = []
        self._id_movimiento = 1

    def agregar(self, movimiento):
        movimiento.id = self._id_movimiento
        self._id_movimiento += 1
        self.movimientos.append(movimiento)

    def eliminar(self, id):
        for i in self.movimientos:
            if i.id == id:
                self.movimientos.remove(i)
                return True
        return False    

    def saldo_total(self):
        return sum(i.importe() for i in self.movimientos)
    
