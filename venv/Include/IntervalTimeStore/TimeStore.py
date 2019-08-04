
import pymysql
import time
connection = pymysql.connect(host="localhost", user="root", passwd="", db="datasoft")
myCursor = connection.cursor()


while True:
    try:
        myCursor.execute ("""INSERT INTO randomtime 
                values(0, CURRENT_DATE(), NOW(), 28)""")
        connection.commit()
        print ("Data committed")
    except:
        print ("Error")
        connection.rollback()
    time.sleep(3)
connection.close()




