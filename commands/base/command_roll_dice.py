from random import choice

from commands.admin.add_coins import add_coins
from commands.admin.take_away_coins import take_away_coins
from config import cursor, array_of_dashes, dashes


async def roll_dice(ctx):
    money = cursor.execute(f"""SELECT money FROM members WHERE id_of_user = {ctx.message.author.id}""").fetchall()[0]
    message = ctx.message.content.split()
    bet = int(message[-1])
    more_less = message[-2].lower()
    if int(bet) <= money[0]:
        if (more_less == 'больше' or more_less == 'меньше') and bet <= money[0]:
            res = [choice(array_of_dashes) for _ in range(2)]
            count = 0
            dishes = []

            for i in res:
                for key, value in dashes.items():
                    if key == str(ord(i)):
                        dishes.append(i)
                        count += value

            if count >= 6:
                if message[-2].lower() == 'больше':
                    add_coins(ctx.message.author, int(bet))
                    money = cursor.execute(
                        f"""SELECT money FROM members WHERE id_of_user = {ctx.message.author.id}""").fetchall()[0]
                    await ctx.channel.send(f"{ctx.message.author.mention}\n"
                                           f'Вы выйграли, выпало число {count} ({dishes[0]} + {dishes[1]})\n'
                                           f'Ваш баланс - {money[0]}')
                else:
                    take_away_coins(ctx.message.author, int(bet))
                    money = cursor.execute(
                        f"""SELECT money FROM members WHERE id_of_user = {ctx.message.author.id}""").fetchall()[0]
                    await ctx.channel.send(f'f"{ctx.message.author.mention}\n"'
                                           f'Вы проиграли, выпало число {count} ({dishes[0]} + {dishes[1]})\n'
                                           f'Ваш баланс - {money[0]}')

            elif count <= 6:
                if message[-2].lower() == 'меньше':
                    add_coins(ctx.message.author, int(bet))
                    money = cursor.execute(
                        f"""SELECT money FROM members WHERE id_of_user = {ctx.message.author.id}""").fetchall()[0]
                    await ctx.channel.send(f'f"{ctx.message.author.mention}\n"'
                                           f'Вы выйграли, выпало число {count} ({dishes[0]} + {dishes[1]})\n'
                                           f'Ваш баланс - {money[0]}')
                else:
                    take_away_coins(ctx.message.author, int(bet))
                    money = cursor.execute(
                        f"""SELECT money FROM members WHERE id_of_user = {ctx.message.author.id}""").fetchall()[0]
                    await ctx.channel.send(f'f"{ctx.message.author.mention}\n"'
                                           f'Вы проиграли, выпало число {count} ({dishes[0]} + {dishes[1]})\n'
                                           f'Ваш баланс - {money[0]}')

        else:
            await ctx.channel.send('Что-то введено не верно, повторите попытку')
    else:
        await ctx.send(f"Недостаточно коинов.\n"
                       f"Ваш баланс - {money[0]}")
