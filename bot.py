import telebot
from deepface import DeepFace
import time

import DATA
import face
import infrastructyre

bot = telebot.TeleBot(DATA.TOKEN, parse_mode=None)


@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, "Howdy, how are you doing?")


# @bot.message_handler(func=lambda message: True)
# def echo_all(message):
#     bot.reply_to(message, message.text)

@bot.message_handler(commands=['comparison', 'com'])
def comparison_face(message):
    result = DeepFace.verify(img1_path="img/jim1.jpg",
                             img2_path="img/jim2.jpg")
    bot.reply_to(message, "Jim verified - " + str(result.get('verified')))
    print(result)


@bot.message_handler(commands=['comparison1', 'com1'])
def comparison_face1(message):
    infrastructyre.time_saver(message=message, bot=bot)
    result = face.comparison_face("img/jim1.jpg", "img/jim2.jpg")
    bot.reply_to(message, "Body verified - " + str(result.get('verified')))
    print(result)


@bot.message_handler(content_types=['photo'])
def photo(message):
    print('message.photo =', message.photo)
    fileID = message.photo[-1].file_id
    print('fileID =', fileID)
    file_info = bot.get_file(fileID)
    print('file.file_path =', file_info.file_path)
    downloaded_file = bot.download_file(file_info.file_path)

    with open("photos/image_handler.jpg", 'wb') as new_file:
        new_file.write(downloaded_file)

    # infrastructyre.time_saver(message=message, bot=bot)
    result = face.face_verify("img/body11.jpg")
    bot.reply_to(message, "Verified - " + result)
    print(result)
    result_dist = face.face_analyz()

    # print data json
    infrastructyre.print_data_json(message, bot, result_dist)


@bot.message_handler(commands=['photos'])
def photostest(message):
    print('analyz last photo')
    infrastructyre.time_saver(message=message, bot=bot)
    result = face.face_verify("img/body11.jpg")
    infrastructyre.serch_last_photo(message=message, bot=bot)
    bot.reply_to(message, "Verified - " + result)
    print(result)
    result_dist = face.face_analyz()
    # print data json
    infrastructyre.print_data_json(message, bot, result_dist)


@bot.message_handler(commands=['singIN'])
def sing(message):
    print('sing')
    bot.send_message(message.chat.id, 'Регитсрация')
    bot.send_message(message.chat.id, 'Пришлите фото для регистрации')


@bot.message_handler(commands=['test'])
def test(message):
    infrastructyre.users_counter_file()


bot.infinity_polling()
