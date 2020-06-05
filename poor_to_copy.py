'''
练习：使用进程池拷贝pycharmprojects任意一个文件夹下所有文件，实时打印拷贝的速度百分比
思路：
    旧的文件夹绝对路径
    新的文件夹绝对路径
    将旧的文件夹所有文件都copy到新的
'''


import os
from multiprocessing import Pool,Process,Queue


q=Queue()
def do_file(f,old_file,new_file):
    fr=open(old_file+f,'rb')

    fw=open(new_file+f,'wb')

    while True:
        date=fr.read(1024)
        if not date:
            break

        n=fw.write(date)
        q.put(n)







def main():
    f = input('请输入要拷贝的文件夹名：')
    old_file='/home/sen/PycharmProjects/'+f+'/'
    file_list=os.listdir(old_file)

    new_file='/home/sen/PycharmProjects/'+'-备份/'
    os.mkdir(new_file)
    pool = Pool(5)
    all_size=0
    now_size=0
    for file in file_list:
       pool.apply_async(func=do_file,args=(file,old_file,new_file))
       all_size+=os.path.getsize(old_file+file)
    print('该文件夹大小为：%dKB'%(all_size//1024))

    pool.close()




    pool.join()

if __name__ == '__main__':
    main()




