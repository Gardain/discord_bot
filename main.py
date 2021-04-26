import random
import discord

from commands.admin import command_de_login, command_help, command_info, command_login
from config import bot, dashes, settings
from discord_bot.commands.admin.add_coins import add_coins
from discord_bot.commands.admin.take_away_coins import take_away_coins


@bot.listen('on_message')  # исправил проблему с on_message (запрещал запуск любых дополнительных команд)
async def on_message(msg):
    if msg.author != bot.user:
        if msg.content.lower() == 'приве2т':
            await msg.channel.send(f'Привет, {msg.author.mention}')


@bot.command()  # основная информация о пользователе
async def info(ctx, member: discord.Member = None):
    member = member or ctx.message.author
    await command_info.info(ctx, member)


@bot.command()  # команда для выдачи пользователю роли
async def add_role(ctx, role: discord.Role, member: discord.Member = None):
    member = member or ctx.message.author
    await member.add_roles(role)


@bot.command()  # "Регистрация" на канале
async def login(ctx):
    await command_login.login(ctx)


@bot.command()  # "Выход" из канала
async def de_login(ctx):
    await command_de_login.de_login(ctx)


@bot.command()  # добавил команду help
async def help(msg):
    await command_help.help(msg)


@bot.command()
async def games(msg):
    await msg.channel.send(f'У меня есть такие игры:\n'
                           f'!roll_dice\n'
                           f'!my_randint\n'
                           f'!heads_and_tails')


@bot.command()
async def heads_and_tails(ctx, user_word, bet):
    num = random.choice(["орёл", "решка"])
    if num == "орёл":
        if user_word.lower() == 'орёл':
            add_coins(ctx.message.author, int(bet) * 2)
            await ctx.send("Орёл! Вы выиграли!")
        else:
            take_away_coins(ctx.message.author, int(bet))
            await ctx.send("Орёл! Вы проиграли!")
    else:
        if user_word.lower() == 'решка':
            add_coins(ctx.message.author, int(bet) * 2)
            await ctx.send("Решка! Вы выиграли!")
        else:
            take_away_coins(ctx.message.author, int(bet))
            await ctx.send("Решка! Вы проиграли!")


@bot.command()
async def roll_dice(ctx, count):
    res = [random.choice(dashes) for _ in range(int(count))]
    await ctx.send(" ".join(res))


#@bot.command()
#async def my_randint(ctx, min_int, max_int):
 #   num = random.randint(int(min_int), int(max_int))
 #   await ctx.send(num)


bot.run(settings['token'])
