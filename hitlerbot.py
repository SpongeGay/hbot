import discord
from discord.ext.commands import Bot
from discord.ext import commands
import asyncio
import time
import random
from discord import Game


Client = discord.client
client = commands.Bot(command_prefix = '!')
Clientdiscord = discord.Client()


@client.event
async def on_member_join(member):
    await client.change_presence(game=Game(name='h!help'))
    await client.send_message(member, 'Its Me Legendary Nazi Hitler')
    print('Sent message to ' + member.name)
async def on_ready():
    await client.change_presence(game=Game(name='      '))
    print('Ready, Freddy') 


@client.event
async def on_message(message):
    if message.content == 'h!isstalingay':
        await client.send_message(message.channel,'Hes 100% gay communist')
    if message.content == 'h!invite':
        await client.send_message(message.channel,'https://discordapp.com/api/oauth2/authorize?client_id=504598858500931585&permissions=0&redirect_uri=https%3A%2F%2Fdiscordapp.com%2Foauth2%2Fauthorize%3Fclient_id%3D503174689175240715scope%3Dbot&scope=bot')
    if message.content == 'h!srvinvite':
        await client.send_message(message.channel,'https://discord.gg/guEQ92')
    if message.content.startswith('h!ping'):
        await client.send_message(message.channel,'Nazis Ping Run <@%s> :gun:'  %(message.author.id))
    if message.content == 'h!berlinsfear':
        em = discord.Embed(description='')
        em.set_image(url='https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSvKoZSJgTBd2ZZy5-m5X0Qb6qnrbLi6UcXMqbFtqEY0zCk0ymobA')
        await client.send_message(message.channel, embed=em)
    if message.content == 'h!help':
        await client.send_message(message.channel,'```This Bot Is Aplha So Heres Some Commands:h!berlinsfear,h!isstalingay,h!germaninsult,h!ping,h!invite,h!srvinvite```')
client.run('NTA0NTk4ODU4NTAwOTMxNTg1.DrHX-Q.8n9xGtHg5zhluRGMK_TtenqVhgU')
