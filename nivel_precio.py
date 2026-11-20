"""
Autor: Samuel Márquez Estrada
Date: nov 19 2026
Cola FIFO implementada como lista doblemente enlazada. La idea es ordenar las ordenes por orden de llegada
"""
from orden import Orden

class Cola: 
    def __init__(self):
        """Inicializa la cola con head y tail en None
        """
        self.head = None
        self.tail = None
        
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
        self.head = nodo.siguiente
        self.head.anterior = None
        nodo.siguiente = None
        return nodo
    
    def encolar(self, nodo : Orden):
        """Añade un nuevo nodo a la cola

        Args:
            nodo (Orden): nodo que se va a añadir al final de la cola
        """
        if self.head is None:
            self.head = nodo
            self.tail = nodo
        nodo.anterior = self.tail
        self.tail = nodo
        
    def eliminar(self, nodo : Orden):
        """Elimina un nodo conocido

        Args:
            nodo (Nodo): nodo que se quiere eliminar
        """
        nodo.anterior.siguiente = nodo.siguiente
        nodo.siguiente.anterior = nodo.anterior
        