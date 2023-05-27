import sqlite3
from deepface import DeepFace

import face
import infrastructyre


class Authorize():

    bot = "object"
    status = False
    user_id = 0

    login = 0
    login_photo = 0
    password = 0

    def __init__(self, bot) -> None:
        self.bot = bot


###


    def getUserId(self):
        print("User id - " + str(self.user_id))
        return self.user_id

    def getStatus(self):
        print("STATUS - " + str(self.status))
        return self.status

    def getBotAut(self):
        print("bot  - " + str(self.bot))

###

    def photo_reg(self, message):
        print('message.photo =', message)
        print('message.photo =', message.photo)
        fileID = message.photo[-1].file_id
        print('fileID-1 =', fileID)
        file_info = self.bot.get_file(fileID)
        print('file.file_path =', file_info.file_path)
        downloaded_file = self.bot.download_file(file_info.file_path)

        with open("photos/registr_img.jpg", 'wb') as new_file:
            new_file.write(downloaded_file)

        mesg = self.bot.send_message(message.chat.id, 'Введите пароль: ↓')

        self.bot.register_next_step_handler(mesg, self.addtoDB)

    def addtoDB(self, message):

        print("pass - " + message.text)

        login = "login"
        with open("photos/registr_img.jpg", 'rb') as f:
            login_photo = f.read()

        print("l_p - " + str(login_photo))

        con = sqlite3.connect("bgface.db")
        print(con)

        c = con.cursor()

        # con.execute(
        #     '''CREATE TABLE Users (Id INTEGER PRIMARY KEY, login VARCHAR(255), login_photo BLOB, password VARCHAR(255));''')

        c.execute('INSERT INTO Users (login, login_photo, password) VALUES (?, ?, ?)',
                  ("login", login_photo, message.text))
        con.commit()
        con.close()

        mesg = self.bot.send_message(
            message.chat.id, 'Данные сохранены √')

        self.status = True
        print("self.status - " + str(self.status))
        self.getStatus()

###

    def photo_log(self, message):
        print('message.photo =', message)
        print('message.photo =', message.photo)
        fileID = message.photo[-1].file_id
        print('fileID-1 =', fileID)
        file_info = self.bot.get_file(fileID)
        print('file.file_path =', file_info.file_path)
        downloaded_file = self.bot.download_file(file_info.file_path)

        with open("photos/log_img.jpg", 'wb') as new_file:
            new_file.write(downloaded_file)

        mesg = self.bot.send_message(message.chat.id, 'Введите логин: ↓')

        self.bot.register_next_step_handler(mesg, self.logIN)

    def logIN(self, message):
        conn = sqlite3.connect("bgface.db")
        cursor = conn.cursor()

        # Выполняем запрос к базе данных
        cursor.execute(
            'select login_photo from Users where id = ?', message.text)

        # Получаем результат запроса
        result = cursor.fetchall()

        if result is None:
            mesg = self.bot.send_message(
                message.chat.id, 'Такого пользователя нету')
        else:
            self.user_id = message.text
            with open("photos/log_img.jpg", 'rb') as f:
                login_photo = f.read()

                result = face.face_verify("photos/log_img.jpg")
                self.bot.send_message(message.chat.id, "Verified - " + result)
                print(result)
                result_dist = face.face_analyz()

                # print data json
                infrastructyre.print_data_json(message, self.bot, result_dist)

        # Закрываем соединение с базой данных
        conn.close()

    def louOUT(self):
        self.status = False


# def photo(message):
#     print('message.photo =', message.photo)
#     fileID = message.photo[-1].file_id
#     print('fileID =', fileID)
#     file_info = bot.get_file(fileID)
#     print('file.file_path =', file_info.file_path)
#     downloaded_file = bot.download_file(file_info.file_path)

#     with open("photos/image_handler.jpg", 'wb') as new_file:
#         new_file.write(downloaded_file)

#     result = face.face_verify("img/body11.jpg")
#     bot.reply_to(message, "Verified - " + result)
#     print(result)
#     result_dist = face.face_analyz()

#     # print data json
#     infrastructyre.print_data_json(message, bot, result_dist)
