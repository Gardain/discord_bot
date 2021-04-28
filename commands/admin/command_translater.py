async def translater(ctx, role, member):
    roles = []
    for i in ctx.message.author.roles:
        roles.append(i.name)
    member = member or ctx.message.author
    if 'Переводчик' not in roles:
        await member.add_roles(role)
    else:
        await ctx.channel.send('Вы уже приобрели данную роль <з')
