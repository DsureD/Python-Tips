import requests


url = ""
resp = requests.get(url)
# 有时候网页有生僻字，gb2312也无法转换，就会报错：
# UnicodeEncodeError: 'gbk' codec can't encode character '\ufffd' in position 6511: illegal multibyte sequence
# 可以试试 'gb18030'
# resp.encoding='gb18030'
# page_content = resp.text.encode('gbk','ignore').decode('gbk') # 很有用的，有时候须配合resp.encoding='utf-8'用

resp.encoding = 'unicode-escape'   # 当返回值是这些时： \u767b\u5f55\u5931\u8d25

# 据说这个才是通用解码标准
page_content = resp.text.encode('iso-8859-1').decode('gbk') # 很有用的，有时候须配合resp.encoding='utf-8'用
print(page_content)
