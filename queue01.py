from multiprocessing import Process, Queue

from time import sleep
from random import randint

q=Queue(10)
def fq1():
    s=0
    for i in range(10):
        sleep(0.6)
        tuple01=(randint(1,10),randint(1,10))
        q.put(tuple01)
        s+=1
        print('传入第%d个'%s)
        if q.full():
            q.close()
            return
def fq2() :
    for i in range(10):
        sleep(1)
        x,y=q.get()

        print('x+y=%d'%(x+y))
    q.close()




process1=Process(target=fq1)
process2=Process(target=fq2)
process1.start()
process2.start()
process1.join()
process2.join()
















