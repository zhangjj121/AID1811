import asyncio
import random

from numpy import *

# def line(l,n):
#     random.shuffle(l)
#     t = 0
#     for x  in l :
#         t+=1
#         if x == n:
#             print('查找成功','查找了%d次'%t)
#             break
#         else:
#             continue


# if  __name__ =='__main__':
#     l = [x for x in range(1,14)]
#     line(l,6)
        
#递归实现二分法

def line(l,n,left,right):
    if left >right:
        return -1
    m=(left+right)//2

    if l[m] == n:
        print(m)
        return m
    elif l[m]>n:
        
        return line(l,n,left,m-1)
    else:
        return line(l,n,m+1,right)
        
if  __name__ =='__main__':
    l = [x for x in range(1,14)]
  
    # res = line(l,6,0,len(l))
    # line(l,6,0,len(l))

#矩阵乘法 
# A = array([[1,2,3],[4,5,6]])
# B= array([[1,4],[2,5],[3,6]])
# M = A.dot(B) 
# print(M)

l=[100,190,160,175,144,156]
# l=[200,100, 144, 156, 160, 175, 190]
def line(l):
    for x in range(len(l)-1):#外部循环代表走访次数
        # f=False
        for y in range(len(l)-x-1):#走访一遍后，最后的数据不用再做对比
            if l[y]>l[y+1]:
                l[y],l[y+1]=l[y+1],l[y]
                # f=True
        # if f ==False:
        #     break
                
    print(l)
    print(x+1)
        
line(l)

print('sd的方式都上帝给符合认同和高飞的')S
