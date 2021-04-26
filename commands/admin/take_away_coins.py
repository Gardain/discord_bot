from discord_bot.config import cursor, sqlite_connection


def take_away_coins(msg_user, count_lose):  # функция для добавления коинов
    money = cursor.execute(f"""SELECT money FROM members WHERE id_of_user = {msg_user.id}""").fetchall()
    cursor.execute(f"""UPDATE members SET money = {int(money[0][0]) - count_lose} WHERE id_of_user = {msg_user.id}""")
    sqlite_connection.commit()
