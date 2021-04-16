from discord.ext.commands import Bot
from config import settings

bot = Bot(command_prefix=settings['command_prefix'])


@bot.listen('on_message')  # исправил проблему с on_message (запрещал запуск любых дополнительных команд)
async def on_message(msg):
    if msg.author != bot.user:
        if msg.content.lower() == 'привет':
            await msg.channel.send(f'Привет, {msg.author.mention}')


@bot.command()  # добавил команду help
async def help(msg):
    await msg.channel.send(f'Привет, {msg.author.mention}\n'
                           f'Я умею выполнять следующие команды:\n'
                           f'!help - выводит список всех доступных команд')


bot.run(settings['token'])
