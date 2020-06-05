import time
from multiprocessing import Process,Array

# shm=Array('i',[1,3,5,7])   #列表必须是数字形式
#shm=Array('i',5)           # 代表 有五个位置槽默认为0 [0,0,0,0,0]
# shm 是一个可迭代类型 但不是列表本身
shm=Array('c',b'memory')      # 代表共享内容为字节串
def f1():
    for i in shm:
        print(i)
    shm[0]=b'M'

p=Process(target=f1,)
p.start()          #子进程运行
time.sleep(1)      #父进程等待一秒运行
for i in shm:
    print(i)
print('#############')
print(shm.value)   #将整个字节串打印出来
p.join()



















