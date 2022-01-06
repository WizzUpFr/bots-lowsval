import discord
from discord.ext import commands, tasks
import random

bot = commands.Bot(command_prefix = "?", description = "Bot de Lowsval")
status = ["?help",
		"Mon insta : Lowsval",
		"Tu as besoin d'aide ? demande à mon créateur @Lowsval#1775",
		"Tu veux m'a photo pour savoir ça ? ",
		"Le savais-tu aaron est homophobe ?  moi aussi je suis choqué "]

@bot.event
async def on_ready():
	print("Le bot est prêt !")
	changeStatus.start()

@bot.command()
async def start(ctx, secondes = 10):
	changeStatus.change_interval(seconds = secondes)

@tasks.loop(seconds = 5)
async def changeStatus():
	game = discord.Game(random.choice(status))
	await bot.change_presence(status = discord.Status.dnd, activity = game)




async def createMutedRole(ctx):
    mutedRole = await ctx.guild.create_role(name="Muted",
                                            permissions=discord.Permissions(
                                                send_messages=False,
                                                speak=False),
                                            reason="Creation du role Muted pour mute des gens.")
    for channel in ctx.guild.channels:
        await channel.set_permissions(mutedRole, send_messages=False, speak=False)
    return mutedRole


async def getMutedRole(ctx):
    roles = ctx.guild.roles
    for role in roles:
        if role.name == "Muted":
            return role

    return await createMutedRole(ctx)


@bot.command()
async def mute(ctx, member: discord.Member, *, reason="Aucune raison n'a été renseigné"):
    mutedRole = await getMutedRole(ctx)
    await member.add_roles(mutedRole, reason=reason)
    await ctx.send(f"{member.mention} a été mute !")


@bot.command()
async def unmute(ctx, member: discord.Member, *, reason="Aucune raison n'a été renseigné"):
    mutedRole = await getMutedRole(ctx)
    await member.remove_roles(mutedRole, reason=reason)
    await ctx.send(f"{member.mention} a été unmute !")



bot.run("")
