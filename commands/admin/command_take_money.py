from discord.utils import get

from config import cursor


async def take_money(ctx, member):
    cursor.execute(f"""UPDATE members SET money = %s WHERE id = %s""")