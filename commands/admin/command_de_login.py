from dicord_bot.config import cursor, sqlite_connection


async def de_login(ctx):  # "Регистрация" на канале
    if cursor.execute("""SELECT id_of_user FROM members""").fetchall() and \
            ctx.message.author.id in cursor.execute("""SELECT id_of_user FROM members""").fetchall()[0]:
        cursor.execute(f"""DELETE from members where id_of_user = {ctx.message.author.id}""")
        sqlite_connection.commit()
        await ctx.channel.send('Удалление аккаунта завершено...')
    else:
        await ctx.channel.send('Нельзя удалить то, чего нет!!!')
