import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    port=3306,
    user="root",
    passwd="",
    database="telegram_bot"
)

myqursor = mydb.cursor()


def coffee_menu():
    while True:
        choose = input("Press [1] if you want add\nPress [2] if you want delete\n"
                       "Press [3] if you want update\nPress [4] lists menu\nPress [5] Back<---\n"
                       "-------------------------\n")

        if choose == '1':
            name = input('insert name coffee: ')
            cash = input('price for coffee: ')
            sql = "insert into menu_new_coffee(name,price) values(%s,%s)"
            values = (name, cash)
            myqursor.execute(sql, values)
            mydb.commit()
            print("Your coffee successful add")

        elif choose == '2':
            sql = "select * from menu_new_coffee"
            myqursor.execute(sql)
            result = myqursor.fetchall()
            for i in result:
                print(str(i[0]) + " " + i[1])
            delete_menu = int(input('\nInsert ID coffee which you want delete: '))
            sql = "Delete from menu_coffee where id=" + str(delete_menu)
            print('Your coffee successful deleted')
            myqursor.execute(sql)
            mydb.commit()

        elif choose == '3':
            sql = "select * from menu_new_coffee"
            myqursor.execute(sql)
            result = myqursor.fetchall()
            for i in result:
                print(str(i[0]) + " " + i[1])
            update_coffee = int(input("\nInsert ID ooffee which you want update: "))
            new_name = input("Insert new coffee name: ")
            new_cash = input('new price for coffee: ')

            new_sql = "update menu_new_coffee set name=%s, price=%s where id=" + str(update_coffee)
            new_values = (new_name, new_cash)
            myqursor.execute(new_sql, new_values)
            mydb.commit()
            print('Coffee successful update')

        elif choose == '4':
            sql = "select * from menu_new_coffee"
            myqursor.execute(sql)
            result = myqursor.fetchall()
            for i in result:
                print(str(i[0]) + " " + i[1] + " " + i[2])

        elif choose == '5':
            break

        else:
            print('Insert error input, try again')
            print('-----------------------------')


def sirops_menu():
    while True:
        choose = input("Press [1] if you want add\nPress [2] if you want delete\n"
                       "Press [3] if you want update\nPress [4] lists menu\nPress [5] Back<---\n"
                       "-------------------------\n")

        if choose == '1':
            name = input('insert name sirop: ')
            cash = input('price for sirop: ')
            sql = "insert into menu_sirop(name,price) values(%s,%s)"
            values = (name, cash)
            myqursor.execute(sql, values)
            mydb.commit()
            print("Your sirop successful add")

        elif choose == '2':
            sql = "select * from menu_sirop"
            myqursor.execute(sql)
            result = myqursor.fetchall()
            for i in result:
                print(str(i[0]) + " " + i[1])
            delete_menu = int(input('\nInsert ID sirop which you want delete: '))
            sql = "Delete from menu_sirop where id=" + str(delete_menu)
            print('Your sirop successful deleted')
            myqursor.execute(sql)
            mydb.commit()

        elif choose == '3':
            sql = "select * from menu_sirop"
            myqursor.execute(sql)
            result = myqursor.fetchall()
            for i in result:
                print(str(i[0]) + " " + i[1])
            update_coffee = int(input("\nInsert ID sirop which you want update: "))
            new_name = input("Insert new sirop name: ")
            new_cash = input('new sirop for coffee: ')

            new_sql = "update menu_sirop set name=%s, price=%s where id=" + str(update_coffee)
            new_values = (new_name, new_cash)
            myqursor.execute(new_sql, new_values)
            mydb.commit()
            print('Sirop successful update')

        elif choose == '4':
            sql = "select * from menu_sirop"
            myqursor.execute(sql)
            result = myqursor.fetchall()
            for i in result:
                print(str(i[0]) + " " + i[1] + " " + i[2])

        elif choose == '5':
            break

        else:
            print('Insert error input, try again')
            print('-----------------------------')


def teas_menu():
    while True:
        choose = input("Press [1] if you want add\nPress [2] if you want delete\n"
                       "Press [3] if you want update\nPress [4] lists menu\nPress [5] Back<---\n"
                       "-------------------------\n")

        if choose == '1':
            name = input("Insert name your tea: ")
            cash = int(input("price for tea: "))
            sql = "insert into menu_new_tea(name,price) values(%s,%s)"
            values = (name, cash)
            myqursor.execute(sql, values)
            mydb.commit()
            print('Tea successful add')

        elif choose == '2':
            sql = "select * from menu_new_tea"
            myqursor.execute(sql)
            result = myqursor.fetchall()
            for i in result:
                print(str(i[0]) + " " + i[1])

            delete_tea = int(input('Insert ID tea which you want delete: '))
            sql = "Delete from menu_tea where id=" + str(delete_tea)
            print('Your tea successful deleted')
            myqursor.execute(sql)
            mydb.commit()

        elif choose == '3':
            sql = "select * from menu_new_tea"
            myqursor.execute(sql)
            result = myqursor.fetchall()
            for i in result:
                print(str(i[0]) + " " + i[1])

            update_tea = int(input('Insert ID tea which you want update: '))
            new_name = input("Insert new name for tea: ")
            new_cash = input("Insert new price for tea: ")
            new_sql = "update menu_new_tea set name=%s, price=%s where id=" + str(update_tea)
            new_values = (new_name, new_cash)
            myqursor.execute(new_sql, new_values)
            mydb.commit()
            print("Tea successful update")

        elif choose == '4':
            sql = "select * from menu_new_tea"
            myqursor.execute(sql)
            result = myqursor.fetchall()
            for i in result:
                print(str(i[0]) + " " + i[1] + " " + i[2])

        elif choose == '5':
            break


def milkshakes_menu():
    while True:
        choose = input("Press [1] if you want add\nPress [2] if you want delete\n"
                       "Press [3] if you want update\nPress [4] lists menu\nPress [5] Back<---\n"
                       "-------------------------\n")

        if choose == '1':
            name = input("Insert name your milkshake: ")
            cash_450 = input("price for 450ml: ")
            sql = "insert into menu_milkshakes(name,size_450_ml) values(%s,%s)"
            values = (name, cash_450)
            myqursor.execute(sql, values)
            mydb.commit()
            print('Milkshake successful add')

        elif choose == '2':
            sql = "select * from menu_milkshakes"
            myqursor.execute(sql)
            result = myqursor.fetchall()
            for i in result:
                print(str(i[0]) + " " + i[1])

            delete_milkshakes = int(input('Insert ID milkshake which you want delete: '))
            sql = "Delete from menu_milkshakes where id=" + str(delete_milkshakes)
            print('Your milkshakes successful deleted')
            myqursor.execute(sql)
            mydb.commit()

        elif choose == '3':
            sql = "select * from menu_milkshakes"
            myqursor.execute(sql)
            result = myqursor.fetchall()
            for i in result:
                print(str(i[0]) + " " + i[1])

            update_milkshakes = int(input('Insert ID milkshake which you want delete: '))
            new_name = input("Insert new name for milkshake: ")
            new_cash_450 = input("Insert new price for 450 ml: ")
            new_sql = "update menu_milkshakes set name=%s, size_450_ml=%s where id=" + str(update_milkshakes)
            new_values = (new_name, new_cash_450)
            myqursor.execute(new_sql, new_values)
            mydb.commit()
            print("Milkshake successful update")

        elif choose == '4':
            sql = "select * from menu_milkshakes"
            myqursor.execute(sql)
            result = myqursor.fetchall()
            for i in result:
                print(str(i[0]) + " " + i[1] + " " + i[2])

        elif choose == '5':
            break


def branded_milkshakes_menu():
    while True:
        choose = input("Press [1] if you want add\nPress [2] if you want delete\n"
                       "Press [3] if you want update\nPress [4] lists menu\nPress [5] Back<---\n"
                       "-------------------------\n")

        if choose == '1':
            name = input("Insert name your branded milkshake: ")
            cash_450 = input("price for 450ml: ")
            sql = "insert into menu_branded_milkshakes(name,size_450_ml) values(%s,%s)"
            values = (name, cash_450)
            myqursor.execute(sql, values)
            mydb.commit()
            print('Branded Milkshake successful add')

        elif choose == '2':
            sql = "select * from menu_branded_milkshakes"
            myqursor.execute(sql)
            result = myqursor.fetchall()
            for i in result:
                print(str(i[0]) + " " + i[1])

            delete_milkshakes = int(input('Insert ID branded milkshake which you want delete: '))
            sql = "Delete from menu_branded_milkshakes where id=" + str(delete_milkshakes)
            print('Your branded milkshakes successful deleted')
            myqursor.execute(sql)
            mydb.commit()

        elif choose == '3':
            sql = "select * from menu_branded_milkshakes"
            myqursor.execute(sql)
            result = myqursor.fetchall()
            for i in result:
                print(str(i[0]) + " " + i[1])

            update_branded_milkshakes = int(input('Insert ID branded milkshake which you want delete: '))
            new_name = input("Insert new name for branded milkshake: ")
            new_cash_450 = input("Insert new price for 450 ml: ")
            new_sql = "update menu_branded_milkshakes set name=%s, size_450_ml=%s where id=" + str(update_branded_milkshakes)
            new_values = (new_name, new_cash_450)
            myqursor.execute(new_sql, new_values)
            mydb.commit()
            print("Branded Milkshake successful update")

        elif choose == '4':
            sql = "select * from menu_branded_milkshakes"
            myqursor.execute(sql)
            result = myqursor.fetchall()
            for i in result:
                print(str(i[0]) + " " + i[1] + " " + i[2])

        elif choose == '5':
            break


def lemonades_menu():
    while True:
        choose = input("Press [1] if you want add\nPress [2] if you want delete\n"
                       "Press [3] if you want update\nPress [4] lists menu\nPress [5] Back<---\n"
                       "-------------------------\n")

        if choose == '1':
            name = input("Insert name your lemonade: ")
            cash_450 = input("price for 450ml: ")
            sql = "insert into menu_lemonades(name,size_450_ml) values(%s,%s)"
            values = (name, cash_450)
            myqursor.execute(sql, values)
            mydb.commit()
            print('Lemonade successful add')

        elif choose == '2':
            sql = "select * from menu_lemonades"
            myqursor.execute(sql)
            result = myqursor.fetchall()
            for i in result:
                print(str(i[0]) + " " + i[1])

            delete_lemonade = int(input('Insert ID lemonade which you want delete: '))
            sql = "Delete from menu_lemonades where id=" + str(delete_lemonade)
            print('Your lemonade successful deleted')
            myqursor.execute(sql)
            mydb.commit()

        elif choose == '3':
            sql = "select * from menu_lemonades"
            myqursor.execute(sql)
            result = myqursor.fetchall()
            for i in result:
                print(str(i[0]) + " " + i[1])

            update_lemonade = int(input('Insert ID lemonade which you want delete: '))
            new_name = input("Insert new name for lemonade: ")
            new_cash = input("Insert new price for 450 ml: ")
            new_sql = "update menu_lemonades set name=%s, size_450_ml=%s where id=" + str(update_lemonade)
            new_values = (new_name, new_cash_450)
            myqursor.execute(new_sql, new_values)
            mydb.commit()
            print("Lemonade successful update")

        elif choose == '4':
            sql = "select * from menu_lemonades"
            myqursor.execute(sql)
            result = myqursor.fetchall()
            for i in result:
                print(str(i[0]) + " " + i[1] + " " + i[2])

        elif choose == '5':
            break


def sandwiches_menu():
    while True:
        choose = input("Press [1] if you want add\nPress [2] if you want delete\n"
                       "Press [3] if you want update\nPress [4] lists menu\nPress [5] Back<---\n"
                       "-------------------------\n")

        if choose == '1':
            name = input("Insert name your food: ")
            sum = input("price food: ")
            sql = "insert into menu_sandwiches(name,sum) values(%s,%s)"
            values = (name, sum)
            myqursor.execute(sql, values)
            mydb.commit()
            print('Food successful add')

        elif choose == '2':
            sql = "select * from menu_sandwiches"
            myqursor.execute(sql)
            result = myqursor.fetchall()
            for i in result:
                print(str(i[0]) + " " + i[1])

            delete_food = int(input('Insert ID food which you want delete: '))
            sql = "Delete from menu_lemonades where id=" + str(delete_food)
            print('Your food successful deleted')
            myqursor.execute(sql)
            mydb.commit()

        elif choose == '3':
            sql = "select * from menu_sandwiches"
            myqursor.execute(sql)
            result = myqursor.fetchall()
            for i in result:
                print(str(i[0]) + " " + i[1])

            update_food = int(input('Insert ID food which you want delete: '))
            new_name = input("Insert new name for food: ")
            new_cash = input("Insert new price for food: ")
            new_sql = "update menu_sandwiches set name=%s, sum=%s where id=" + str(update_food)
            new_values = (new_name, new_cash)
            myqursor.execute(new_sql, new_values)
            mydb.commit()
            print("Food successful update")

        elif choose == '4':
            sql = "select * from menu_sandwiches"
            myqursor.execute(sql)
            result = myqursor.fetchall()
            for i in result:
                print(str(i[0]) + " " + i[1] + " " + i[2])

        elif choose == '5':
            break


while True:
    global_choose = input('Press [1] if you want to work with coffee table\n'
                          'Press [2] if you want to work with authors teas table\n'
                          'Press [3] if you want to work with milkshakes table\n'
                          'Press [4] if you want to work with branded milkshakes table\n'
                          'Press [5] if you want to work with lemonades table\n'
                          'Press [6] if you want to work with sandwiches and baking table\n'
                          'Press [7] if you want to work with sirop table\n'
                          'Press [0] if you want to exit\n')

    if global_choose == '1':
        print("-------------------------")
        coffee_menu()

    elif global_choose == '2':
        print("-------------------------")
        teas_menu()

    elif global_choose == '3':
        print("-------------------------")
        milkshakes_menu()

    elif global_choose == '4':
        print("-------------------------")
        branded_milkshakes_menu()

    elif global_choose == '5':
        print("-------------------------")
        lemonades_menu()

    elif global_choose == '6':
        print("-------------------------")
        sandwiches_menu()

    elif global_choose == '7':
        print("-------------------------")
        sirops_menu()

    elif global_choose == '0':
        print('Thank you, dear user, see you again!!!')
        exit(0)





