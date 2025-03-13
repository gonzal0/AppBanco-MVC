import tkinter as tk
from View.BancoApp import BancoApp
from Controller.BancoController import BancoController

if __name__ == "__main__":
    root = tk.Tk()
    controller = BancoController(None)  # El controlador se asigna después
    view = BancoApp(root, controller)
    controller.view = view  # Asignar la vista al controlador
    root.mainloop()