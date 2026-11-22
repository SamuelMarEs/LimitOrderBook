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

class Heap_ordenes:
    def __init__(self):
        self.datos : list[Nodo_precio] = []
        self.tamano = 0
        self.niveles : dict[Cola] = {}

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
        if self.tamano == 0:
            return None
        cima = self.datos[0]
        
        while cima is not None and self.niveles[cima.precio].activas == 0:
            # Si no hay ofertas activas en el precio
            # Elimina el precio
            self.eliminar(0)
            # Actualiza la cima del heap
            cima = self.datos[0]
        return cima 

    def mejor_precio(self):
        nodo = self.cima()
        return nodo.precio if nodo else None

    def insertar(self, orden : Orden):
        precio = orden.precio
        if precio in self.niveles:
            # Si el precio ya está en el heap, no hace falta volverlo a añadir
            # Añade la oferta al nivel correspondiente
            self.niveles[precio].encolar(orden)
        else:
            if self.tamano == len(self.datos):
                self.datos.append(None)
            # Añade el precio al heap
            i = self.tamano
            nodo = Nodo_precio(precio)
            self.datos[i] = nodo
            nodo.indice = i
            self.tamano += 1
            self.flotar(i)
            # Crea un nivel nuevo
            self.niveles[precio] = Cola()
            # Añade la oferta al nivel correspondiente
            self.niveles[precio].encolar(orden)

    def extraer(self):
        if self.tamano == 0:
            raise IndexError("heap vacio")
        cima : Nodo_precio = self.cima()
        while self.niveles[cima.precio].activas == 0:
            # Si no hay ordenes activas en este nivel de precio
            # Entonces elimina el precio de la cima
            self.eliminar(0)
            # Actualiza la cima
            cima = self.cima()
        return cima.precio
    
    def eliminar(self, indice):
        i = indice
        u = self.tamano - 1
        if i != u:
            self.intercambiar(i, u)
        self.datos[u].indice = None
        self.datos[u] = None
        self.tamano = u
        if i < self.tamano:
            self.flotar(i)
            self.hundir(i)

class Bid_heap(Heap_ordenes):
    def gana(self, a, b):
        if b is not None:
            return a.precio > b.precio
        else:
            return True
    
class Ask_heap(Heap_ordenes):
    def gana(self, a, b):
        if b is not None:
            return a.precio < b.precio
        else:
            return True
