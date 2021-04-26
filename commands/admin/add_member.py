from discrd_bot.config import cursor, sqlite_connection


def add_member(msg_user):  # функция для добавления нового юзера в базу данных
    cursor.execute(f"""INSERT INTO members(id_of_user, money) VALUES({msg_user.id}, {1000})""")
    sqlite_connection.commit()
