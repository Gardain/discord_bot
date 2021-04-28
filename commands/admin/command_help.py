async def help(msg):
    await msg.channel.send(f'Привет, {msg.author.mention}\n'
                           f'Я умею выполнять следующие команды:\n'
                           f':helmet_with_cross: !help - выводит список всех доступных команд :helmet_with_cross:\n\n'
                           f':game_die: !games - выводит список возможных игр :game_die:\n\n'
                           f':bookmark_tabs: !info - получить информацию о пользователе :bookmark_tabs:\n\n'
                           f':red_circle: !shop_help  - Выводит команды доступные для покупки :red_circle:\n\n'
                           f':green_book: !gdz - позволяет получить ссылку на решебник '
                           f' введеного пользователем учебника(доступен только для обладателей'
                           f' роли :boom:Школьник):green_book:\n\n'
                           
                           f':x:!ban - забанить кента(доступен только для обладателей роли'
                           f' :boom:Суперадмин) :x:\n\n'
                           f':inbox_tray: !login - зарегистрироваться на сервере :inbox_tray:\n\n'
                           f':outbox_tray: !de_login - удалить свой аккаунт с сервера. :outbox_tray:')
