"""
Autor: Emiliano Panuncio Almaraz Gonzalez
Date: nov 20 2026
Heaps de bids (compras) y asks (ventas) para el Limit Order Book

Prioridad precio-tiempo:
- Bid_heap: gana el precio MÁS ALTO (max-heap)
- Ask_heap: gana el precio MÁS BAJO (min-heap)
- A igual precio, gana la que llegó antes (timestamp menor)
"""

from orden import Orden

def padre(i):
    return (i - 1) // 2
def izquierdo(i):
    return 2 * i + 1
def derecho(i):
    return 2 * i + 2

class Heap_ordenes:
    def __init__(self):
        self.datos = []
        self.tamano = 0

    def gana(self, a, b):
        raise NotImplementedError

    #---Operaciones Basicas---
    def intercambiar(self, i, j):
        A = self.datos
        A[i], A[j] = A[j], A[i]
        A[i].key = i
        A[j].key = j

    def flotar(self, i):
        A = self.datos
        while i > self.gana(A[i], A[padre(i)]):
            p = padre(i)
            self.intercambiar(i,p)
            i = p

    def hundir(self, i):
        A, n = self.datos, self.tamano
        l, r = izquierdo(i), derecho(i)
        mejor = i

        if l < n and self.gana(A[l], A[mejor]):
            mejor = l
        if r < n and self.gana(A[r], A[mejor]):
            mejor = r
        if mejor != i:
            self.intercambiar(i, mejor)
            self.hundir(mejor)

    #---Operaciones de Cola de Prioridad---
    def vacio(self):
        return self.tamano == 0

    def cima(self):
        if self.tamano == 0:
            return None
        return self.datos[0]

    def mejor_precio(self):
        orden = self.cima()
        return orden.precio if orden else None

    def insertar(self, orden):
        if self.tamano == len(self.datos):
            self.datos.append(None)
        i = self.tamano
        self.datos[i] = orden
        orden.key = i
        self.tamano += 1
        self.flotar(i)

    def extraer(self):
        if self.tamano == 0:
            raise IndexError("heap vacio")
        return self.eliminar(self.datos[0])

    def eliminar(self, orden):
        i = orden.key
        u = self.tamano - 1
        if i != u:
            self.intercambiar(i, u)
        self.datos[u] = None
        self.tamano = u
        orden.indice = None
        if i < self.tamano:
            self.flotar(i)
            self.hundir(i)
        return orden

class Bid_heap(Heap_ordenes):
    def gana(self, a, b):
        if a.precio != b.precio:
            return a.precio > b.precio
        return a.timestamp < b.precio
    
class Ask_heap(Heap_ordenes):
    def gana(self, a, b):
        if a.precio != b.precio:
            return a.precio < b.precio
        return a.timestamp < b.precio