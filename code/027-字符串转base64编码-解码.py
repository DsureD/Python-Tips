import base64

str1 = 'abcdefg0123456'

key_base64 = base64.b64encode(str1.encode('utf-8')).decode("utf-8")  # 把字符串转成bas64码(加密)
print(key_base64, type(key_base64))  # YWJjZGVmZzAxMjM0NTY=

key = 'YWJjZGVmZzAxMjM0NTY='
base64_to_string = base64.b64decode(key.encode('utf-8')).decode("utf-8")  # 把bas64码转成字符串(解密)
print(base64_to_string)  # abcdefg0123456

key_64 = 'JUNtOrj0nwPqCk1J6+TzWg=='
base64_to_bytes = base64.b64decode(key_64)  # 把bas64码转成字节(解密)
print(base64_to_bytes)
