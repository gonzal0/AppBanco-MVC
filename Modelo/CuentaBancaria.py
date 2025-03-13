import tkinter as tk
from tkinter import messagebox
#from CuentaBancaria import CuentaBancaria

# Clase que representa una Cuenta Bancaria
class CuentaBancaria:
    def __init__(self, titular, saldo=0.0):
        self.titular = titular
        self.saldo = saldo

    def depositar(self, cantidad):
        if cantidad > 0:
            self.saldo += cantidad
            return f"Depósito exitoso. Nuevo saldo: ${self.saldo:.2f}"
        return "Cantidad inválida para depositar."

    def retirar(self, cantidad):
        if 0 < cantidad <= self.saldo:
            self.saldo -= cantidad
            return f"Retiro exitoso. Nuevo saldo: ${self.saldo:.2f}"
        return "Fondos insuficientes o cantidad inválida."

    def consultar_saldo(self):
        return f"Saldo actual: ${self.saldo:.2f}"