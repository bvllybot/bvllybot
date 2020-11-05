from discord.ext import commands
import discord
from tokens import dev, prod

client = commands.Bot(command_prefix='!')

@client.command()
async def test(ctx):
    await ctx.send('testing')
    pass

# or:

@client.command()
async def bvlly(ctx, *arg): # <--- *arg stores arguments as tuples. Check print statements to see how it works
    print('in bvlly function ')
    print(arg) # <--- tuple. access tuple like a list/array 
    if arg:
        if arg[0] == 'help':
            await ctx.send('this is me helping your dumb ass')
    else:
        await ctx.send('fuck you pinging me for? try using a command you retard')
client.run(dev)