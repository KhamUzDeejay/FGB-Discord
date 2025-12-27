import discord
from discord.ext import commands
from apscheduler.schedulers.asyncio import AsyncIOScheduler
import pytz

from config import *
from database import *
from stores import epic, gog

intents = discord.Intents.default()
bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"Conectado como {bot.user}")
    scheduler = AsyncIOScheduler()
    scheduler.add_job(check_games, "interval", minutes=CHECK_INTERVAL_MINUTES)
    scheduler.start()

async def check_games():
    channel = bot.get_channel(CHANNEL_ID)
    tz = pytz.timezone(TIMEZONE)

    games = epic.get_games() + gog.get_games()

    for g in games:
        if already_sent(g["store"], g["id"]):
            continue

        price_text = f"~~${g['price']:.2f}~~ - **GRATIS**"
        end_text = (
            g["end"].astimezone(tz).strftime("%d %b %Y %H:%M")
            if g["end"] else "Tiempo limitado"
        )

        embed = discord.Embed(
            title=f"🎁 {g['name']}",
            description=(
                f"🏢 **{g['store']}**\n"
                f"⏰️ **Hasta:** {end_text}\n"
                f"💵 {price_text}\n"
                f"🔗 [Reclamar]({g['url']})"
            ),
            color=0x00ffcc
        )
        embed.set_thumbnail(url=g["image"])

        await channel.send(embed=embed)
        mark_sent(g["store"], g["id"])

bot.run(DISCORD_TOKEN)
