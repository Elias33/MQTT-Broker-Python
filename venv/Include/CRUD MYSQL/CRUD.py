'''
python MYSQL connectivity
'''
import pymysql
import sys

'''
create database connection
'''
class mySQLCONN:
    my_sql_connection = pymysql.connect(host="localhost", user="root", passwd="", db="elias")
    myCursor = my_sql_connection.cursor()
    search=False

    select_option = int(input("Please signup. Or do you already signup ? If yes then press 1:\n"))
    while True:
        if select_option == 1:
            print("Congraluations man...\n")
            print("What do you want ? Please select:\n")
            choose_option = int(input(("1. Insert 2. Update 3. Delete. 4. Search user. 5. Exit system\n")))
            if choose_option == 1:
                print("You select 1")
                print("Enter your credential information for insertion::\n")
                user_name = input("What is your name?:\n")
                user_phone = input("What is your phone:\n")
                user_city = input("Your city:\n")

                sql = """INSERT INTO information(name,phone,city) VALUES('%s','%s','%s')""" % (
                    user_name, user_phone, user_city)

                myCursor.execute(sql)
                print("insert successfully")

                my_sql_connection.commit()
                my_sql_connection.close()
            elif choose_option == 2:
                print("Do you want to upate data ?:\n")
                print("This programme will give you access only phone number update:\n")

                new_number = input("Enter new phone number:\n")
                user_id = input("Enter your user ID for update data:\n")
                sql = "update information set phone='%s' where id='%s'" % (new_number, user_id)

                myCursor.execute(sql)
                print("update successfully")

                my_sql_connection.commit()
                my_sql_connection.close()


            elif choose_option == 3:
                print("Functionality is not included")

            elif choose_option==4:
                search_value= input("Enter number to search :\n")
                myCursor.execute("SELECT * FROM information WHERE phone=%s", (search_value,))
                data = "error"  # initially just assign the value
                for i in myCursor:
                    data = i  # if cursor has no data then loop will not run and value of data will be 'error'
                if data == "error":
                    print("User Does not exist")
                else:
                    print("User exist")
                    my_sql_connection.commit()
                    my_sql_connection.close()



            elif choose_option==5:
                sys.exit(1)


            else:
                print("Sorry. Input mismatch")

        else:
            print("Please fill the form:\n")


