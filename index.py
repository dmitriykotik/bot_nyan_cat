from datetime import datetime
from http import client, server
from msilib.schema import Component, Icon
from multiprocessing import Manager
from multiprocessing.connection import Client
from sqlite3 import connect
from unicodedata import category
import discord
from discord.ext import commands
from config import settings
from discord.ext import commands
from discord.ext import commands, tasks
from discord.ext.commands import Bot
from discord import member
from discord.utils import get
import asyncio
import asyncio
import functools
import itertools
import math
import random
import os
import discord
from async_timeout import timeout
from discord.ext import commands
from discord_components import DiscordComponents, ComponentsBot, Button, ButtonStyle, Select, SelectOption
from discord import FFmpegPCMAudio, PCMVolumeTransformer
import typing as t
import discord
from discord.ext import commands
import os
from discord import FFmpegPCMAudio
from discord.ext.commands import Bot
from discord.utils import get
import asyncio
from youtube_dl import YoutubeDL
from asyncio import sleep
import random



YDL_OPTIONS = {'format': 'bestaudio', 'noplaylist':'False'}
FFMPEG_OPTIONS = {'before_options': '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5', 'options': '-vn'}


bot = commands.Bot(command_prefix = settings['prefix'])
bot.remove_command('help')



songs = asyncio.Queue()
play_next_song = asyncio.Event()

chat = None
keyword = "test"


@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound ):
        await ctx.send(embed = discord.Embed(description = f'** {ctx.author.name}, данной команды не существует, попробуй перепроверить свою введённую команду, и отправь её снова.**', color=0xFF0000))
#
@bot.event
async def on_ready():
    timestamp = datetime.now()
    with open("log.txt", "a") as rst:
        rst.write("\n[РЕСТАРТ " + str(timestamp) + "]")
    time = datetime.now()
    with open("log.txt", "a") as rstr:
        rstr.write(f"\n[Получена причина рестарта в " + str(time) + " : Изменение или исправление кода бота, или критическая ошибка]")
    
    

@bot.command()
async def offline(ctx):
    
    await ctx.send("Проверьте консоль")
    print("Укажите этот параметр если бот будет остановлен:")
    print("#ncfis - Будет отсутствовать интернет подключение")
    print("#offhost - Отключение сервера")
    print("#apply - Редактирование кода")
    print("#cancel - выход")
    stop_code = input()
    if stop_code == "#ncfis":
        time = datetime.now()
        with open("log.txt", "a") as rstr:
            rstr.write(f"\n[БОТ ОСТАНОВЛЕН " + str(time) + "]")
            rstr.write(f"\n[Причина остановки: Отсутствует интернет соединение]")
        print("Перезагрузите бота или остановите")
        a = input()
    if stop_code == "#offhost":
        time = datetime.now()
        with open("log.txt", "a") as rstr:
            rstr.write(f"\n[БОТ ОСТАНОВЛЕН " + str(time) + "]")
            rstr.write(f"\n[Причина остановки: Неудаётся подключится к серверу]")
        print("Перезагрузите бота или остановите")
        a = input()
    if stop_code == "#errh":
        time = datetime.now()
        with open("log.txt", "a") as rstr:
            rstr.write(f"\n[БОТ ОСТАНОВЛЕН " + str(time) + "]")
            rstr.write(f"\n[Причина остановки: Критическая ошибка]")
        print("Перезагрузите бота или остановите")
        a = input()
    if stop_code == "#apply":
        time = datetime.now()
        with open("log.txt", "a") as rstr:
            rstr.write(f"\n[БОТ ОСТАНОВЛЕН " + str(time) + "]")
            rstr.write(f"\n[Причина остановки: Применение кода]")
        print("Перезагрузите бота или остановите")
        a = input()
    if stop_code == "#cancel":
        print("Программа Причина остановки бота закрыта")
        
            
        return
    





@bot.event
async def on_message(message):
    msg = message
    await bot.process_commands(msg)
    if (msg.content.startswith('#')):
        with open("log.txt", "a") as n:
            n.write("\n" + "<" + msg.content + "|" + str(msg.author) + "|" + str(msg.author.id) + str(msg.created_at) + ">")

        print("Command!") # Не обращайте внимание.. 
        pass
    else:
        
        with open("log.txt", "a") as n:
            n.write("\n" + "<" + msg.content + "|" + str(msg.author) + "|" + str(msg.author.id) + str(msg.created_at) + ">")
        #разрешённые
        if message.content.startswith("._."):
            with open("log.txt", "a") as n:
                n.write("\n" + "<" + msg.content + "|" + str(msg.author) + "|" + str(msg.author.id) + str(msg.created_at) + ">")
            return
        if message.content.startswith("._?"):
            with open("log.txt", "a") as n:
                n.write("\n" + "<" + msg.content + "|" + str(msg.author) + "|" + str(msg.author.id) + str(msg.created_at) + "> ")
            return
        if message.content.startswith(".-."):
            with open("log.txt", "a") as n:
                n.write("\n" + "<" + msg.content + "|" + str(msg.author) + "|" + str(msg.author.id) + str(msg.created_at) + "> ")
            return
        if message.content.startswith("._,"):
            with open("log.txt", "a") as n:
                n.write("\n" + "<" + msg.content + "|" + str(msg.author) + "|" + str(msg.author.id) + str(msg.created_at) + "> ")
            return
        if message.content.startswith("-_-"):
            with open("log.txt", "a") as n:
                n.write("\n" + "<" + msg.content + "|" + str(msg.author) + "|" + str(msg.author.id) + str(msg.created_at) + "> ")
            return
        if message.content.startswith("..."):
            with open("log.txt", "a") as n:
                n.write("\n" + "<" + msg.content + "|" + str(msg.author) + "|" + str(msg.author.id) + str(msg.created_at) + "> ")
            return


        #запрещённые
        if message.content.startswith("_ _"):
            await asyncio.sleep(0)
            await message.delete()
            with open("log.txt", "a") as n:
                n.write("\n" + "<" + msg.content + "|" + str(msg.author) + "|" + str(msg.author.id) + str(msg.created_at) + "> " + "DELETED Reason: Спам слово")
        if message.content.startswith("."):
            await asyncio.sleep(0)
            await message.delete()
            with open("log.txt", "a") as n:
                n.write("\n" + "<" + msg.content + "|" + str(msg.author) + "|" + str(msg.author.id) + str(msg.created_at) + "> " + "DELETED Reason: Спам слово")

@bot.event
async def on_message_delete(message):
    msg = message
    with open("log.txt", "a") as n:
        n.write("\n" + "<" + msg.content + "|" + str(msg.author) + "|" + str(msg.author.id) + str(msg.created_at) + "> " + "DELETED Reason: Сообщение удалено")
    
    #await message.send(f"{message.content}")

@bot.event
async def on_button_click(interaction):
  global vc
  if interaction.custom_id == 'stop':
    await vc.disconnect()
  if interaction.custom_id == 'replay':
    global info
    
    await vc.disconnect()
    voice_channel = interaction.message.author.voice.channel
    vc = await voice_channel.connect()

    with YoutubeDL(YDL_OPTIONS) as ydl:
        info = info

    URL = info['formats'][0]['url']

    vc.play(discord.FFmpegPCMAudio(executable="C:\\ffmpeg\\bin\\ffmpeg.exe", source = URL, **FFMPEG_OPTIONS))
@bot.event
async def on_button_click(interaction):
  if interaction.custom_id == 'but1':
    DiscordComponents(bot)
    print(interaction.channel_mentions)
    await interaction.send("Напишите: #support A (опишите проблему с указанием текста вашего сообщения)")

var = 0



@bot.command()
async def notepad(ctx, *, text):
    file = random.randint(1, 1000000000)
    with open(f"C:\путь\к\папке\для\хранения\общедоступных\файлов\{file}.txt", "w") as b:
            b.write(f'{text}')
    await ctx.send(file=discord.File(f"C:\путь\к\папке\для\хранения\общедоступных\файлов\{file}.txt"))
    with open("Files.txt", "a") as b:
        b.write(f'\n{file}.txt')



@bot.command()
async def dir(ctx):
    f = open(r"Путь к файлу Files.txt", "r")
    await ctx.send(f.read())

    

#выгрузка файла
@bot.command()
async def download(ctx, file):
    await ctx.send(file=discord.File(r'' + file))


#загрузка файла на сервер
@bot.command()
async def upload(ctx):
    DiscordComponents(bot)
    embed=discord.Embed(title="Пользовательское соглашение перед загрузкой файла", description="**Перед загрузкой файлов обязательно прочтите**", color=0xeeff00)
    embed.add_field(name="1. Порнография", value="Запрещается загрузка на сервер фотографий порнографического характера, также архивы с такими фото, видео и тд. Такие типы будут удалены с серверов, и будет запрещена загрузка на сервера в течении недели.", inline=False)
    embed.add_field(name="2. Трояны", value="Запрещается загрузка на сервер трояны, черви и тд. Они будут удалены антивирусами или в ручную.", inline=True)
    embed.add_field(name="3. Слив", value="Запрещается загрузка на сервер слив фото, программ, архивов которые скрывают. Так как любой файл могут скачать с сервера, такие файлы будут удалятся.", inline=True)
    embed.add_field(name="4. ОС", value="Конечно очень странно будет если вы найдёте ОС размером **8 МБ**, но такие образы как iso, img, ima, и тд относящиеся к дискетам и дискам.", inline=True)
    embed.add_field(name="Принятие", value="После нажатия на кнопку Я принимаю пользовательское соглашение вы принимаете, что не собираетесь загружать на сервера, что то из подобного по пунктам 1, 2, 3. При нарушении пользовательского соглашения наказания разные от блокировки доступа на 10 минут до бесконечности. Пожалуйста, не нарушайте пользовательское соглашение :3", inline=True)
    await ctx.send(embed=embed,
        components = [
            Button(style=ButtonStyle.green, label='✅ Я принимаю польз. соглашение', custom_id='ok'),
        ]

    )
    interaction = await bot.wait_for("button_click", check = lambda i: i.custom_id == "ok")
    await interaction.send(content = "Вы приняли пользовательское соглашение")
    for attachment in ctx.message.attachments:
        await attachment.save(f'C:\Files\{attachment.filename}')
        with open("Files.txt", "a") as b:
            b.write(f'\n{attachment.filename}')


@bot.command()
async def send_log(ctx):
    await ctx.send(file=discord.File(r'c:\путь\к\файлу\log.txt'))


    

#тестирование бота
@bot.command()

async def init(ctx):
    if var == 0:
        embed = discord.Embed(
            title = 'Успешно!',
            description = '**Инициализация прошла успешно!**',
        )
        await ctx.send(embed = embed)
    else:
        embed=discord.Embed(title="Ой, подождите...", description="Кажется бот находится на технических работах -_- Пожалуйста подождите окончания технических работ .-.", color=0x007bff)
        await ctx.send(embed=embed)


    
#установить статус бота играет в
@bot.command()
async def playing(ctx):
    if var == 0:
        activity = discord.Game(name="#help | Вирус MEMZ")
        await bot.change_presence(status=discord.Status.online, activity=activity)
        print("Успешно!")
        

        embed = discord.Embed(
            title = 'Успешно!',
            description = 'Статус бота изменён на: Играет!',
            colour = discord.Colour.from_rgb(0, 255, 0)
        )
        await ctx.send(embed = embed) # Отправляем Embed
    else:
        embed=discord.Embed(title="Ой, подождите...", description="Кажется бот находится на технических работах -_- Пожалуйста подождите окончания технических работ .-.", color=0x007bff)
        await ctx.send(embed=embed)

#установить статус бота стримит
@bot.command()
async def streaming(ctx):
    if var == 0:
        activity = discord.Streaming(name="#help | Ждёмс стрима люди", url="https://twitch.tv/adminkinlvs")
        await bot.change_presence(status=discord.Status.online, activity=activity)
        print("Успешно!")
        

        embed = discord.Embed(
            title = 'Успешно!',
            description = 'Статус бота изменён на: Стримит!',
            colour = discord.Colour.from_rgb(0, 255, 0)
        )
        await ctx.send(embed = embed) # Отправляем Embed
    else:
        embed=discord.Embed(title="Ой, подождите...", description="Кажется бот находится на технических работах -_- Пожалуйста подождите окончания технических работ .-.", color=0x007bff)
        await ctx.send(embed=embed)

#установить статус бота слушает
@bot.command()
async def listening(ctx):
    if var == 0:
        activity = discord.Activity(type=discord.ActivityType.listening, name="#help | Балалайка")
        await bot.change_presence(status=discord.Status.online, activity=activity)
        print("Успешно!")
        

        embed = discord.Embed(
            title = 'Успешно!',
            description = 'Статус бота изменён на: Слушает!',
            colour = discord.Colour.from_rgb(0, 255, 0)
        )
        await ctx.send(embed = embed) # Отправляем Embed
    else:
        embed=discord.Embed(title="Ой, подождите...", description="Кажется бот находится на технических работах -_- Пожалуйста подождите окончания технических работ .-.", color=0x007bff)
        await ctx.send(embed=embed)

#установить статус бота смотрит
@bot.command()
@commands.has_any_role(929030139159924736, 913963226356666389, 40705134462271548, 978941351645290496)
async def watching(ctx):
    if var == 0:
        activity = discord.Activity(type=discord.ActivityType.watching, name="#help | Как создать папку (ещё 4 часа)")
        await bot.change_presence(status=discord.Status.online, activity=activity)
        print("Успешно!")
        

        embed = discord.Embed(
            title = 'Успешно!',
            description = 'Статус бота изменён на: Смотрит!',
            colour = discord.Colour.from_rgb(0, 255, 0)
        )
        await ctx.send(embed = embed) # Отправляем Embed
    else:
        embed=discord.Embed(title="Ой, подождите...", description="Кажется бот находится на технических работах -_- Пожалуйста подождите окончания технических работ .-.", color=0x007bff)
        await ctx.send(embed=embed)

#технические работы
@bot.command()

async def tworks(ctx, reason = "Неуказанно"):
    global var
    activity = discord.Game(name=f"Технические работы! Причина: {reason}")
    await bot.change_presence(status=discord.Status.dnd, activity=activity)
    embed=discord.Embed(title="Технические работы включены!", color=0xff0000)
    await ctx.send(embed=embed)
    print("Успешно!")
    var = 1


# рестарт
@bot.command()

async def tworks_restart(ctx, reason = "Неуказанно"):
    await ctx.channel.purge( limit = 1 )
    global var
    await ctx.send("Рестарт через 1 минуту")
    await asyncio.sleep(55)
    await ctx.send("Рестарт через 5!")
    await asyncio.sleep(1)
    await ctx.send("Рестарт через 4!")
    await asyncio.sleep(1)
    await ctx.send("Рестарт через 3!")
    await asyncio.sleep(1)
    await ctx.send("Рестарт через 2!")
    await asyncio.sleep(1)
    await ctx.send("Рестарт через 1!")
    await asyncio.sleep(1)
    await ctx.send("Рестарт!")
    var = 1
    await ctx.voice_client.disconnect()
    activity = discord.Game(name=f"Технические работы! Причина: {reason}")
    await bot.change_presence(status=discord.Status.dnd, activity=activity)
    embed=discord.Embed(title="Технические работы включены!", color=0xff0000)
    await ctx.send(embed=embed)
    




#выход из технических работ
@bot.command()

async def exit_tworks(ctx,):
    await ctx.channel.purge( limit = 1 )
    global var
    activity = discord.Game(name="#help | Вирус MEMZ")
    await bot.change_presence(status=discord.Status.dnd, activity=activity)
    print("Успешно!")
    embed=discord.Embed(title="Технические работы выключены!", color=0x00ff04)
    await ctx.send(embed=embed)
    var = 0
    


#-=-=-=-=-=-=-=--=-=-=-=
#установить свой статус бота играет в
@bot.command()

async def my_playing(ctx, reason = "Люблю рп :3"):
    if var == 0:
        channel = bot.get_channel(988199433479028757)
        activity = discord.Game(name=f"#help | {reason}")
        await bot.change_presence(status=discord.Status.online, activity=activity)
        print("Успешно!")
        embed2=discord.Embed(title="Опа", description="Использование команды #my_playing", color=0x04ff00)
        embed2.add_field(name=f"{ctx.author.name}", value=f"{reason}", inline=True)
        await channel.send(embed=embed2)
        

        embed = discord.Embed(
            title = 'Успешно!',
            description = 'Статус бота изменён на: Играет!',
            colour = discord.Colour.from_rgb(0, 255, 0)
        )
        await ctx.send(embed = embed) # Отправляем Embed
    else:
        embed=discord.Embed(title="Ой, подождите...", description="Кажется бот находится на технических работах -_- Пожалуйста подождите окончания технических работ .-.", color=0x007bff)
        await ctx.send(embed=embed)
    

#установить свой статус бота стримит
@bot.command()

async def my_streaming(ctx, reason = "Стрим на рп"):
    if var == 0:
        channel = bot.get_channel(988199433479028757)
        activity = discord.Streaming(name=f"#help | {reason}", url="https://twitch.tv/AdminkinLvs")
        await bot.change_presence(status=discord.Status.online, activity=activity)
        print("Успешно!")
        embed2=discord.Embed(title="Опа", description="Использование команды #my_streaming", color=0x04ff00)
        embed2.add_field(name=f"{ctx.author.name}", value=f"{reason}", inline=True)
        await channel.send(embed=embed2)
        

        embed = discord.Embed(
            title = 'Успешно!',
            description = 'Статус бота изменён на: Стримит!',
            colour = discord.Colour.from_rgb(0, 255, 0)
        )
        await ctx.send(embed = embed) # Отправляем Embed
    else:
        embed=discord.Embed(title="Ой, подождите...", description="Кажется бот находится на технических работах -_- Пожалуйста подождите окончания технических работ .-.", color=0x007bff)
        await ctx.send(embed=embed)


#установить статус бота слушает
@bot.command()

async def my_listening(ctx, reason = "I love RPLands!"):
    if var == 0:
        channel = bot.get_channel(988199433479028757)
        activity = discord.Activity(type=discord.ActivityType.listening, name=f"#help | {reason}")
        await bot.change_presence(status=discord.Status.online, activity=activity)
        print("Успешно!")
        embed2=discord.Embed(title="Опа", description="Использование команды #my_listening", color=0x04ff00)
        embed2.add_field(name=f"{ctx.author.name}", value=f"{reason}", inline=True)
        await channel.send(embed=embed2)
        

        embed = discord.Embed(
            title = 'Успешно!',
            description = 'Статус бота изменён на: Слушает!',
            colour = discord.Colour.from_rgb(0, 255, 0)
        )
        await ctx.send(embed = embed) # Отправляем Embed
    else:
        embed=discord.Embed(title="Ой, подождите...", description="Кажется бот находится на технических работах -_- Пожалуйста подождите окончания технических работ .-.", color=0x007bff)
        await ctx.send(embed=embed)


#установить свой статус бота смотрит
@bot.command()

async def my_watching(ctx, reason = "Ой кажется батон забыли"):
    if var == 0:
        channel = bot.get_channel(988199433479028757)
        activity = discord.Activity(type=discord.ActivityType.watching, name=f"#help | {reason}")
        await bot.change_presence(status=discord.Status.online, activity=activity)
        print("Успешно!")
        embed2=discord.Embed(title="Опа", description="Использование команды #my_watching", color=0x04ff00)
        embed2.add_field(name=f"{ctx.author.name}", value=f"{reason}", inline=True)
        await channel.send(embed=embed2)


        embed = discord.Embed(
            title = 'Успешно!',
            description = 'Статус бота изменён на: Смотрит!',
            colour = discord.Colour.from_rgb(0, 255, 0)
        )
        await ctx.send(embed = embed) # Отправляем Embed
    else:
        embed=discord.Embed(title="Ой, подождите...", description="Кажется бот находится на технических работах -_- Пожалуйста подождите окончания технических работ .-.", color=0x007bff)
        await ctx.send(embed=embed)



#913963226356666389

#отправка сообщения в лс пользователю
@bot.command()
@commands.has_any_role(929030139159924736, 913979911411236935,  940705134462271548, 978941351645290496)
async def send_ls(ctx, member: discord.Member, message):
    if var == 0:
        await ctx.channel.purge( limit = 1 )
        await member.send(f'{message} - это сообщение вам отправил {ctx.author.mention}')
    else:
        embed=discord.Embed(title="Ой, подождите...", description="Кажется бот находится на технических работах -_- Пожалуйста подождите окончания технических работ .-.", color=0x007bff)
        await ctx.send(embed=embed)
@send_ls.error
async def test_error(ctx, error):
    if isinstance(error, commands.errors.MissingAnyRole):
        embed = discord.Embed(
            title = 'Ошибка!',
            description = 'К сожалению у вас нет прав на использование данной команды.',
            colour = discord.Colour.from_rgb(255, 0, 0)
        )
        await ctx.send(embed = embed) # Отправляем Embed

#размут
@bot.command()

async def unmute( ctx, member: discord.Member ):
    role = discord.utils.get( ctx.message.guild.roles, name = 'Топовая Свинка' )
    await member.remove_roles(role)
    await ctx.send("Успешно!")
    await ctx.channel.purge( limit = 2 )
    embed = discord.Embed(
        title = 'Уведомление',
        description = f'Пользователь **{member.mention}** был размьючен',
        colour = discord.Colour.from_rgb( 0, 255, 0 )
    )
    await ctx.send( embed = embed )

    channel = bot.get_channel(979800629520265346)
    embed=discord.Embed(title="Опа", description="Использование команды !unmute", color=0x04ff00)
    embed.add_field(name=f"{ctx.author.name}", value=f"(Нет подробностей)", inline=True)
    await channel.send(embed=embed)

@unmute.error
async def test_error(ctx, error):
    if isinstance(error, commands.errors.MissingAnyRole):
        embed = discord.Embed(
            title = 'Ошибка!',
            description = 'К сожалению у вас нет прав на использование данной команды.',
            colour = discord.Colour.from_rgb(255, 0, 0)
        )
        await ctx.send(embed = embed) # Отправляем Embed


#очистка чата
@bot.command( pass_context = True )

async def clear( ctx, amouth = 10 ):
    if var == 0:
        await ctx.channel.purge( limit = amouth )
        embed = discord.Embed(
            title = 'Очистка чата',
            description = f'**Чат** был **очищен** пользователем ***{ ctx.message.author.mention }***.',
            colour = discord.Colour.from_rgb(50, 200, 5)
        )
        await ctx.send(embed = embed)
        await ctx.channel.purge( limit = 2 )

        channel = bot.get_channel(979800629520265346)
        embed=discord.Embed(title="Опа", description="Использование команды !clear", color=0x04ff00)
        embed.add_field(name=f"{ctx.author.name}", value=f"Отчищено {amouth} сообщений", inline=True)
        await channel.send(embed=embed)
    else:
        embed=discord.Embed(title="Ой, подождите...", description="Кажется бот находится на технических работах -_- Пожалуйста подождите окончания технических работ .-.", color=0x007bff)
        await ctx.send(embed=embed)



#мут
@bot.command()

async def mute( ctx, member: discord.Member, reason = 'без причины' ):
    role = discord.utils.get( ctx.message.guild.roles, name = 'Топовая Свинка' )
    await member.add_roles(role)
    await ctx.send("Успешно!")
    await ctx.channel.purge( limit = 2 )
    embed = discord.Embed(
        title = 'Уведомление',
        description = f'Пользователь **{member.mention}** был замьючен по причине: **{reason}**',
        colour = discord.Colour.from_rgb( 255, 230, 0 )
    )
    await ctx.send( embed = embed )

    channel = bot.get_channel(979800629520265346)
    embed=discord.Embed(title="Опа", description="Использование команды !mute", color=0x04ff00)
    embed.add_field(name=f"{ctx.author.name}", value=f"Пользоватеь получивший мут: {member} Причина: {reason}", inline=True)
    await channel.send(embed=embed)

@mute.error
async def test_error(ctx, error):
    if isinstance(error, commands.errors.MissingAnyRole):
        embed = discord.Embed(
            title = 'Ошибка!',
            description = 'К сожалению у вас нет прав на использование данной команды.',
            colour = discord.Colour.from_rgb(255, 0, 0)
        )
        await ctx.send(embed = embed) # Отправляем Embed

#бан
@bot.command()

async def ban(ctx, member : discord.Member, *, reason = "На вас наложили великую печать бана!"):
    embed = discord.Embed(
        title = 'Успешно!',
        description = f'Пользователь **{member}** был заблокирован навсегда по причине: **{reason}**',
        colour = discord.Colour.from_rgb( 50, 200, 5 )
    )
    await ctx.send( embed = embed )
    await member.ban(reason = reason)

    channel = bot.get_channel(979800629520265346)
    embed=discord.Embed(title="Опа", description="Использование команды !ban", color=0x04ff00)
    embed.add_field(name=f"{ctx.author.name}", value=f"Пользователь получивший бан: {member} Причина: {reason}", inline=True)
    await channel.send(embed=embed)

@ban.error
async def test_error(ctx, error):
    if isinstance(error, commands.errors.MissingAnyRole):
        embed = discord.Embed(
            title = 'Ошибка!',
            description = 'К сожалению у вас нет прав на использование данной команды.',
            colour = discord.Colour.from_rgb(255, 0, 0)
        )
        await ctx.send(embed = embed) # Отправляем Embed

#кик
@bot.command()
async def kick(ctx, member: discord.Member, *, reason=None):
    embed = discord.Embed(
        title = 'Успешно!',
        description = f'Пользователь **{member}** был кикнут с сервера по причине: **{reason}**',
        colour = discord.Colour.from_rgb( 50, 200, 5 )
    )
    await ctx.send( embed = embed )
    await member.kick(reason=reason)

    channel = bot.get_channel(979800629520265346)
    embed=discord.Embed(title="Опа", description="Использование команды !kick", color=0x04ff00)
    embed.add_field(name=f"{ctx.author.name}", value=f"Кикнутый пользователь: {member} Причина: {reason}", inline=True)
    await channel.send(embed=embed)

@kick.error
async def test_error(ctx, error):
    if isinstance(error, commands.errors.MissingAnyRole):
        embed = discord.Embed(
            title = 'Ошибка!',
            description = 'К сожалению у вас нет прав на использование данной команды.',
            colour = discord.Colour.from_rgb(255, 0, 0)
        )
        await ctx.send(embed = embed) # Отправляем Embed


#-система предупреждений
@bot.command()

async def warn(ctx, member: discord.Member, int: int, reason = None):
    embed=discord.Embed(title="Предупреждение!", description=f"**Пользователь {member} получает {int}-е из 3-х предупреждений!** По причине: **{reason}**", color=0xff0000)
    await ctx.send(embed=embed)
    if int <1 :
        embed=discord.Embed(title=f"{member} Нельзя использовать такие числа", color=0xff0000)
        await ctx.send(embed=embed)
        role = discord.utils.get( ctx.message.guild.roles, name = 'Топовая Свинка' )
        await member.add_roles(role)
        await ctx.message.author.add_roles( role )
    if int == 1:
        embed=discord.Embed(title=f"{member} Больше не нарушай!", color=0xff0000)
        await ctx.send(embed=embed)
    if int == 2:
        embed=discord.Embed(title=f"{member} Я же сказал больше не нарушай!!! Это твой последний шанс!", color=0xff0000)
        await ctx.send(embed=embed)
    if int == 3:
        embed=discord.Embed(title=f"{member} Я же просил не нарушать! Теперь я вынужден выдать тебе временно мут :(", color=0xff0000)
        await ctx.send(embed=embed)
        role = discord.utils.get( ctx.message.guild.roles, name = 'Топовая Свинка' )
        await member.add_roles(role)
    if int >3 :
        embed=discord.Embed(title=f"{member} Как ты так умудрился? Помочь ничем не могу, правила, на то и правила что-бы их не нарушать", color=0xff0000)
        await ctx.send(embed=embed)
        role = discord.utils.get( ctx.message.guild.roles, name = 'Топовая Свинка' )
        await member.add_roles(role)

    channel = bot.get_channel(979800629520265346)
    embed=discord.Embed(title="Опа", description="Использование команды !warn", color=0x04ff00)
    embed.add_field(name=f"{ctx.author.name}", value=f"Пользователь получивший предупреждение: {member} Кол-во полученых предупреждений: {int} Причина: {reason}", inline=True)
    await channel.send(embed=embed)

@warn.error
async def test_error(ctx, error):
    if isinstance(error, commands.errors.MissingAnyRole):
        embed = discord.Embed(
            title = 'Ошибка!',
            description = 'К сожалению у вас нет прав на использование данной команды.',
            colour = discord.Colour.from_rgb(255, 0, 0)
        )
        await ctx.send(embed = embed) # Отправляем Embed

#фишки

#кноксбот
@bot.command()

async def кноксбот(ctx):
    if var == 0:
        embed = discord.Embed(
            title = '...',
            description = 'Да',
            colour = discord.Colour.from_rgb(0, 255, 0)
        )
        await ctx.send(embed = embed) # Отправляем Embed 
    else:
        embed=discord.Embed(title="Ой, подождите...", description="Кажется бот находится на технических работах -_- Пожалуйста подождите окончания технических работ .-.", color=0x007bff)
        await ctx.send(embed=embed)

      

#необязан
@bot.command()

async def необязан(ctx):
    if var == 0:
        embed = discord.Embed(
            title = 'Вы Фрайз?',
            description = 'Это любимое слово фрайза, теперь вы НЕОБЯЗАНЫ',
            colour = discord.Colour.from_rgb(0, 255, 0)
        )
        await ctx.send(embed = embed) # Отправляем Embed
    else:
        embed=discord.Embed(title="Ой, подождите...", description="Кажется бот находится на технических работах -_- Пожалуйста подождите окончания технических работ .-.", color=0x007bff)
        await ctx.send(embed=embed)


#БААААН
@bot.command()

async def БААААН(ctx):
    if var == 0:
        embed = discord.Embed(
            title = 'Вы плохо себя ведете на сьемках?',
            description = 'ЗНАЧИТ ВАМ БАААААААН',
            colour = discord.Colour.from_rgb(0, 255, 0)
        )
        await ctx.send(embed = embed) # Отправляем Embed
    else:
        embed=discord.Embed(title="Ой, подождите...", description="Кажется бот находится на технических работах -_- Пожалуйста подождите окончания технических работ .-.", color=0x007bff)
        await ctx.send(embed=embed)


#собака_серая
@bot.command()

async def собака_серая(ctx):
    if var == 0:
        embed = discord.Embed(
            title = 'Шо то на китайском',
            description = 'Ах ты собака серая',
            colour = discord.Colour.from_rgb(0, 255, 0)
        )
        await ctx.send(embed = embed) # Отправляем Embed
    else:
        embed=discord.Embed(title="Ой, подождите...", description="Кажется бот находится на технических работах -_- Пожалуйста подождите окончания технических работ .-.", color=0x007bff)
        await ctx.send(embed=embed)


#илья_и_мич
@bot.command()

async def ильяимич(ctx):
    if var == 0:
        embed = discord.Embed(
            title = 'Что?',
            description = 'Что Илья с Мичём делали в туалете?',
            colour = discord.Colour.from_rgb(0, 255, 0)
        )
        await ctx.send(embed = embed) # Отправляем Embed
    else:
        embed=discord.Embed(title="Ой, подождите...", description="Кажется бот находится на технических работах -_- Пожалуйста подождите окончания технических работ .-.", color=0x007bff)
        await ctx.send(embed=embed)
 

#ШЫЫЫШ
@bot.command()

async def ШЫЫЫШ( ctx ):
    if var == 0:
        embed = discord.Embed(
            title = 'ШЫЫЫЫЫЫЫЫЫЫЫЫШ',
            description = '**Это любимая фраза Ластика :)**',
            colour = discord.Colour.from_rgb( 50, 200, 5 )
        )
        await ctx.send( embed = embed )
    else:
        embed=discord.Embed(title="Ой, подождите...", description="Кажется бот находится на технических работах -_- Пожалуйста подождите окончания технических работ .-.", color=0x007bff)
        await ctx.send(embed=embed)


#да
@bot.command()

async def да( ctx ):
    if var == 0:
        embed = discord.Embed(
            title = 'ДА',
            description = '**Провода**',
            colour = discord.Colour.from_rgb( 50, 200, 5 )
        )
        await ctx.send( embed = embed )
    else:
        embed=discord.Embed(title="Ой, подождите...", description="Кажется бот находится на технических работах -_- Пожалуйста подождите окончания технических работ .-.", color=0x007bff)
        await ctx.send(embed=embed)


#нет
@bot.command()

async def нет( ctx ):
    if var == 0:
        embed = discord.Embed(
            title = 'НЕТ',
            description = '**Мопед**',
            colour = discord.Colour.from_rgb( 50, 200, 5 )
        )
        await ctx.send( embed = embed )
    else:
        embed=discord.Embed(title="Ой, подождите...", description="Кажется бот находится на технических работах -_- Пожалуйста подождите окончания технических работ .-.", color=0x007bff)
        await ctx.send(embed=embed)

    
#дурку
@bot.command()

async def дурку( ctx, member = discord.member ):
    if var == 0:
        embed = discord.Embed(
            title = 'Вызывали дурку?',
            description = f'Вызываем дурку {member}',
            colour = discord.Colour.from_rgb( 50, 200, 5 )
        )
        await ctx.send( embed = embed )
    else:
        embed=discord.Embed(title="Ой, подождите...", description="Кажется бот находится на технических работах -_- Пожалуйста подождите окончания технических работ .-.", color=0x007bff)
        await ctx.send(embed=embed)


@bot.command()
async def open_source(ctx):
    embed = discord.Embed(
        title = 'Исходный код уже доступен!',
        description = f'Скачать исходный код бота можно на сайте: https://github.com/dmitriykotik/bot_nyan_cat',
        colour = discord.Colour.from_rgb( 50, 200, 5 )
    )
    await ctx.send( embed = embed )

#осуждаю
@bot.command()

async def ОСУЖДАЮ( ctx, member = discord.member ):
    if var == 0:
        embed = discord.Embed(
            title = 'АХТУНГ!',
            description = f'ОСУЖДАЮ ТЕБЯ {member}',
            colour = discord.Colour.from_rgb( 50, 200, 5 )
        )
        await ctx.send( embed = embed )
    else:
        embed=discord.Embed(title="Ой, подождите...", description="Кажется бот находится на технических работах -_- Пожалуйста подождите окончания технических работ .-.", color=0x007bff)
        await ctx.send(embed=embed)


#мьёдик
@bot.command()

async def мьёдик(ctx):
    if var == 0:
        embed=discord.Embed(title="МЬЁЁЁДИИИИККККК", description="БЖЖЖЖЖЖЖЖЖЖ", color=0xe1ff00)
        embed.set_author(name="Пчёлка", icon_url="https://qrim.org/wp-content/uploads/2013/10/Pchela.jpg")
        embed.add_field(name="Купи", value="ВКУСНАЙ МЬЁДИК МОЖНО КУПИТЬ В МАГАЗИНЕ У ИЛЬИ И ПЛЮХИ БЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖ, А Я ДАЛЬШЕ ЛЕТАТЬ :)", inline=False)
        await ctx.send(embed=embed)
    else:
        embed=discord.Embed(title="Ой, подождите...", description="Кажется бот находится на технических работах -_- Пожалуйста подождите окончания технических работ .-.", color=0x007bff)
        await ctx.send(embed=embed)


#ДА_ЁЁЁ
@bot.command()

async def ДА_ЁЁЁ(ctx):
    if var == 0:
        embed=discord.Embed(title="АЙ", description="ДА ЁЁЁЁЁЁЁЁЁЁЁЁЁЁМАЁ", color=0x04ff00)
        await ctx.send(embed=embed)
    else:
        embed=discord.Embed(title="Ой, подождите...", description="Кажется бот находится на технических работах -_- Пожалуйста подождите окончания технических работ .-.", color=0x007bff)
        await ctx.send(embed=embed)


#БЛИИИИИИИН
@bot.command()

async def БЛИИИИИИИН(ctx):
    if var == 0:
        embed=discord.Embed(title="БЛИИИИИИИИИИИИИИИИИИИИИИИИИИИИИИИИИИИИИИИИИИИИИИИИИИИИИИИИИИИИИИИИИИИИИИИИИИИИИИИН", color=0x04ff00)
        await ctx.send(embed=embed)
    else:
        embed=discord.Embed(title="Ой, подождите...", description="Кажется бот находится на технических работах -_- Пожалуйста подождите окончания технических работ .-.", color=0x007bff)
        await ctx.send(embed=embed)
 

#повтарюша 
@bot.command()

async def say(ctx, message = None):
    if var == 0:
        channel = bot.get_channel(978911406525124628)
        await ctx.channel.purge( limit = 1 )
        await ctx.send(f"{message}")
        embed=discord.Embed(title="Опа", description="Использование команды #say", color=0x04ff00)
        embed.add_field(name=f"{ctx.author.name}", value=f"{message}", inline=True)
        await channel.send(embed=embed)
    else:
        embed=discord.Embed(title="Ой, подождите...", description="Кажется бот находится на технических работах -_- Пожалуйста подождите окончания технических работ .-.", color=0x007bff)
        await ctx.send(embed=embed)

    
#добавление новости
@bot.command()

async def add_news(ctx, message = None):
    if var == 0:
        channel = bot.get_channel(978911337423966228)
        embed=discord.Embed(title="Успешно!", description="Ваша новость отправлена на модерацию!", color=0x04ff00)
        await ctx.send(embed=embed)
        #{ctx.author.name}
        embed=discord.Embed(title="Опа", description="Новость на новую модерацию", color=0x04ff00)
        embed.add_field(name=f"{ctx.author.name}", value=f"{message}", inline=True)
        await channel.send(embed=embed)
    else:
        embed=discord.Embed(title="Ой, подождите...", description="Кажется бот находится на технических работах -_- Пожалуйста подождите окончания технических работ .-.", color=0x007bff)
        await ctx.send(embed=embed)



#новости рп
@bot.command()

async def news_rp(ctx):
    if var == 0:
        embed=discord.Embed(title="Новости РП", description="Пока что новостей нет :(", color=0x04ff00)
        await ctx.send(embed=embed)
    else:
        embed=discord.Embed(title="Ой, подождите...", description="Кажется бот находится на технических работах -_- Пожалуйста подождите окончания технических работ .-.", color=0x007bff)
        await ctx.send(embed=embed)


#газета
@bot.command()

async def news(ctx):
    if var == 0:
        embed=discord.Embed(title="Газета", color=0x00fffb)
        embed.add_field(name="Новость 1", value="Вышло новое обновление бота! Version 1.4 1a", inline=True)
        embed.add_field(name="Новость 2", value="Дообавлены команды: !ДА_ЁЁЁ и !БЛИИИИИИИН", inline=True)
        embed.add_field(name="Новость 3", value="Вышло новое обновление бота! Version 1.4 1b", inline=True)
        embed.add_field(name="Новость 4", value="Вышло новое обновление бота! Version 1.5 1a", inline=True)
        embed.add_field(name="Новость 5", value="Вышло новое обновление бота! Version 1.5 1b", inline=True)
        embed.add_field(name="Новость 6", value="Бот временно будет на тех обслуживании", inline=True)
        embed.set_footer(text="Последнее обновление: 18.06.2022 15:47")
        mes = await ctx.send(embed=embed)
        await mes.add_reaction("👍")
        await mes.add_reaction("👎")
    else:
        embed=discord.Embed(title="Ой, подождите...", description="Кажется бот находится на технических работах -_- Пожалуйста подождите окончания технических работ .-.", color=0x007bff)
        await ctx.send(embed=embed)



#отправка идеи на модерацию
@bot.command()

async def create_command(ctx, command = "Нет команды, отказ от принятия", desc = "Без описания"):
    if var == 0:
        embed=discord.Embed(title="Спасибо! :)", description="Спасибо за участие в проекте: Улучшение бота Nyan Cat! Мы обязательно посмотрим вашу команду!", color=0x04ff00)
        await ctx.send(embed=embed)
        channel=bot.get_channel(979837297769984000)
        embed=discord.Embed(title="Опа", description="Использование команды #create_command ", color=0x04ff00)
        embed.add_field(name=f"{ctx.author.name}", value=f"Команда: {command} Описание: {desc}", inline=True)
        await channel.send(embed=embed)
    else:
        embed=discord.Embed(title="Ой, подождите...", description="Кажется бот находится на технических работах -_- Пожалуйста подождите окончания технических работ .-.", color=0x007bff)
        await ctx.send(embed=embed)


#~ Музыка
#подключить бота к гс
@bot.command()

async def connect(ctx):
    if var == 0:
        await ctx.author.voice.channel.connect()
        await ctx.message.delete()
        channel = bot.get_channel(987511963913433168)
        embed1=discord.Embed(title="Опа", description="Использование команды #connect", color=0x04ff00)
        embed1.add_field(name=f"{ctx.author.name}", value=f"Подключил бота к голосовому каналу", inline=True)
        await channel.send(embed=embed1)
    else:
        embed=discord.Embed(title="Ой, подождите...", description="Кажется бот находится на технических работах -_- Пожалуйста подождите окончания технических работ .-.", color=0x007bff)
        await ctx.send(embed=embed)


#отключить бота от гс по причине
@bot.command()

async def disconnect(ctx, reason = None):
    if var == 0:
        await ctx.voice_client.disconnect()
        await ctx.message.delete()
        embed=discord.Embed(title="Nyan cat | Music", color=0x00bfff)
        embed.add_field(name="Упс", value=f"Сеанс завершён по причине: {reason}", inline=False)
        await ctx.send(embed=embed)
        channel = bot.get_channel(987511963913433168)
        embed1=discord.Embed(title="Опа", description="Использование команды #disconnect", color=0x04ff00)
        embed1.add_field(name=f"{ctx.author.name}", value=f"Отключил бота от голосового чата по причине: {reason}", inline=True)
        await channel.send(embed=embed1)
    else:
        embed=discord.Embed(title="Ой, подождите...", description="Кажется бот находится на технических работах -_- Пожалуйста подождите окончания технических работ .-.", color=0x007bff)
        await ctx.send(embed=embed)


#проиграть песню
@bot.command()

async def play(ctx, arg):
    if var == 0:
        global vc
        global info
        DiscordComponents(bot)

        try:
            voice_channel = ctx.message.author.voice.channel
            vc = await voice_channel.connect()
        except:
            print('Уже подключен или не удалось подключиться')
            await ctx.voice_client.disconnect()
            

            try:
                voice_channel = ctx.message.author.voice.channel
                vc = await voice_channel.connect()
            except:
                print('Уже подключен или не удалось подключиться')
                await ctx.voice_client.disconnect()
                

            if vc.is_playing():
                print(f'{ctx.message.author.mention}, музыка уже проигрывается, если вы хотите проиграть свою музыку остановите эту песню коммандой #stop')

            else:
                with YoutubeDL(YDL_OPTIONS) as ydl:
                    info = ydl.extract_info(arg, download=False)

                URL = info['formats'][0]['url']

                DiscordComponents(bot)
                vc.play(discord.FFmpegPCMAudio(executable="C:\\ffmpeg\\bin\\ffmpeg.exe", source = URL, **FFMPEG_OPTIONS))
                embed=discord.Embed(title="Nyan cat | Music", color=0x00bfff)
                embed.add_field(name="#stop", value="Остановить песню", inline=False)
                embed.add_field(name="#replay", value="Повторно воспроизвести песню", inline=False)
                await ctx.send(embed=embed,
                    components = [
                            Button(style=ButtonStyle.red, label='Остановить песню', custom_id='stop'),
                            Button(style=ButtonStyle.green, label='Повторить песню', custom_id='replay'),
                        ]
                )
                interaction = await bot.wait_for("button_click", check = lambda i: i.custom_id == "stop")
                await interaction.send(content = "Песня остановлена!")
                interaction = await bot.wait_for("button_click", check = lambda i: i.custom_id == "replay")
                await interaction.send(content = "Песня повторена")
                

                channel = bot.get_channel(987511963913433168)
                embed1=discord.Embed(title="Опа", description="Использование команды #play", color=0x04ff00)
                embed1.add_field(name=f"{ctx.author.name}", value=f"Включил песню {arg}", inline=True)
                
                await channel.send(
                    embed=embed1)
                

                        
                while vc.is_playing():
                    await sleep(1)
                if not vc.is_paused():
                    await vc.disconnect()
                    embed=discord.Embed(title="Nyan cat | Music", color=0x00bfff)
                    embed.add_field(name="Упс", value="Сеанс завершён по причине: Песня остановлена", inline=False)
                    await ctx.send(embed=embed)


        if vc.is_playing():
            print(f'{ctx.message.author.mention}, музыка уже проигрывается, если вы хотите проиграть свою музыку остановите эту песню коммандой #stop')

        else:
            with YoutubeDL(YDL_OPTIONS) as ydl:
                info = ydl.extract_info(arg, download=False)

            URL = info['formats'][0]['url']

            vc.play(discord.FFmpegPCMAudio(executable="C:\\ffmpeg\\bin\\ffmpeg.exe", source = URL, **FFMPEG_OPTIONS))
            embed=discord.Embed(title="Nyan cat | Music", color=0x00bfff)
            embed.add_field(name="#stop", value="Остановить песню", inline=False)
            embed.add_field(name="#replay", value="Повторно воспроизвести песню", inline=False)
            await ctx.send(embed=embed,
                    components = [
                            Button(style=ButtonStyle.red, label='Остановить песню', custom_id='stop'),
                            Button(style=ButtonStyle.green, label='Повторить песню', custom_id='replay'),
                        ]
                )
            interaction = await bot.wait_for("button_click", check = lambda i: i.custom_id == "stop")
            await interaction.send(content = "Песня остановлена!")
            interaction = await bot.wait_for("button_click", check = lambda i: i.custom_id == "replay")
            await interaction.send(content = "Песня повторена")


            channel = bot.get_channel(987511963913433168)
            embed1=discord.Embed(title="Опа", description="Использование команды #play", color=0x04ff00)
            embed1.add_field(name=f"{ctx.author.name}", value=f"Включил песню {arg}", inline=True)
            await channel.send(
                    embed=embed1)
            
            

                    
            while vc.is_playing():
                await sleep(1)
            if not vc.is_paused():
                await vc.disconnect()
                embed=discord.Embed(title="Nyan cat | Music", color=0x00bfff)
                embed.add_field(name="Упс", value="Сеанс завершён по причине: Песня остановлена", inline=False)
                await ctx.send(embed=embed)
    else:
        embed=discord.Embed(title="Ой, подождите...", description="Кажется бот находится на технических работах -_- Пожалуйста подождите окончания технических работ .-.", color=0x007bff)
        await ctx.send(embed=embed)



#проиграть песню
@bot.command()

async def replay(ctx):
    if var == 0:
        global vc
        global info

        try:
            voice_channel = ctx.message.author.voice.channel
            vc = await voice_channel.connect()
        except:
            print('Уже подключен или не удалось подключиться')
            await ctx.voice_client.disconnect()
            

            try:
                voice_channel = ctx.message.author.voice.channel
                vc = await voice_channel.connect()
            except:
                print('Уже подключен или не удалось подключиться')
                await ctx.voice_client.disconnect()
                

            if vc.is_playing():
                print(f'{ctx.message.author.mention}, музыка уже проигрывается, если вы хотите проиграть свою музыку остановите эту песню коммандой #stop')

            else:
                with YoutubeDL(YDL_OPTIONS) as ydl:
                    info = info

                URL = info['formats'][0]['url']

                vc.play(discord.FFmpegPCMAudio(executable="C:\\ffmpeg\\bin\\ffmpeg.exe", source = URL, **FFMPEG_OPTIONS))
                embed=discord.Embed(title="Nyan cat | Music", color=0x00bfff)
                embed.add_field(name="#stop", value="Остановить песню", inline=False)
                embed.add_field(name="#replay", value="Повторно воспроизвести песню", inline=False)
                await ctx.send(embed=embed)
                channel = bot.get_channel(987511963913433168)
                embed1=discord.Embed(title="Опа", description="Использование команды #replay", color=0x04ff00)
                embed1.add_field(name=f"{ctx.author.name}", value=f"Повторил песню", inline=True)
                await channel.send(embed=embed1)

                        
                while vc.is_playing():
                    await sleep(1)
                if not vc.is_paused():
                    await ctx.voice_client.disconnect()
                    embed=discord.Embed(title="Nyan cat | Music", color=0x00bfff)
                    embed.add_field(name="Упс", value="Сеанс завершён по причине: Песня остановлена", inline=False)
                    await ctx.send(embed=embed)


        if vc.is_playing():
            print(f'{ctx.message.author.mention}, музыка уже проигрывается, если вы хотите проиграть свою музыку остановите эту песню коммандой #stop')

        else:
            with YoutubeDL(YDL_OPTIONS) as ydl:
                info = info

            URL = info['formats'][0]['url']

            vc.play(discord.FFmpegPCMAudio(executable="C:\\ffmpeg\\bin\\ffmpeg.exe", source = URL, **FFMPEG_OPTIONS))
            embed=discord.Embed(title="Nyan cat | Music", color=0x00bfff)
            embed.add_field(name="#stop", value="Остановить песню", inline=False)
            embed.add_field(name="#replay", value="Повторно воспроизвести песню", inline=False)
            await ctx.send(embed=embed)
            channel = bot.get_channel(987511963913433168)
            embed1=discord.Embed(title="Опа", description="Использование команды #replay", color=0x04ff00)
            embed1.add_field(name=f"{ctx.author.name}", value=f"Повторил песню", inline=True)
            await channel.send(embed=embed1)

                    
            while vc.is_playing():
                await sleep(1)
            if not vc.is_paused():
                await ctx.voice_client.disconnect()
                embed=discord.Embed(title="Nyan cat | Music", color=0x00bfff)
                embed.add_field(name="Упс", value="Сеанс завершён по причине: Песня остановлена", inline=False)
                await ctx.send(embed=embed)
    else:
        embed=discord.Embed(title="Ой, подождите...", description="Кажется бот находится на технических работах -_- Пожалуйста подождите окончания технических работ .-.", color=0x007bff)
        await ctx.send(embed=embed)

#остановка музыки
@bot.command()

async def stop(ctx):
    if var == 0:
        embed=discord.Embed(title="Nyan cat | Music", color=0x00bfff)
        embed.add_field(name="Упс", value="Песня остановлена!", inline=False)
        await ctx.send(embed=embed)
        await ctx.voice_client.disconnect()
        channel = bot.get_channel(987511963913433168)
        embed1=discord.Embed(title="Опа", description="Использование команды #stop", color=0x04ff00)
        embed1.add_field(name=f"{ctx.author.name}", value=f"Выключил песню (нет подробностей)", inline=True)
        await channel.send(embed=embed1)
    else:
        embed=discord.Embed(title="Ой, подождите...", description="Кажется бот находится на технических работах -_- Пожалуйста подождите окончания технических работ .-.", color=0x007bff)
        await ctx.send(embed=embed)


#справка 
@bot.group(invoke_without_command= True)

async def help(ctx):
    if var == 0:
        embed=discord.Embed(title="Команды бота | Страница 1", color=0x00ffe1)
        embed.set_author(name="Плюха", icon_url="https://lh3.googleusercontent.com/a-/AOh14GgIQrdFuoijR1E5aRlUt029GVLtZEBxOyY8EDBZ-g=s96-c-rg-br100")
        embed.add_field(name="#send_ls (@user) (сообщение)", value="Отправляет сообщение определённому пользователю. Права доступа: Staff, Developer, Президент.", inline=False)
        embed.add_field(name="#clear (кол-во)", value="Удаляет определённое кол-во сообщений. Права доступа: Staff, Developer.", inline=True)
        embed.add_field(name="#кноксбот", value="Фишки. Права доступа: Все, кроме не зарегистрированных серверов и не купивших проходку ", inline=True)
        embed.add_field(name="#необязан", value="Фишки. Права доступа: Все, кроме не зарегистрированных серверов и не купивших проходку ", inline=True)
        embed.add_field(name="#БААААН", value="Фишки. Права доступа: Все, кроме не зарегистрированных серверов и не купивших проходку ", inline=True)
        embed.add_field(name="#собака_серая ", value="Фишки. Права доступа: Все, кроме не зарегистрированных серверов и не купивших проходку ", inline=True)
        embed.add_field(name="#ильяимич", value="Фишки. Права доступа: Все, кроме не зарегистрированных серверов и не купивших проходку ", inline=True)
        embed.add_field(name="#ШЫЫЫШ", value="Фишки. Права доступа: Все, кроме не зарегистрированных серверов и не купивших проходку ", inline=True)
        embed.add_field(name="#да", value="Фишки. Права доступа: Все, кроме не зарегистрированных серверов и не купивших проходку ", inline=True)
        embed.add_field(name="#нет", value="Фишки. Права доступа: Все, кроме не зарегистрированных серверов и не купивших проходку ", inline=True)
        embed.add_field(name="#дурку (@user)", value="Фишки. Права доступа: Все, кроме не зарегистрированных серверов и не купивших проходку ", inline=True)
        embed.add_field(name="#осуждаю (@user)", value="Фишки. Права доступа: Все, кроме не зарегистрированных серверов и не купивших проходку ", inline=True)
        embed.add_field(name="#мьёдик", value="Фишки. Права доступа: Все, кроме не зарегистрированных серверов и не купивших проходку ", inline=True)
        embed.add_field(name="#ДА_ЁЁЁ", value="Фишки. Права доступа: Все, кроме не зарегистрированных серверов и не купивших проходку ", inline=True)
        embed.add_field(name="#БЛИИИИИИИН", value="Фишки. Права доступа: Все, кроме не зарегистрированных серверов и не купивших проходку ", inline=True)
        embed.add_field(name="#say (сообщение в "")", value="Фишки, повторяет сообщение пользователя (ВЕДЁТСЯ ЛОГИРОВАНИЕ!). Права доступа: Все, кроме не зарегистрированных серверов и не купивших проходку ", inline=True)
        embed.add_field(name="#open_source", value="Исходный код бота. Права доступа: Все, кроме не зарегистрированных серверов и не купивших проходку ", inline=True)
        embed.add_field(name="#add_news (текст в "")", value="Отправляет вашу новость на модерацию, после она будет опубликована в газете бота. Права доступа: Все, кроме не зарегистрированных серверов и не купивших проходку ", inline=True)
        embed.add_field(name="#news_rp", value="Газета РП. Права доступа: Все, кроме не зарегистрированных серверов и не купивших проходку ", inline=True)
        embed.add_field(name="#news", value="Общая газета. Права доступа: Все, кроме не зарегистрированных серверов и не купивших проходку ", inline=True)
        embed.add_field(name="#create_command (команда без #) (описание команды)", value="Отправка вашей идеи для команд на модерацию. Права доступа: Все, кроме не зарегистрированных серверов и не купивших проходку ", inline=True)
        embed.add_field(name="#connect", value="Подключение бота к голосовому каналу. Права доступа: Staff, Developer", inline=True)
        embed.add_field(name="#disconnect", value="Отключение бота от голосового канала. Права доступа: Staff, Developer", inline=True)
        embed.add_field(name="#play (URL)", value="Воспроизвести музыку. Права доступа: Все, кроме не зарегистрированных серверов и не купивших проходку ", inline=True)
        embed.add_field(name="#stop", value="Остановить музыку. Права доступа: Все, кроме не зарегистрированных серверов и не купивших проходку ", inline=True)

        embed2=discord.Embed(title="Команды бота | Страница 2", color=0x00ffe1)
        embed2.set_author(name="Плюха", icon_url="https://lh3.googleusercontent.com/a-/AOh14GgIQrdFuoijR1E5aRlUt029GVLtZEBxOyY8EDBZ-g=s96-c-rg-br100")
        embed2.add_field(name="#replay", value="Повторное воспроизведение музыки. Права доступа: Все, кроме не зарегистрированных серверов и не купивших проходку", inline=True)
        embed2.add_field(name="#help", value="Помощь по командам, вы кстати тут. Права доступа: Все, кроме не зарегистрированных серверов и не купивших проходку", inline=True)
        embed2.add_field(name="#playing", value="Установить статус бота: Играет. Права доступа: Все, кроме не зарегистрированных серверов и не купивших проходку", inline=True)
        embed2.add_field(name="#streaming", value="Установить статус бота: Стримит. Права доступа: Все, кроме не зарегистрированных серверов и не купивших проходку", inline=True)
        embed2.add_field(name="#listening", value="Установить статус бота: Слушает. Права доступа: Все, кроме не зарегистрированных серверов и не купивших проходку", inline=True)
        embed2.add_field(name="#watching", value="Установить статус бота: Смотрит. Права доступа: Все, кроме не зарегистрированных серверов и не купивших проходку", inline=True)
        embed2.add_field(name="#my_playing (текст в кавычках)", value="Установить СВОЙ статус бота: Играет. Права доступа: Все, кроме не зарегистрированных серверов и не купивших проходку", inline=True)
        embed2.add_field(name="#my_streaming (текст в кавычках)", value="Установить СВОЙ статус бота: Стримит. Права доступа: Все, кроме не зарегистрированных серверов и не купивших проходку", inline=True)
        embed2.add_field(name="#my_listening (текст в кавычках)", value="Установить СВОЙ статус бота: Слушает. Права доступа: Все, кроме не зарегистрированных серверов и не купивших проходку", inline=True)
        embed2.add_field(name="#my_watching (текст в кавычках)", value="Установить СВОЙ статус бота: Смотрит. Права доступа: Все, кроме не зарегистрированных серверов и не купивших проходку", inline=True)
        
        embed3=discord.Embed(title="Команды бота | Страница 3", color=0x00ffe1)
        embed3.set_author(name="Плюха", icon_url="https://lh3.googleusercontent.com/a-/AOh14GgIQrdFuoijR1E5aRlUt029GVLtZEBxOyY8EDBZ-g=s96-c-rg-br100")
        embed3.add_field(name="#upload (прикрепите файл размером меньше 8 мб)", value="Загружает файл на сервер по адресу: C:\Files\(файл в расширением). Права доступа: Все, кроме не зарегистрированных серверов и не купивших проходку", inline=True)
        embed3.add_field(name="#download (адрес файла)", value="Скачать файл с сервера например: #download C:\Files\YT.rar. Права доступа: Все, кроме не зарегистрированных серверов и не купивших проходку", inline=True)
        embed3.add_field(name="#dir", value="Просматривает все доступные для скачивания файлы по адресу C:\Files\. Права доступа: Все, кроме не зарегистрированных серверов и не купивших проходку", inline=True)
        embed3.add_field(name="#notepad (текст (можно использовать множество строк))", value="Создаёт txt файл из вашего сообщения. Права доступа: Все, кроме не зарегистрированных серверов и не купивших проходку", inline=True)
        embed3.set_footer(text="Как вам список? Дата написания списка команд: 21.06.2022 23:07")
        await ctx.send(embed=embed)
        await ctx.send(embed=embed2)
        help = await ctx.send(embed=embed3)
        await help.add_reaction("👍")
        await help.add_reaction("👎")
    else:
        embed3=discord.Embed(title="Ой, подождите...", description="Кажется бот находится на технических работах -_- Пожалуйста подождите окончания технических работ .-. Но я могу загрузить вам список команд из резерва", color=0x007bff)
        await ctx.send(embed=embed3)
        embed=discord.Embed(title="Команды бота | Страница 1", color=0x00ffe1)
        embed.set_author(name="Плюха", icon_url="https://lh3.googleusercontent.com/a-/AOh14GgIQrdFuoijR1E5aRlUt029GVLtZEBxOyY8EDBZ-g=s96-c-rg-br100")
        embed.add_field(name="#send_ls (@user) (сообщение)", value="Отправляет сообщение определённому пользователю. Права доступа: Staff, Developer, Президент.", inline=False)
        embed.add_field(name="#clear (кол-во)", value="Удаляет определённое кол-во сообщений. Права доступа: Staff, Developer.", inline=True)
        embed.add_field(name="#кноксбот", value="Фишки. Права доступа: Все, кроме не зарегистрированных серверов и не купивших проходку ", inline=True)
        embed.add_field(name="#необязан", value="Фишки. Права доступа: Все, кроме не зарегистрированных серверов и не купивших проходку ", inline=True)
        embed.add_field(name="#БААААН", value="Фишки. Права доступа: Все, кроме не зарегистрированных серверов и не купивших проходку ", inline=True)
        embed.add_field(name="#собака_серая ", value="Фишки. Права доступа: Все, кроме не зарегистрированных серверов и не купивших проходку ", inline=True)
        embed.add_field(name="#ильяимич", value="Фишки. Права доступа: Все, кроме не зарегистрированных серверов и не купивших проходку ", inline=True)
        embed.add_field(name="#ШЫЫЫШ", value="Фишки. Права доступа: Все, кроме не зарегистрированных серверов и не купивших проходку ", inline=True)
        embed.add_field(name="#да", value="Фишки. Права доступа: Все, кроме не зарегистрированных серверов и не купивших проходку ", inline=True)
        embed.add_field(name="#нет", value="Фишки. Права доступа: Все, кроме не зарегистрированных серверов и не купивших проходку ", inline=True)
        embed.add_field(name="#дурку (@user)", value="Фишки. Права доступа: Все, кроме не зарегистрированных серверов и не купивших проходку ", inline=True)
        embed.add_field(name="#осуждаю (@user)", value="Фишки. Права доступа: Все, кроме не зарегистрированных серверов и не купивших проходку ", inline=True)
        embed.add_field(name="#мьёдик", value="Фишки. Права доступа: Все, кроме не зарегистрированных серверов и не купивших проходку ", inline=True)
        embed.add_field(name="#ДА_ЁЁЁ", value="Фишки. Права доступа: Все, кроме не зарегистрированных серверов и не купивших проходку ", inline=True)
        embed.add_field(name="#БЛИИИИИИИН", value="Фишки. Права доступа: Все, кроме не зарегистрированных серверов и не купивших проходку ", inline=True)
        embed.add_field(name="#say (сообщение в "")", value="Фишки, повторяет сообщение пользователя (ВЕДЁТСЯ ЛОГИРОВАНИЕ!). Права доступа: Все, кроме не зарегистрированных серверов и не купивших проходку ", inline=True)
        embed.add_field(name="#open_source", value="Исходный код бота. Права доступа: Все, кроме не зарегистрированных серверов и не купивших проходку ", inline=True)
        embed.add_field(name="#add_news (текст в "")", value="Отправляет вашу новость на модерацию, после она будет опубликована в газете бота. Права доступа: Все, кроме не зарегистрированных серверов и не купивших проходку ", inline=True)
        embed.add_field(name="#news_rp", value="Газета РП. Права доступа: Все, кроме не зарегистрированных серверов и не купивших проходку ", inline=True)
        embed.add_field(name="#news", value="Общая газета. Права доступа: Все, кроме не зарегистрированных серверов и не купивших проходку ", inline=True)
        embed.add_field(name="#create_command (команда без #) (описание команды)", value="Отправка вашей идеи для команд на модерацию. Права доступа: Все, кроме не зарегистрированных серверов и не купивших проходку ", inline=True)
        embed.add_field(name="#connect", value="Подключение бота к голосовому каналу. Права доступа: Staff, Developer", inline=True)
        embed.add_field(name="#disconnect", value="Отключение бота от голосового канала. Права доступа: Staff, Developer", inline=True)
        embed.add_field(name="#play (URL)", value="Воспроизвести музыку. Права доступа: Все, кроме не зарегистрированных серверов и не купивших проходку ", inline=True)
        embed.add_field(name="#stop", value="Остановить музыку. Права доступа: Все, кроме не зарегистрированных серверов и не купивших проходку ", inline=True)

        embed2=discord.Embed(title="Команды бота | Страница 2", color=0x00ffe1)
        embed2.set_author(name="Плюха", icon_url="https://lh3.googleusercontent.com/a-/AOh14GgIQrdFuoijR1E5aRlUt029GVLtZEBxOyY8EDBZ-g=s96-c-rg-br100")
        embed2.add_field(name="#replay", value="Повторное воспроизведение музыки. Права доступа: Все, кроме не зарегистрированных серверов и не купивших проходку", inline=True)
        embed2.add_field(name="#help", value="Помощь по командам, вы кстати тут. Права доступа: Все, кроме не зарегистрированных серверов и не купивших проходку", inline=True)
        embed2.add_field(name="#playing", value="Установить статус бота: Играет. Права доступа: Все, кроме не зарегистрированных серверов и не купивших проходку", inline=True)
        embed2.add_field(name="#streaming", value="Установить статус бота: Стримит. Права доступа: Все, кроме не зарегистрированных серверов и не купивших проходку", inline=True)
        embed2.add_field(name="#listening", value="Установить статус бота: Слушает. Права доступа: Все, кроме не зарегистрированных серверов и не купивших проходку", inline=True)
        embed2.add_field(name="#watching", value="Установить статус бота: Смотрит. Права доступа: Все, кроме не зарегистрированных серверов и не купивших проходку", inline=True)
        embed2.add_field(name="#my_playing (текст в кавычках)", value="Установить СВОЙ статус бота: Играет. Права доступа: Все, кроме не зарегистрированных серверов и не купивших проходку", inline=True)
        embed2.add_field(name="#my_streaming (текст в кавычках)", value="Установить СВОЙ статус бота: Стримит. Права доступа: Все, кроме не зарегистрированных серверов и не купивших проходку", inline=True)
        embed2.add_field(name="#my_listening (текст в кавычках)", value="Установить СВОЙ статус бота: Слушает. Права доступа: Все, кроме не зарегистрированных серверов и не купивших проходку", inline=True)
        embed2.add_field(name="#my_watching (текст в кавычках)", value="Установить СВОЙ статус бота: Смотрит. Права доступа: Все, кроме не зарегистрированных серверов и не купивших проходку", inline=True)
        
        embed3=discord.Embed(title="Команды бота | Страница 3", color=0x00ffe1)
        embed3.set_author(name="Плюха", icon_url="https://lh3.googleusercontent.com/a-/AOh14GgIQrdFuoijR1E5aRlUt029GVLtZEBxOyY8EDBZ-g=s96-c-rg-br100")
        embed3.add_field(name="#upload (прикрепите файл размером меньше 8 мб)", value="Загружает файл на сервер по адресу: C:\Files\(файл в расширением). Права доступа: Все, кроме не зарегистрированных серверов и не купивших проходку", inline=True)
        embed3.add_field(name="#download (адрес файла)", value="Скачать файл с сервера например: #download C:\Files\YouTube.rar", inline=True)
        embed3.add_field(name="#dir", value="Просматривает все доступные для скачивания файлы по адресу C:\Files\. Права доступа: Все, кроме не зарегистрированных серверов и не купивших проходку", inline=True)
        embed3.add_field(name="#notepad (текст (можно использовать множество строк))", value="Создаёт txt файл из вашего сообщения. Права доступа: Все, кроме не зарегистрированных серверов и не купивших проходку", inline=True)
        embed3.set_footer(text="Как вам список? Дата написания списка команд: 21.06.2022 23:07")
        await ctx.send(embed=embed)
        await ctx.send(embed=embed2)
        help = await ctx.send(embed=embed3)
        await help.add_reaction("👍")
        await help.add_reaction("👎")

















































































































































































































































bot.run(settings['token'])