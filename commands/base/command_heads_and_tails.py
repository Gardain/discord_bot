import random

from discord_bot.commands.admin.add_coins import add_coins
from discord_bot.commands.admin.take_away_coins import take_away_coins
from discord_bot.config import bot, cursor


@bot.command()
async def heads_and_tails(ctx, user_word, bet):
    num = random.choice(["орёл", "решка"])
    if num == "орёл":
        if user_word.lower() == 'орёл':
            add_coins(ctx.message.author, int(bet) * 2)
            await ctx.send("Орёл! Вы выиграли!")
            money = cursor.execute(
                f"""SELECT money FROM members WHERE id_of_user = {ctx.message.author.id}""").fetchall()[0]
            await ctx.channel.send(f'Ваш баланс - {money[0]}')
        else:
            take_away_coins(ctx.message.author, int(bet))
            await ctx.send("Орёл! Вы проиграли!")
            money = cursor.execute(
                f"""SELECT money FROM members WHERE id_of_user = {ctx.message.author.id}""").fetchall()[0]
            await ctx.channel.send(f'Ваш баланс - {money[0]}')
    else:
        if user_word.lower() == 'решка':
            add_coins(ctx.message.author, int(bet) * 2)
            await ctx.send("Решка! Вы выиграли!")
            money = cursor.execute(
                f"""SELECT money FROM members WHERE id_of_user = {ctx.message.author.id}""").fetchall()[0]
            await ctx.channel.send(f'Ваш баланс - {money[0]}')
        else:
            take_away_coins(ctx.message.author, int(bet))
            await ctx.send("Решка! Вы проиграли!")
            money = cursor.execute(
                f"""SELECT money FROM members WHERE id_of_user = {ctx.message.author.id}""").fetchall()[0]
            await ctx.channel.send(f'Ваш баланс - {money[0]}')