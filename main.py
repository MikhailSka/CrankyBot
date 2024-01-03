import discord
from discord.ext import commands
from memegen import meme
from mainTherapy import bot as therapy_bot, chatgpt_response

intents = discord.Intents.default()
intents.message_content = True

TOKEN = 'bot_token_here'

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.command()
async def memegen(ctx):
    await ctx.reply(meme())

@bot.command()
async def run_therapy(ctx):
    print("Command executed")
    await chatgpt_response(ctx)
    await ctx.send(f'Generating response...')

bot.run(TOKEN)

