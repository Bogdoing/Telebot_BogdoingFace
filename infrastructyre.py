import time


def time_saver(message, bot):
    msg = bot.send_message(message.chat.id, 'Loading')
    flag = 0
    while (flag < 10):
        time.sleep(0.05)
        bot.edit_message_text(chat_id=message.chat.id,
                              message_id=msg.message_id, text='Loading\\')
        time.sleep(0.05)
        bot.edit_message_text(chat_id=message.chat.id,
                              message_id=msg.message_id, text='Loading|')
        time.sleep(0.05)
        bot.edit_message_text(chat_id=message.chat.id,
                              message_id=msg.message_id, text='Loading/')
        time.sleep(0.05)
        bot.edit_message_text(chat_id=message.chat.id,
                              message_id=msg.message_id, text='Loading-')
        flag = flag + 1


def serch_last_photo(message, bot):
    # bot.send_message(message.chat.id, 'Loading')
    # time_saver(message, bot)
    if message.text == 'Loading' or "Loading":
        bot.delete_message(message.chat.id, message.message_id)
        # bot.delete_message(message.chat.id, message.message_id + 1)


def print_data_json(message, bot, result_dist):
    bot.send_message(message.chat.id, f'''
[+] Age: {result_dist.get("age")}
[+] Gender: {result_dist.get("dominant_gender")}
  -Woman {round(result_dist.get("gender").get("Woman"), 4)}%
  -Man {round(result_dist.get("gender").get("Man"), 4)}%

[+] Race domain: {result_dist.get("dominant_race")} 
[+] Race all:
 -asian {round(result_dist.get("race").get("asian"), 4)}% 
 -indian {round(result_dist.get("race").get("indian"), 4)}% 
 -black {round(result_dist.get("race").get("black"), 4)}% 
 -white {round(result_dist.get("race").get("white"), 4)}% 
 -middle eastern {round(result_dist.get("race").get("middle eastern"), 4)}% 
 -latino hispanic {round(result_dist.get("race").get("latino hispanic"), 4)}%

[+] Dominant emotion: {result_dist.get("dominant_emotion")}
[+] Dominant emotion:
 -angry {round(result_dist.get("emotion").get("angry"), 4)}% 
 -disgust {round(result_dist.get("emotion").get("disgust"), 4)}% 
 -fear {round(result_dist.get("emotion").get("fear"), 4)}% 
 -happy {round(result_dist.get("emotion").get("happy"), 4)}% 
 -sad {round(result_dist.get("emotion").get("sad"), 4)}% 
 -surprise {round(result_dist.get("emotion").get("surprise"), 4)}% 
 -neutral {round(result_dist.get("emotion").get("neutral"), 4)}%

''')

    # bot.send_message(message.chat.id, f'[+] Age: {result_dist.get("age")}')
    # bot.send_message(
    #     message.chat.id, f'[+] Gender: {result_dist.get("dominant_gender")} \n *Woman {round(result_dist.get("gender").get("Woman"), 4)}% \n *Man {round(result_dist.get("gender").get("Man"), 4)}%')
    # # bot.send_message(
    # #     message.chat.id, f'[+] Race domain: {result_dist.get("dominant_race")}')
    # bot.send_message(
    #     message.chat.id, f'[+] Race domain: {result_dist.get("dominant_race")} \n[+] Race all: \n *asian {round(result_dist.get("race").get("asian"), 4)}% \n *indian {round(result_dist.get("race").get("indian"), 4)}% \n *black {round(result_dist.get("race").get("black"), 4)}% \n *white {round(result_dist.get("race").get("white"), 4)}% \n *middle eastern {round(result_dist.get("race").get("middle eastern"), 4)}% \n *latino hispanic {round(result_dist.get("race").get("latino hispanic"), 4)}%')

    # bot.send_message(
    #     message.chat.id, f'[+] Dominant emotion: {result_dist.get("dominant_emotion")} \n[+] Dominant emotion:\n *angry {round(result_dist.get("emotion").get("angry"), 4)}% \n *disgust {round(result_dist.get("emotion").get("disgust"), 4)}% \n *fear {round(result_dist.get("emotion").get("fear"), 4)}% \n *happy {round(result_dist.get("emotion").get("happy"), 4)}% \n *sad {round(result_dist.get("emotion").get("sad"), 4)}% \n *surprise {round(result_dist.get("emotion").get("surprise"), 4)}% \n *neutral {round(result_dist.get("emotion").get("neutral"), 4)}%')


def users_counter_file():
    counter = ''
    try:
        with open("data/userscounter.txt", "r") as file:
            for line in file:
                counter = line
                # print(line, end="")
    except:
        print('ERORS READ userscounter')
    print(counter)
    try:
        count_int = int(counter)
        print(count_int)
        count_int = count_int + 1
    except:
        print('ERORS CONVERT userscounter')

    count_writer = 0  # это запысыватеся в файл
    with open("data/userscounter.txt", "w") as file:
        str_count = str(count_writer)
        file.write(str_count)
    # try:
    #     count_writer = 0
    #     with open("data/userscounter.txt", "w") as file:
    #         file.write(count_writer)
    #         # print('write ' + count_writer)
    # except:
    #     print('ERORS WRITE userscounter')
