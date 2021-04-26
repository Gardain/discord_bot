from discord_bot.config import cursor, sqlite_connection


def add_coins(msg_user, count_win):  # функция для добавления коинов
    money = cursor.execute(f"""SELECT money FROM members WHERE id_of_user = {msg_user.id}""").fetchall()
    print(money)
    cursor.execute(f"""UPDATE members SET money = {int(money[0][0]) + count_win} WHERE id_of_user = {msg_user.id}""")
    sqlite_connection.commit()
