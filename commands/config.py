import sqlite3
from discord.ext.commands import Bot

settings = {  # Добавил файл с конфигом
    'token': 'ODMyMzI3NjIxMTM1NDMzNzU4.YHiLgA.CahtQinYUi91AN0eq8Ahkswp9C8',  # нужен токен,
    'bot': 'Сервер Ermatkus',
    'id': 832327621135433758,  # нужен id(без ковычек)
    'command_prefix': '!'
}


bot = Bot(command_prefix=settings['command_prefix'])
bot.remove_command('help')
dashes = ['\u2680', '\u2681', '\u2682', '\u2683', '\u2684', '\u2685']  # игральные кубики от 1 до 6, unicode символы
sqlite_connection = sqlite3.connect('members.db')
cursor = sqlite_connection.cursor()
