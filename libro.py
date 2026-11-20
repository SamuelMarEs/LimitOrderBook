"""
Autor: 
Date:
(Descripción)
"""
import lado
from nivel_precio import Cola
from orden import Orden


def cancelar(id : str, ):
    pass

def main():
    N : int = int(input())          # Número de ordenes que se van a recibir
    ventas = Cola()
    
    for i in range(N):
        orden = list(map(str, input().split()))
        if orden[1] == "venta":
            ventas.encolar(Orden(orden[0], orden[1], float(orden[2]), float(orden[3]), int(orden[4])))
            
            # Añadir oferta de venta al heap de ventas (bids)
            
        elif orden[1] == "compra":
            oferta = Orden(orden[0], orden[1], float(orden[2]), float(orden[3]), int(orden[4]))
        elif orden[1] == "cancelar":
            pass
        
        

if __name__ == '__main__':
    main()