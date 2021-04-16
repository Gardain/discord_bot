import random

from discord.ext.commands import Bot
from config import settings

bot = Bot(command_prefix=settings['command_prefix'])
bot.remove_command('help')
dashes = ['\u2680', '\u2681', '\u2682', '\u2683', '\u2684', '\u2685']  # игральные кубики от 1 до 6, unicode символы


@bot.listen('on_message')  # исправил проблему с on_message (запрещал запуск любых дополнительных команд)
async def on_message(msg):
    if msg.author != bot.user:
        if msg.content.lower() == 'привет':
            await msg.channel.send(f'Привет, {msg.author.mention}')


@bot.command()  # добавил команду help
async def help(msg):
    await msg.channel.send(f'Привет, {msg.author.mention}\n'
                           f'Я умею выполнять следующие команды:\n'
                           f'!help - выводит список всех доступных команд\n'
                           f'!games - выводит список возможных игр')


@bot.command()  # добавил команду help
async def games(msg):
    await msg.channel.send(f'У меня есть такие игры:\n'
                           f'!roll_dice - в\n'
                           f'!my_randint\n'
                           f'!heads_and_tails')


@bot.command()
async def heads_and_tails(ctx, user_word):
    num = random.randint(0, 1)
    if num == 0:
        if user_word.lower() == 'орёл':
            await ctx.send("Орёл! Вы выиграли!")
        else:
            await ctx.send("Орёл! Вы проиграли!")
    else:
        if user_word.lower() == 'решка':
            await ctx.send("Решка! Вы выиграли!")
        else:
            await ctx.send("Решка! Вы проиграли!")


@bot.command()
async def roll_dice(ctx, count):
    res = [random.choice(dashes) for _ in range(int(count))]
    await ctx.send(" ".join(res))


@bot.command()
async def my_randint(ctx, min_int, max_int):
    num = random.randint(int(min_int), int(max_int))
    await ctx.send(num)


bot.run(settings['token'])
