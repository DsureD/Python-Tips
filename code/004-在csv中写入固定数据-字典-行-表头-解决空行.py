import csv

f = open('csv-test.csv', mode='w', encoding='utf-8-sig', newline="")  # w是覆盖式写入，a为追加写入。【newline=""加了这个没空行】
csvwriter = csv.writer(f)

dict1 = {'Column1': '名字', 'Column2': '栏目2', 'Column3': '栏目3'}
csvwriter.writerow(dict1.keys())  # 写入 "Column1,Column2,Column3"
csvwriter.writerow(dict1.values())  # 写入 “名字,栏目2,栏目3”一行三个单元格
f.close()
