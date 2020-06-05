from multiprocessing import Process,Value
import time
from  random import randint


vals=Value('i',5000)   # i f c 整数浮点 字jie
def man():
    for i in range(10):
        time.sleep(0.5)
        vals.value+=randint(200,1000)

def woman():
    for i in range(10):
        time.sleep(1)
        vals.value-=randint(100,500)





process1=Process(target=man)
process2=Process(target=woman)
process1.start()
process2.start()
process1.join()
process2.join()
print('结余为：%d元'%vals.value)









