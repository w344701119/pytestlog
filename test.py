#!/usr/bin/python3
# arr=[1,2,3,4,5,6,7]

# def changeArr(inArr):
#     inArr[1]=100    
#     print(id(inArr))
#     for item in range(1,100):
#         inArr.append(item)
#     print(inArr)    
    
# print(id(arr))
# arr.append(1);

# changeArr(arr);
# print(id(arr))
# print(arr)


import sys
 
# def fibonacci(n): # 生成器函数 - 斐波那契
#     a, b, counter = 0, 1, 0
#     while True:
#         print(b)
#         if (counter > n): 
#             return
#         yield a
#         a, b = b, a + b
#         counter += 1

# f = fibonacci(10) # f 是一个迭代器，由生成器返回生成
 

# while True:
#     try:
#         print (next(f), end=" ")
#     except StopIteration:
#         sys.exit()








# def FindNum(target,arr):
#     for v in arr:
#         try:
#             p= v.index(target)
#             return True
#         except:
#             continue
#     return False 

##查找二维数组中是否有目标数
# def Find(target,array):
#     for v in array:
#         try:
#             p=v.index(target)
#         except:
#             p=-1
#             continue  
#     if p!=-1:
#         return True
#     else:
#         return False

# re=Find(7,[[1,2,3,4],[7,5,6,8]])
# print(re)

# ##替换空格
# def replaceSpace(s):
#     s=s.replace(" ","%20")
#     return s
# print(replaceSpace("hell work"))

# def Fibonacci(n):
#     if (n<=0):
#         return 0
#     elif (n==1 or n==2):
#         return 1
#     else:
#         return Fibonacci(n-1)+Fibonacci(n-2)
    
# print(Fibonacci(4))





def Fibonacci(n):
    a,b=0,1
    c=0
    while n>=c:
        a,b=b,a+b
        c+=1    
        if c == n:
            return a
   
    

print(Fibonacci(4))

