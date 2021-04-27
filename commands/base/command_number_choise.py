import random

from discord_bot.commands.admin.add_coins import add_coins
from discord_bot.commands.admin.take_away_coins import take_away_coins
from discord_bot.config import bot, cursor


async def choose_number(ctx, number, bet):
    if int(bet) < 100:
        await ctx.send("Минимальная ставка: 100 коинов")
    else:
        num = random.randint(1, 5)
        if int(number) == num:
            money = cursor.execute(
                f"""SELECT money FROM members WHERE id_of_user = {ctx.message.author.id}""").fetchall()[0]
            add_coins(ctx.message.author, int(bet) * 5)
            await ctx.send(f"Выпало число {num}, вы выиграли!!!!!!!!\n"
                           f"Ваш баланс - {money[0]}")
        else:
            take_away_coins(ctx.message.author, int(bet))
            money = cursor.execute(
                f"""SELECT money FROM members WHERE id_of_user = {ctx.message.author.id}""").fetchall()[0]
            await ctx.send(f"Выпало число {num}, вы проиграли(\n"
                           f"Ваш баланс - {money[0]}")
