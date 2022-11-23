from PySimpleGUI import PySimpleGUI as sg
from telegram import *

#Layout
#DarkBlue19
sg.theme('Reddit')
layout = [
    [sg.Text('Texto de envio:'), sg.Input()],
    [sg.Button('Enviar')]
]
valores = ['Texto de envio:']
#Janela
janela = sg.Window('Bot Telegram', layout)
#Ler os eventos
while True:
    eventos, valores = janela.read()
    if eventos == sg.WINDOW_CLOSED:
        break
    if eventos == 'Enviar':

        import telebot
        from dados import *
        from front import *



        bot = telebot.TeleBot(token)

        #texto = layout['Texto de envio:']



        def SendMenssage():
    
            bot.send_message(chat_id1, valores )

            bot.send_message(chat_id2, valores)


            bot.get_updates()
    
        SendMenssage()