'''
要求：将此文件夹中的图片进行拆解为一半一半，并且保存为新的图片 上下 使用两个子进程同时执行 可以重复执行
'''

import os
from multiprocessing import Process

file='11b.jpg'
size=os.path.getsize(file)
print(size)

def top():
    f=open(file,'rb')
    s=0
    f2 = open('top.jpg', 'wb')
    while s<size//2:
        fi=f.read(1024)
        f2.write(fi)
        s+=1024
    f2.write(f.read((size//2)//1024))



def down():
    f=open(file,'rb')
    f.seek(size//2)
    tip=f.read()
    f2=open('down.jpg','wb')
    f2.write(tip)

process1=Process(target=top)
process2=Process(target=down)
process1.start()
process2.start()
process1.join()
process2.join()









