import discord

from commands.admin.add_member import add_member
from config import cursor


async def login(ctx):  # "Регистрация" на канале
    if not cursor.execute("""SELECT id_of_user FROM members""").fetchall() or ctx.message.author.id not in \
            cursor.execute("""SELECT id_of_user FROM members""").fetchall()[0]:
        add_member(ctx.message.author)
        member = ctx.message.author
        role = discord.utils.get(member.guild.roles, name="Простолюдин")
        await member.add_roles(role)  # при регистрации даётся самая низшая роль
        await ctx.channel.send('Регистрация завершена')
    else:
        await ctx.channel.send('Вы уже зарегестрированы на канале')
