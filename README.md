# Job-Hunter

Discord bot that automatically monitors and notifies about new job and internship offers from the **Career Office of Cracow University of Technology** (Biuro Karier Politechniki Krakowskiej).

## Overview

The project consists of three modules:

### 1. Web Scraping (Selenium + Page Object Model)

The scraping module uses **Selenium WebDriver** with the **Page Object Model (POM)** design pattern to navigate and extract offer data from the Career Office website (`kariery.pk.edu.pl`).

**Structure:**

- `Pages/base_page.py` — base class with shared WebDriver utilities (`find_element`, `find_all_elements`, `WebDriverWait`)
- `Pages/career_page.py` — page object for the career portal; handles cookie acceptance, filtering by IT/Programming, pagination, and extracting offer details (name, dates, link)
- `Locators/careerPageLocators.py` — XPath locators for all page elements, separated from page logic
- `DTOs/rawOffer.py` — lightweight `dataclass` representing a scraped offer before database mapping

The scraper supports two modes:

- `get_offers()` — full scrape of all available offers
- `get_new_offers(exists_by_href)` — incremental scrape that skips offers already present in the database

### 2. Database (SQLAlchemy + Repository Pattern)

The persistence layer uses **SQLAlchemy ORM** with the **Repository** design pattern to separate data access logic from business logic.

**Structure:**

- `Models/base.py` — SQLAlchemy `DeclarativeBase`
- `Models/offer.py` — `Offer` model (id, name, add_date, exp_date, href)
- `Models/subscription.py` — `Subscription` model (id, guild_id, channel_id) for tracking registered Discord channels
- `Repository/offerRepository.py` — CRUD operations for offers (`create_offer`, `exists_by_href`, `get_all`)
- `Repository/subscriptionRepository.py` — CRUD operations for channel subscriptions (`create_if_missing`, `get_all`, `delete_by_channel_id`)
- `Services/offerService.py` — business logic layer that coordinates parsing and deduplication of new offers
- `Parsers/offerParser.py` — maps `RawOffer` DTOs to `Offer` ORM models
- `database.py` — engine and session factory

### 3. Discord Bot (discord.py + Cogs)

The bot is built with **discord.py** using the **Cog** extension system for modular command organization. Commands are implemented as **hybrid commands** (both slash `/` and prefix `!`).

**Structure:**

- `BOT/discordBot.py` — bot class with gateway setup, extension loading, and on-join greeting
- `BOT/cogs/offer_cog.py` — main Cog containing all commands and the background scraping loop

**Available commands:**
| Command | Description |
|---|---|
| `/register` | Register the current channel to receive new offer notifications |
| `/unregister` | Unregister the current channel from notifications |
| `/showoffers` | Receive a DM with an XLSX file containing all offers from the database |
| `/help` | Show available commands |

## How It Works

1. **Bot starts** — loads the `OfferCog`, syncs slash commands with Discord, and begins the background loop
2. **Every 10 minutes** — the bot launches a Selenium browser in a separate thread, navigates to the Career Office website, applies IT/Programming filters, and scrapes offer links page by page
3. **Incremental scraping** — for each offer link found, the scraper checks if it already exists in the database; known offers are skipped, new ones have their details (name, dates, URL) extracted
4. **Database save** — new offers are parsed into ORM models and saved to the SQLite database
5. **Notifications** — if new offers were found, the bot sends them one by one (with 5-second intervals) to every registered Discord channel
6. **On demand** — users can request a full XLSX export of all offers via DM using `/showoffers`

## Setup

### Requirements

- Python 3.12+
- Google Chrome + ChromeDriver
- Discord Bot Token with `applications.commands` and `bot` scopes

### Installation

```bash
pip install -r requirements.txt
```

### Configuration

Create a `.env` file in the project root:

```env
DISCORD_TOKEN=your_bot_token_here
```

### Running

```bash
python main.py
```

## Testing

Integration tests verify the full notification pipeline against a real Discord channel:

```bash
pytest -q -s
```

Set `TEST_CHANNEL_ID` in `.env` to target a specific channel.

## Tech Stack

- **Web Scraping:** Selenium WebDriver, Page Object Model
- **Database:** SQLAlchemy ORM, Repository Pattern, SQLite
- **Discord Bot:** discord.py, Hybrid Commands, Cogs, Background Tasks
- **Testing:** pytest, pytest-asyncio
