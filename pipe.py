from multiprocessing import Process,Pipe
from time import sleep

fd1,fd2=Pipe()
def fu1():
    sleep(1)
    fd1.send('我是李元霸,你是谁')
    sleep(2)
    date=fd1.recv()
    print('李收到了：',date)
def fu2():
    print('楚留香来也')
    date=fd2.recv()

    print('楚留香收到：',date)
    fd2.send('我是楚留香，久仰大名')



process1=Process(target=fu1)
process2=Process(target=fu2)
process1.start()
process2.start()
process1.join()
process2.join()
