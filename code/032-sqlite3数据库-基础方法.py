import sqlite3


conn = sqlite3.connect('../students.db')  # 建立连接
c = conn.cursor()  # 创建游标
c.execute('CREATE TABLE info(name,age,school)')  # 创建数据库表info 写入表头
students = [
    ['mike',18,'aaa'],
    ['hello',23,'bbb'],
    ['python',45,'ccc'],
]
c.executemany('INSERT INTO info VALUES (?,?,?)',students)  # 插入多条数据
conn.commit()  # 修改后要提交

