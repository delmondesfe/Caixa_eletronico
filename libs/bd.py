import pymysql
import pymysql.cursors

conn = pymysql.connect(host='localhost',
                        user ='root',
                        password='password',
                        db = 'banco',
                        cursorclass=pymysql.cursors.DictCursor)


print(conn)