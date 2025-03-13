from Modelo.CuentaBancaria import CuentaBancaria

class BancoController:
    def __init__(self, view):
        self.view = view
        self.model = CuentaBancaria("Usuario")

    def depositar(self, cantidad):
        try:
            cantidad = float(cantidad)
            mensaje = self.model.depositar(cantidad)
            self.view.mostrar_info(mensaje)
            self.view.actualizar_saldo(self.model.consultar_saldo())
        except ValueError:
            self.view.mostrar_error("Ingrese un número válido")

    def retirar(self, cantidad):
        try:
            cantidad = float(cantidad)
            mensaje = self.model.retirar(cantidad)
            self.view.mostrar_info(mensaje)
            self.view.actualizar_saldo(self.model.consultar_saldo())
        except ValueError:
            self.view.mostrar_error("Ingrese un número válido")