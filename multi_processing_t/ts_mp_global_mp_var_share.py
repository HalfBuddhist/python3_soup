"""测试多进程下共享数据：

1，即使在启动进程时没有使用参数来传递过去，访问mp.Value 等变量也是可以进程间协作的。

"""

import multiprocessing
from ctypes import c_bool, c_int

_is_set_up = multiprocessing.Value(c_bool, False)
aa = 1
cc = multiprocessing.Value(c_int, 10)

def func():
    _is_set_up.value = True
    global aa
    aa += 1
    cc.value += 1
    print("2.", _is_set_up)
    print("2.", aa)
    print("2.", cc)
    print("Set in subprocess.")
    
print("1.", _is_set_up)
print("1.", aa)
print("1.", cc)
p = multiprocessing.Process(target=func)
p.start()
p.join()
print("3.", _is_set_up)
print("3.", aa)
print("3.", cc)
_is_set_up.value = False
aa += 1
cc.value += 1
print("4.", _is_set_up)
print("4.", aa)
print("4.", cc)