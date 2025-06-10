# Import discord library and commands extension
import discord
from discord.ext import commands

# Replace with your actual channel IDs - enable developer mode in Discord settings to get these IDs
INPUT_CHANNEL_ID = 123456789012345678  # ID of channel where trade ideas are typed - ideally a private channel not available to everyone
OUTPUT_CHANNEL_ID = 876543210987654321  # ID of channel where embed is posted - public channel

# Intents with message content access - ensure the Bot has the required permissions in Discord developer portal - Presence Intent and Message COntent Indtent
intents = discord.Intents.default()
intents.message_content = True

# Bot setup
bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f'✅ Bot is live as {bot.user}')

@bot.event
async def on_message(message):
    # Ignore messages from bots or from the other channels
    if message.channel.id != INPUT_CHANNEL_ID or message.author.bot:
        return

    # Expected message format: [ticker or asset] [buy/sell] [limit/market] [price/market current] [stop loss] [take profit]
    parts = message.content.split()
    if len(parts) != 6:
        await message.channel.send("❌ Invalid format. Use: `[ticker] [buy/sell] [limit/market] [price/market current] [stop loss] [take profit]`")
        return

    ticker, action, order_type, entry, sl, tp = parts

    # Build the embed using the discord lib
    embed = discord.Embed(
        title=f"{ticker.upper()} - {action.upper()}",
        description=f"**{order_type.upper()} ORDER**\n"
                    f"- Entry: {entry.upper()}\n"
                    f"- Stop Loss: {sl}\n"
                    f"- Take Profit: {tp}",
        color=discord.Color.green() if action.lower() == "buy" else discord.Color.red()
    )

    if message.attachments:
        embed.set_image(url=message.attachments[0].url)

    # Get the output channel and send the embed
    target_channel = bot.get_channel(OUTPUT_CHANNEL_ID)
    if target_channel:
        await target_channel.send(embed=embed)
    else:
        await message.channel.send("⚠️ Output channel not found. Check OUTPUT_CHANNEL_ID.")

# Replace with your actual bot token
bot.run("BOT_TOKEN")
