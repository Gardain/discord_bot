from config import cursor


async def info(ctx, member):
    if member.id in cursor.execute("""SELECT id_of_user FROM members""").fetchall()[0] or :
        money = cursor.execute(f"""SELECT money FROM members WHERE id_of_user = {ctx.message.author.id}""").fetchall()[0]
        await ctx.channel.send(f'Данные пользователя {member.mention}\n'
                                   f'id - {member.id}\n'
                                   f'name - {member.name}\n'
                                   f'coins - {money[0]}')
    else:
        await ctx.channel.send('Невозможно вывести информацию о пользователе')