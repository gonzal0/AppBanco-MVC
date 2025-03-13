# Clase principal de la aplicación
import tkinter as tk
from tkinter import messagebox
from Modelo.CuentaBancaria import CuentaBancaria

class BancoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Banco POO - Tkinter")
        self.root.geometry("300x200")

        self.cuenta = CuentaBancaria("Usuario")
        
        # Etiqueta de saldo
        self.label_saldo = tk.Label(root, text=self.cuenta.consultar_saldo(), font=("Arial", 12))
        self.label_saldo.pack(pady=10)
        
        # Entrada de cantidad
        self.entry_cantidad = tk.Entry(root)
        self.entry_cantidad.pack(pady=5)
        
        # Botones de operación
        btn_depositar = tk.Button(root, text="Depositar", command=self.depositar)
        btn_depositar.pack(pady=5)
        
        btn_retirar = tk.Button(root, text="Retirar", command=self.retirar)
        btn_retirar.pack(pady=5)
        
    def actualizar_saldo(self):
        self.label_saldo.config(text=self.cuenta.consultar_saldo())

    def depositar(self):
        try:
            cantidad = float(self.entry_cantidad.get())
            mensaje = self.cuenta.depositar(cantidad)
            messagebox.showinfo("Depósito", mensaje)
            self.actualizar_saldo()
        except ValueError:
            messagebox.showerror("Error", "Ingrese un número válido")

    def retirar(self):
        try:
            cantidad = float(self.entry_cantidad.get())
            mensaje = self.cuenta.retirar(cantidad)
            messagebox.showinfo("Retiro", mensaje)
            self.actualizar_saldo()
        except ValueError:
            messagebox.showerror("Error", "Ingrese un número válido")
