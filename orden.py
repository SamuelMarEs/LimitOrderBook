"""
Autor: Samuel Márquez Estrada
Date: nov 19 2026
Class orden para guardar las distintas ofertas de compra y venta para el LOB
"""
class Orden:
    def __init__(self, key : str, lado : str, precio : float, cantidad : float, timestamp : int):
        self.key = key
        self.lado = lado
        self.precio = precio
        self.cantidad = cantidad
        self.timestamp = timestamp
        self.anterior = None
        self.siguiente = None