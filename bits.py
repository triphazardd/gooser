@bot.command()
async def hug(ctx, *, user: discord.Member = None):
    user = user 
    embed = make_embed(title= "", desc=f"Gooser gives **{user}** a big hug on behalf of **{ctx.author}**")
    await ctx.send(embed=embed)
    
#don't forget to define everything but if i'm just dumping this in gooser it should be already done, if not, back to square one lol 
#also work out: how to remove tags (see the hi test goose command maybe), add the cute gif to it, tips in the footer of the embed?,
