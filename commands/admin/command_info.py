from config import cursor


async def info(ctx, member):
    money = cursor.execute(f"""SELECT money FROM members WHERE id_of_user = {ctx.message.author.id}""").fetchall()[0]
    await ctx.channel.send(f'Данные пользователя {member.mention}\n'
                               f'id - {member.id}\n'
                               f'name - {member.name}\n'
                               f'coins - {money[0]}')