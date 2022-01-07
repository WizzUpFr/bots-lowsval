import discord
from discord.ext import command, has_permissions

@bot.command(aliases= ['purge','delete'])
@commands.has_permissions(manage_messages=True)
async def clear(ctx, amount=None): # Set default value as None
    if amount == None:
        await ctx.channel.purge(limit=1000000)
    else:
        try:
            int(amount)
        except: # Error handler
            await ctx.send('Please enter a valid integer as amount.')
        else:
            await ctx.channel.purge(limit=amount)
