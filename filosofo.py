import threading
import time
import random

class Filosofo(threading.Thread):

    def __init__(self, id_filosofo, lista_de_palillos):
        threading.Thread.__init__(self)
        self.id_filosofo = id_filosofo
        self.lista_de_palillos = lista_de_palillos
        self.palillo_izquierdo = (self.id_filosofo+1) % len(self.lista_de_palillos)
        self.palillo_derecho = self.id_filosofo

    def obtener_tenedor_izquierdo(self):
        self.lista_de_palillos[self.palillo_izquierdo].acquire()
        print(f"El filosofo {self.id_filosofo} obtiene el tenedor izquierdo")

    def obtener_tenedor_derecho(self):
        self.lista_de_palillos[self.palillo_derecho].acquire()
        print(f"El filosofo {self.id_filosofo} obtiene el tenedor derecho")

    def liberar_tenedor_izquierdo(self):
        self.lista_de_palillos[self.palillo_izquierdo].release()
        print(f"El filosofo {self.id_filosofo} libera el tenedor izquierdo")
        

    def liberar_tenedor_derecho(self):
        self.lista_de_palillos[self.palillo_derecho].release()
        print(f"El filosofo {self.id_filosofo} libera el tenedor derecho")
    
    def comer(self):
        print(f"El filosofo {self.id_filosofo} tiene hambre")
        self.obtener_tenedor_izquierdo()
        self.obtener_tenedor_derecho()
        print(f"El filosofo {self.id_filosofo} come")
        time.sleep( random.randint(5, 10) / 10 )
        self.liberar_tenedor_derecho()
        self.liberar_tenedor_izquierdo()
        print(f"El filosofo {self.id_filosofo} termino de comer")
        
    def pensar(self):
        print(f"El filosofo {self.id_filosofo} piensa")
        time.sleep( random.randint(5, 10) / 10 )

    def run(self):
        limite = 1000
        for i in range(0, limite):
            self.pensar()
            self.comer()