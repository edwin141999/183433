import time
import random
import threading
import queue

queue = queue.Queue(maxsize=5)

def Productor():
    while True:
        if not queue.full():
            item = random.randint(1,5)
            queue.put(item)
            print('\nElemento de cola',item)
            time.sleep(random.randint(1,5))
            
def Consumidor():
    while True:
        if not queue.empty():
            item = queue.get()
            queue.task_done()
            print('\nElemento terminado',item)
            time.sleep(random.randint(1,5))
            
if __name__ == "__main__":
    thread_productor = threading.Thread(target=Productor)
    thread_consumidor = threading.Thread(target=Consumidor)
    
    thread_productor.start()
    thread_consumidor.start()