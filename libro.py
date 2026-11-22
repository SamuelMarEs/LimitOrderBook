"""
Autor: Samuel Márquez y Emiliano Panuncio
Date: nov 19 2026
Class Libro con todo lo que corresponde al LimitOrderBook de una acción
"""
from orden import Orden
from lado import Ask_heap, Bid_heap

class Libro:
    def __init__(self):
        self.ofertas : dict = {}
        self.best_bid : float = None
        self.best_ask : float = None
        self.transacciones : list = []
        
        # Esta parte es la que te toca a ti pan Pan:okey
        self.heap_bids = Bid_heap()
        self.heap_asks = Ask_heap()

    def actualizar_best(self):
        self.best_bid = self.heap_bids.mejor_precio()
        self.best_ask = self.heap_asks.mejor_precio()
        
    def new_bid(self, bid : Orden):
        self.ofertas[bid.key] = bid
        self.heap_bids.insertar(bid)
        self.actualizar_best()
    
    def new_ask(self, ask : Orden):
        self.ofertas[ask.key] = ask
        self.heap_asks.insertar(ask)
        self.actualizar_best()    
    
    def cancelar(self, key : str):
        """cancela una orden por su ID

        Args:
            key (str): ID de la orden que se desea cancelar

        Raises:
            IndexError: si la orden no se encuentra en las ofertas
        """
        
        if key not in self.ofertas:
            raise IndexError("No se encontró la llave")
        
        oferta = self.ofertas[key]
        precio = oferta.precio
        
        if oferta.lado == "venta":
            self.heap_asks.niveles[precio].eliminar(oferta)
        else:
            self.heap_bids.niveles[precio].eliminar(oferta)
        del self.ofertas[key]
        self.actualizar_best()
    
    def emparejar(self):
        while self.best_bid is not None and self.best_ask is not None and self.best_bid >= self.best_ask:
            bid = self.heap_bids.niveles[self.best_bid].head
            ask = self.heap_asks.niveles[self.best_ask].head
            cantidad = min(bid.cantidad, ask.cantidad)
            precio = self.best_bid if bid.timestamp < ask.timestamp else self.best_ask

            self.transacciones.append((bid.key, ask.key, precio, cantidad))

            bid.cantidad -= cantidad
            ask.cantidad -= cantidad

            if bid.cantidad == 0:
                self.cancelar(bid.key)
            if ask.cantidad == 0:
                self.cancelar(ask.key)
            self.actualizar_best()