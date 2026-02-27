import discord
from discord.ext import commands
import logging
from dotenv import load_dotenv
import os

load_dotenv()
token = os.getenv('DISCORD_TOKEN')

handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')
intents = discord.Intents.default()
intents.message_content = True
intents.members = True

bot = commands.Bot(command_prefix='/', intents=intents)


@bot.event
async def on_ready():
    print(f"We are ready to go in, {bot.user.name}")


@bot.event
async def on_message(message):
    if message.author == bot.user:
        return 
    
    if "eliza" in message.content.lower():
        await message.delete()
        await message.channel.send(f"{message.author.mention} pomyliłeś, przecież to")

    await bot.process_commands(message)

bot.run(token, log_handler=handler, log_level=logging.DEBUG)