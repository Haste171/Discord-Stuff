# Discord selfbot that cycles through your statuses even if your not on the actual client. (Preferably used to host a status)

import discord
import json
import asyncio
import colorama
import random
import os
from itertools import cycle
from discord.ext import commands, tasks
from colorama import Fore, Back, Style

colorama.init()

with open('./config.json') as f:
    config = json.load(f)
    
token = config.get('token')
status1 = config.get('status1')
status2 = config.get('status2')
ver = 'v1.0'
prefix='289342w93uh5n' # ignore ( i got lazy)
bot = commands.Bot(description="Status Changing Selfbot", command_prefix=prefix, self_bot=True)

def setSize():
    os.system('mode 75,24')
setSize()

@bot.event
async def on_ready():
    print(f"""
{Fore.RED}
{Style.BRIGHT}            ███████╗████████╗ █████╗ ████████╗██╗   ██╗███████╗
{Style.BRIGHT}            ██╔════╝╚══██╔══╝██╔══██╗╚══██╔══╝██║   ██║██╔════╝
{Style.NORMAL}            ███████╗   ██║   ███████║   ██║   ██║   ██║███████╗
{Style.NORMAL}            ╚════██║   ██║   ██╔══██║   ██║   ██║   ██║╚════██║
{Style.BRIGHT}            ███████║   ██║   ██║  ██║   ██║   ╚██████╔╝███████║
{Style.BRIGHT}            ╚══════╝   ╚═╝   ╚═╝  ╚═╝   ╚═╝    ╚═════╝ ╚══════╝
                                                            
{Style.NORMAL}                    ██╗      ██████╗  ██████╗ ██████╗          
{Style.NORMAL}                    ██║     ██╔═══██╗██╔═══██╗██╔══██╗         
{Style.BRIGHT}                    ██║     ██║   ██║██║   ██║██████╔╝         
{Style.BRIGHT}                    ██║     ██║   ██║██║   ██║██╔═══╝          
{Style.NORMAL}                    ███████╗╚██████╔╝╚██████╔╝██║              
{Style.NORMAL}                    ╚══════╝ ╚═════╝  ╚═════╝ ╚═╝     

{Fore.BLUE}{Style.BRIGHT}                  ═════════════════════════════════  
                  
{Fore.WHITE}                            User: {Style.NORMAL}{Fore.BLUE}{bot.user.name}#{bot.user.discriminator}{Fore.RESET}
{Fore.WHITE}                            Version: {Style.NORMAL}{Fore.BLUE}{ver}{Fore.RESET}{Style.BRIGHT}
{Fore.GREEN}                               Running! {Style.NORMAL}{Style.BRIGHT}     

{Fore.BLUE}                  ═════════════════════════════════ 
    """)
    bot.status = cycle([status1, status2])
    changer.start()

@tasks.loop(seconds=10)
async def changer():
    await bot.wait_until_ready()
    await bot.change_presence(activity=discord.Game(name=next(bot.status)))

bot.run(token, bot=False)
