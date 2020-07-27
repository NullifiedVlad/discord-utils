from discord.ext import commands
import discord
import asyncio

answer = input('Do you want create cfg file? (y/n)\n')

if answer == 'y':

    token = input('Enter your token: ')
    with open('config.py', 'w') as f:
        f.write(f'token = "{token}"')
else:
    print('Starting the discord utils')

from config import token
bot = commands.Bot(command_prefix='/', self_bot=True)
print('Ready!')


@bot.event
async def on_message(message):
    await bot.process_commands(message)


@bot.command()
async def spam(ctx, count, *, words):
    await ctx.message.delete()
    for i in range(int(count)+1):
        await ctx.send(words)


@bot.command()
async def embed(ctx, *, text):
    await ctx.message.delete()
    await ctx.send(embed=discord.Embed(title=text, color=0xff00b7))


@bot.command()
async def loading(ctx, *, label):
    await ctx.message.delete()
    bars = [
        '[----------]0%',
        '[#---------]10%',
        '[##--------]20%',
        '[###-------]30%',
        '[####------]40%',
        '[#####-----]50%',
        '[######----]60%',
        '[#######---]70%',
        '[########--]80%',
        '[#########-]90%',
        '[##########]100%']
    msg = await ctx.send(embed=discord.Embed(title=f'**{label}**', description='None', color=0x0095ff))
    for bar in bars:
        print(bar)
        await msg.edit(embed=discord.Embed(title=f'**{label}**', description=bar, color=0x0095ff))
        await asyncio.sleep(1)
    await msg.edit(embed=discord.Embed(title=f'**{label}**', description='Completed!', color=0x00ff1a))

bot.run(token, bot=False)
