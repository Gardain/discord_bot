import discord
import requests

from commands.admin import command_de_login, command_help, command_info
from commands.base import command_login, command_roll_dice, command_gdz
from commands.base import command_number_choise, command_heads_and_tails
from config import bot, settings, cursor
from discord_bot.commands.admin import command_shop, command_student, command_translater, command_admin


@bot.listen('on_message')  # исправил проблему с on_message (запрещал запуск любых дополнительных команд)
async def on_message(msg):
    if msg.author != bot.user:
        if msg.content.lower() == 'привет':
            await msg.channel.send(f'Привет, {msg.author.mention}')


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
    # if 'Суперадмин' in roles:
    await member.add_roles(role)
    # else:
    # await ctx.channel.send('У вас нет прав на использование этой команды')


@bot.command()
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


@bot.command()
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
    await command_shop.shop(ctx)


@bot.command()  # Покупка роли Школьник
async def student(ctx, role: discord.Role, member: discord.Member = None):
    await command_student.student(ctx, role, member)


@bot.command()  # Покупка роли Переводчик
async def translater(ctx, role: discord.Role, member: discord.Member = None):
    await command_translater.translater(ctx, role, member)


@bot.command()  # Покупка роли Администратор
async def admin(ctx, role: discord.Role, member: discord.Member = None):
    await command_admin.admin(ctx, role, member)



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
async def roll_dice(ctx):
    await command_roll_dice.roll_dice(ctx)


@bot.command()
async def choose_number(ctx, number, bet):
    await command_number_choise.choose_number(ctx, number, bet)


@bot.command()
async def heads_and_tails(ctx, user_word, bet):
    money = cursor.execute(f"""SELECT money FROM members WHERE id_of_user = {ctx.message.author.id}""").fetchall()[0]
    if int(bet) <= money[0]:
        await command_heads_and_tails.heads_and_tails(ctx, user_word, bet)
    else:
        await ctx.send(f"Не достаточно коинов.\n"
                       f"Ваш баланс - {money[0]}")


@bot.command()
async def translate(ctx, language='en|ru', *text):
    roles = []
    for i in ctx.message.author.roles:
        roles.append(i.name)

    if 'Переводчик' in roles:
        url = "https://api.mymemory.translated.net/get"
        fromm, on = language.split('|')
        if (fromm == 'ru' or fromm == 'en') and (on == 'ru' or on == 'en'):
            querystring = {"langpair": f"{fromm}|{on}", "q": text}
            response = requests.request("GET", url, params=querystring).json()
            await ctx.send(f'Перевод текста:\n{response["responseData"]["translatedText"]}')
        else:
            await ctx.send(f'Неверно введен язык ввода, повторите попытку')
    else:
        await ctx.channel.send('У вас нет прав на использование этой команды')


@bot.command()
async def gdz(ctx):
    await command_gdz.c_gdz(ctx)


bot.run(settings['token'])
