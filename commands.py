from discord.ext import commands
import discord
import re
import json 
import random

# local import 
from tokens import dev, prod

with open('shitposts.json') as f:
    shitposts = json.load(f)


client = commands.Bot(command_prefix='!')
@client.command()
async def test(ctx):
    await ctx.send('testing')
    pass

@client.command()
async def bvlly(ctx, *arg): # <--- *arg stores arguments as tuples. Check print statements to see how it works

    print('in bvlly function ')
    print(arg) # <--- tuple. access tuple like a list/array 

    if arg:
        roles = ctx.guild.roles # <--- get server roles
        author_role = ctx.author.roles # <-- all message author roles
        #print(author_role) 
        if arg[0] == 'help':
            message = "this is me helping your dumb ass"
            await ctx.send(message.upper())

        if re.match('\<\@\!\d+\>', arg[0]) and ('administrater' in str(author_role)):
            print('in re.match')
            print(author_role)
            print(arg[0])
            user_id = arg[0]
            message = random.choice(shitposts)
            print(message)
            await ctx.send(f"{user_id} {message.upper()}")

    else:
        await ctx.send('fuck you pinging me for? try using a command you retard')
# prod
client.run(prod)
# dev
#client.run(dev)