import discord
from discord.ext import commands

bot = commands.Bot(command_prefix = "?", description = "Bot de Lowsval")

@bot.event
async def on_ready():
    print("Le bot est prêt!")


@bot.command()
async def clear(ctx, nombre : int):
    messages = await ctx.channel.history(limit = nombre + 1).flatten()
    for message in messages:
        await message.delete()
