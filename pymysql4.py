#用对象的方式来写
import pymysql

class Dept(object):

    def __init__(self,name,number):
        self.name = name
        self.number = number

    def __str__(self):
        return f'{self.name}\t{self.number}'

def main():
    conn = pymysql.connect(host='127.0.0.1',port=3306,user='root',password='yjx20010304',
    database= 'java_ceshi', charset='utf8',cursorclass=pymysql.cursors.DictCursor)
    try:
        with conn.cursor() as cursor:
            cursor.execute('select * from nan')
            data = cursor.fetchall()
            for row in data:
                dept = Dept(**row)#(**row)解包语法，把字典拆了（name = '',number = ''）
                print(dept)
    except pymysql.MySQLError as error:
        print(error)
    finally:
        conn.close()
if __name__ == '__main__':
    main()
