import discord
import requests

from commands.admin import command_de_login, command_help, command_info, command_shop_help, command_rules
from commands.admin.translate_api import translate_api
from commands.base import command_login, command_roll_dice, command_gdz
from commands.base import command_number_choise, command_heads_and_tails
from config import bot, settings, cursor

from commands.admin import command_buy


@bot.command()  # основная информация о пользователе
async def info(ctx, member: discord.Member = None):
    member = member or ctx.message.author
    await command_info.info(ctx, member)


@bot.command()  # команда для выдачи пользователю роли
async def add_role(ctx, role: discord.Role, member: discord.Member = None):
    roles = []
    for i in ctx.message.author.roles:
        roles.append(i.name)

    member = member or ctx.message.author
    if 'Суперадмин' in roles:
        await member.add_roles(role)

    else:
        await ctx.channel.send('У вас нет прав на использование этой команды')


@bot.command()  # Покупка роли
async def buy(ctx, role: discord.Role):
    await command_buy.buy(ctx, role)


@bot.command()  # бан пользователя
async def ban(ctx, member: discord.Member = None, reason=None):
    roles = []
    for i in ctx.message.author.roles:
        roles.append(i.name)

    member = member or ctx.message.author
    if 'Суперадмин' in roles:
        if member == ctx.message.author:
            await ctx.channel.send(f'Нельзя банить самого себя!!!')
        else:
            await ctx.guild.ban(member, reason=reason)
            await ctx.channel.send(f"{member} is banned!")
    else:
        await ctx.channel.send('У вас нет прав на использование этой команды')


@bot.command()  # кикнуть пользователя
async def kick(ctx, member: discord.Member = None, reason=None):
    roles = []
    for i in ctx.message.author.roles:
        roles.append(i.name)

    member = member or ctx.message.author
    if 'Админ' in roles:
        if member == ctx.message.author:
            await ctx.channel.send(f'Нельзя кикнуть самого себя!!!')
        else:
            await ctx.guild.kick(member, reason=reason)
            await ctx.channel.send(f"{member} is kicked!")
    else:
        await ctx.channel.send('У вас нет прав на использование этой команды')


@bot.command()  # разбан пользователя
async def unban(ctx, member):
    banned_users = await ctx.guild.bans()
    for ban_entry in banned_users:
        user = ban_entry.user
        if user.name == member:
            await ctx.guild.unban(user)
            await ctx.send(f"Добро пожаловать. Снова. {member}")


@bot.command()  # "Регистрация" на канале
async def login(ctx):
    await command_login.login(ctx)


@bot.command()  # Выводит список возможных ролей
async def shop(ctx):
    await command_shop_help.shop_help(ctx)


@bot.command()  # "Выход" из канала
async def de_login(ctx):
    await command_de_login.de_login(ctx)


@bot.command()  # добавил команду help
async def help(msg):
    await command_help.help(msg)


@bot.command()  # выводит список игр
async def games(msg):
    emb = discord.Embed(title='Навигация по командам', colour=discord.Color.gold())
    emb.add_field(name='!roll_dice', value='Игра в кости\n'
                                           'Пример ввода: !roll_dice [больше или меньше] [ставка]')
    emb.add_field(name='!choose_number', value='Угадай число от 1 до 5 и сорви Джекпот!!!\n'
                                               'Пример ввода: !choose_number [ставка]')
    emb.add_field(name='!heads_and_tails', value='Игра в монетку.\n'
                                                 ' Пример ввода: !heads_and_tails [орел или решка] [ставка]')
    await msg.channel.send(embed=emb)


@bot.command()  # игра в кости
async def roll_dice(ctx):
    await command_roll_dice.roll_dice(ctx)


@bot.command()  # игра в выбор номера
async def choose_number(ctx, number, bet):
    await command_number_choise.choose_number(ctx, number, bet)


@bot.command()  # игра в "Орел и Решку"
async def heads_and_tails(ctx, user_word, bet):
    money = cursor.execute(f"""SELECT money FROM members WHERE id_of_user = {ctx.message.author.id}""").fetchall()[0]
    if int(bet) <= money[0]:
        await command_heads_and_tails.heads_and_tails(ctx, user_word, bet)
    else:
        await ctx.send(f"Не достаточно коинов.\n"
                       f"Ваш баланс - {money[0]}")


@bot.command()  # переводчик
async def translate(ctx, language='en|ru', *text):
    roles = []
    print(text)
    for i in ctx.message.author.roles:
        roles.append(i.name)

    if 'Переводчик' in roles:
        if language == "en|ru" or language == "ru|en":
            translate = translate_api(f"{language}", ' '.join(text))
            await ctx.send(f'Перевод текста:\n{translate}')
        else:
            await ctx.send(f'Неверно введен язык ввода, повторите попытку')
    else:
        await ctx.channel.send('У вас нет прав на использование этой команды')


@bot.command()  # гдз
async def gdz(ctx):
    await command_gdz.c_gdz(ctx)


@bot.command()  # вывод списка преобретаемых ролей
async def shop_help(ctx):
    await command_shop_help.shop_help(ctx)


@bot.command()  # правила сервера
async def rules(ctx):
    await command_rules.rules(ctx)



bot.run(settings['token'])
