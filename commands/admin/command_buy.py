import random

from discord_bot.commands.admin.take_away_coins import take_away_coins
from discord_bot.config import cursor


async def buy(ctx, desired_role):
    roles = {
        "Админ": 50000,
        "Школьник": 10000,
        "Переводчик": 10000,
        "Премеум": 10000,
        "Премеум+": 20000,
        "Суперадмин": 500000
    }

    desired_role_named = desired_role.name
    user = ctx.message.author
    autor_roles = [role.name for role in ctx.message.author.roles]
    money = cursor.execute(f"""SELECT money FROM members WHERE id_of_user = {ctx.message.author.id}""").fetchall()[0]
    if desired_role_named in roles:
        if desired_role_named not in autor_roles:
            if money[0] >= roles[desired_role_named]:
                return_you_got_this_role = random.choice(
                    [f":ballot_box_with_check: {user.mention} приобрел роль {desired_role.mention}.",
                     f":ballot_box_with_check: {user.mention} купил роль {desired_role.mention}.",
                     f":ballot_box_with_check: {user.mention} получил роль {desired_role.mention}."]
                )
                take_away_coins(ctx.message.author, roles[desired_role_named])
                await user.add_roles(desired_role)
                await ctx.channel.send(return_you_got_this_role)
            else:
                await ctx.channel.send(f':x:Не хватает коинов:x:\n'
                                       f':ballot_box_with_check:Ваш баланс - {money[0]}')

        else:
            await ctx.channel.send(f'У вас уже есть эта роль <3')
    else:
        await ctx.channel.send(f':x: Такой роли не существует. '
                               f':x: Проверте правильность написания роли.')
