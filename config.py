import sqlite3

from discord.ext.commands import Bot

settings = {  # Добавил файл с конфигом
    'token': 'ODMyMjc1NjM5MzAxOTYzODE2.YHhbFw.2iLCaEjQlbMp2SK-ehDCTxl_7xo',
    'bot': 'Сервер Ermatkus',
    'id': 832327621135433758,  # нужен id(без ковычек)
    'command_prefix': '!'
}

bot = Bot(command_prefix=settings['command_prefix'])
bot.remove_command('help')
array_of_dashes = ['\u2680', '\u2681', '\u2682', '\u2683', '\u2684', '\u2685']

dashes = {'9856': 1,
          '9857': 2,
          '9858': 3,
          '9859': 4,
          '9860': 5,
          '9861': 6}  # игральные кубики от 1 до 6, unicode символы

sqlite_connection = sqlite3.connect('members.db')
cursor = sqlite_connection.cursor()
