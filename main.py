# from mainTherapy import
# import discord
# from discord.ext import commands
# from memegen import meme
# from .mainTherapy import therapyFile
# intents = discord.Intents.default()
# intents.message_content = True

# TOKEN = 'jaki dzban tu wsadził token?'

# bot = commands.Bot(command_prefix='!', intents=intents)

# @bot.command()
# async def memegen(ctx):
#     await ctx.reply(meme())


# @bot.command()
# async def therapyFile(ctx):
#     therapyFile(ctx)
#     await ctx.send(f'Generating response...')
    

# bot.run('TOKEN')

from mainTherapy import bot, chatgpt_response
import discord
from discord.ext import commands
from memegen import meme

intents = discord.Intents.default()
intents.message_content = True

TOKEN = 'nie wsadzać tu na razie tokenu błagam was'

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.command()
async def memegen(ctx):
    await ctx.reply(meme())

@bot.command()
async def run_therapy(ctx):
    await chatgpt_response(ctx)
    await ctx.send(f'Generating response...')

bot.run(TOKEN)

