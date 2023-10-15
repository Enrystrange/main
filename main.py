import discord
from discord.ext import commands
from botlogic import gen_pass,flip_coin,gen_emodji
intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print("fHai fatto l\\'accesso come {bot.user}")

@bot.command()
async def ciao(ctx):
    await ctx.send(f'Ciao! Sono un bot {bot.user}!')

@bot.command()
async def pasw(ctx):
    await ctx.send(gen_pass(10))
@bot.command()
async def flip(ctx):
    await ctx.send(flip_coin())
@bot.command()
async def emoji(ctx):
    await ctx.send(gen_emodji())
bot.run("MTE2MDUxODYzMzk5MTE4ODUzMw.GrqY0V.L-h5lJKVi2YV0F6NJ0-kXygad_cYgTNhOFA2PQ")
