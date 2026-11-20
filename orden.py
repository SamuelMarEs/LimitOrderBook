"""
Autor: Samuel Márquez Estrada
Date: nov 14 2026
Class orden para guardar las distintas ofertas de compra y venta para el LOB
"""
class Orden:
    def __init__(self, id : str, lado : str, precio : float, cantidad : float, timestamp : int):
        self.id = id
        self.lado = lado
        self.precio = precio
        self.cantidad = cantidad
        self.timestammp = timestamp
        self.anterior = None
        self.siguiente = None