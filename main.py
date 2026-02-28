from BOT.discordBot import DiscordBot
import logging
from dotenv import load_dotenv
import os


def main():

    load_dotenv()
    TOKEN = os.getenv('DISCORD_TOKEN')
    DB_URL = os.getenv('DATABASE_CONNECTION_STRING')
    handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')
    bot = DiscordBot(db_url=DB_URL)
    bot.run(TOKEN, log_handler=handler, log_level=logging.DEBUG)


if __name__ == '__main__':
    main()

