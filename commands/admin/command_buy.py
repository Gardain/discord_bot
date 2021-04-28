from discord_bot.config import cursor


async def buy(ctx, desired_role):
    roles = {
        "Админ": 50000,
        "Школьник": 10000,
        "Переводчик": 10000,
        "Премеум": 10000,
        "Премеум+": 20000,
        "Суперадмин": 10000000
    }

    user = ctx.message.author
    autor_roles = [role.name for role in ctx.message.author.roles]
    money = cursor.execute(f"""SELECT money FROM members WHERE id_of_user = {ctx.message.author.id}""").fetchall()[0]
    if desired_role.name in roles:
        if desired_role.name not in autor_roles:
            if money[0] >= roles[desired_role.name]:
                await user.add_roles(desired_role)
            else:
                await ctx.channel.send(f':x:Не хватает коинов:x:\n'
                                       f'Ваш баланс - {money[0]}')

        else:
            await ctx.channel.send(f'У вас уже есть эта роль <3')
    else:
        await ctx.channel.send(f'Такой роли не существует. '
                               f'Проверте правильность написания роли.')
