import time
import telepot
from telepot.loop import MessageLoop

bot = telepot.Bot("1015265631:AAH4-VmsN3VPsdydnNcDsguLXYamJJYdHGw")

res = bot.getUpdates()
print(bot.getMe())
# message = res[-1]["message"]["text"]
# date = res[-1]["message"]["date"]
# sender = res[-1]["message"]["from"]
chat = res[-1]["message"]["chat"]
# print(res)
# response_message = "Hello I'm a bot I have received your message"
# bot.sendMessage(chat["id"], f"{response_message}:{message}")
print(res)
print(chat["id"])
# bot.sendMessage(682848353, "Welcome")
#
# def handle(msg):
#     content_type, chat_type, chat_id = telepot.glance(msg)
#     print(content_type, chat_type, chat_id)
#
#     if content_type == 'text':
#         bot.sendMessage(chat_id, msg['text'] + "?")
#
#
# MessageLoop(bot, handle).run_as_thread()
# print('Listening ...')
#
# # Keep the program running.
# while 1:
#     time.sleep(10)
