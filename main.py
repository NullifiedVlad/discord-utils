import asyncio
import io
import os

import discord
import requests
from PIL import Image, ImageDraw, ImageFont
from discord.ext import commands
from googletrans import Translator
from colorama import Fore
import SiteParser
from configs import settings


# pyinstaller -F -i "media\icons\logo.ico" main.py


class SelfBot(commands.Bot):
    def __init__(self, command_prefix, **options):
        super().__init__(command_prefix, **options)
        self.__isChatlog = False
        self.__isRainBow = False
        with open('token.txt', 'r') as token:
            self.__token = token.read()

    def start_bot(self):
        self.remove_command('help')
        print(f'{Fore.GREEN}Запустился{Fore.WHITE}')

        @self.event
        async def on_ready():
            """
            Этот ивент не работает должным образом с обычными профилями дискорда
            Если хотите внести сюда кариктеровки , то учитывайте это!
            Иногда срабатывает сразу иногда через какоето время
            """
            await self.change_presence(activity=discord.Game('discord utils'))

        @self.event
        async def on_message(message):
            """
            Записывает чат если перемнная __isChatlog == True
            :param message: прнимает сообщение
            :return: Ничего
            """
            if self.__isChatlog:
                with open('chat-log.txt', 'a') as f:
                    f.write(f'<{message.guild.name}> <{message.channel.name}> '
                            f'{message.author}: {message.content}\n')
            else:
                pass
            await self.process_commands(message)

        @self.command(aliases=['help'])
        async def help_message(ctx):
            """
            Сообщение где описываются все команды
            :param ctx:
            :return:
            """
            hembed = discord.Embed(title='**Функции**', description='Discord utils', color=0x0095ff, )
            # заголовки
            hembed.add_field(name=f'**{self.command_prefix}_help**', value='Это сообщение.', inline=False)
            hembed.add_field(name=f'**d_cat**', value='Отправить кота.', inline=False)
            hembed.add_field(name=f'**d_embed**', value='Отправить ембиент.', inline=False)
            hembed.add_field(name=f'**d_spam**', value='Поспамить.', inline=False)
            hembed.add_field(name=f'**d_emoji**', value='Анимированные эмодзи', inline=False)
            hembed.add_field(name=f'**d_rev**', value='Перевернуть сообщение.', inline=False)
            hembed.add_field(name=f'**d_ascii**', value='Анимированные залго смайлы.', inline=True)
            hembed.add_field(name=f'**d_nigga**', value='Сделать мем про ниггу.', inline=False)
            hembed.add_field(name=f'**d_loading**', value='Создать загрузку.', inline=False)
            hembed.add_field(name=f'**d_why**', value='Нахуя, а главное зачем.', inline=False)
            hembed.add_field(name=f'**d_hearts**', value='Радужное сердце.', inline=False)
            hembed.add_field(name=f'**d_change_game**', value='Изменить игру в профиле.', inline=False)
            hembed.add_field(name=f'**d_think**', value='Гигант мысли, отец...', inline=False)
            hembed.add_field(name=f'**d_joke**', value='Отправить рандомный анекдот', inline=False)
            hembed.add_field(name=f'**d_trans**', value='Перевод на другие языки.', inline=False)
            hembed.add_field(name=f'**d_mae<hi,owo,kiss,scared>**', value='Стикеры про Мэй', inline=False)
            hembed.add_field(name=f'**d_fresko**', value='Сделать мем про Жака Фреска.', inline=False)
            hembed.add_field(name=f'**d_chat_log**', value='Включить либо выключить лог чата.', inline=False)
            hembed.set_thumbnail(url='https://cdn4.iconfinder.com/data/icons/logos-and-brands/512'
                                     '/91_Discord_logo_logos-512.png')
            hembed.set_footer(text=f'Created by Vladislav Alpatov',
                              icon_url='https://steamcdn-a.akamaihd.net/steamcommunity/public/images/avatars/88'
                                       '/88a9bb41c035dee03f76cb1e48adc40b45f3ac9e_full.jpg')
            hembed.set_author(name=self.user.name, icon_url=ctx.author.avatar_url)
            await ctx.message.edit(embed=hembed, content=None)

        @self.command()
        async def spam(ctx, count: int, *, words: str):
            for i in range(count):
                await ctx.send(words)

        @self.command()
        async def embed(ctx, *, text: str):
            await ctx.message.edit(embed=discord.Embed(title=text, color=settings.embed_message_color), content=None)

        @self.command()
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

        @self.command()
        async def cat(ctx):
            await ctx.message.delete()
            image = requests.get('https://thiscatdoesnotexist.com/')
            with open('cat.jpg', 'wb') as f:
                f.write(image.content)
            await ctx.send(file=discord.File('cat.jpg'))
            os.remove('cat.jpg')

        @self.command()
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
                await ctx.message.edit(embed=discord.Embed(title=f'**{label}**',
                                                           description=bar,
                                                           color=settings.loading_color), content=None)
                await asyncio.sleep(1)
            await ctx.message.edit(embed=discord.Embed(title=f'**{label}**',
                                                       description='Completed!',
                                                       color=settings.loading_color_ready),
                                   content=None)

        @self.command(aliases=['ascii'])
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
                '¯\\_(ツ)_/¯',
                'ᕙ(⇀‸↼‶)ᕗ',
                'ᕦ(ò_óˇ)ᕤ',
                '(づ￣ ³￣)づ',
                '(งツ)ว',
                'ヾ(-__- )ゞ',
                '♪♪ ヽ(ˇ∀ˇ )ゞ',
                '(っ▀¯▀)つ',
                '~(^-^)~',
                '\\(ᵔᵕᵔ)/',
                '[¬º-°]¬',
                'ฅ^•ﻌ•^ฅ',
                '(╯°□°）╯︵ ┻━┻'
            )
            for face in faces:
                await ctx.message.edit(content=face)
                await asyncio.sleep(1)
            await ctx.message.delete()

        @self.command()
        async def rev(ctx, *, text: str):
            """
            Переворачивает сообщение
            """
            await ctx.message.edit(content=text[::-1])

        @self.command()
        async def quote(ctx):
            """
            Парсит и отправляет цитату
            """
            await ctx.message.edit(content=f'`{SiteParser.Quotes().getQuoteMessage()}`')

        @self.command()
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

                image = Image.open(io.BytesIO(requests.get('https://raw.githubusercontent.com/VladislavAlpatov'
                                                           '/discord-utils/master/media/nigga/nigga.jpg').content))
                # скачиваем шрифт
                arial = io.BytesIO(requests.get('https://github.com/VladislavAlpatov/discord-utils/blob/master/media'
                                                '/fonts/arialbd.ttf?raw=true').content)
                draw = ImageDraw.Draw(image)
                font = ImageFont.truetype(arial, large, encoding="unic")
                draw.text((200 - int(len(text)) * to_sum, 600 - large), str(text), fill=(0, 0, 0), font=font)
                image.save('nigga-out.jpg')
                await ctx.send(file=discord.File('nigga-out.jpg'))
                os.remove('nigga-out.jpg')
            else:
                await ctx.send('To many symbols')

        @self.command()
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

        @self.command()
        async def chat_log(ctx):
            if self.__isChatlog:
                self.__isChatLog = False
                await ctx.message.edit(content=None, embed=discord.Embed(title=':x: Лог чата выключен!',
                                                                         color=0xf00))
            else:
                self.__isChatLog = True
                await ctx.message.edit(content=None, embed=discord.Embed(title='Лог чата включен!',
                                                                         color=0x15ff00))
            await asyncio.sleep(2)
            await ctx.message.delete()

        @self.command()
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

                image.save(f'{ctx.author.id}.png')

                await ctx.message.delete()
                await ctx.send(file=discord.File(f'{ctx.author.id}.png'))

                os.remove(f'{ctx.author.id}.png')
            except IndexError:
                await ctx.message.edit(embed=discord.Embed(title=':x: Вы не приложили картинку к команде!',
                                                           color=0xff0000), content=None)

                await asyncio.sleep(1.5)
                await ctx.message.delete()

        @self.command()
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

        @self.command()
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

        @self.command()
        async def change_game(ctx, *, game: str):
            """
            Изменение игры в профиле
            """
            await self.change_presence(activity=discord.Game(game))
            await ctx.message.edit(content=None, embed=discord.Embed(title=f'Игра изменна на: "**{game}**"',
                                                                     color=0xff5f5f))
            await asyncio.sleep(1.5)
            await ctx.message.delete()

        @self.command()
        async def trans(ctx, mode: str, *, text: str):
            await ctx.message.edit(content='Перевожу...')
            try:
                text = Translator().translate(text=text, dest=mode)
                await ctx.message.edit(content=text.text)
            except ValueError:
                await ctx.message.edit(content=None, embed=discord.Embed(title=':x: Вы выбрали несуществующий язык!',
                                                                         color=0xff5f5f))
                await asyncio.sleep(1.5)
                await ctx.message.delete()

        @self.command()
        async def joke(ctx):
            await ctx.message.edit(content=SiteParser.Jokes().getJoke())

        @self.command()
        async def fresko(ctx, *, text: str):
            """
            Мем с Жаком Фреско
            :param ctx: парметры
            :param text: Текст в картинке (всего 56 симболов)
            :return: возращает картинку
            """
            if len(text) <= 56:
                try:
                    await ctx.message.delete()

                    image = Image.open('media/memes/fresko.jpg')

                    # скачиваем шрифт
                    arial = io.BytesIO(
                        requests.get('https://github.com/VladislavAlpatov/discord-utils/blob/master/media'
                                     '/fonts/arialbd.ttf?raw=true').content)

                    draw = ImageDraw.Draw(image)
                    font = ImageFont.truetype(arial, 35, encoding="unic")
                    draw.text((5, 60), f'{text[:18]}\n{text[18:33]}\n{text[33:56]}', fill=(0, 0, 0), font=font)
                    image.save('fresko.jpg')
                    await ctx.send(file=discord.File('fresko.jpg'))

                except Exception as e:
                    print(f'Ошибка: {e}')
                finally:
                    os.remove('fresko.jpg')

            else:
                await ctx.message.edit(content=None, embed=discord.Embed(title=':x: Вы превыси лимит допустимых '
                                                                               'симболов!',
                                                                         color=0xff5f5f))
                await asyncio.sleep(2)
                await ctx.message.delete()

        @self.command()
        async def avatar(ctx, *, user: discord.Member):
            await ctx.message.delete()
            avatar_embed = discord.Embed()
            avatar_embed.set_thumbnail(url=user.avatar_url)
            await ctx.send(content=None, embed=avatar_embed)

        self.run(self.__token, bot=False)


if __name__ == '__main__':
    input(f'''{Fore.RED}МЫ НЕ НЕСЁМ ОТВЕТСЕННОСТИ ЗА ВАШ АККАУНТ!
ВСЮ ОТВEСТВЕННОСТЬ ЗА НАРУШЕНИЕ ToS ВЫ БЕРЁТЕ НА СЕБЯ! {Fore.WHITE}
{Fore.YELLOW}
В файле token.txt ЗАМЕНИТЕ ТОКЕН НА СВОЙ!
Иначе вы получите ошибку!
{Fore.WHITE}
Для продолжения введите Enter: ''')
SelfBot(command_prefix=settings.command_prefix, self_bot=True).start_bot()
