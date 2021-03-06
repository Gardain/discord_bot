import discord

from commands.admin import command_buy
from commands.admin import command_de_login, command_help, command_info, command_shop_help, command_rules
from commands.admin.translate_api import translate_api
from commands.base import command_login, command_roll_dice, command_gdz
from commands.base import command_number_choise, command_heads_and_tails
from config import bot, settings, cursor


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
    await msg.channel.send(f'{msg.message.author.mention}. Навигация по играм:\n\n'
                           f':game_die: !roll_dice - игра в кости (Пример: !roll_dice [больше или меньше'
                           f' половины суммы костей(бросается две кости)] [ставка]; !roll_dice меньше 100\n\n'

                           f':tada: !choose_number - Угадай число от 1 до 5 и сорви Джекпот!!!'
                           f' (Пример: !choose_number [число от 1 до 5] [ставка];'
                           f' !choose_number 5 1000)\n\n'

                           f':coin: !heads_and_tails - игра в монетку. (Пример: !heads_and_tails [орел или решка]'
                           f' [ставка]; !heads_and_tails орел 1000')


@bot.command()  # игра в кости
async def roll_dice(ctx):
    await command_roll_dice.roll_dice(ctx)


@bot.command()  # игра в выбор номера
async def choose_number(ctx, number=None, bet=None):
    if number and bet:
        await command_number_choise.choose_number(ctx, number, bet)
    else:
        await ctx.send(f"Данные введены неверно.\n "
                       f"Пример ввода: !choose_number [число от 1 до 5] [ставка]")


@bot.command()  # игра в "Орел и Решку"
async def heads_and_tails(ctx, user_word=None, bet=None):
    money = cursor.execute(f"""SELECT money FROM members WHERE id_of_user = {ctx.message.author.id}""").fetchall()[0]
    if user_word and bet:
        if int(bet) <= money[0]:
            await command_heads_and_tails.heads_and_tails(ctx, user_word, bet)
        else:
            await ctx.send(f"Не достаточно коинов.\n"
                           f"Ваш баланс - {money[0]}")
    else:
        await ctx.send(f"Данные введены неверно.\n "
                       f"Пример ввода: !heads_and_tails [орел или решка] [ставка]")


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
