import requests
url = ''
resp = requests.get(url)
with open('test.mp4','wb') as file:
    for i in resp.iter_content(chunk_size=1024):  # 每次写入resp的1024字节（1kb），边下边存，不会全部一次加载到内存中，例如文件很大就适合。
        file.write(i)
print('done')
