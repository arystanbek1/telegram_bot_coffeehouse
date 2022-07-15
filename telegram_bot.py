import telebot
import os
import random
import mysql.connector

token = "5294113772:AAHJcHPyY-W_3TT-A3fY7O4jdykiYd-eMuk"
bot = telebot.TeleBot(token)

mydb = mysql.connector.connect(
    host="localhost",
    port=3306,
    user="root",
    passwd="",
    database="telegram_bot"
)
choose_coffee = 0
choose_count = 0
choose_sirop = 0
myqursor = mydb.cursor()
arr = []
i_coffee_name = ""
i_coffee_count = 0
i_price = ""
i_sirop_name = 0
i_sirop_price = 0
i_count_sirop = 0
id_person = 0
all_sum = 0
choose_tea = 0
choose_count_tea = 0
choose_milkshake = 0
choose_count_milkshake = 0
choose_branded_milkshake = 0
choose_count_branded_milkshake = 0
choose_lemonade = 0
choose_count_lemonade = 0
choose_sandwich = 0
choose_count_sandwich = 0


def select_all_coffee():
    sql = "select * from menu_new_coffee"
    myqursor.execute(sql)
    result = myqursor.fetchall()
    return result


def select_all_sirops():
    sql = "select * from menu_sirop"
    myqursor.execute(sql)
    result = myqursor.fetchall()
    return result


def select_all_teas():
    sql = "select * from menu_new_tea"
    myqursor.execute(sql)
    result = myqursor.fetchall()
    return result


def select_all_milkshakes():
    sql = "select * from menu_milkshakes"
    myqursor.execute(sql)
    result = myqursor.fetchall()
    return result


def select_all_branded_milkshakes():
    sql = "select * from menu_branded_milkshakes"
    myqursor.execute(sql)
    result = myqursor.fetchall()
    return result


def select_all_lemonades():
    sql = "select * from menu_lemonades"
    myqursor.execute(sql)
    result = myqursor.fetchall()
    return result


def select_all_sandwiches():
    sql = "select * from menu_sandwiches"
    myqursor.execute(sql)
    result = myqursor.fetchall()
    return result


@bot.message_handler(commands=["start"])
def handle_start(message):
    user_markup = telebot.types.ReplyKeyboardMarkup(True, False)
    user_markup.row("Наше меню 📋")
    user_markup.row("Оформить заказ 🚘", "Связаться с менеджером 👩‍💻")
    user_markup.row("Наша локация 📍", "Корзина 🛒")
    user_markup.row("Выйти")
    bot.send_message(message.chat.id, "Добро пожаловать в GALLIARD COFFE BAR ☕️\n"
                                      "Меня зовут Jarvis 🤖\nЧем я могу вам помочь? 😁", reply_markup=user_markup)


def back_to_menu(message):
    user_markup = telebot.types.ReplyKeyboardMarkup(True, False)
    user_markup.row("Наше меню 📋")
    user_markup.row("Оформить заказ 🚘", "Связаться с менеджером 👩‍💻")
    user_markup.row("Наша локация 📍", "Корзина 🛒")
    user_markup.row("Выйти")
    bot.send_message(message.chat.id, "Что желаете?", reply_markup=user_markup)


def second_menu(message):
    user_markup = telebot.types.ReplyKeyboardMarkup(True, False)
    user_markup.row("Кофейные напитки ☕️", "Авторские чаи 🍵")
    user_markup.row("Молочные коктейли 🍹", "Фирменные коктейли🍹")
    user_markup.row("Лимонады🥤", "Сэндвичи и выпечки 🥪🥐")
    user_markup.row("Назад в главное меню 🔙")
    bot.send_message(message.chat.id, "Выберите категорию 🙈", reply_markup=user_markup)


@bot.message_handler(commands=["stop"])
def handle_stop(message):
    hide_markup = telebot.types.ReplyKeyboardRemove()
    bot.send_message(message.chat.id, "пока!!!", reply_markup=hide_markup)


@bot.message_handler(commands=["help"])
def handle_help(message):
    bot.send_message(message.chat.id, "Чем могу Вам помочь?")


@bot.message_handler(content_types=["text"])
def handle_menu(message):
    global choose_coffee
    global choose_count
    global i_price_name
    global choose_sirop
    global id_person
    global choose_tea
    global choose_count_tea
    global choose_milkshake
    global choose_count_milkshake
    global choose_branded_milkshake
    global choose_count_branded_milkshake
    global choose_lemonade
    global choose_count_lemonade
    global choose_sandwich
    global choose_count_sandwich
    global i_count_sirop

    if message.text == "Наше меню 📋":
        second_menu(message)

    elif message.text == "Кофейные напитки ☕️":
        global i_size
        i_size = message.text
        choose_coffee = 1
        user_markup = telebot.types.ReplyKeyboardMarkup(True, False)

        menu_coffee = select_all_coffee()
        for coffee in menu_coffee:
            user_markup.row(coffee[1])
        user_markup.row('Назад в меню')
        bot.send_message(message.chat.id, "Вид кофе ☕️", reply_markup=user_markup)

    elif message.text and choose_coffee == 1:
        choose_coffee = 2
        global i_coffee_name
        i_coffee_name = message.text
        user_markup = telebot.types.ReplyKeyboardMarkup(True, False)
        sql = 'SELECT price FROM menu_new_coffee WHERE name="' + f'{i_coffee_name}"'
        myqursor.execute(sql)
        result = myqursor.fetchall()
        user_markup.row(result[0][0])
        user_markup.row('Назад в меню')
        bot.send_message(message.chat.id, "Цена за кофе в тенге", reply_markup=user_markup)

    elif message.text.isdigit() and choose_coffee == 2:
        global i_price
        i_price = message.text
        choose_count = 1
        choose_coffee = 0
        user_markup = telebot.types.ReplyKeyboardMarkup(True, False)
        user_markup.row("1", "2", "3")
        user_markup.row("4", "5", "6")
        user_markup.row("7", "8", "9")
        user_markup.row('Написать количество')
        user_markup.row('Назад в меню')
        bot.send_message(message.chat.id, "Какое количество вы хотите?", reply_markup=user_markup)

    elif message.text == "Написать количество" and choose_count == 1:
        user_markup = telebot.types.ReplyKeyboardMarkup(True, False)
        choose_count = 2
        user_markup.row('Назад в меню')
        bot.send_message(message.chat.id, "Напишите количество в чат", reply_markup=user_markup)

    elif message.text.isdigit() and choose_count == 2 or choose_count == 1:
        choose_sirop = 1
        choose_count = 0
        global i_coffee_count
        i_coffee_count = message.text
        id_person = message.from_user.id
        user_markup = telebot.types.ReplyKeyboardMarkup(True, False)
        user_markup.row("Да", "Нет")
        user_markup.row('Назад в меню')
        bot.send_message(message.chat.id, "Хотите ли вы добавить сироп? 🍯", reply_markup=user_markup)
        func_coffee()

    elif message.text == "Да" and choose_sirop == 1 or choose_sirop == 13 and message.text == "Да!":
        menu_sirop = select_all_sirops()
        choose_sirop = 2
        user_markup = telebot.types.ReplyKeyboardMarkup(True, False)
        for sirop in menu_sirop:
            user_markup.row(sirop[1])
        user_markup.row('Назад в меню')
        bot.send_message(message.chat.id, "Вид сиропов 🍯", reply_markup=user_markup)

    elif message.text and choose_sirop == 2:
        global i_sirop_name
        i_sirop_name = message.text
        user_markup = telebot.types.ReplyKeyboardMarkup(True, False)
        sql = 'SELECT price FROM menu_sirop WHERE name="' + f'{i_sirop_name}"'
        myqursor.execute(sql)
        result = myqursor.fetchall()
        try:
            user_markup.row(result[0][0])
        except:
            user_markup.row('150')
        choose_sirop = 0
        user_markup.row('Назад в меню')
        bot.send_message(message.chat.id, "Цена за сироп в тенге", reply_markup=user_markup)

    elif message.text == '150':
        choose_sirop = 12
        global i_sirop_price
        i_sirop_price = message.text
        user_markup = telebot.types.ReplyKeyboardMarkup(True, False)
        user_markup.row("1", "2", "3")
        user_markup.row("4", "5", "6")
        user_markup.row("7", "8", "9")
        bot.send_message(message.chat.id, "Какое количество вы хотите?", reply_markup=user_markup)

    elif message.text and choose_sirop == 12:
        choose_sirop = 13
        global i_count_sirop
        i_count_sirop = message.text
        id_person = message.from_user.id
        user_markup = telebot.types.ReplyKeyboardMarkup(True, False)
        user_markup.row("Да!", "Нет!")
        user_markup.row('Назад в меню')
        bot.send_message(message.chat.id, "Желаете еще сиропчика)? 🍯", reply_markup=user_markup)
        func_sirop()

    elif message.text == "Нет!" and choose_sirop == 13:
        bot.send_message(message.chat.id, "Ваш заказ добавлен в корзину ✅")
        second_menu(message)
# -----------------------------------------------------------------------------------------------------------------------------------------------
    elif message.text == "Авторские чаи 🍵":
        i_size = message.text
        choose_tea = 1
        user_markup = telebot.types.ReplyKeyboardMarkup(True, False)
        menu_tea = select_all_teas()
        for tea in menu_tea:
            user_markup.row(tea[1])
        user_markup.row('Назад в меню')
        bot.send_message(message.chat.id, "Вид чаев ☕️", reply_markup=user_markup)

    elif message.text and choose_tea == 1:
        choose_tea = 2
        i_coffee_name = message.text
        user_markup = telebot.types.ReplyKeyboardMarkup(True, False)
        sql = 'SELECT price FROM menu_new_tea WHERE name="' + f'{i_coffee_name}"'
        myqursor.execute(sql)
        result1 = myqursor.fetchall()
        user_markup.row(result1[0][0])
        user_markup.row('Назад в меню')
        bot.send_message(message.chat.id, "Цена за чай в тенге", reply_markup=user_markup)

    elif message.text.isdigit() and choose_tea == 2:
        i_price = message.text
        choose_count_tea = 1
        choose_tea = 0
        user_markup = telebot.types.ReplyKeyboardMarkup(True, False)
        user_markup.row("1", "2", "3")
        user_markup.row("4", "5", "6")
        user_markup.row("7", "8", "9")
        user_markup.row('Написать количество')
        user_markup.row('Назад в меню')
        bot.send_message(message.chat.id, "Какое количество вы хотите?", reply_markup=user_markup)

    elif message.text == "Написать количество" and choose_count_tea == 1:
        user_markup = telebot.types.ReplyKeyboardMarkup(True, False)
        choose_count_tea = 2
        user_markup.row('Назад в меню')
        bot.send_message(message.chat.id, "Напишите количество в чат", reply_markup=user_markup)

    elif message.text.isdigit() and choose_count_tea == 2 or choose_count_tea == 1:
        choose_count_tea = 0
        i_coffee_count = message.text
        id_person = message.from_user.id
        second_menu(message)
        func_tea()

# -----------------------------------------------------------------------------------------------------------------------------------------------
    elif message.text == "Молочные коктейли🍹":
        i_size = message.text
        choose_milkshake = 1
        user_markup = telebot.types.ReplyKeyboardMarkup(True, False)
        menu_milkshake = select_all_milkshakes()
        for milkshake in menu_milkshake:
            user_markup.row(milkshake[1])
        user_markup.row('Назад в меню')
        bot.send_message(message.chat.id, "Вид молочных коктейлев🍹", reply_markup=user_markup)

    elif message.text and choose_milkshake == 1:
        choose_milkshake = 2
        i_coffee_name = message.text
        user_markup = telebot.types.ReplyKeyboardMarkup(True, False)
        sql = 'SELECT price FROM menu_milkshakes WHERE name="' + f'{i_coffee_name}"'
        myqursor.execute(sql)
        result1 = myqursor.fetchall()
        user_markup.row(result1[0][0])
        user_markup.row('Назад в меню')
        bot.send_message(message.chat.id, "Цена за молочный коктейль в тенге", reply_markup=user_markup)

    elif message.text.isdigit() and choose_milkshake == 2:
        i_price = message.text
        choose_count_milkshake = 1
        choose_milkshake = 0
        user_markup = telebot.types.ReplyKeyboardMarkup(True, False)
        user_markup.row("1", "2", "3")
        user_markup.row("4", "5", "6")
        user_markup.row("7", "8", "9")
        user_markup.row('Написать количество')
        user_markup.row('Назад в меню')
        bot.send_message(message.chat.id, "Какое количество вы хотите?", reply_markup=user_markup)

    elif message.text == "Написать количество" and choose_count_tea == 1:
        user_markup = telebot.types.ReplyKeyboardMarkup(True, False)
        choose_count_milkshake = 2
        user_markup.row('Назад в меню')
        bot.send_message(message.chat.id, "Напишите количество в чат 🙈", reply_markup=user_markup)

    elif message.text.isdigit() and choose_count_milkshake == 2 or choose_count_milkshake == 1:
        choose_count_milkshake = 0
        i_coffee_count = message.text
        id_person = message.from_user.id
        second_menu(message)
        func_milkshakes()
# -----------------------------------------------------------------------------------------------------------------------------------------------
    elif message.text == "Фирменные коктейли🍹":
        i_size = message.text
        choose_branded_milkshake = 1
        user_markup = telebot.types.ReplyKeyboardMarkup(True, False)
        menu_branded_milkshake = select_all_branded_milkshakes()
        for branded_milkshake in menu_branded_milkshake:
            user_markup.row(branded_milkshake[1])
        user_markup.row('Назад в меню')
        bot.send_message(message.chat.id, "Вид фирменных коктейлев🍹", reply_markup=user_markup)

    elif message.text and choose_branded_milkshake == 1:
        choose_branded_milkshake = 2
        i_coffee_name = message.text
        user_markup = telebot.types.ReplyKeyboardMarkup(True, False)
        sql = 'SELECT price FROM menu_branded_milkshakes WHERE name="' + f'{i_coffee_name}"'
        myqursor.execute(sql)
        result1 = myqursor.fetchall()
        user_markup.row(result1[0][0])
        user_markup.row('Назад в меню')
        bot.send_message(message.chat.id, "Цена за фирменный коктейль в тенге", reply_markup=user_markup)

    elif message.text.isdigit() and choose_branded_milkshake == 2:
        i_price = message.text
        choose_count_branded_milkshake = 1
        choose_branded_milkshake = 0
        user_markup = telebot.types.ReplyKeyboardMarkup(True, False)
        user_markup.row("1", "2", "3")
        user_markup.row("4", "5", "6")
        user_markup.row("7", "8", "9")
        user_markup.row('Написать количество')
        user_markup.row('Назад в меню')
        bot.send_message(message.chat.id, "Какое количество вы хотите?", reply_markup=user_markup)

    elif message.text == "Написать количество" and choose_count_branded_milkshake == 1:
        user_markup = telebot.types.ReplyKeyboardMarkup(True, False)
        choose_count_branded_milkshake = 2
        user_markup.row('Назад в меню')
        bot.send_message(message.chat.id, "Напишите количество в чат", reply_markup=user_markup)

    elif message.text.isdigit() and choose_count_branded_milkshake == 2 or choose_count_branded_milkshake == 1:
        choose_count_branded_milkshake = 0
        i_coffee_count = message.text
        id_person = message.from_user.id
        second_menu(message)
        func_branded_milkshakes()
# -----------------------------------------------------------------------------------------------------------------------------------------------
    elif message.text == "Лимонады🥤":
        i_size = message.text
        choose_lemonade = 1
        user_markup = telebot.types.ReplyKeyboardMarkup(True, False)
        menu_lemonade = select_all_lemonades()
        for lemonade in menu_lemonade:
            user_markup.row(lemonade[1])
        user_markup.row('Назад в меню')
        bot.send_message(message.chat.id, "Вид лимонадов🥤", reply_markup=user_markup)

    elif message.text and choose_lemonade == 1:
        choose_lemonade = 2
        i_coffee_name = message.text
        user_markup = telebot.types.ReplyKeyboardMarkup(True, False)
        sql = 'SELECT price FROM menu_lemonades WHERE name="' + f'{i_coffee_name}"'
        myqursor.execute(sql)
        result1 = myqursor.fetchall()
        user_markup.row(result1[0][0])
        user_markup.row('Назад в меню')
        bot.send_message(message.chat.id, "Цена за лимонад в тенге", reply_markup=user_markup)

    elif message.text.isdigit() and choose_lemonade == 2:
        i_price = message.text
        choose_count_lemonade = 1
        choose_lemonade = 0
        user_markup = telebot.types.ReplyKeyboardMarkup(True, False)
        user_markup.row("1", "2", "3")
        user_markup.row("4", "5", "6")
        user_markup.row("7", "8", "9")
        user_markup.row('Написать количество')
        user_markup.row('Назад в меню')
        bot.send_message(message.chat.id, "Какое количество вы хотите?", reply_markup=user_markup)

    elif message.text == "Написать количество" and choose_count_lemonade == 1:
        user_markup = telebot.types.ReplyKeyboardMarkup(True, False)
        choose_count_lemonade = 2
        user_markup.row('Назад в меню')
        bot.send_message(message.chat.id, "Напишите количество в чат 🙈", reply_markup=user_markup)

    elif message.text.isdigit() and choose_count_lemonade == 2 or choose_count_lemonade == 1:
        choose_count_lemonade = 0
        i_coffee_count = message.text
        id_person = message.from_user.id
        second_menu(message)
        func_lemonade()
    # -----------------------------------------------------------------------------------------------------------------------------------------------
    elif message.text == "Сэндвичи и выпечки 🥪🥐":
        i_size = message.text
        choose_sandwich = 1
        user_markup = telebot.types.ReplyKeyboardMarkup(True, False)
        menu_sandwich = select_all_sandwiches()
        for sandwich in menu_sandwich:
            user_markup.row(sandwich[1])
        user_markup.row('Назад в меню')
        bot.send_message(message.chat.id, "Виды сэндвичей и выпечек", reply_markup=user_markup)

    elif message.text and choose_sandwich == 1:
        choose_sandwich = 2
        i_coffee_name = message.text
        user_markup = telebot.types.ReplyKeyboardMarkup(True, False)
        sql = 'SELECT price FROM menu_sandwiches WHERE name="' + f'{i_coffee_name}"'
        myqursor.execute(sql)
        result1 = myqursor.fetchall()
        user_markup.row(result1[0][0])
        user_markup.row('Назад в меню')
        bot.send_message(message.chat.id, "Цена за сэндвич(выпечку): в тенге", reply_markup=user_markup)

    elif message.text.isdigit() and choose_sandwich == 2:
        i_price = message.text
        choose_count_sandwich = 1
        choose_sandwich = 0
        user_markup = telebot.types.ReplyKeyboardMarkup(True, False)
        user_markup.row("1", "2", "3")
        user_markup.row("4", "5", "6")
        user_markup.row("7", "8", "9")
        user_markup.row('Написать количество')
        user_markup.row('Назад в меню')
        bot.send_message(message.chat.id, "Какое количество вы хотите?", reply_markup=user_markup)

    elif message.text == "Написать количество" and choose_count_sandwich == 1:
        user_markup = telebot.types.ReplyKeyboardMarkup(True, False)
        choose_count_sandwich = 2
        user_markup.row('Назад в меню')
        bot.send_message(message.chat.id, "Напишите количество в чат 🙈", reply_markup=user_markup)

    elif message.text.isdigit() and choose_count_sandwich == 2 or choose_count_sandwich == 1:
        choose_count_sandwich = 0
        i_coffee_count = message.text
        id_person = message.from_user.id
        second_menu(message)
        func_sandwich()
    # -----------------------------------------------------------------------------------------------------------------------------------------------
    elif message.text == "Корзина 🛒":
        id_person = message.from_user.id
        user_markup = telebot.types.ReplyKeyboardMarkup(True, False)
        user_markup.row("🛒")
        user_markup.row('Назад в главное меню')
        bot.send_message(message.chat.id, "Нажмите на корзину", reply_markup=user_markup)

    elif message.text == "🛒":
        user_markup = telebot.types.ReplyKeyboardMarkup(True, False)
        sql = "select name_food,count,sum,all_sum from menu_new_basket where id_user=" + str(id_person)
        myqursor.execute(sql)
        result = myqursor.fetchall()
        sum = 0
        count = 0
        for i in result:
            sum += i[3]
            count += 1
            bot.send_message(message.chat.id, str(count) + ") Ваш заказ: " + i[0] + ", в количестве: " + str(i[1]) + ", сумма за 1 шт: " + str(
                i[2]) + ", итого: " + str(i[3]))
        bot.send_message(message.chat.id, "-----------------------------------", reply_markup=user_markup)
        bot.send_message(message.chat.id, "Итоговая сумма составляет: " + str(sum) + " тенге")
        bot.send_message(message.chat.id, "1️⃣ Перейдите по ссылке: https://pay.kaspi.kz/pay/3hcbcxv6\n2️⃣ Оплатите сумму: " + str(sum) + ' тенге' +
                         "\n3️⃣ Отправьте скрин или чек в чат\n4️⃣ Через 15 минут ваш заказ будет готов ☕️🥪")
        bot.send_message(message.chat.id, "Спасибо что вы выбрали кофейню GALLIARD 😊🙏")

        sql = "Delete from menu_new_basket"
        myqursor.execute(sql)
        mydb.commit()

    elif message.text == "Нет" and choose_sirop == 1:
        second_menu(message)

    elif message.text == "Назад в меню" and choose_coffee == 3 or choose_coffee == 2 or choose_coffee == 1 or choose_sandwich == 1 or choose_sandwich == 2:
        second_menu(message)

    elif message.text == "Назад в меню" and choose_milkshake == 1 or choose_milkshake == 2 or choose_tea == 1 or choose_tea == 2:
        second_menu(message)

    elif message.text == "Назад в меню" and choose_branded_milkshake == 1 or choose_count_branded_milkshake == 2 or choose_sirop == 13:
        second_menu(message)

    elif message.text == "Назад в меню" and choose_lemonade == 1 or choose_lemonade == 2:
        second_menu(message)

    elif message.text == "Назад в главное меню":
        user_markup = telebot.types.ReplyKeyboardMarkup(True, False)
        user_markup.row("Наше меню 📋")
        user_markup.row("Оформить заказ 🚘", "Связаться с менеджером 👩‍💻")
        user_markup.row("Наша локация 📍", "Корзина 🛒")
        user_markup.row("Выйти")
        bot.send_message(message.chat.id, "Что желаете?", reply_markup=user_markup)

    elif message.text == "Назад":
        user_markup = telebot.types.ReplyKeyboardMarkup(True, False)
        user_markup.row("Наше меню 📋")
        user_markup.row("Оформить заказ 🚘", "Связаться с менеджером 👩‍💻")
        user_markup.row("Наша локация 📍", "Корзина 🛒")
        user_markup.row("Выйти")
        bot.send_message(message.chat.id, "Что желаете?", reply_markup=user_markup)

    elif message.text.lower() == "выйти":
        user_markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
        user_markup.row("Да", "Нет")
        bot.send_message(message.chat.id, "Вы точно хотите выйти?😔", reply_markup=user_markup)

    elif message.text.lower() == "да":
        bot.send_message(message.chat.id, "Спасибо что поситили нас ")

    elif message.text.lower() == "нет":
        user_markup = telebot.types.ReplyKeyboardMarkup(True, False)
        user_markup.row("Наше меню 📋")
        user_markup.row("Оформить заказ 🚘", "Связаться с менеджером 👩‍💻")
        user_markup.row("Наша локация 📍", "Корзина 🛒")
        user_markup.row("Выйти")
        bot.send_message(message.chat.id, "Что желаете?", reply_markup=user_markup)

    elif message.text == "Назад в меню":
        second_menu(message)

    elif message.text == "Назад в главное меню 🔙":
        choose_sirop = 0
        choose_tea = 0
        choose_count_tea = 0
        choose_lemonade = 0
        choose_count_lemonade = 0
        choose_count = 0
        choose_count_branded_milkshake = 0
        choose_branded_milkshake = 0
        choose_milkshake = 0
        choose_count_milkshake = 0
        choose_sandwich = 0
        choose_count_sandwich = 0
        choose_coffee = 0
        user_markup = telebot.types.ReplyKeyboardMarkup(True, False)
        user_markup.row("Наше меню 📋")
        user_markup.row("Оформить заказ 🚘", "Связаться с менеджером 👩‍💻")
        user_markup.row("Наша локация 📍", "Корзина 🛒")
        user_markup.row("Выйти")
        bot.send_message(message.chat.id, "Что желаете?", reply_markup=user_markup)

    elif message.text == "Оформить заказ 🚘":
        user_markup = telebot.types.ReplyKeyboardMarkup(True, False)
        user_markup.row("1️⃣ С помощью доставки 🚘")
        user_markup.row("2️⃣ Самовывозом 🚶‍")
        user_markup.row("Назад в главное меню")
        bot.send_message(message.chat.id, "У нас есть два вида оформление заказа:", reply_markup=user_markup)

    elif message.text == "1️⃣ С помощью доставки 🚘":
        user_markup = telebot.types.ReplyKeyboardMarkup(True, False)
        bot.send_message(message.chat.id,
                         "У нас есть два вида доставки:\n1️⃣ Яндекс еда: https://eda.yandex.kz/almaty/r/galliard\n"
                         "2️⃣ Chocofood: https://chocofood.kz/ru/18?category=20  ", reply_markup=user_markup)

    elif message.text == "2️⃣ Самовывозом 🚶‍":
        user_markup = telebot.types.ReplyKeyboardMarkup(True, False)
        user_markup.row("Нажмите сюда если Вы готовы оформить заказ")
        user_markup.row("Назад в главное меню")
        bot.send_message(message.chat.id,
                         "Самовывоз 🚶:\nОчень удобно и экономит ваше время⏳\nСейчас я вам расскажу как пошагово офромить заказ 📖\n"
                         "1️⃣ Вы можете собрать свое меню 📋\n"
                         "2️⃣ После перейти в корзину 🛒\n"
                         "3️⃣ Опалтить по ссылке через приложение каспи📲\n"
                         "4️⃣ После отправить чек либо скриншот оплаты в чат 🧾\n"
                         "5️⃣ Через 15 минут ваш продукт будет готов \n", reply_markup=user_markup)

    elif message.text == "Нажмите сюда если Вы готовы оформить заказ":
        second_menu(message)

    elif message.text == "Наша локация 📍":
        user_markup = telebot.types.ReplyKeyboardMarkup(True, False)
        bot.send_location(message.chat.id, latitude=43.229137, longitude=76.857828)
        bot.send_message(message.chat.id, "Наша локация в 2 гис: https://go.2gis.com/1j0lm", reply_markup=user_markup)

    elif message.text == "Связаться с менеджером 👩‍💻":
        user_markup = telebot.types.ReplyKeyboardMarkup(True, False)
        user_markup.row("Связаться через приложение ватсапп 📲")
        user_markup.row("Позвонить 📞 нам по номеру +7-700-300-78-68")
        user_markup.row("Назад в главное меню")
        bot.send_message(message.chat.id, "Выберите категорию 🙈", reply_markup=user_markup)

    elif message.text == "Связаться через приложение ватсапп":
        user_markup = telebot.types.ReplyKeyboardMarkup(True, False)
        bot.send_message(message.chat.id, "https://wa.me/77003007868", reply_markup=user_markup)


def func_coffee():
    global i_coffee_name
    global i_coffee_count
    global i_price
    global all_sum
    all_sum = int(i_price) * int(i_coffee_count)
    sql = "insert into menu_new_basket(name_food,id_user,count,sum,all_sum) values(%s,%s,%s,%s,%s)"
    values = (i_coffee_name, id_person, i_coffee_count, i_price, all_sum)
    myqursor.execute(sql, values)
    mydb.commit()


def func_sirop():
    global i_sirop_name
    global i_sirop_price
    all_sum = int(i_sirop_price) * int(i_count_sirop)
    sql = "insert into menu_new_basket(name_food, id_user, count, sum, all_sum) values(%s,%s,%s,%s,%s)"
    values = (i_sirop_name, id_person, i_count_sirop, i_sirop_price, all_sum)
    myqursor.execute(sql, values)
    mydb.commit()


def func_tea():
    global i_coffee_name
    global i_coffee_count
    global i_price
    global all_sum
    all_sum = int(i_price) * int(i_coffee_count)
    sql = "insert into menu_new_basket(name_food,id_user,count,sum,all_sum) values(%s,%s,%s,%s,%s)"
    values = (i_coffee_name, id_person, i_coffee_count, i_price, all_sum)
    myqursor.execute(sql, values)
    mydb.commit()


def func_milkshakes():
    global i_coffee_name
    global i_coffee_count
    global i_price
    global all_sum
    all_sum = int(i_price) * int(i_coffee_count)
    sql = "insert into menu_new_basket(name_food,id_user,count,sum,all_sum) values(%s,%s,%s,%s,%s)"
    values = (i_coffee_name, id_person, i_coffee_count, i_price, all_sum)
    myqursor.execute(sql, values)
    mydb.commit()


def func_branded_milkshakes():
    global i_coffee_name
    global i_coffee_count
    global i_price
    global all_sum
    all_sum = int(i_price) * int(i_coffee_count)
    sql = "insert into menu_new_basket(name_food,id_user,count,sum,all_sum) values(%s,%s,%s,%s,%s)"
    values = (i_coffee_name, id_person, i_coffee_count, i_price, all_sum)
    myqursor.execute(sql, values)
    mydb.commit()


def func_lemonade():
    global i_coffee_name
    global i_coffee_count
    global i_price
    global all_sum
    all_sum = int(i_price) * int(i_coffee_count)
    sql = "insert into menu_new_basket(name_food,id_user,count,sum,all_sum) values(%s,%s,%s,%s,%s)"
    values = (i_coffee_name, id_person, i_coffee_count, i_price, all_sum)
    myqursor.execute(sql, values)
    mydb.commit()


def func_sandwich():
    global i_coffee_name
    global i_coffee_count
    global i_price
    global all_sum
    all_sum = int(i_price) * int(i_coffee_count)
    sql = "insert into menu_new_basket(name_food,id_user,count,sum,all_sum) values(%s,%s,%s,%s,%s)"
    values = (i_coffee_name, id_person, i_coffee_count, i_price, all_sum)
    myqursor.execute(sql, values)
    mydb.commit()


bot.polling(none_stop=True, interval=0)

# elif "как" in message.text.lower() and "дела" in message.text.lower():
#     bot.send_message(message.chat.id, "Хорошо, как твои дела жаным?")
# elif message.text.lower() == "нормально":
#     bot.send_message(message.chat.id, "ммм) что делаешь)? я так соскучился по тебе <3")
# elif message.text.lower() == "/document":
#     directory = "/Users/arystanbekabdrahmanov/Desktop/documents"
#     all_files = os.listdir(directory)
#     random_file = random.choice(all_files)
#     document = open(directory + "/" + random_file, "rb")
#     bot.send_chat_action(message.chat.id, "upload_document")
#     bot.send_document(message.chat.id, document)
#     document.close()
# elif message.text.lower() == "/photo":
#     directory = "/Users/arystanbekabdrahmanov/Desktop/photo"
#     all_files = os.listdir(directory)
#     random_file = random.choice(all_files)
#     photo = open(directory + "/" + random_file, "rb")
#     bot.send_chat_action(message.chat.id, "upload_photo")
#     bot.send_document(message.chat.id, photo)
#     photo.close()
# elif message.text.lower() == "/location":
#     bot.send_location(message.chat.id, latitude=43.248072949999994, longitude=76.91317278422463)
# else:
#     bot.send_message(message.chat.id, "Я таких команд не знаю!!!")


# /Users/arystanbekabdrahmanov/Desktop/dcouments/antonio-gabola-_wZaegHzdQc-unsplash.jpg
