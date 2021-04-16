async def help(msg):
    await msg.channel.send(f'Привет, {msg.author.mention}\n'
                           f'Я умею выполнять следующие команды:\n'
                           f'!help - выводит список всех доступных команд\n'
                           f'!games - выводит список возможных игр')