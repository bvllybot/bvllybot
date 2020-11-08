import discord
from discord.ext import commands
import random
import re
import json


#directory imports
#from lookism import shitposts
from tokens import dev, prod
from gods import gods
import filters as f # f for filter

client = discord.Client()

#@bot.command()
#async def test(ctx):
    #await ctx.send('testing')
    #pass

with open('shitposts.json') as ff:
    shitposts = json.load(ff)
@client.event
async def on_ready():
    #print('started')
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        print(client.user)
        return
    nigger = f.nigger_filter(message)
    white = f.white_filter(message)

#kimbo
    #morocco = f.morocco_filter(message)
    #if morocco:
        ##you need to change channel id to the channel you want the message to be posted to
         ##channel = client.get_channel(667421091039412260)
         #await message.channel.send('***Girlfriend wants to travel to Morocco with me, should i be worried? I\'m a little bit worried. What if the low inhibition moroccans rape my blonde wh6te girlfriend and she likes it? I wouldnt be worried if she said somewhere like Netherlands or England or some cuck place with a bunch of wh8te bois. But its literally Morocco, with dark badboys. What do I do? Man Badr Hari is from Morocco. I would willingly go to Europe or some place with her as I\'m the baddest boy in Europe. But moroccans are all gigabadboys***')
         #return


    jesus = f.jesus_filter(message)
    if jesus:
         #channel = client.get_channel(667421091039412260)
         await message.channel.send('***Revelation 1:14 His head and hair were white like wool, as white as snow, and His eyes like a flame of fire; 15His feet were like fine brass, as if refined in a furnace, and His voice as the sound of many waters; *** https://cdn.discordapp.com/attachments/667421091039412260/772949110902751232/ab3ce2728273e58215256c0347b9e2b7.jpg')
         return

    rules = f.rules_filter(message)
    if rules:
         #channel = client.get_channel(667421091039412260)
         await message.channel.send('Never use homophobic, ableist, racist or sexist language. Anyone caught using this sort of language will be banned!')

    cuck = f.cuck_filter(message)
    if cuck:
        #put the the name first then the code for it
        await message.add_reaction("<:transthumbsup:769514995587219486>")
        return
 #kimbo    
    
    #print(checked)
    if nigger and (message.author.id not in gods):
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

#token
#production
client.run(prod)
# testing

#client.run(dev)
#bot.run(dev)