
from gdz import GDZ

from config import bot


async def c_gdz(ctx):
    gdz = GDZ()

    await ctx.channel.send('введите свой класс:')
    correct_books = []
    clas = await bot.wait_for('message', check=lambda message: message.author == ctx.author)
    clas = clas.content
    for i in gdz.books:
        if int(clas) in i.classes:
            correct_books.append(i)

    await ctx.channel.send('Поиск:')
    search = await bot.wait_for('message', check=lambda message: message.author == ctx.author)
    search = search.content.split(' ')

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
    stroka = ''
    for i in books:
        stroka += f'{count}. {i[0]}\n'
        count += 1
    await ctx.channel.send(stroka)

    await ctx.channel.send('\nВведите номер учебника')
    number_of_book = await bot.wait_for('message', check=lambda message: message.author == ctx.author)
    number_of_book = int(number_of_book.content)
    print(books[number_of_book - 1][0])
    await ctx.channel.send(API_ENDPOINT + books[number_of_book - 1][0])
