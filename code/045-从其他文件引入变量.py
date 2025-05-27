
# 文件 a.py 中内容

appid = 'appid_123'
token = 'token_456'





# 文件 b.py 中内容

from a import appid, token

print(appid, token)

