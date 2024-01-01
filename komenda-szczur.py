import discord
import random
import os
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)
bot = commands.Bot(command_prefix='/', intents=intents)
szczur = commands.CommandSzczur(bot)

szczurek = ["szczour.jpg","Therock.jpg","unnamed.jpg"]

@szczur.command(name = "szczur", guild=discord.Object(id=12417128931))
async def first_command(interaction):
    with open(f'CRANKYBOT/{random.choice(szczurek)}', 'rb') as f:
            picture = discord.File(f)

@bot.slash_command(name="hapoo", guild_ids=[...])
async def first_slash(ctx):
    await ctx.respond("Szczor hoho")
