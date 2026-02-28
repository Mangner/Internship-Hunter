import os
import asyncio
from contextlib import suppress
from datetime import date

import pytest
from dotenv import load_dotenv

from BOT.discordBot import DiscordBot
from BOT.cogs.offer_cog import OfferCog
from database import Database
from Models.offer import Offer
from Repository.offerRepository import OfferRepository
from Repository.subscriptionRepository import SubscriptionRepository

TEST_DB_FILE = os.path.join(os.path.dirname(__file__), "offers_test.db")


@pytest.mark.asyncio
async def test_notify_discord_channel():
    load_dotenv()
    token = os.getenv("DISCORD_TOKEN")
    if not token:
        pytest.skip("DISCORD_TOKEN is not set")

    channel_id = int(os.getenv("TEST_CHANNEL_ID", "1477353912548724700"))
    db_url = f"sqlite:///{TEST_DB_FILE}"

    class TestBot(DiscordBot):
        async def setup_hook(self):
            return

    bot = TestBot(db_url=db_url)
    await bot.login(token)
    bot_task = asyncio.get_running_loop().create_task(bot.connect(reconnect=False))
    await bot.wait_until_ready()
    await asyncio.sleep(2)
    print(f"[test] Bot ready. Guilds in cache: {[g.name for g in bot.guilds]}")
    cog = OfferCog(bot, db_url=db_url, start_loop=False)

    db = Database(db_url)
    db.create_tables()
    session = db.get_session()
    try:
        SubscriptionRepository(session).create_if_missing(channel_id=channel_id, guild_id=None)
        offer = Offer(
            offer_name="Test Offer",
            add_date=date.today(),
            exp_date=date.today(),
            href="https://example.com/test-offer",
        )
        OfferRepository(session).create_offer(offer)
        session.refresh(offer)
        session.expunge(offer)
    finally:
        session.close()
        db.dispose()

    try:
        await cog._notify_subscribers([offer], delay_seconds=0)
    finally:
        await bot.close()
        bot_task.cancel()
        with suppress(asyncio.CancelledError):
            await bot_task

    if os.path.exists(TEST_DB_FILE):
        os.remove(TEST_DB_FILE)
