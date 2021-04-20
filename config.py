import sqlite3

from discord.ext.commands import Bot

settings = {  # Добавил файл с конфигом
    'token': 'ODMyMjc1NjM5MzAxOTYzODE2.YHhbFw.T_g8oYA8NJjm4Tg5697bDIs9QPw',
    'bot': 'Сервер Ermatkus',
    'id': 832327621135433758,  # нужен id(без ковычек)
    'command_prefix': '!'
}

role_ids = {  # IDs of the roles for the teams
    'Простолюдин': 236628751650258944,
    'Администратор': 325076193122451457,
}

bot = Bot(command_prefix=settings['command_prefix'])
bot.remove_command('help')
dashes = ['\u2680', '\u2681', '\u2682', '\u2683', '\u2684', '\u2685']  # игральные кубики от 1 до 6, unicode символы
sqlite_connection = sqlite3.connect('members.db')
cursor = sqlite_connection.cursor()
