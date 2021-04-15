import discord
from discord.ext import commands

settings = {
    'token': 'ODMyMzI3NjIxMTM1NDMzNzU4.YHiLgA.PpFKpb-b2SjWMDl4vai_MEW65kQ',
    'bot': 'bot-231412341234',
    'id': 832327621135433758,
    'prefix': '$'
}

bot = commands.Bot(
    command_prefix=settings['prefix'])  # Так как мы указали префикс в settings, обращаемся к словарю с ключом prefix.


@bot.command()  # Не передаём аргумент pass_context, так как он был нужен в старых версиях.
async def hello(ctx):  # Создаём функцию и передаём аргумент ctx.
    author = ctx.message.author  # Объявляем переменную author и записываем туда информацию об авторе.

    await ctx.send(
        f'Hello, {author.mention}!')  # Выводим сообщение с упоминанием автора, обращаясь к переменной author.


bot.run(settings['token'])  # Обращаемся к словарю settings с ключом token, для получения токена
