import discord
from discord.ext import commands
import asyncio
import requests
import os
from PIL import Image, ImageDraw, ImageFont
import SiteParser
from googletrans import Translator
import io

# pyinstaller -F -i "media\icons\logo.ico" main.py


class SelfBot:
    def __init__(self, **options):
        super().__init__(**options)
        self.bot = commands.Bot(command_prefix='d_', self_bot=True)
        with open('token.txt', 'r') as token:
            self.__token = token.read()

    def run(self):
        self.bot.remove_command('help')
        print('Запустился')

        @self.bot.event
        async def on_ready():
            """
            Этот ивент не работает должным образом с обычными профилями
            Иногда срабатывает сразу иногда через какоето время
            """
            await self.bot.change_presence(activity=discord.Game('discord utils'))

        @self.bot.event
        async def on_message(message):
            await self.bot.process_commands(message)

        @self.bot.command(aliases=['help'])
        async def help_message(ctx):
            hembed = discord.Embed(title='**Функции**', description='Discord utils', color=0x0095ff, )
            # заголовки
            hembed.add_field(name='**d_help**', value='Это сообщение.', inline=False)
            hembed.add_field(name='**d_cat**', value='Отправить кота.', inline=False)
            hembed.add_field(name='**d_embed**', value='Отправить ембиент.', inline=False)
            hembed.add_field(name='**d_spam**', value='Поспамить.', inline=False)
            hembed.add_field(name='**d_emoji**', value='Анимированные эмодзи', inline=False)
            hembed.add_field(name='**d_rev**', value='Перевернуть сообщение.', inline=False)
            hembed.add_field(name='**d_ascii**', value='Анимированные залго смайлы.', inline=True)
            hembed.add_field(name='**d_nigga**', value='Сделать мем про ниггу.', inline=False)
            hembed.add_field(name='**d_loading**', value='Создать загрузку.', inline=False)
            hembed.add_field(name='**d_why**', value='Нахуя, а главное зачем.', inline=False)
            hembed.add_field(name='**d_hearts**', value='Радужное сердце.', inline=False)
            hembed.add_field(name='**d_change_game**', value='Изменить игру в профиле.', inline=False)
            hembed.add_field(name='**d_think**', value='Гигант мысли, отец...', inline=False)
            hembed.add_field(name='**d_trans**', value='Перевод на другие языки.', inline=False)
            hembed.add_field(name='**d_mae<hi,owo,kiss,scared>**', value='Стикеры про Мэй', inline=False)
            hembed.set_thumbnail(url='https://cdn4.iconfinder.com/data/icons/logos-and-brands/512'
                                     '/91_Discord_logo_logos-512.png')
            hembed.set_footer(text=f'Created by Vladislav Alpatov',
                              icon_url='https://steamcdn-a.akamaihd.net/steamcommunity/public/images/avatars/88'
                                       '/88a9bb41c035dee03f76cb1e48adc40b45f3ac9e_full.jpg')
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
            bars = (
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
                '[##########]100%')
            for bar in bars:
                await ctx.message.edit(embed=discord.Embed(title=f'**{label}**', description=bar, color=0x0095ff),
                                       content=None)
                await asyncio.sleep(1)
            await ctx.message.edit(embed=discord.Embed(title=f'**{label}**', description='Completed!', color=0x00ff1a),
                                   content=None)

        @self.bot.command(aliases=['ascii'])
        async def zalgo(ctx):
            """
            Анимированные zalgo эмодзи
            """
            faces = (
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
            )
            for face in faces:
                await ctx.message.edit(content=face)
                await asyncio.sleep(1)
            await ctx.message.delete()

        @self.bot.command()
        async def rev(ctx, *, text: str):
            """
            Переворачивает сообщение
            """
            await ctx.message.edit(content=text[::-1])

        @self.bot.command()
        async def quote(ctx):
            """
            Парсит и отправляет цитату
            """
            await ctx.message.edit(content=f'`{SiteParser.Quotes().getQuoteMessage()}`')

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

                image = Image.open(io.BytesIO(requests.get('https://github.com/VladislavAlpatov/discord-utils/blob'
                                                           '/master/media/nigga/nigga.jpg?raw=true').content))
                draw = ImageDraw.Draw(image)
                font = ImageFont.truetype('arialbd.ttf', large, encoding="unic")
                draw.text((200 - int(len(text)) * to_sum, 600 - large), str(text), fill=(0, 0, 0), font=font)
                image.save('nigga-out.jpg')
                await ctx.send(file=discord.File('nigga-out.jpg'))
                os.remove('nigga-out.jpg')
            else:
                await ctx.send('To many symbols')

        @self.bot.command()
        async def hearts(ctx):
            """
            Анимированные сердечки OwO
            """
            hearts1 = (
                ':heart:',
                ':orange_heart:',
                ':green_heart:',
                ':blue_heart:',
                ':purple_heart:',
                ':black_heart:',
                ':white_heart:'
            )
            for heart in hearts1:
                await ctx.message.edit(content=heart)
                await asyncio.sleep(0.5)
            await ctx.message.delete()

        @self.bot.command(aliases=['зачем', 'нахуя'])
        async def why(ctx):
            """
            Делает мем нахуя а главное зачем
            ВАЖНО! Берёт картинку из сообщения
            """
            # скачиваем фотографию
            try:
                # импортируем фотки
                image = Image.open(io.BytesIO(requests.get('https://github.com/VladislavAlpatov/discord-utils/blob'
                                                           '/master/media/memes/why.jpg?raw=true').content))  # прикол
                image_on_paste = Image.open(io.BytesIO(requests.get(ctx.message.attachments[0].url).content))

                # изменяем размер и вставляем фотографию
                image_on_paste = image_on_paste.resize((614, 336), Image.ANTIALIAS)
                image.paste(image_on_paste, (72, 42))

                image.save(f'{str(ctx.author.id)}.png')

                await ctx.message.delete()
                await ctx.send(file=discord.File(f'{str(ctx.author.id)}.png'))

                os.remove(f'{str(ctx.author.id)}.png')
            except IndexError:
                await ctx.message.edit(embed=discord.Embed(title=':x: Вы не приложили картинку к команде!',
                                                           color=0xff0000), content=None)

                await asyncio.sleep(1.5)
                await ctx.message.delete()

        @self.bot.command(aliases=['мысль', 'гигант'])
        async def think(ctx):
            """
            Делает мем гигант мысли
            ВАЖНО! Берёт картинку из сообщения
            """
            try:

                image = Image.open(io.BytesIO(requests.get('https://github.com/VladislavAlpatov/discord-utils/blob'
                                                           '/master/media/memes/think.jpg?raw=true').content))
                image_on_paste = Image.open(io.BytesIO(requests.get(str(ctx.message.attachments[0].url)).content))

                image_on_paste = image_on_paste.resize((500, 400), Image.ANTIALIAS)
                image.paste(image_on_paste, (130, 13))

                image.save(f'{str(ctx.author.id)}.png')

                await ctx.message.delete()
                await ctx.send(file=discord.File(f'{str(ctx.author.id)}.png'))

                os.remove(f'{str(ctx.author.id)}.png')
            except KeyError:
                await ctx.message.edit(embed=discord.Embed(title=':x: Вы не приложили картинку к команде!',
                                                           color=0xff0000), content=None)
                await asyncio.sleep(1.5)
                await ctx.message.delete()

        @self.bot.command()
        async def mae(ctx, emotion: str):
            """
            Стикеры с Мей
            https://bit.ly/2Evc2iI
            """
            await ctx.message.delete()
            images = {
                'hi': 'https://github.com/VladislavAlpatov/discord-utils/blob/master/media/Mae/hi.png?raw=true',
                'kiss': 'https://github.com/VladislavAlpatov/discord-utils/blob/master/media/Mae/kiss.png?raw=true',
                'emm': 'https://github.com/VladislavAlpatov/discord-utils/blob/master/media/Mae/emm.png?raw=true',
                'owo': 'https://github.com/VladislavAlpatov/discord-utils/blob/master/media/Mae/OwO.png?raw=true',
                'omg': 'https://github.com/VladislavAlpatov/discord-utils/blob/master/media/Mae/omg.png?raw=true',
                'tired': 'https://github.com/VladislavAlpatov/discord-utils/blob/master/media/Mae/tired.png?raw=true',
                'scared': 'https://github.com/VladislavAlpatov/discord-utils/blob/master/media/Mae/scared.png?raw=true',
                'pff': 'https://github.com/VladislavAlpatov/discord-utils/blob/master/media/Mae/pff.png?raw=true'
            }

            try:
                content = requests.get(images[emotion]).content
                with open('sticker.png', 'wb') as f:
                    f.write(content)
                await ctx.send(file=discord.File('sticker.png'))
                os.remove('sticker.png')
            except KeyError:
                error_message = await ctx.send(embed=discord.Embed(title=':x: Похоже вашего стикера нет в списке!',
                                                                   color=0xff0000), content=None)
                await asyncio.sleep(1.5)
                await error_message.delete()

        @self.bot.command()
        async def change_game(ctx, *, game: str):
            """
            Изменение игры в профиле
            """
            await self.bot.change_presence(activity=discord.Game(game))
            await ctx.message.edit(content=None, embed=discord.Embed(title=f'Игра изменна на: "**{game}**"',
                                                                     color=0xff5f5f))
            await asyncio.sleep(1.5)
            await ctx.message.delete()

        @self.bot.command()
        async def trans(ctx, mode: str, *, text: str):
            await ctx.message.edit(content='Перевожу...')
            try:
                text = Translator().translate(text=text, dest=mode)
                await ctx.message.edit(content=text.text)
            except ValueError:
                await ctx.message.edit(content=None, embed=discord.Embed(title=f':x: Вы выбрали несуществующий язык!',
                                                                         color=0xff5f5f))
                await asyncio.sleep(1.5)
                await ctx.message.delete()

        self.bot.run(self.__token, bot=False)


if __name__ == '__main__':
    input("""В файле token.txt замените токен на свой!
Иначе вы получите ошибку!
Для продолжения введите Enter: """)
    SelfBot().run()
