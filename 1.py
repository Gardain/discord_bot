from discord.ext import commands
from config import settings

bot = commands.Bot(settings['prefix'])

bot.remove_command('help')


@bot.listen('on_message')
async def welcome(msg):
    if str(msg.content).lower() == 'привет':
        if msg.author.name != 'SO_EZ_bot':
            await msg.channel.send(f'Привет, {msg.author.mention}')
            await bot.process_commands(msg)


@bot.command()
async def help(ctx):
    await ctx.send(f'Здравствуйте, {ctx.author.mention}\n'
                   f'Я могу выполнять такие команды:\n'
                   f'!help - выводит список всех команд')


bot.run(settings['token'])
