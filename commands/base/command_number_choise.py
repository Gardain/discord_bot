import random

from commands.admin.add_coins import add_coins
from commands.admin.take_away_coins import take_away_coins
from config import cursor


async def choose_number(ctx, number, bet):
    if int(bet) < 100:
        await ctx.send("Минимальная ставка: 100 коинов")
    else:
        money = cursor.execute(
            f"""SELECT money FROM members WHERE id_of_user = {ctx.message.author.id}""").fetchall()[0]
        if int(bet) <= money[0]:
            num = random.randint(1, 5)
            if int(number) == num:
                add_coins(ctx.message.author, int(bet) * 5)
                money = cursor.execute(
                    f"""SELECT money FROM members WHERE id_of_user = {ctx.message.author.id}""").fetchall()[0]
                await ctx.send(f"{ctx.message.author.mention}\n"
                               f"Выпало число {num}, вы выиграли!!!!!!!!\n"
                               f"Ваш баланс - {money[0]}")
            else:
                take_away_coins(ctx.message.author, int(bet))
                money = cursor.execute(
                    f"""SELECT money FROM members WHERE id_of_user = {ctx.message.author.id}""").fetchall()[0]
                await ctx.send(f"{ctx.message.author.mention}\n"
                               f"Выпало число {num}, вы проиграли(\n"
                               f"Ваш баланс - {money[0]}")
        else:
            await ctx.send(f"{ctx.message.author.mention}\n"
                           f"Недостаточно коинов.\n"
                           f"Ваш баланс - {money[0]}")
