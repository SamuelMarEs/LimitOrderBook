"""
Autor: Samuel Márquez, Emiliano Panuncio
Date: nov 19 2026
(Descripción)
"""
from libro import Libro  
from orden import Orden  
        
def main():
    N : int = int(input())          # Número de ordenes que se van a recibir
    LOB = Libro()
    
    for _ in range(N):
        orden = list(map(str, input().split()))
        if orden[1] == "venta":
            ask = Orden(orden[0], orden[1], float(orden[2]), float(orden[3]), int(orden[4]))
            LOB.new_ask(ask)        # Registra la oferta de venta en el libro
            
        elif orden[1] == "compra":
            bid = Orden(orden[0], orden[1], float(orden[2]), float(orden[3]), int(orden[4]))
            LOB.new_bid(bid)        # Registra la oferta de compra en el libro
            
        elif orden[1] == "cancelar":
            key =  orden[0]
            LOB.cancelar(key)       # Cancela la oferta
    
        LOB.emparejar()             # Empareja en prioridad precio-tiempo
        
    for accion in LOB.transacciones:
        print(*accion)
        

if __name__ == '__main__':
    main()