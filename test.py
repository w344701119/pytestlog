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
 
def fibonacci(n): # 生成器函数 - 斐波那契
    a, b, counter = 0, 1, 0
    while True:
        print(b)
        if (counter > n): 
            return
        yield a
        a, b = b, a + b
        counter += 1

f = fibonacci(10) # f 是一个迭代器，由生成器返回生成
 

# while True:
#     try:
#         print (next(f), end=" ")
#     except StopIteration:
#         sys.exit()
