from discord_bot.config import cursor


async def take_money():
    cursor.execute(f"""UPDATE members SET money = %s WHERE id = %s""")