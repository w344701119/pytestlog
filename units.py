

# for x in range(1, 11):
#     str='{0:2d} {1:3d} {2:4d}'.format(x, x*x, x*x*x)
#     print(str)
# for x in range(1, 11):
#     print(repr(x).rjust(2), repr(x*x).rjust(3), end=' ')
#    # 注意前一行 'end' 的使用
#     print(repr(x*x*x).rjust(4))

# table = {'Google': 1, 'Runoob': 2, 'Taobao': 3}
# print('Runoob: {0[Runoob]:d}; Google: {0[Google]:d}; Taobao: {0[Taobao]:d}'.format(table))



# 使用pickle模块将数据对象保存到文件
# import pprint,pickle

# data1 = {'a': [1, 2.0, 3, 4+6j],
#          'b': ('string', u'Unicode string'),
#          'c': None}

# # selfref_list = [1, 2, 3]
# # selfref_list.append(selfref_list)

# output = open('data.pkl', 'wb')

# # Pickle dictionary using protocol 0.
# pickle.dump(data1, output)

# # Pickle the list using the highest protocol available.
# # pickle.dump(selfref_list, output, -1)

# output.close()

# pkl_file = open('data.pkl', 'rb')
# data1=pickle.load(pkl_file)
# pprint.pprint(data1)
# data2=pickle.load(pkl_file)
# pprint.pprint(data2)
# pkl_file.close()


# int = 0
# def fun1():
# 	int = 1
# 	def fun2():
# 		print(int)
# 	fun2()

# fun1()    

import time

t =time.localtime()

print("time.asctime(t) : %s" % time.asctime(t))
# print(time.clock())

time.perf_counter()  # 返回系统运行时间

print(time.perf_counter)
time.process_time()  # 返回进程运行时间

print(time.process_time)