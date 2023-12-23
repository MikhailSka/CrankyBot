from mainTherapy import
import discord
from discord.ext import commands
from memegen import meme
intents = discord.Intents.default()
intents.message_content = True

TOKEN = 'MTE4NTU0MTQ3NTc1MzI4MzU4NQ.Gd-81r.l8XKUSXZTQ6U8fnb8FNv-lTvzynSEXQDS-RP2E'

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.command()
async def memegen(ctx):
    await ctx.reply(meme())

bot.run(TOKEN)
