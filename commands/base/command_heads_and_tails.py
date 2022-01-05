import random

from discord_bot.commands.admin.add_coins import add_coins
from discord_bot.commands.admin.take_away_coins import take_away_coins
from discord_bot.config import cursor


async def heads_and_tails(ctx, user_word, bet):
    money = cursor.execute(
        f"""SELECT money FROM members WHERE id_of_user = {ctx.message.author.id}""").fetchall()[0]
    if int(bet) <= money[0]:
        num = random.choice(["орёл", "решка"])
        if user_word.lower() == "орёл" or user_word.lower() == "решка":
            if num == "орёл":
                if user_word.lower() == 'орёл':
                    add_coins(ctx.message.author, int(bet))
                    money = cursor.execute(
                        f"""SELECT money FROM members WHERE id_of_user = {ctx.message.author.id}""").fetchall()[0]
                    await ctx.send(f"{ctx.message.author.mention}\n"
                                   f"Орёл! Вы выиграли!\n"
                                   f"Ваш баланс - {money[0]}")
                else:
                    take_away_coins(ctx.message.author, int(bet))
                    money = cursor.execute(
                        f"""SELECT money FROM members WHERE id_of_user = {ctx.message.author.id}""").fetchall()[0]
                    await ctx.channel.send(f"{ctx.message.author.mention}\n"
                                           f"Орел! Вы проиграли!\n"
                                           f"Ваш баланс - {money[0]}")
            else:
                if user_word.lower() == 'решка':
                    add_coins(ctx.message.author, int(bet))
                    money = cursor.execute(
                        f"""SELECT money FROM members WHERE id_of_user = {ctx.message.author.id}""").fetchall()[0]
                    await ctx.channel.send(f"{ctx.message.author.mention}\n"
                                           f"Решка! Вы выиграли!\n"
                                           f"Ваш баланс - {money[0]}")
                else:
                    take_away_coins(ctx.message.author, int(bet))
                    money = cursor.execute(
                        f"""SELECT money FROM members WHERE id_of_user = {ctx.message.author.id}""").fetchall()[0]
                    await ctx.channel.send(f"{ctx.message.author.mention}\n"
                                           f"Решка! Вы проиграли!\n"
                                           f"Ваш баланс - {money[0]}")
        else:
            await ctx.send(f"Данные введены неверно.\n "
                           f"Пример ввода: !heads_and_tails [орел или решка] [ставка]")
    else:
        await ctx.channel.send(f" {ctx.message.author.mention} \n"
                               f"Недостаточно коинов.\n"
                               f"Ваш баланс - {money[0]}")
