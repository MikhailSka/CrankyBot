import discord
from discord.ext import commands    
import openai
from dotenv import load_dotenv
import os

load_dotenv()

intents = discord.Intents.default()
intents.message_content = True 
bot = commands.Bot(command_prefix='\/', intents=intents)

# Set up the OpenAI API key
openai.api_key = os.getenv('OPENAI_API_KEY')

@bot.command(name='therapy_mode')
async def therapy_mode(ctx):
    therapy_mode = True

@bot.command(name='therapy_')
async def chatgpt_response(ctx):
    prompt = f"User: {ctx.message.content}\n"
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=prompt,
        max_tokens=150
    )
    await ctx.send(response.choices[0].text.strip())

# Run your bot
bot.run('YOUR_DISCORD_BOT_TOKEN')
