from multiprocessing import Process,Semaphore
import os
from time import sleep


sem=Semaphore(3)         #三个信号量 信号量为0时 阻塞

def fu1():

    sem.acquire()  #执行任务消耗一个信号量
    print('进程开始')

    sleep(1)
    print('进程结束')
    sem.release()   #执行完毕增加一个信号量
for i in range(5):
    p=Process(target=fu1,)
    p.start()





