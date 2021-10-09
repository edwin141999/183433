import time
import random
import threading
import queue
import sys

platos = queue.Queue(maxsize=5)

filosofos = ['Socrates','Platon','Heraclito','Aristóteles','Tales de Mileto']
contador = 0

def Filosofos():
    global contador
    while contador <5:
        if not platos.full():
            filosofo = random.choice(filosofos)
            filosofos.remove(filosofo)
            platos.put(filosofo)
            print('Filosofo:',filosofo,"esta comiendo")
            contador+=1
            time.sleep(random.randint(1,3))
            
def Cena():
    global contador
    while contador <=5:
        if not platos.empty():
            cena = platos.get()
            platos.task_done()
            print('Filosofo:',cena, 'termino de comer\n')
            time.sleep(random.randint(1,3))
            
if __name__ == "__main__":
    thread_productor = threading.Thread(target=Filosofos)
    thread_consumidor = threading.Thread(target=Cena)
    
    thread_productor.daemon = True
    thread_consumidor.daemon = True
    
    thread_productor.start()
    thread_consumidor.start()
    
    auxiliar=5
    
    while True:
        if contador == auxiliar:
            time.sleep(2)
            sys.exit()