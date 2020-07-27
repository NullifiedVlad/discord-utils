from discord.ext import commands
import discord
import asyncio
import requests
import os


# 430897863887814658


def main():
    print('''
██╗   ██╗████████╗██╗██╗     ███████╗
██║   ██║╚══██╔══╝██║██║     ██╔════╝
██║   ██║   ██║   ██║██║     ███████╗
██║   ██║   ██║   ██║██║     ╚════██║
╚██████╔╝   ██║   ██║███████╗███████║
 ╚═════╝    ╚═╝   ╚═╝╚══════╝╚══════╝ by NullifiedVlad
                                     ''')
    with open('token.txt', 'r') as f:
        token = f.read()
    bot = commands.Bot(command_prefix='/')

    print('Working')

    @bot.event
    async def on_ready():
        await bot.change_presence(activity=discord.Game(f'discord utils'))

    @bot.event
    async def on_message(message):
        await bot.process_commands(message)

    @bot.command()
    async def spam(ctx, count: int, *, words):
        for i in range(count):
            await ctx.send(words)

    @bot.command()
    async def embed(ctx, *, text):
        await ctx.message.delete()
        await ctx.send(embed=discord.Embed(title=text, color=0xff00b7))

    @bot.command()
    async def cat(ctx):
        await ctx.message.delete()
        image = requests.get('https://thiscatdoesnotexist.com/')
        with open('cat.jpg', 'wb') as f:
            f.write(image.content)
        await ctx.send(file=discord.File('cat.jpg'))
        os.remove('cat.jpg')

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
            await msg.edit(embed=discord.Embed(title=f'**{label}**', description=bar, color=0x0095ff))
            await asyncio.sleep(1)
        await msg.edit(embed=discord.Embed(title=f'**{label}**', description='Completed!', color=0x00ff1a))

    @bot.command()
    async def ascii(ctx):
        await ctx.message.delete()
        faces = [
            '( ͡° ͜ʖ ͡°)',
            '( ͠° ͟ʖ ͡°)',
            '( ͡~ ͜ʖ ͡°)',
            '( ͡ʘ ͜ʖ ͡ʘ)',
            '( ͡o ͜ʖ ͡o)',
            '( ‾ʖ̫‾)',
            '( ಠ ͜ʖಠ)',
            '( ͡° ʖ̯ ͡°)',
            '(▀̿Ĺ̯▀̿ ̿)',
            '(ง ͠° ͟ل͜ ͡°)ง'
        ]
        msg = await ctx.send('( ͡° ͜ʖ ͡°)')
        for face in faces:
            await msg.edit(content=face)
            await asyncio.sleep(1)
        await ctx.message.delete()

    @bot.command()
    async def rev(ctx, *, text):
        await ctx.message.delete()

        await ctx.send(text[::-1])

    @bot.command(aliases=['шуе', 'ШУЕ'])
    async def hue(ctx):
        await ctx.message.delete()
        words = [
            'шУе сила',
            'шуЕ сила',
            'шуе Сила',
            'шуе сИла',
            'шуе сиЛа',
            'шуе силА',
            'шуе сила',
        ]
        msg = await ctx.send('Шуе')
        for i in words:
            await msg.edit(content=i)
            await asyncio.sleep(1)

    @bot.command()
    async def typing(ctx, *, text):
        await ctx.message.delete()
        msg = ''
        smsg = await ctx.send('x')
        for word in text:
            msg += word
            await smsg.edit(content=msg)
            await asyncio.sleep(1)

    bot.run(token, bot=False)


if __name__ == '__main__':
    main()
