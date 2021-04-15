from discord.ext.commands import Bot

TOKEN = "ODMyMjg3MjIwNTYzNTc0ODQy.YHhl4A.CWinKRReJe8a-sZgR_JNUFRxpgg"

client = Bot(description="Test bot", command_prefix="!", pm_help=False)


@client.event
async def on_message(msg):
    if msg.author != client.user:
        if msg.content.lower() == 'привет':
            await msg.channel.send(f'Привет, {msg.author.mention}')


async def on_message(msg):
    client.run(TOKEN)
