import telebot
from deepface import DeepFace
import sqlite3


import DATA
import face
import infrastructyre
import authorize

bot = telebot.TeleBot(DATA.TOKEN, parse_mode=None)
aut = authorize.Authorize(bot)


@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, "Howdy, how are you doing?")


@bot.message_handler(commands=['singin'])
def sing(message):
    print('singIN')
    print('getStatus - ' + str(aut.getStatus()))
    if aut.getStatus() == True:
        mesg = bot.send_message(message.chat.id, 'Вы уже авторизированны.')
    else:
        mesg = bot.send_message(message.chat.id, 'Отправте своё фото: ↓')
        print("botT - " + str(bot))
        aut.getBotAut()
        bot.register_next_step_handler(mesg, aut.photo_reg)


@bot.message_handler(commands=['login'])
def login(message):
    print('logIN')
    if aut.getStatus() == True:
        mesg = bot.send_message(message.chat.id, 'Вы уже авторизированны.')
    else:
        mesg = bot.send_message(message.chat.id, 'Введите свой Id: ↓')
        print("botT - " + str(bot))
        aut.getBotAut()
        bot.register_next_step_handler(mesg, aut.logInId)


@bot.message_handler(commands=['logout'])
def logout(message):
    print('logOUT')
    if aut.getStatus() == False:
        mesg = bot.send_message(message.chat.id, 'Вы ещё не авторизированны.')
    else:
        mesg = bot.send_message(message.chat.id, 'Вы вышли.')
        print("botT - " + str(bot))
        aut.louOUT()


@bot.message_handler(commands=['info'])
def info(message):
    print('info')
    if aut.getStatus() == False:
        bot.send_message(
            message.chat.id, 'Чтобы узнать информациб пользователя необходимо авторизоваться')
    else:
        result_dist = face.face_analyz()
        infrastructyre.print_data_json(message, bot, result_dist)


@bot.message_handler(commands=['face'])
def faces(message):
    mesg = bot.send_message(message.chat.id, 'Отправьте фото для обработки: ↓')
    bot.register_next_step_handler(mesg, faces_analyze)


def faces_analyze(message):
    print('message.photo =', message.photo)
    fileID = message.photo[-1].file_id
    print('fileID =', fileID)
    file_info = bot.get_file(fileID)
    print('file.file_path =', file_info.file_path)
    downloaded_file = bot.download_file(file_info.file_path)

    with open("photos/image_handler.jpg", 'wb') as new_file:
        new_file.write(downloaded_file)

    result_dist = face.face_analyz()
    if result_dist == "Error face - face_analyz":
        print("ERORS")
        bot.send_message(
            message.chat.id, 'Face not found. Try again \nЛицо не найдено. Попробуйте ещё раз')
    else:
        infrastructyre.print_data_json(message, bot, result_dist)


bot.infinity_polling()


# @bot.message_handler(commands=['comparison', 'com'])
# def comparison_face(message):
#     result = DeepFace.verify(img1_path="img/jim1.jpg",
#                              img2_path="img/jim2.jpg")
#     bot.reply_to(message, "Jim verified - " + str(result.get('verified')))
#     print(result)


# @bot.message_handler(commands=['comparison1', 'com1'])
# def comparison_face1(message):
#     infrastructyre.time_saver(message=message, bot=bot)
#     result = face.comparison_face("img/jim1.jpg", "img/jim2.jpg")
#     bot.reply_to(message, "Body verified - " + str(result.get('verified')))
#     print(result)
