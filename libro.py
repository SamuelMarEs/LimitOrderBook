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
        
        # Esta parte es la que te toca a ti pan Pan:okey
        self.heap_bids = Bid_heap()
        self.heap_asks = Ask_heap()

    def actualizar_best(self):
        self.best_bid = self.heap_bids.mejor_precio()
        self.best_ask = self.heap_asks.mejor_precio()
        
    def new_bid(self, bid : Orden):
        self.cola_bids.encolar(bid)
        self.ofertas[bid.key] = bid
        self.heap_bids.insertar(bid)
        self.actualizar_best()
        # Añadir oferta de compra al heap de compras (bids)
        # Que al hacerlo, se actualice tambien el best_bid al precio de la mejor oferta (cima del heap)
    
    def new_ask(self, ask : Orden):
        self.asks.encolar(ask)
        self.ofertas[ask.key] = ask
        self.heap_asks.insertar(ask)
        self.actualizar_best()    
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
        self.sacar(orden)
        self.actualizar_best()
        return orden.cantidad


    def sacar(self, orden):
        if orden.lado == "venta":
            self.cola_asks.eliminar(orden)
            self.heap_asks.eliminar(orden)
        else:
            self.cola_bids.eliminar(orden)
            self.heap_bids.eliminar(orden)
        del self.ofertas[orden.key]
    
    def emparejar(self):
            bid = self.heap_bids.cima()
            ask = self.heap_asks.cima()

            while bid is not None and ask is not None and bid.precio >= ask.precio:
                cantidad = min(bid.cantidad, ask.cantidad)
                precio = bid.precio if bid.timestamp < ask.timestamp else ask.precio

                self.transacciones.append((bid.key, ask.key, precio, cantidad))

                bid.cantidad -= cantidad
                ask.cantidad -= cantidad

                if bid.cantidad == 0:
                    self.sacar(bid)
                if ask.cantidad == 0:
                    self.sacar(ask)

                bid = self.heap_bids.cima()
                ask = self.heap_asks.cima()

            self._actualizar_best()