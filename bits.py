#maybe when i get a new laptop i should migrate my code here idk
#i really don't know what I've written for this, it doesn't even work 
import discord
import os
import discord.ext
from discord.ext import commands
prefix="Gooser "
token=token
client = commands.Bot(command_prefix=prefix) #i'm not sure which one I actually need and so if I have both ik it works somehow, this might be that actual problem
bot = commands.Bot(command_prefix=prefix)
bot.remove_command('help')

standardmum = 5
ur mum = ######come up with something for this

@bot.command()
async def urmum(ctx):
    if urmum > standardmum:
        embed = discord.Embed(title= "ur mum wide", description= "haha")
        ctx.send(embed=embed)
    else:
        embed = discord.Embed(title= "", desc = "your mother is a wonderful person and I'd love to spend more time with her")
        ctx.send(embed=embed)
 
bot.run(token)
client.run(token) #see line 9 i guess
