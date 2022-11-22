import telebot
from dados import *



bot = telebot.TeleBot(token)

texto = input('Qual mensagem devo enviar? ')



def SendMenssage():
    
    bot.send_message(chat_id1, texto )

    bot.send_message(chat_id2, texto)


    bot.get_updates()
    
SendMenssage()