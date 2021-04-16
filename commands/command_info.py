from commands.config import cursor


async def info(ctx):
    if not cursor.execute("""SELECT id FROM members""").fetchall() or ctx.message.author.id not in \
            cursor.execute("""SELECT id FROM members""").fetchall()[0]:
        # если id пользователя нет в базе, то бот просит залогиниться
        await ctx.channel.send('Вы забыли зарегестрироваться на канале\n'
                               'Введите !login, что бы пройти регестрацию')
    else:
        result = cursor.execute("""SELECT * FROM members""").fetchall()
        for i in result:
            if i[0] == ctx.message.author.id:
                await ctx.channel.send(f'Данные пользователя {ctx.message.author.mention}\n'
                                       f'id - {i[0]}\n'
                                       f'name - {i[1]}\n'
                                       f'coins - {i[2]}')
