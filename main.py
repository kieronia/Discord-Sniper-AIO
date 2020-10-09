from discord.ext import commands
import discord,re,requests,os,datetime,time,random,sys,asyncio
from colorama import Fore, init, Style
from configparser import ConfigParser
import pyPrivnote as pn



init(convert = True)

os.system("title ////Fibre Sniper////")
config = ConfigParser()
config.read('config.ini')
token = config.get('SETTINGS', 'token')
token = token.replace('"', "")

nitro = config.get('SETTINGS', 'nitro')
giveaway = config.get('SETTINGS', 'giveaway')
privnote = config.get('SETTINGS', 'privnote')
pastebin = config.get('SETTINGS', 'pastebin')


nitro = nitro.lower()
giveaway = giveaway.lower()
privnote = privnote.lower()
pastebin = pastebin.lower()

if nitro == "yes" or nitro == "true":
    nitro = "On"
elif nitro == "no" or nitro == "false":
    nitro = "Off"
else:
    nitro = "Invalid Option!"

if giveaway == "yes" or giveaway == "true":
    giveaway = "On"
elif giveaway == "no" or giveaway == "false":
    giveaway = "Off"
else:
    giveaway = "Invalid Option!"

if privnote == "yes" or privnote == "true":
    privnote = "On"
elif privnote == "no" or privnote == "false":
    privnote = "Off"
else:
    privnote = "Invalid Option!"


if pastebin == "yes" or pastebin == "true":
    pastebin = "On"
elif pastebin == "no" or pastebin == "false":
    pastebin = "Off"
else:
    pastebin = "Invalid Option!"



def faketype(words):
  words
  for char in words:
    time.sleep(random.choice([0.03]))
    sys.stdout.write(char)
    sys.stdout.flush()
  time.sleep(1)
os.system("cls")
print(Fore.GREEN)
faketype(f"[+] Loading uppp!\n{Fore.CYAN}[!] Nitro Status : {Fore.YELLOW}{nitro}\n{Fore.CYAN}[!] Giveaway Status : {Fore.YELLOW}{giveaway}\n{Fore.CYAN}[!] Privnote Status : {Fore.YELLOW}{privnote}\n{Fore.CYAN}[!] Pastebin Status : {Fore.YELLOW}{pastebin}")#cool animation to pass up the time :shrug:
time.sleep(0.4)
faketype("....")



bot = commands.Bot(command_prefix=".", self_bot=True)
 

@bot.event
async def on_connect():
    os.system("cls")
    print(f"""{Fore.CYAN}
        ███████╗██╗██████╗ ██████╗ ███████╗          
        ██╔════╝██║██╔══██╗██╔══██╗██╔════╝          
        █████╗  ██║██████╔╝██████╔╝█████╗            
        ██╔══╝  ██║██╔══██╗██╔══██╗██╔══╝            
        ██║     ██║██████╔╝██║  ██║███████╗          
        ╚═╝     ╚═╝╚═════╝ ╚═╝  ╚═╝╚══════╝          
                                             
        ███████╗███╗   ██╗██╗██████╗ ███████╗██████╗ 
        ██╔════╝████╗  ██║██║██╔══██╗██╔════╝██╔══██╗
        ███████╗██╔██╗ ██║██║██████╔╝█████╗  ██████╔╝
        ╚════██║██║╚██╗██║██║██╔═══╝ ██╔══╝  ██╔══██╗
        ███████║██║ ╚████║██║██║     ███████╗██║  ██║
        ╚══════╝╚═╝  ╚═══╝╚═╝╚═╝     ╚══════╝╚═╝  ╚═╝
        [{Fore.WHITE}+{Fore.CYAN}] Sniping on acct {Fore.WHITE}: {Fore.GREEN}{bot.user.name}

        {Fore.YELLOW}[{Fore.WHITE}!{Fore.YELLOW}] Nitroooo Status {Fore.WHITE}: {Fore.MAGENTA}{nitro}
        {Fore.YELLOW}[{Fore.WHITE}!{Fore.YELLOW}] Giveaway Status {Fore.WHITE}: {Fore.MAGENTA}{giveaway}
        {Fore.YELLOW}[{Fore.WHITE}!{Fore.YELLOW}] Privnote Status {Fore.WHITE}: {Fore.MAGENTA}{privnote}
        {Fore.YELLOW}[{Fore.WHITE}!{Fore.YELLOW}] Pastebin Status {Fore.WHITE}: {Fore.MAGENTA}{pastebin}{Fore.RESET}
        
    """)#write all trues and falses of each snipe type

@bot.event
async def on_message(ctx):
    if nitro == "On":
        if 'discord.gift' in ctx.content: 
            nitrotext = open("nitrolog.txt","a") 
            code = re.search("discord.gift/(.*)", ctx.content).group(1)
            currentDT = datetime.datetime.now()
            hour = str(currentDT.hour)
            minute = str(currentDT.minute)
            second = str(currentDT.second)
            try:
                print(f"{Fore.WHITE}[{Fore.CYAN}!{Fore.WHITE}] {hour}:{minute}:{second}{Fore.YELLOW} Nitro Found! // Server: {ctx.guild.name} // Channel: {ctx.channel.name} // Sent By: {ctx.author.name}#{ctx.author.discriminator}")
                nitrotext.write(f"[!] Nitro Found! // Server: {ctx.guild.name} // Channel: {ctx.channel.name} // Sent By: {ctx.author.name}#{ctx.author.discriminator} -- {hour}:{minute}:{second}\n")
            except:
                print(f"{Fore.WHITE}[{Fore.CYAN}!{Fore.WHITE}] {hour}:{minute}:{second} {Fore.YELLOW}Nitro Found! // Sent By: {ctx.author.name}#{ctx.author.discriminator}")
                nitrotext.write(f"[!] Nitro Found! Sent By: {ctx.author.name}#{ctx.author.discriminator} -- {hour}:{minute}:{second}\n")
            if len(code) == 24 or len(code) == 16:
                print(f"{Fore.WHITE}[{Fore.GREEN}+{Fore.WHITE}] {hour}:{minute}:{second}{Fore.GREEN} Testing code : discord.gift/{code}")
                r = requests
                result = r.post('https://discordapp.com/api/v6/entitlements/gift-codes/'+code+'/redeem', json={"channel_id":str(ctx.channel.id)}, headers={'authorization':token}).text
                code = re.search("discord.gift/(.*)", ctx.content).group(1)
                currentDT = datetime.datetime.now()
                hour = str(currentDT.hour)
                minute = str(currentDT.minute)
                second = str(currentDT.second)
                if 'this gift has been redeemed already.' in result.lower():
                    print(f"{Fore.WHITE}[{Fore.RED}-{Fore.WHITE}] {hour}:{minute}:{second}{Fore.RED} Already Claimed Code : discord.gift/{code}")
                    nitrotext.write(f"[-] discord.gift/{code} Has already been claimed -- {hour}:{minute}:{second}\n")
                elif 'nitro' in result.lower():
                    print(f"{Fore.WHITE}[{Fore.GREEN}+{Fore.WHITE}] {hour}:{minute}:{second}{Fore.GREEN} SNIPED Code : discord.gift/{code}")
                    nitrotext.write(f"[+] discord.gift/{code} WAS SNIPED!!! -- {hour}:{minute}:{second}\n")
                elif 'unknown gift code' in result.lower():
                    print(f"{Fore.WHITE}[{Fore.RED}-{Fore.WHITE}] {hour}:{minute}:{second} {Fore.RED}Invalid Code : discord.gift/{code}")
                    nitrotext.write(f"[-] discord.gift/{code} Was an invalid code -- {hour}:{minute}:{second}\n")
            else:
                print(f"{Fore.WHITE}[{Fore.RED}-{Fore.WHITE}] {hour}:{minute}:{second}{Fore.RED} Fake Code : discord.gift/{code}")
                nitrotext.write(f"[-] discord.gift/{code} Was a fake code -- {hour}:{minute}:{second}\n") 
            nitrotext.close()
    if privnote == "On":
        if 'pastebin' in ctx.content: #while it cant exactly be "sniped" - people still drop stuff in pastebin from time to time that you might not see , depending on whether its a method or sum, still usefull to have imo
        
            code = re.search("pastebin.com/(.*)", ctx.content).group(1) 
            currentDT = datetime.datetime.now()
            hour = str(currentDT.hour)
            minute = str(currentDT.minute)
            second = str(currentDT.second)
            try:
                print(f"{Fore.WHITE}[{Fore.CYAN}!{Fore.WHITE}] {hour}:{minute}:{second} {Fore.YELLOW}Pastebin Found! // Server: {ctx.guild.name} // Channel: {ctx.channel.name} // Sent By: {ctx.author.name}#{ctx.author.discriminator}")
            except:
                print(f"{Fore.WHITE}[{Fore.CYAN}!{Fore.WHITE}] {hour}:{minute}:{second} {Fore.YELLOW}Pastebin Found! // Sent By: {ctx.author.name}#{ctx.author.discriminator}")
            if len(code) == 8:
                print(f"{Fore.WHITE}[{Fore.GREEN}+{Fore.WHITE}] {hour}:{minute}:{second}{Fore.GREEN} Reading Pastebin : pastebin.com/{code}")
                r = requests
                pasteresult = r.get(f"https://pastebin.com/raw/{code}")
                currentDT = datetime.datetime.now()
                hour = str(currentDT.hour)
                minute = str(currentDT.minute)
                second = str(currentDT.second)
                if pasteresult.status_code == 404: 
                    print(f"{Fore.WHITE}[{Fore.RED}-{Fore.WHITE}] {hour}:{minute}:{second}{Fore.RED} Invalid Pastebin : pastebin.com/{code}")
                else:
                    print(f"{Fore.WHITE}[{Fore.GREEN}+{Fore.WHITE}] {hour}:{minute}:{second}{Fore.GREEN} Valid Pastebin : pastebin.com/{code} - Saved!")
                    with open(f'Pastebin/{code}.txt', 'w+') as pastebinsave:
                        pastebinsave.write(f"[+] Results from pastebin.com/{code}:\n\n{pasteresult.text}")
                        pastebinsave.close()
            else:
                print(f"{Fore.WHITE}[{Fore.RED}-{Fore.WHITE}] {hour}:{minute}:{second}{Fore.RED} Invalid Pastebin Format : pastebin.com/{code}")




    if giveaway == "On":
        if 'giveaway' in str(ctx.content).lower(): #add win calc too!
            if ctx.author.id == 294882584201003009  or ctx.author.id == 673918978178940951 or ctx.author.id == 716967712844414996 or ctx.author.id == 582537632991543307 or ctx.author.id == 450017151323996173 or ctx.author.id == 574812330760863744:
                await asyncio.sleep(8) # so yall dont get accused of sniping giveaways but still enter all - min gw time for the big giveaway bot is 10 seconds
                await ctx.add_reaction("🎉")
                gwlog = open("giveawaylog.txt","a") 
                currentDT = datetime.datetime.now()
                hour = str(currentDT.hour)
                minute = str(currentDT.minute)
                second = str(currentDT.second)
                print(f"{Fore.WHITE}[{Fore.CYAN}!{Fore.WHITE}] {hour}:{minute}:{second} {Fore.YELLOW} Giveaway Entered! // Server: {ctx.guild.name} // Channel: {ctx.channel.name} //  Bot: {ctx.author.name}#{ctx.author.discriminator}")
                try:
                    gwlog.write(f"[!] Giveaway Entered! // Server: {ctx.guild.name} // Channel: {ctx.channel.name} // Bot: {ctx.author.name}#{ctx.author.discriminator} -- {hour}:{minute}:{second}\n")
                except:
                    gwlog.write(f"[+] Giveaway Entered : Server/Channel Not writable because of characters used :| //  Bot: {ctx.author.name}#{ctx.author.discriminator} -- {hour}:{minute}:{second}\n[+] Message: {ctx.content}\n")
                


        if f'<@{bot.user.id}>' in str(ctx.content): #expermintal but meh
            if ctx.author.id == 294882584201003009 or ctx.author.id == 673918978178940951 or ctx.author.id == 716967712844414996 or ctx.author.id == 582537632991543307 or ctx.author.id == 450017151323996173 or ctx.author.id == 574812330760863744:
                gwlog = open("giveawaylog.txt","a") 
                currentDT = datetime.datetime.now()
                hour = str(currentDT.hour)
                minute = str(currentDT.minute)
                second = str(currentDT.second)
                print(f"{Fore.WHITE}[{Fore.CYAN}!{Fore.WHITE}] {hour}:{minute}:{second} {Fore.GREEN} Giveaway Won! // Server: {ctx.guild.name} // Channel: {ctx.channel.name} //  Bot: {ctx.author.name}#{ctx.author.discriminator}")
                try:
                    gwlog.write(f"[+] Giveaway Won: {ctx.guild.name} // Channel: {ctx.channel.name} //  Bot: {ctx.author.name}#{ctx.author.discriminator} -- {hour}:{minute}:{second}\n[+] Message: {ctx.content}\n")
                except:
                    gwlog.write(f"[+] Giveaway Won: Server/Channel Not writable because of characters used :| //  Bot: {ctx.author.name}#{ctx.author.discriminator} -- {hour}:{minute}:{second}\n[+] Message: {ctx.content}\n")

    if privnote == "On":
        if 'privnote' in ctx.content: #while it cant exactly be "sniped" - people still drop stuff in pastebin from time to time that you might not see , depending on whether its a method or sum, still usefull to have imo
        
            code = re.search("privnote.com/(.*)", ctx.content).group(1) 
            currentDT = datetime.datetime.now()
            hour = str(currentDT.hour)
            minute = str(currentDT.minute)
            second = str(currentDT.second)
            try:
                print(f"{Fore.WHITE}[{Fore.CYAN}!{Fore.WHITE}] {hour}:{minute}:{second} {Fore.YELLOW}Privnote Found! // Server: {ctx.guild.name} // Channel: {ctx.channel.name} // Sent By: {ctx.author.name}#{ctx.author.discriminator}")
            except:
                print(f"{Fore.WHITE}[{Fore.CYAN}!{Fore.WHITE}] {hour}:{minute}:{second} {Fore.YELLOW}Privnote Found! // Sent By: {ctx.author.name}#{ctx.author.discriminator}")
            print(f"{Fore.WHITE}[{Fore.GREEN}+{Fore.WHITE}] {hour}:{minute}:{second}{Fore.GREEN} Checking Privnote : privnote.com/{code}")
            try:
                privnotesnipe = pn.read_note(f"https://privnote.com/{code}")
                print(f"{Fore.WHITE}[{Fore.GREEN}+{Fore.WHITE}] {hour}:{minute}:{second}{Fore.GREEN} SNIPED Privnote : privnote.com/{code}")
                with open(f'Privnote/{code}.txt', 'w+') as pastebinsave:
                    pastebinsave.write(f"[+] Results from privnote.com/{code}:\n\n{privnotesnipe}")
                    pastebinsave.close()
            except:
                print(f"{Fore.WHITE}[{Fore.RED}-{Fore.WHITE}] {hour}:{minute}:{second}{Fore.RED} Privnote Already Read")


bot.run(token, bot=False)

