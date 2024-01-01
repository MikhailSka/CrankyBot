import discord
import random
import os
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)
bot = commands.Bot(command_prefix='!', intents=intents)
karma = commands.CommandSzczur(bot)

KARMAS = ["KARMA.jpg","KARMA2.webp","KARMA3.jpg","KARMA4.jpg"]

@karma.command(name = "karma", guild=discord.Object(id=12417128931))
async def first_command(interaction):
    with open(f'CRANKYBOT/{random.choice(KARMAS)}', 'rb') as f:
            picture = discord.File(f)

@bot.slash_command(name="karma", guild_ids=[...])
async def first_slash(ctx):
    await ctx.respond("nuh uh")
@bot.slash_command(name="christmas", guild_ids=[...])
async def first_slash(ctx):
    await ctx.respond("Marry Christmas! I got a present for you!")
    with open(f'CRANKYBOT/{"DOGECOIN.jpg"}', 'rb') as f:
            picture = discord.File(f)