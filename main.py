from threading import BoundedSemaphore
from filosofo import Filosofo

if __name__ == '__main__':
    
    numero_de_filosofos = 5
    lista_de_palillos = []

    for i in range(0, numero_de_filosofos):
        lista_de_palillos.append( BoundedSemaphore(1) )

    for i in range(0, numero_de_filosofos):
        Filosofo(i, lista_de_palillos).start()
        