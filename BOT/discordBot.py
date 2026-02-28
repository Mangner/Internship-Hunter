import discord
from discord.ext import commands


class DiscordBot(commands.Bot):
    def __init__(self, db_url: str):
        intents = discord.Intents.default()
        intents.message_content = True
        intents.members = True
        super().__init__(command_prefix='!', intents=intents, help_command=None)
        self.db_url = db_url

    async def on_ready(self):
        print(f"We are ready to go in, {self.user.name}")

    async def setup_hook(self):
        await self.load_extension("BOT.cogs.offer_cog")
        await self.tree.sync()

    async def on_guild_join(self, guild: discord.Guild):
        channel = guild.system_channel
        if channel is None:
            for text_channel in guild.text_channels:
                permissions = text_channel.permissions_for(guild.me)
                if permissions.send_messages:
                    channel = text_channel
                    break

        if channel is None:
            return

        await channel.send(
            "Hello! I am a bot that notifies you about new job and internship offers "
            "from the Career Office of Cracow University of Technology. "
            "Type /help to see available commands."
        )