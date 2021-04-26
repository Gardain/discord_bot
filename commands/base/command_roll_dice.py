from random import choice

from config import cursor, dashes, array_of_dashes


async def roll_dice(ctx):
    money = cursor.execute(f"""SELECT money FROM members WHERE id_of_user = {ctx.message.author.id}""").fetchall()[0]
    message = ctx.message.content.split()

    if (message[-2].lower() == 'больше' or message[-2].lower() == 'меньше') and \
            int(message[-1]) <= money[0]:
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
                await ctx.channel.send(f'Вы выйграли, выпало число {count} ({dishes[0]} + {dishes[1]})')
            else:
                await ctx.channel.send(f'Вы проиграли, выпало число {count} ({dishes[0]} + {dishes[1]})')

        elif count <= 6:
            if message[-2].lower() == 'меньше':
                await ctx.channel.send(f'Вы выйграли, выпало число {count} ({dishes[0]} + {dishes[1]})')
            else:
                await ctx.channel.send(f'Вы проиграли, выпало число {count} ({dishes[0]} + {dishes[1]})')

    else:
        await ctx.channel.send('Что-то введено не верно, повторите попытку')
