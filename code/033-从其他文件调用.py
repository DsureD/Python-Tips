from test_file_py import *  # 从test_file_py这个文件导入所有

from test_file_py import some_function_name  # 从test_file_py这个文件导入some_function_name这个函数

some_function_name('参数1', '参数2') #  可直接调用那个文件中的函数


import test_file  # 直接导入py文件，下面调用方法，会是test_file.函数()

test_file.some_function_name('参数1', '参数2')
