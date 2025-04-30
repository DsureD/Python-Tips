import requests

from urllib3.exceptions import InsecureRequestWarning

# 禁用安全请求警告
requests.packages.urllib3.disable_warnings(category=InsecureRequestWarning)

headers = {}
url = ""
resp = requests.get(url,headers=headers,verify=False)
print(resp.text)
