from http import client
from msilib.schema import Icon
from multiprocessing import Manager
from multiprocessing.connection import Client
import discord
from discord.ext import commands
from config import settings
from discord.ext import commands
from discord.ext import commands, tasks
from discord.ext.commands import Bot
from discord import member
from discord.utils import get

bot = commands.Bot(command_prefix = settings['prefix'])

chat = None

@bot.event

async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound ):
        await ctx.send(embed = discord.Embed(description = f'** {ctx.author.name}, данной команды не существует, попробуй перепроверить свою введённую команду, и отправь её снова.**', color=0xFF0000))




#установить статус бота играет в
@bot.command()
@commands.has_any_role(929030139159924736)
async def playing(ctx):
    activity = discord.Game(name="!help | Вирус MEMZ")
    await bot.change_presence(status=discord.Status.idle, activity=activity)
    print("Успешно!")

    embed = discord.Embed(
        title = 'Успешно!',
        description = 'Статус бота изменён на: Играет!',
        colour = discord.Colour.from_rgb(0, 255, 0)
    )
    await ctx.send(embed = embed) # Отправляем Embed
    
@playing.error
async def test_error(ctx, error):
    if isinstance(error, commands.errors.MissingAnyRole):
        embed = discord.Embed(
            title = 'Ошибка!',
            description = 'К сожалению у вас нет прав на использование данной команды.',
            colour = discord.Colour.from_rgb(255, 0, 0)
        )
        await ctx.send(embed = embed) # Отправляем Embed

#установить статус бота стримит
@bot.command()
@commands.has_any_role(929030139159924736)
async def streaming(ctx):
    activity = discord.Streaming(name="!help | Ждёмс стрима люди", url="https://twitch.tv/adminkinlvs")
    await bot.change_presence(status=discord.Status.idle, activity=activity)
    print("Успешно!")

    embed = discord.Embed(
        title = 'Успешно!',
        description = 'Статус бота изменён на: Стримит!',
        colour = discord.Colour.from_rgb(0, 255, 0)
    )
    await ctx.send(embed = embed) # Отправляем Embed
    
@playing.error
async def test_error(ctx, error):
    if isinstance(error, commands.errors.MissingAnyRole):
        embed = discord.Embed(
            title = 'Ошибка!',
            description = 'К сожалению у вас нет прав на использование данной команды.',
            colour = discord.Colour.from_rgb(255, 0, 0)
        )
        await ctx.send(embed = embed) # Отправляем Embed

#установить статус бота слушает
@bot.command()
@commands.has_any_role(929030139159924736)
async def listening(ctx):
    activity = discord.Activity(type=discord.ActivityType.listening, name="!help | Imagine Dragons - Believer")
    await bot.change_presence(status=discord.Status.idle, activity=activity)
    print("Успешно!")

    embed = discord.Embed(
        title = 'Успешно!',
        description = 'Статус бота изменён на: Слушает!',
        colour = discord.Colour.from_rgb(0, 255, 0)
    )
    await ctx.send(embed = embed) # Отправляем Embed
    
@playing.error
async def test_error(ctx, error):
    if isinstance(error, commands.errors.MissingAnyRole):
        embed = discord.Embed(
            title = 'Ошибка!',
            description = 'К сожалению у вас нет прав на использование данной команды.',
            colour = discord.Colour.from_rgb(255, 0, 0)
        )
        await ctx.send(embed = embed) # Отправляем Embed

#установить статус бота смотрит
@bot.command()
@commands.has_any_role(929030139159924736)
async def watching(ctx):
    activity = discord.Activity(type=discord.ActivityType.watching, name="!help | HFM - Как приготовить кокосовый рулет")
    await bot.change_presence(status=discord.Status.idle, activity=activity)
    print("Успешно!")

    embed = discord.Embed(
        title = 'Успешно!',
        description = 'Статус бота изменён на: Смотрит!',
        colour = discord.Colour.from_rgb(0, 255, 0)
    )
    await ctx.send(embed = embed) # Отправляем Embed
    
@playing.error
async def test_error(ctx, error):
    if isinstance(error, commands.errors.MissingAnyRole):
        embed = discord.Embed(
            title = 'Ошибка!',
            description = 'К сожалению у вас нет прав на использование данной команды.',
            colour = discord.Colour.from_rgb(255, 0, 0)
        )
        await ctx.send(embed = embed) # Отправляем Embed





#отправка сообщения в лс пользователю
@bot.command()
@commands.has_any_role(929030139159924736, 913979911411236935)
async def send_ls(ctx, member: discord.Member, message):
    await member.send(f'{message} - это сообщение вам отправил {ctx.author.mention}')

@send_ls.error
async def test_error(ctx, error):
    if isinstance(error, commands.errors.MissingAnyRole):
        embed = discord.Embed(
            title = 'Ошибка!',
            description = 'К сожалению у вас нет прав на использование данной команды.',
            colour = discord.Colour.from_rgb(255, 0, 0)
        )
        await ctx.send(embed = embed) # Отправляем Embed

#кноксбот
@bot.command()
async def кноксбот(ctx):
    embed = discord.Embed(
        title = '...',
        description = 'Да',
        colour = discord.Colour.from_rgb(0, 255, 0)
    )
    await ctx.send(embed = embed) # Отправляем Embed


#размут
@bot.command()
@commands.has_any_role(929030139159924736,913979911411236935)
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
@commands.has_any_role(929030139159924736,913979911411236935)
async def clear( ctx, amouth = 10 ):
    await ctx.channel.purge( limit = amouth )
    embed = discord.Embed(
        title = 'Очистка чата',
        description = f'**Чат** был **очищен** пользователем ***{ ctx.message.author.mention }***.',
        colour = discord.Colour.from_rgb(50, 200, 5)
    )
    await ctx.send(embed = embed)
    await ctx.channel.purge( limit = 2 )

@clear.error
async def test_error(ctx, error):
    if isinstance(error, commands.errors.MissingAnyRole):
        embed = discord.Embed(
            title = 'Ошибка!',
            description = 'К сожалению у вас нет прав на использование данной команды.',
            colour = discord.Colour.from_rgb(255, 0, 0)
        )
        await ctx.send(embed = embed) # Отправляем Embed

#мут
@bot.command()
@commands.has_any_role(929030139159924736,913979911411236935)
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

@mute.error
async def test_error(ctx, error):
    if isinstance(error, commands.errors.MissingAnyRole):
        embed = discord.Embed(
            title = 'Ошибка!',
            description = 'К сожалению у вас нет прав на использование данной команды.',
            colour = discord.Colour.from_rgb(255, 0, 0)
        )
        await ctx.send(embed = embed) # Отправляем Embed

#необязан
@bot.command()
async def необязан(ctx):
    embed = discord.Embed(
        title = 'Вы Фрайз?',
        description = 'Это любимое слово фрайза, теперь вы НЕОБЯЗАНЫ',
        colour = discord.Colour.from_rgb(0, 255, 0)
    )
    await ctx.send(embed = embed) # Отправляем Embed

#БААААН
@bot.command()
async def БААААН(ctx):
    embed = discord.Embed(
        title = 'Вы плохо себя ведете на сьемках?',
        description = 'ЗНАЧИТ ВАМ БАААААААН',
        colour = discord.Colour.from_rgb(0, 255, 0)
    )
    await ctx.send(embed = embed) # Отправляем Embed

#собака_серая
@bot.command()
async def собака_серая(ctx):
    embed = discord.Embed(
        title = 'Шо то на китайском',
        description = 'Ах ты собака серая',
        colour = discord.Colour.from_rgb(0, 255, 0)
    )
    await ctx.send(embed = embed) # Отправляем Embed

#илья_и_мич
@bot.command()
async def ильяимич(ctx):
    embed = discord.Embed(
        title = 'Что?',
        description = 'Что Илья с Мичём делали в туалете?',
        colour = discord.Colour.from_rgb(0, 255, 0)
    )
    await ctx.send(embed = embed) # Отправляем Embed

#ШЫЫЫШ
@bot.command()
async def ШЫЫЫШ( ctx ):
    embed = discord.Embed(
        title = 'ШЫЫЫЫЫЫЫЫЫЫЫЫШ',
        description = '**Это любимая фраза Ластика :)**',
        colour = discord.Colour.from_rgb( 50, 200, 5 )
    )
    await ctx.send( embed = embed )

#да
@bot.command()
async def да( ctx ):
    embed = discord.Embed(
        title = 'ДА',
        description = '**Провода**',
        colour = discord.Colour.from_rgb( 50, 200, 5 )
    )
    await ctx.send( embed = embed )

#нет
@bot.command()
async def нет( ctx ):
    embed = discord.Embed(
        title = 'НЕТ',
        description = '**Мопед**',
        colour = discord.Colour.from_rgb( 50, 200, 5 )
    )
    await ctx.send( embed = embed )

#бан
@bot.command()
@commands.has_any_role(929030139159924736)
async def ban(ctx, member : discord.Member, *, reason = "На вас наложили великую печать бана!"):
    embed = discord.Embed(
        title = 'Успешно!',
        description = f'Пользователь **{member}** был заблокирован навсегда по причине: **{reason}**',
        colour = discord.Colour.from_rgb( 50, 200, 5 )
    )
    await ctx.send( embed = embed )
    await member.ban(reason = reason)

#кик
@bot.command()
@commands.has_any_role(929030139159924736)
async def kick(ctx, member: discord.Member, *, reason=None):
    embed = discord.Embed(
        title = 'Успешно!',
        description = f'Пользователь **{member}** был кикнут с сервера по причине: **{reason}**',
        colour = discord.Colour.from_rgb( 50, 200, 5 )
    )
    await ctx.send( embed = embed )
    await member.kick(reason=reason)
    
#дурку
@bot.command()
async def дурку( ctx, member = discord.member ):
    embed = discord.Embed(
        title = 'Вызывали дурку?',
        description = f'Вызываем дурку {member}',
        colour = discord.Colour.from_rgb( 50, 200, 5 )
    )
    await ctx.send( embed = embed )

@bot.command()
async def open_source(ctx):
    embed = discord.Embed(
        title = 'Исходный код уже доступен!',
        description = f'Скачать исходный код бота можно на сайте: https://github.com/dmitriykotik/bot_nyan_cat',
        colour = discord.Colour.from_rgb( 50, 200, 5 )
    )
    await ctx.send( embed = embed )




#команды Sudo
@bot.command()
async def sudo_send_ls(ctx, passwd, member: discord.Member, message):
    if passwd == "****":
        await member.send(f'{message} - это сообщение вам отправил {ctx.author.mention}')
    else:
        mute_role = discord.utils.get( ctx.message.guild.roles, name = 'Топовая Свинка' )
        await ctx.message.author.add_roles( mute_role )
        await ctx.send("Неверный пароль!")
        await ctx.send(f"За попытку взлома {ctx.message.author.mention} будет Топовой свинкой! :)")

@bot.command()
async def sudo_clear(ctx, passwd, amouth = 10):
    if passwd == "****":
        await ctx.channel.purge( limit = amouth )
        embed = discord.Embed(
            title = 'Очистка чата',
            description = f'**Чат** был **очищен** пользователем ***{ ctx.message.author.mention }*** через пользователя root.',
            colour = discord.Colour.from_rgb(50, 200, 5)
        )
        await ctx.send(embed = embed)
        await ctx.channel.purge( limit = 2 )
    else:
        mute_role = discord.utils.get( ctx.message.guild.roles, name = 'Топовая Свинка' )
        await ctx.message.author.add_roles( mute_role )
        await ctx.send("Неверный пароль!")
        await ctx.send(f"За попытку взлома {ctx.message.author.mention} будет Топовой свинкой! :)")

@bot.command()
async def sudo_mute(ctx, passwd, member: discord.Member, reason = 'без причины'):
    if passwd == "****":
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

    else:
        mute_role = discord.utils.get( ctx.message.guild.roles, name = 'Топовая Свинка' )
        await ctx.message.author.add_roles( mute_role )
        await ctx.send("Неверный пароль!")
        await ctx.send(f"За попытку взлома {ctx.message.author.mention} будет Топовой свинкой! :)")

@bot.command()
async def sudo_unmute(ctx, passwd, member: discord.Member):
    if passwd == "****":
        
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
    else:
        mute_role = discord.utils.get( ctx.message.guild.roles, name = 'Топовая Свинка' )
        await ctx.message.author.add_roles( mute_role )
        await ctx.send("Неверный пароль!")
        await ctx.send(f"За попытку взлома {ctx.message.author.mention} будет Топовой свинкой! :)")

























































































































































































































































bot.run(settings['token'])
