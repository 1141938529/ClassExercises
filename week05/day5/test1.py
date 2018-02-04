import pymysql

if __name__ == '__main__':
    conn = pymysql.connect(host="localhost", port=3306, user="root",
                           password="123456", database="world", charset="utf8")
    cursor = conn.cursor()
    # row = cursor.execute("insert into student(name,age,score,classNum)"
    #                      " VALUES('张三',22,87,'6(2)')", )
    cursor.execute("select * from student where NAME = '张三'")
    result = cursor.fetchall()
    print(result)
    cursor.execute("delete from student WHERE id =12")
    cursor.execute("select * from student where NAME = '张三'")
    # cursor.execute("select * from student")
    conn.commit()
    result = cursor.fetchall()
    print(type(result))
    cursor.close()
    conn.close()
    print( result)
    print("提交成功。")
    pass
