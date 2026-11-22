"""
Autor: Samuel Márquez y Emiliano Panuncio
Date: nov 19 2026

Programa principal del Limit Order Book

Entrada:
    N                                   número de órdenes
    <id> compra <precio> <cantidad> <timestamp>
    <id> venta  <precio> <cantidad> <timestamp>
    <id> cancelar
Cada compra/venta se empareja al llegar, con prioridad precio-tiempo

Salida: lista de transacciones (bid, ask, precio, cantidad)
y el estado final del libro (best_bid, best_ask)
"""
from libro import Libro  
from orden import Orden  
        
def main():
    N : int = int(input())          # Número de ordenes que se van a recibir
    LOB = Libro()
    
    for _ in range(N):
        orden = input().split()
        if orden[1] == "venta":
            ask = Orden(orden[0], orden[1], float(orden[2]), float(orden[3]), int(orden[4]))
            LOB.new_ask(ask)       # Registra la oferta de venta en el libro
            LOB.emparejar()        # Empareja en prioridad precio-tiempo
            
        elif orden[1] == "compra":
            bid = Orden(orden[0], orden[1], float(orden[2]), float(orden[3]), int(orden[4]))
            LOB.new_bid(bid)        # Registra la oferta de compra en el libro
            LOB.emparejar()         # Empareja en prioridad precio-tiempo

        elif orden[1] == "cancelar":
            key =  orden[0]
            LOB.cancelar(key)       # Cancela la oferta
         
        
        
    print("Transacciones:")
    for accion in LOB.transacciones:
        print(*accion)
    print("Estado del libro:")
    print(f"best_bid = {LOB.best_bid}")
    print(f"best_ask = {LOB.best_ask}")

if __name__ == '__main__':
    main()