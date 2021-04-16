from commands.config import cursor, sqlite_connection


async def de_login(ctx):  # "Регистрация" на канале
    if cursor.execute("""SELECT id FROM members""").fetchall() and \
            ctx.message.author.id in cursor.execute("""SELECT id FROM members""").fetchall()[0]:
        cursor.execute(f"""DELETE from members where id = {ctx.message.author.id}""")
        sqlite_connection.commit()
        await ctx.channel.send('Удалление аккаунта завершено...')
    else:
        await ctx.channel.send('Нельзя удалить то, чего нет!!!')
