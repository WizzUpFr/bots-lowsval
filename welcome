import discord
from discord.ext import commands

token = "OTE4Nzg3Mjk5NjcwNjM4NTky.YbMVWg.Lc7j2UN93GhCAMhLIrL_Qcfo6Zw"
prefix = "-"

intents = discord.Intents.all()

bot = commands.Bot(command_prefix=prefix, intents=intents)

@bot.event
asyn def on_ready():
        print(f"Le bot est prêt!")

@bot.event
async def on_member_join(member):
    welcome_channel = bot.get_channel(928755485245595678)
    print(f"{member}" has joined! Welcome {member})
    await welcome_channel.send(f"{member.mention} Has joined! Welcome!")

@bot.event
async def on_member_remove(member):
    welcome_channel = bot.get_channel(928755485245595678)
    print(f"{member} has left!")
    await welcome_channel.send(f"{member.mention} Has removed! Good bye!")

@bot.event
async def on_member_ban(member):
    welcome_channel = bot.get_channel(928755485245595678)
    print(f"{member} has ban!")
    await welcome_channel.send(f"{member.mention} Has banned! Aie!")

@bot.event
async def on_member_unban(member):
    welcome_channel = bot.get_channel(928755485245595678)
    print(f"{member} has unban!")
    await welcome_channel.send(f"{member.mention} Has unban! Welcome back!")

bot.run(token)
