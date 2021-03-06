import discord

from discord_bot.commands.admin.add_member import add_member
from discord_bot.config import cursor


async def login(ctx):  # "Регистрация" на канале
    if not cursor.execute("""SELECT id_of_user FROM members""").fetchall() or ctx.message.author.id not in \
            cursor.execute("""SELECT id_of_user FROM members""").fetchall()[0]:
        add_member(ctx.message.author)
        await ctx.channel.send('Регистрация завершена')
    else:
        await ctx.channel.send('Вы уже зарегестрированы на канале')
