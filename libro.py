"""
Autor: Samuel Márquez y Emiliano Panuncio
Date: nov 19 2026
Class Libro con todo lo que corresponde al LimitOrderBook de una acción
"""
from nivel_precio import Cola
from orden import Orden
from lado import Ask_heap, Bid_heap

class Libro:
    def __init__(self):
        self.cola_bids : Cola = Cola()
        self.cola_asks : Cola = Cola()
        self.ofertas : dict = {}
        self.best_bid : float = None
        self.best_ask : float = None
        self.transacciones : list = []
        
        # Esta parte es la que te toca a ti pan
        self.heap_bids = Bid_heap
        self.heap_asks = Ask_heap
        
    def new_bid(self, bid : Orden):
        self.cola_bids.encolar(bid)
        self.ofertas[bid.key] = bid
        
        # Añadir oferta de compra al heap de compras (bids)
        # Que al hacerlo, se actualice tambien el best_bid al precio de la mejor oferta (cima del heap)
    
    def new_ask(self, ask : Orden):
        self.asks.encolar(ask)
        self.ofertas[ask.key] = ask
                    
        # Añadir oferta de compra al heap de ventas (asks)
        # Que al hacerlo, se actualice tambien el best_bid al precio de la mejor oferta (cima del heap)
    
    def cancelar(self, key : str):
        """cancela una orden por su ID

        Args:
            key (str): ID de la orden que se desea cancelar

        Raises:
            IndexError: si la orden no se encuentra en las ofertas
        """
        if key not in self.ofertas:
            raise IndexError("No se encontró la llave")
            
        orden = self.ofertas[key]
        if orden.lado == "venta":
            self.asks.eliminar(orden)
        elif orden.lado == "compra":
            self.bids.eliminar(orden)
            
        del self.ofertas[key]
    
    def emparejar(self):
        # PAAAAN en teoría esta te toca a ti, pero bueno intenta que sea coherente con lo demas
        # Lo que sea que haga, pero que actualice self.transacciones 
        # De preferencia que sea formato: comprador(ID), vendedor(ID), precio, cantidad
        pass