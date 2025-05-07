from bs4 import BeautifulSoup

soup = BeautifulSoup(open("xxx.html",encoding = "utf-8"),"lxml"）

print(soup.a)  # 第一个标签名为<a>的数据

print(soup.a.attrs) # 获取标签的属性和属性值

# bs4的意思一些函数
# （1） find
print(soup.find("a"))  # 返回的hi第一个符合条件的数据

print(soup.find('a',title= 'a2'))

print(soup.find('a',class_='a1'))  # 注意class后下划线

# （2）find_all
print(soup.find_all('a'))  # 返回列表，所有a标签

print(soup.find_all(['a','span','td']))  # 同时获取多个标签，注意列表

print(soup.find_all('li',limit = 2))  # 获取前二个li标签的数据

#  （3）select()方法，css选择器
print(soup.select('a')  # 返回的是一个列表

print(soup.select(".a1")  # .点是class属性值，即class="a1"。类选择器

print(soup.select("#l2")  # 井号#是id属性值，即id="l2"。类选择器


print(soup.select("li[id]"))  # 查找到li标签中有id的标签，属性选择器


print(soup.select("li[id="l2"]"))  # 查找到li标签中有id为l2的标签，属性选择器


print(soup.select("div li"))   # 找到div下面的所有li标签，层级选择器 后代选择器

print(soup.select("div > ul > li"))   # 找到div下面的所有li标签， 子代选择器

print(soup.select("a,li"))  # 同时找到多个标签数据


# （4）节点信息
obj = soup.select("#d1")[0]
#如果标签对象中，只有内容，string和get_text()都可以使用。
#如果标签对象中，除了内容还有其他标签，string就获取不到内容（返回None），而get_text()是可以的
print(obj.string)  # 获取节点内容
print(obj.get_text())  # 推荐

# 节点的属性
obj = soup.select("#p1")[0]

print(obj.name) # name是标签的名字

print(obj.attrs) # 将属性值作为一个字典返回

print(obj.attrs.get('class')) # 获取class的属性值
print(obj.get('class')) # 获取class的属性值
print(obj['class']) # 获取class的属性值
