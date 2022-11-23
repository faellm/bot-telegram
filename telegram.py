import telebot
from dados import *
from front import *



bot = telebot.TeleBot(token)

texto = layout['Texto de envio:']



def SendMenssage():
    
    bot.send_message(chat_id1, texto )

    bot.send_message(chat_id2, texto)


    bot.get_updates()
    
SendMenssage()