#python 连接mysql  pymysql的基本用法 添加
import pymysql

def main():
    conn = pymysql.connect(host='127.0.0.1',port=3306,user='root',password='yjx20010304',
    database= 'url', charset='utf8')#5创建连接对象
    try:
        with conn.cursor() as cursor:#上下文语法，用完自动关
            result = cursor.execute('insert into urls values ("1234")')#执行，给个字符串进来，写sql语句
            if result == 1:#"laoli","1234"这儿必须为双引号
                print('添加成功')
            conn.commit()#成功就手动提交，把"laoli","1234"提交进去
    except pymysql.MySQLError as error:#捕获异常，并重新命名
        print(error)
        conn.rollback()#成功了提交，失败了回滚，相当于之前添加数据的操作就不做了，撤销了
    finally:
        conn.close()#关闭连接，释放资源，不管前面成没成功最后都必须要关闭连接，否则造成数据的泄漏
#8conn.cursor()返回一个游标对象 用来发出sql语句
#connect是pymysql中的一个函数，名字叫连接
#host第一个参数叫做主机，要连接到哪台主机，是个字符串
#port第二个参数叫做端口，你要连接到这台服务器的哪个端口，不是字符串
#user第三个参数，指定你的用户名是什么，字符串
#password第四个参数，指定你的口令，字符串
#database第五个参数，指定数据库的名字，字符串
#charset第六个参数，指定你的字符集，'utf8'mysql中不是'utf-8'
#在pymysql.connect中，不止这些参数，后面的程序会涉及

if __name__ == '__main__':
    main()
