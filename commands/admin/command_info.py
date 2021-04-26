from discord.utils import get


async def info(ctx, member):
    if get(ctx.message.author.roles, name="Администратор"):
        await ctx.channel.send(f'Данные пользователя {member.mention}\n'
                               f'id - {member.id}\n'
                               f'name - {member.name}\n'
                               f'coins - 1000') #  aaaaaaaaaaaaaaa
    else:
        await ctx.channel.send(f'У вас нет прав для использования этой команды :(')