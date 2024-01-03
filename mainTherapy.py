import discord
from discord.ext import commands
import openai
from dotenv import load_dotenv
import os
import asyncio

load_dotenv()

intents = discord.Intents.default()
intents.message_content = True 
bot = commands.Bot(command_prefix='!', intents=intents)


openai.api_key = 'api key here'

async def chatgpt_response(ctx):
    prompt = f"User: {ctx.message.content}\n"
    
    while True:
        try:
            response = openai.Completion.create(
                model="text-davinci-002",
                prompt=prompt,
                max_tokens=150
            )
            break 
        except openai.error.RateLimitError as e:
          
            if 'Retry-After' in e.headers:
                wait_time = int(e.headers['Retry-After'])
            else:
      
                wait_time = 10
            
            await asyncio.sleep(wait_time)

    await ctx.send(response['choices'][0]['text'].strip())







