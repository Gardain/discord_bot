import discord


async def pay(ctx):
    emb = discord.Embed(title='Навигация по командам', colour=discord.Color.purple())
    emb.add_field(name='!ban', value='ограничение доступа к серверу')
    emb.add_field(name='!ban', value='ограничение доступа к серверу')
    emb.add_field(name='!ban', value='ограничение доступа к серверу')
    emb.add_field(name='!ban', value='ограничение доступа к серверу')
    emb.add_field(name='!ban', value='ограничение доступа к серверу')
    await ctx.channel.send(embed=emb)
