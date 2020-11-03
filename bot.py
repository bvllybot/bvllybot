import discord
from discord.ext import commands
import random
import re
from tokens import dev, prod

from lookism import shitposts
from gods import gods

bot = commands.Bot(command_prefix='.', description='')
client = discord.Client()

## kimbo
def morocco_filter(message):
    match = re.search('m[o-p0-9][r-s0-5]+[o-s0-5][c-e0-5]+o', message.content.lower())
    if match:
         return True

def jesus_filter(message):
    match = re.search('jesus', message.content.lower())
    if match:
         return True

def rules_filter(message):
    match = re.search('rules', message.content.lower())
    if match:
         return True 
 
def cuck_filter(message):
    match = re.search('cuck|sissy|gasm|gay|homosexual|femboy|transgender|submissive|femdom|bnwo|rim', message.content.lower())
    if match:
         return True
 
##kimbo

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

#kimbo
    morocco = morocco_filter(message)
    if morocco:
        #you need to change channel id to the channel you want the message to be posted to
         channel = client.get_channel(667421091039412260)
         await channel.send('***Girlfriend wants to travel to Morocco with me, should i be worried? I\'m a little bit worried. What if the low inhibition moroccans rape my blonde wh6te girlfriend and she likes it? I wouldnt be worried if she said somewhere like Netherlands or England or some cuck place with a bunch of wh8te bois. But its literally Morocco, with dark badboys. What do I do? Man Badr Hari is from Morocco. I would willingly go to Europe or some place with her as I\'m the baddest boy in Europe. But moroccans are all gigabadboys***')


    jesus = jesus_filter(message)
    if jesus:
         channel = client.get_channel(667421091039412260)
         await channel.send('***Revelation 1:14 His head and hair were white like wool, as white as snow, and His eyes like a flame of fire; 15His feet were like fine brass, as if refined in a furnace, and His voice as the sound of many waters; *** https://cdn.discordapp.com/attachments/667421091039412260/772949110902751232/ab3ce2728273e58215256c0347b9e2b7.jpg')

    rules = rules_filter(message)
    if rules:
         channel = client.get_channel(667421091039412260)
         await channel.send('Never use homophobic, ableist, racist or sexist language. Anyone caught using this sort of language will be banned!')

    cuck = cuck_filter(message)
    if cuck:
        #put the the name first then the code for it
        await message.add_reaction("<:anatolia:772960807473905665>")
 #kimbo    
    
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

print('test')
#client.run('NzcyNDU4MjI4MjMxMDQ1MTcx.X569yQ.YuYco7McSzlRmdwCFswJXlbPLxE')
