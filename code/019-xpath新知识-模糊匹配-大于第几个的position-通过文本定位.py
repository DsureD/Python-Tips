from lxml import etree
import requests

url = ""
resp = requests.get(url)
tree = etree.HTML(resp.text)
result = tree.xpath('//tbody[contains(@id,"normal")]/tr/td[2]/em/span/text()')
'''
//tbody[@id="normalthread_1600839"] 全部这样写只能匹配到一个
//tbody[contains(@id,"normal")]这样会匹配到多个
'''
text = tree.xpath('//a[text()="某个文字"]')  # 通过文本来定位
books = tree.xpath('//tr[position()>1]')  # 这样position 可以只提取从第2个开始（大于1），xpath从1开始数
text2 = tree.xpath('//a[starts-with(text(),"某个文字")]')  # 通过文本开头来定位
text3 = tree.xpath('//a[starts-with(@href,"https://")]')  # 通过属性开头来定位

'''
//div[@class="normal" and @name="123"] 通过and加条件匹配，还有 or；or not，not
'''
