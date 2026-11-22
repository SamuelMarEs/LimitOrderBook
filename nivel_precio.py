"""
Autor: Samuel Márquez Estrada
Date: nov 19 2026
Cola FIFO implementada como lista doblemente enlazada. La idea es ordenar las ofertas por orden de llegada dentro del mismo precio
"""
from orden import Orden

class Cola: 
    def __init__(self):
        """Inicializa la cola con head y tail en None
        """
        self.head = None
        self.tail = None
        self.activas = 0
        
    def desencolar(self) -> Orden:
        """Desencola el primer nodo de la cola (FIFO)

        Returns:
            Orden: orden al inicio de la cola desenlazado
            
        Raises:
            IndexError: si la cola está vacía
        """
        if self.head is None:
            raise IndexError("Cola vacía")
        
        nodo : Orden = self.head
        self.eliminar(nodo)
        return nodo
    
    def encolar(self, nodo : Orden):
        """Añade un nuevo nodo a la cola

        Args:
            nodo (Orden): nodo que se va a añadir al final de la cola
        """
        nodo.siguiente = None
        nodo.anterior = self.tail
        if self.tail is None:
            self.head = nodo
        else:
            self.tail.siguiente = nodo
        self.tail = nodo
        self.activas += 1
        
    def eliminar(self, nodo : Orden):
        """Elimina un nodo conocido

        Args:
            nodo (Nodo): nodo que se quiere eliminar
        """
        if nodo.anterior is not None:
            nodo.anterior.siguiente = nodo.siguiente
        else:
            self.head = nodo.siguiente
        if nodo.siguiente is not None:
            nodo.siguiente.anterior = nodo.anterior
        else:
            self.tail = nodo.anterior
        nodo.anterior = nodo.siguiente = None
        self.activas -= 1