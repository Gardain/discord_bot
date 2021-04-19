from commands.config import cursor, sqlite_connection


def add_coins(msg_user):  # функция для добавления нового юзера в базу данных
    cursor.execute(f"""INSERT INTO members(id, name, money) VALUES({msg_user.id}, '{msg_user.name}', {1000})""")
    sqlite_connection.commit()
