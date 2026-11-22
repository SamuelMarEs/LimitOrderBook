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
from nivel_precio import Cola


def padre(i):
    return (i - 1) // 2
def izquierdo(i):
    return 2 * i + 1
def derecho(i):
    return 2 * i + 2

class Nodo_precio:
    def __init__(self, precio : float):
        self.precio = precio
        self.indice = None

class Heap_ordenes:
    def __init__(self):
        self.datos : list[Nodo_precio] = []
        self.tamano = 0
        self.niveles : dict[float, Cola] = {}

    def gana(self, a, b):
        raise NotImplementedError

    #---Operaciones Basicas---
    def intercambiar(self, i, j):
        A = self.datos
        A[i], A[j] = A[j], A[i]
        A[i].indice = i
        A[j].indice = j

    def flotar(self, i):
        A = self.datos
        while i > 0 and self.gana(A[i], A[padre(i)]):
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
        while self.tamano > 0 and self.niveles[self.datos[0].precio].activas == 0:
            # Si no hay ofertas activas en el precio
            # Elimina el precio
            self.eliminar(0)
        return self.datos[0] if self.tamano > 0 else None 

    def mejor_precio(self):
        nodo = self.cima()
        return nodo.precio if nodo else None

    def insertar(self, orden : Orden):
        precio = orden.precio
        if precio not in self.niveles:
            nodo = Nodo_precio(precio)
            nodo.indice = self.tamano
            self.datos.append(nodo)
            self.tamano += 1
            self.flotar(nodo.indice)
            self.niveles[precio] = Cola()
        self.niveles[precio].encolar(orden)

    def eliminar(self, indice):
        precio = self.datos[indice].precio
        u = self.tamano - 1
        if indice != u:
            self.intercambiar(indice, u)
        self.datos.pop().indice = None
        self.tamano = u
        if indice < self.tamano:
            self.flotar(indice)
            self.hundir(indice)
        del self.niveles[precio]

class Bid_heap(Heap_ordenes):
    def gana(self, a, b):
        return a.precio > b.precio
    
class Ask_heap(Heap_ordenes):
    def gana(self, a, b):
        return a.precio < b.precio

