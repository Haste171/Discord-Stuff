from selenium import webdriver
import colorama
import os
from colorama import Fore, Style, Back, init
init(convert=True)
os.system('mode 60,12')
print(f"""{Style.BRIGHT}{Fore.BLUE}
   _____     _                _                _       
  |_   _|__ | | _____ _ __   | |    ___   __ _(_)_ __  
    | |/ _ \| |/ / _ \ '_ \  | |   / _ \ / _` | | '_ \  {Style.NORMAL}{Fore.BLUE}
    | | (_) |   <  __/ | | | | |__| (_) | (_| | | | | | 
    |_|\___/|_|\_\___|_| |_| |_____\___/ \__, |_|_| |_|
                                         |___/    
{Style.BRIGHT}
     ----------------- Made by Haste -----------------   
{Fore.RESET}{Style.NORMAL}
""")
token = input('Enter Token: ')
profile = webdriver.FirefoxProfile()
profile.set_preference("general.useragent.override", 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) discord/0.0.305 Chrome/69.0.3497.128 Electron/4.0.8 Safari/537.36')
driver = webdriver.Firefox(profile)
script = """
        function login(token) {
        setInterval(() => {
        document.body.appendChild(document.createElement `iframe`).contentWindow.localStorage.token = `"${token}"`
        }, 50);
        setTimeout(() => {
        location.reload();
        }, 2500);
        }
        """
driver.get("https://canary.discordapp.com/login")
driver.execute_script(script+f'\nlogin("{token}")')
