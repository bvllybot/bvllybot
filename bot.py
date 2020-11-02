import discord
from discord.ext import commands
import random
import re
from tokens import dev, prod

from lookism import shitposts
from gods import gods

bot = commands.Bot(command_prefix='.', description='')
client = discord.Client()

def nigger_filter(message):
    match1 = re.search('n[a-i0-9][a-g0-5][a-g0-5][a-e0-5]r', message.content.lower())
    match2 = re.search('n[a-i0-9][a-g0-5][a-g0-5][a4]', message.content.lower())
    if match1 or match2:
        return True 

def white_filter(message):
    match = message.content.lower()
    if "white" in match:
        return True

@client.event
async def on_ready():
    #print('started')
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        print(client.user)
        return
    checked = nigger_filter(message)
    white = white_filter(message)
    #print(checked)
    if checked and (message.author.id not in gods):
        #print(message.author)
        #print(type(message.author))
        #print(discord.member.Member)
        await message.delete()
        await message.author.send('https://discord.gg/Swwe7hknrT')
        await message.author.send(f'{random.choice(shitposts).upper()}\n\n\n')
        #await discord.member.Member.kick(message.author)

    if white and (message.author.id not in gods):
        #print(message.author)
        #print(type(message.author))
        #print(discord.member.Member)
        await message.delete()
        await message.author.send('https://discord.gg/Swwe7hknrT')
        await message.author.send("WH*TE BOY, YOU HAVE BROKEN THE ToS OF NOT USING * FOR WH*TE")
        #await discord.member.Member.kick(message.author)
#testing changes 123 4 5 
#token
#production
client.run(prod)
# testing

#client.run('NzcyNDU4MjI4MjMxMDQ1MTcx.X569yQ.YuYco7McSzlRmdwCFswJXlbPLxE')