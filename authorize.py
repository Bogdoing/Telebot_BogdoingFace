import sqlite3
from deepface import DeepFace

from PIL import Image
import io

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
        with open("photos/image_handler.jpg", 'wb') as new_file:
            new_file.write(downloaded_file)

        mesg = self.bot.send_message(message.chat.id, 'Введите пароль: ↓')
        self.bot.register_next_step_handler(mesg, self.addtoDB)

    def addtoDB(self, message):
        print("pass - " + message.text)
        with open("photos/registr_img.jpg", 'rb') as f:
            login_photo = f.read()

        print("l_p - " + str(login_photo))
        con = sqlite3.connect("bgface.db")
        print(con)
        c = con.cursor()
        c.execute('INSERT INTO Users (login, login_photo, password) VALUES (?, ?, ?)',
                  ("login", login_photo, message.text))
        con.commit()
        c.execute(
            'SELECT MAX(id) id from Users ')
        result = c.fetchall()
        con.close()

        self.bot.send_message(
            message.chat.id, 'Данные сохранены √')
        self.bot.send_message(
            message.chat.id, 'Ваш ID - ' + str(result))

        self.status = True
        print("self.status - " + str(self.status))
        self.getStatus()

###

    def logInId(self, message):

        con = sqlite3.connect("bgface.db")
        c = con.cursor()
        c.execute(
            'SELECT MAX(id) id from Users ')
        result = c.fetchall()
        con.close()

        print("result = " + str(result) + " | message = " + message.text)

        if int(result[0][0]) < int(message.text):
            print("IF | result = " + str(result) +
                  " >= message = " + message.text)
            self.bot.send_message(
                message.chat.id, 'Вы ввели не корректный ID пользователя')
        else:
            print("ELSE | result = " + str(result) +
                  " <= message = " + message.text)
            self.user_id = message.text
            mesg = self.bot.send_message(
                message.chat.id, 'Отправте своё фото: ↓')
            self.bot.register_next_step_handler(mesg, self.logIN)

    def logIN(self, message):
        print('message.photo =', message.photo)
        fileID = message.photo[-1].file_id
        print('fileID =', fileID)
        file_info = self.bot.get_file(fileID)
        print('file.file_path =', file_info.file_path)
        downloaded_file = self.bot.download_file(file_info.file_path)

        with open("photos/image_handler.jpg", 'wb') as new_file:
            new_file.write(downloaded_file)

        conn = sqlite3.connect("bgface.db")
        cursor = conn.cursor()
        cursor.execute(
            'select login_photo from Users where id = ?', (self.user_id,))
        result = cursor.fetchone()[0]

        if result is None:
            self.bot.send_message(
                message.chat.id, 'Такого пользователя нету')
        else:
            with open("photos/log_db_img.jpg", 'wb') as new_file:
                new_file.write(result)
            result = face.face_verify_2(
                "photos/image_handler.jpg", "photos/log_db_img.jpg")
            self.bot.send_message(message.chat.id, "Verified - " + result)
            print(result)
            if result == 'is True':
                self.status = True
                self.bot.send_message(
                    message.chat.id, 'Авторизация прошла успешно ID пользователя : ' + str(self.user_id))
            else:
                self.status = False
                self.bot.send_message(
                    message.chat.id, 'Авторизация провалилась . \nПроверьте пароль или отправьте более чёткое фото')

        conn.close()

###

    def louOUT(self):
        self.status = False
