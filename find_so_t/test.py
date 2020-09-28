"""测试从系统中寻找动态库 so
"""
##### find from the python search sys.path
import sys
sys.path.append('/usr/lib/python3/dist-packages')
import cephfs  # cephfs.cpython-36m-x86_64-linux-gnu.so
print(type(cephfs.LibCephFS))


##### find from the ld directories
from ctypes.util import find_library
libcephfs_path = find_library('cephfs')
print(libcephfs_path)
if libcephfs_path:
    print('Found.')
else:
    print('Not Found.')
