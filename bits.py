#maybe when i get a new laptop i should migrate my code here idk
#i really don't know what I've written for this, it doesn't even work 
import discord
import random
import discord.ext
from discord.ext import commands
prefix="Gooser "
token=token
bot = commands.Bot(command_prefix=prefix)
bot.remove_command('help')

standardmum = 5
ur mum = random.randint(1,10)

@bot.command()
async def urmum(ctx):
    if urmum > standardmum:
        embed = discord.Embed(title= "ur mum wide", description= "haha")
        ctx.send(embed=embed)
    else:
        embed = discord.Embed(title= "", desc = "your mother is a wonderful person and I'd love to spend more time with her")
        ctx.send(embed=embed)
 
bot.run(token)
#I wrote this so long ago i know it has no chance of working ever and I don't even remember enough python for it to work
