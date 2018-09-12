from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import logging

PROXY = {'proxy_url': 'socks5://t1.learn.python.ru:1080',
    'urllib3_proxy_kwargs': {'username': 'learn', 'password': 'python'}}
# Enable logging
logging.basicConfig(format='%(asctime)s - %(levelname)s - %(message)s',
                    level=logging.INFO,
                    filename='bot.log'
                    )
import settings
import cities
import ephem
import cities
from datetime import datetime, date
date = datetime.now()

def greet_user(bot, update):
    text = """Привет, {}! 
Я простой бот. Используй команду /help, 
чтобы узнать, что я умею""".format(update.message.chat.first_name)
    update.message.reply_text(text)

def talk_to_me(bot, update):
    user_text = update.message.text 
    update.message.reply_text(user_text)

def help_(bot, update):
    text = """Я понимаю следующие команды: 
    /planet - определение в каком созвездии находится планета сегодня. Чтобы восплользоваться этой функцией, введите название планеты после команды planet
    /wordcount - подсчет слов в  сообщении после команды
    /calculator - выполнение арифметических операции из одного дествия, например "2+3=". Понимает умножение, деление, сложение и вычитание. 
    /fullmoon - вывод ближайщего полнолуния после даты в формате год/месяц/день"""
    update.message.reply_text(text)


def constellation(bot, update, args):
    planet = args[0]
    if planet.lower() == 'меркурий':
        planet = ephem.Mercury(date)
        planet = ephem.constellation(planet)
        update.message.reply_text("Меркурий в созвездии {}".format(planet))

    elif planet.lower() == 'венера':
        planet = ephem.Venus(date)
        planet = ephem.constellation(planet)
        update.message.reply_text("Венера в созвездии {}".format(planet))

    elif planet.lower() == 'марс':
        planet = ephem.Mars(date)
        planet = ephem.constellation(planet)
        update.message.reply_text("Марс в созвездии {}".format(planet))

    elif planet.lower() == 'юпитер':
        planet = ephem.Jupiter (date)
        planet = ephem.constellation(planet)
        update.message.reply_text("Юпитер в созвездии {}".format(planet))

    elif planet.lower() == 'сатурн':
        planet = ephem.Saturn(date)
        planet = ephem.constellation(planet)
        update.message.reply_text("Сатурн в созвездии {}".format(planet))

    elif planet.lower() == 'уран':
        planet = ephem.Uranus(date)
        planet = ephem.constellation(planet)
        update.message.reply_text("Уран в созвездии {}".format(planet))

    elif planet.lower() == 'нептун':
        planet = ephem.Neptune(date)
        planet = ephem.constellation(planet)
        update.message.reply_text("Нептун в созвездии {}".format(planet)) 
    else: 
        update.message.reply_text("Я знаю только семь планет солнечной системы: Меркурий, Марс, Венеру, Юпитер, Уран, Нептун, Сатурн.")

        
def calculate(string):

    if string[-1] is '=':
        errormsg ='В вопросе не хватает цифр или есть неизвестные арифметические операции'
        string = string.replace("=", "")
        if "+" in string:
            digits = string.split('+')
            if (digits[0].isdigit() and digits[1].isdigit()):
                answer = sum(map(int, digits))
            else:
                answer = errormsg
        elif "-" in string:
            digits = string.split('-')
            if (digits[0].isdigit() and digits[1].isdigit()):
                answer = int(digits[0])-int(digits[1])
            else:
                answer = errormsg
        elif "*" in string:
            digits = string.split('*')
            if (digits[0].isdigit() and digits[1].isdigit()):
                answer = (int(digits[0]))*(int(digits[1]))
            else:
                answer = errormsg
        elif "/" in string:
            digits = string.split('/')
            if digits[1] == "0":
                answer = "На ноль делить нельзя!"
            elif (digits[0].isdigit() and digits[1].isdigit()): 
                answer = (int(digits[0]))/(int(digits[1]))
            else:
                    answer = errormsg
    else: 
        answer = ("Выражение должно заканчиваться знаком '='")
    return(answer)


def calc(bot, update, args):

    message = update.message.text.replace("/calculator", "")
    message =message.replace(":", "")
    message =message.replace(" ", "") 
    answer = calculate(message)
    update.message.reply_text(answer)  
    

def wcalc(bot, update, args):
    operands = {"один": 1, 
    "два": 2, 
    "три": 3, 
    "четыре": 4,
     "пять": 5, 
    "шесть": 6, 
    "семь" : 7, 
    "восемь": 8,
     "девять": 9,
      "ноль": 0, 
      "умножить":'*', 
      "поделить":'/', 
      "плюс": '+', 
      "минус": "-", 
      "равно":'='}
    message = ""
    for arg in args:
        if arg in operands:
            message += str(operands[arg])
    answer = calculate(message)
    update.message.reply_text(answer)  

def counter(bot, update, args):

    wordcount = len(args)
    if wordcount in [1, 21, 31, 41]:
        update.message.reply_text(" В сообщении {} слово".format(wordcount))
    elif wordcount in [2, 3, 4, 22, 23, 24, 32, 33, 34] :
        update.message.reply_text(" В сообщении {} слова".format(wordcount))
    else:
        update.message.reply_text(" В сообщении {} слов".format(wordcount))


def moon(bot, update, args):

    next_full_moon = ephem.next_full_moon(args[0])
    update.message.reply_text("Следующее полнолуние будет {}".format(next_full_moon))
            

    

def main():
    updtr = Updater(settings.TELEGRAM_API_KEY, request_kwargs=PROXY)
    dp = updtr.dispatcher
    dp.add_handler(CommandHandler("start",greet_user ))
    dp.add_handler(CommandHandler("help", help_))
    dp.add_handler(CommandHandler("planet", constellation, pass_args=True))
    dp.add_handler(CommandHandler("wordcount", counter, pass_args=True))
    dp.add_handler(CommandHandler("calculator", calc, pass_args=True))
    dp.add_handler(CommandHandler("wcalc", wcalc, pass_args=True))
    dp.add_handler(CommandHandler("fullmoon", moon, pass_args=True))
    dp.add_handler(CommandHandler("cities", cities, pass_args=True))
    dp.add_handler(MessageHandler(Filters.text, talk_to_me))


    updtr.start_polling()
    updtr.idle()


if __name__ == '__main__':
    logging.info('bot started')
    main()