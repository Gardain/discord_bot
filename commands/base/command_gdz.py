import discord
from gdz import GDZ

from discord_bot.config import bot


async def c_gdz(ctx):
    gdz = GDZ()

    await ctx.channel.send('Введите свой класс: (номер класса)')
    correct_books = []
    clas = await bot.wait_for('message', check=lambda message: message.author == ctx.author)
    clas = clas.content
    for i in gdz.books:
        if int(clas) in i.classes:
            correct_books.append(i)

    await ctx.channel.send('Поиск: (предмет и автор)')
    search = await bot.wait_for('message', check=lambda message: message.author == ctx.author)
    search = search.content.lower().split(' ')

    books = []
    API_ENDPOINT = "https://gdz.ru"
    for book in correct_books:
        search_keywords = book.search_keywords.split()
        count = 0

        for i in range(len(search)):
            if search[i] in search_keywords:
                count += 1
            if count == len(search):
                books.append([book.title, book.url])

    await ctx.channel.send('Нам удалось найти следующие учебники:')
    count = 1
    emb = discord.Embed(title='Результаты поиска', colour=discord.Color.purple())
    for i in books:
        emb.add_field(name=f'{i[0]}', value=f'{count}')
        count += 1
    await ctx.channel.send(embed=emb)

    await ctx.channel.send('\nВведите номер учебника')
    number_of_book = await bot.wait_for('message', check=lambda message: message.author == ctx.author)
    number_of_book = int(number_of_book.content)
    await ctx.channel.send(API_ENDPOINT + books[number_of_book - 1][1])
