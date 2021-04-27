import discord

from commands.admin import command_de_login, command_help, command_info
from commands.base import command_login, command_roll_dice
from config import bot, settings
from discord_bot.commands.base import command_number_choise, command_heads_and_tails


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
    emb = discord.Embed(title='Навигация по командам', colour=discord.Color.gold())
    emb.add_field(name='!roll_dice', value='Игра в кости\n'
                                           'Пример ввода: !roll_dice [больше или меньше] [ставка]')
    emb.add_field(name='!choose_number', value='Угадай число от 1 до 5 и сорви Джекпот!!!\n'
                                               'Пример ввода: !choose_number [ставка]')
    emb.add_field(name='!heads_and_tails', value='Игра в монетку.\n'
                                                 ' Пример ввода: !heads_and_tails [орел или решка] [ставка]')
    await msg.channel.send(embed=emb)


@bot.command()
async def heads_and_tails(ctx, user_word, bet):
    await command_heads_and_tails.heads_and_tails(ctx, user_word, bet)


@bot.command()
async def roll_dice(ctx):
    await command_roll_dice.roll_dice(ctx)


@bot.command()
async def choose_number(ctx, number, bet):
    await command_number_choise.choose_number(ctx, number, bet)


bot.run(settings['token'])
