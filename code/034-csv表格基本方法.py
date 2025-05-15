import csv

with open('test123.csv', 'w', encoding='utf-8-sig', newline='') as f:  # utf-8-sig 或 utf_8_sig 写入excel打开不乱码，newline则是不出现空行
    csv_writer = csv.writer(f)
    table_head = ['标题', '日期', '链接']  # 表头列表
    csv_writer.writerow(table_head)  # 写入表头
    title = '1111'  # 标题
    time = '222'  # 时间
    link = '333'  # 链接
    csv_writer.writerow(list([title, time, link]))
