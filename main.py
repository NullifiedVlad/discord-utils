import discord
from discord.ext import commands
import asyncio
import requests
import os
from PIL import Image, ImageDraw, ImageFont
import SiteParser


class SelfBot:
    def __init__(self, **options):
        super().__init__(**options)
        self.bot = commands.Bot(command_prefix='discord_', self_bot=True)
        self.bot.remove_command('help')
        with open('token.txt', 'r') as token:
            self.token = token.read()

    def run(self):

        print('Запустился')

        @self.bot.event
        async def on_ready():
            await self.bot.change_presence(activity=discord.Game(f'discord utils'))

        @self.bot.event
        async def on_message(message):
            await self.bot.process_commands(message)

        @self.bot.command(aliases=['help'])
        async def help_message(ctx):
            hembed = discord.Embed(title='**ФИЧИ**', description='Discord utils', color=0x0095ff, )
            # заголовки
            hembed.add_field(name='**discord_help**', value='Это сообщение.', inline=False)
            hembed.add_field(name='**discord_cat**', value='Отправить кота.', inline=False)
            hembed.add_field(name='**discord_embed**', value='Отправить ембиент.', inline=False)
            hembed.add_field(name='**discord_spam**', value='Поспамить.', inline=False)
            hembed.add_field(name='**discord_emoji**', value='Анимированные эмодзи', inline=False)
            hembed.add_field(name='**discord_rev**', value='Перевернуть сообщение.', inline=False)
            hembed.add_field(name='**discord_ascii**', value='Анимированные залго смайлы.', inline=True)
            hembed.add_field(name='**discord_nigga**', value='Сделать мем про ниггу.', inline=False)
            hembed.add_field(name='**discord_loading**', value='Создать загрузку.', inline=False)
            hembed.add_field(name='**discord_why**', value='Нахуя а главное зачем.', inline=False)
            hembed.add_field(name='**discord_hearts**', value='Радужное сердце.', inline=False)
            hembed.add_field(name='**discord_think**', value='Гигант мысли, отец...', inline=False)
            hembed.add_field(name='**discord_mae<hi,owo,kiss,scared>**', value='Стикеры про Мэй', inline=False)
            hembed.set_thumbnail(url='https://cdn4.iconfinder.com/data/icons/logos-and-brands/512'
                                     '/91_Discord_logo_logos-512.png')
            hembed.set_footer(text=f'Created by nullifiedVlad',
                              icon_url='https://i.imgur.com/WK520CI.jpg')
            hembed.set_author(name=self.bot.user.name, icon_url=ctx.author.avatar_url)
            await ctx.message.edit(embed=hembed, content=None)

        @self.bot.command()
        async def spam(ctx, count: int, *, words: str):
            for i in range(count):
                await ctx.send(words)

        @self.bot.command()
        async def embed(ctx, *, text: str):
            await ctx.message.edit(embed=discord.Embed(title=text, color=0xff00b7), content=None)

        @self.bot.command()
        async def emoji(ctx):
            faces = (
                ':grinning:',
                ':heart_eyes:',
                ':rage:',
                ':hot_face:',
                ':cold_face:',
                ':scream:',
                ':smiling_imp:',
                ':sunglasses:',
                ':poop:',
                ':star_struck:',
                ':partying_face:',
                ':exploding_head:',
                ':kissing_heart:',
                ':clown:',
                ':alien:',
            )
            for face in faces:
                await ctx.message.edit(content=face)
                await asyncio.sleep(0.5)
            await ctx.message.delete()

        @self.bot.command()
        async def cat(ctx):
            await ctx.message.delete()
            image = requests.get('https://thiscatdoesnotexist.com/')
            with open('cat.jpg', 'wb') as f:
                f.write(image.content)
            await ctx.send(file=discord.File('cat.jpg'))
            os.remove('cat.jpg')

        @self.bot.command()
        async def loading(ctx, *, label: str):
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

        @self.bot.command(aliases=['аски', 'эмодзи', 'ascii'])
        async def zalgo(ctx):
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
                '(ง ͠° ͟ل͜ ͡°)ง',
                '♥‿♥',
                '(⩾﹏⩽)',
                '(ಠ ʖ̯ ಠ)',
                '( ˇ෴ˇ )',
                '(͡ಠ ʖ̯ ͡ಠ)',
                '¯\_(ツ)_/¯',
                'ᕙ(⇀‸↼‶)ᕗ',
                'ᕦ(ò_óˇ)ᕤ',
                '(づ￣ ³￣)づ',
                '(งツ)ว',
                'ヾ(-__- )ゞ',
                '♪♪ ヽ(ˇ∀ˇ )ゞ',
                '(っ▀¯▀)つ',
                '~(^-^)~',
                '\(ᵔᵕᵔ)/',
                '[¬º-°]¬',
                'ฅ^•ﻌ•^ฅ',
                '(╯°□°）╯︵ ┻━┻'
            ]
            for face in faces:
                await ctx.message.edit(content=face)
                await asyncio.sleep(1)
            await ctx.message.delete()

        @self.bot.command()
        async def rev(ctx, *, text: str):
            await ctx.message.edit(content=text[::-1])

        @self.bot.command(aliases=['цитата'])
        async def quote(ctx):
            await ctx.message.delete()
            site = SiteParser.Quotes()
            await ctx.send(f'`{site.getQuoteMessage()}`')

        @self.bot.command()
        async def nigga(ctx, *, text: str):
            """
                Костыльная хрень , ктоторая нуждается
                в переделке.
                """
            await ctx.message.delete()
            if int(len(text)) < 40:
                if 8 <= int(len(text)) <= 10:
                    large = 65
                elif int(len(text)) >= 12:
                    large = 50
                else:
                    large = 90

                if int(len(text)) >= 4:
                    to_sum = 8
                else:
                    to_sum = 3

                image = Image.open('media/nigga/nigga.jpg')
                draw = ImageDraw.Draw(image)
                font_name = 'media/fonts/arialbd.ttf'
                font = ImageFont.truetype(font_name, large, encoding="unic")
                draw.text((200 - int(len(text)) * to_sum, 600 - large), str(text), fill=(0, 0, 0), font=font)
                image.save('nigga-out.jpg')
                await ctx.send(file=discord.File('nigga-out.jpg'))
                os.remove('nigga-out.jpg')
            else:
                await ctx.send('To many symbols')

        @self.bot.command()
        async def hearts(ctx):
            hearts1 = [
                ':heart:',
                ':orange_heart:',
                ':green_heart:',
                ':blue_heart:',
                ':purple_heart:',
                ':black_heart:',
                ':white_heart:'
            ]
            for heart in hearts1:
                await ctx.message.edit(content=heart)
                await asyncio.sleep(0.5)
            await ctx.message.delete()

        @self.bot.command(aliases=['зачем', 'нахуя'])
        async def why(ctx):
            # скачиваем фотографию
            with open('image.jpg', 'wb') as f:
                f.write(requests.get(str(ctx.message.attachments[0].url)).content)
            # импортируем фотки
            image = Image.open('media\\think\\why.jpg')  # прикол
            image_on_paste = Image.open('image.jpg')  # кастомная фотка

            # изменяем размер и вставляем фотографию
            image_on_paste = image_on_paste.resize((614, 336), Image.ANTIALIAS)
            image.paste(image_on_paste, (72, 42))

            image.save(f'{str(ctx.author.id)}.png')

            await ctx.message.delete()
            await ctx.send(file=discord.File(f'{str(ctx.author.id)}.png'))

            os.remove(f'{str(ctx.author.id)}.png')
            os.remove('image.jpg')

        @self.bot.command(aliases=['мысль', 'гигант'])
        async def think(ctx):
            url = ctx.message.attachments[0].url
            r = requests.get(str(url))

            with open('image.jpg', 'wb') as f:
                f.write(r.content)

            image = Image.open('media/think/гигант_мысли.jpg')
            image_on_paste = Image.open('image.jpg')

            image_on_paste = image_on_paste.resize((500, 400), Image.ANTIALIAS)
            image.paste(image_on_paste, (130, 13))

            image.save(f'{str(ctx.author.id)}.png')

            await ctx.message.delete()
            await ctx.send(file=discord.File(f'{str(ctx.author.id)}.png'))

            os.remove(f'{str(ctx.author.id)}.png')
            os.remove('image.jpg')

        @self.bot.command()
        async def mae_hi(ctx):
            await ctx.message.delete()
            await ctx.send(file=discord.File('media/Mae/hi.png'))

        @self.bot.command()
        async def mae_kiss(ctx):
            await ctx.message.delete()
            await ctx.send(file=discord.File('media/Mae/kiss.png'))

        @self.bot.command()
        async def mae_scared(ctx):
            await ctx.message.delete()
            await ctx.send(file=discord.File('media/Mae/scared.png'))

        @self.bot.command()
        async def mae_owo(ctx):
            await ctx.message.delete()
            await ctx.send(file=discord.File('media/Mae/OwO.png'))

        self.bot.run(self.token, bot=False)


if __name__ == '__main__':
    print("""
В файле token.txt замените токен на свой!
Иначе вы получите ошибку!""")
    input("Для продолжения введите Enter: ")
    SelfBot().run()
