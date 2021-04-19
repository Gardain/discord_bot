from commands.config import cursor, sqlite_connection


def add_member(msg_user):  # функция для добавления нового юзера в базу данных
    cursor.execute(f"""INSERT INTO members(id, name, money, role) VALUES({msg_user.id},
'{msg_user.name}', {1000}, 'Простолюдин')""")
    sqlite_connection.commit()
