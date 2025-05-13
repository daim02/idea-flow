# IdeaFlow

**IdeaFlow** is a lightweight, simple Discord bot designed to format structured trade ideas into rich embedded messages. Ideal for trading communities or groups of friends that want clean, readable, and consistent trade callouts.

---

## 🚀 Features

- Parses trade messages in a specific format
- Creates clean, color-coded embed cards
- Supports optional image attachments (e.g. chart screenshots)
- Filters messages by channel
- Posts formatted embeds to a separate output channel

---

## 🧩 Message Format

[ticker] [buy/sell] [limit/market] [price/market current] [stop loss] [take profit]


**Example input:**
EURUSD BUY Market MC 1.09451 1.13821


---

## ⚙️ Setup Instructions

### 1. Create a Bot on Discord Developer Portal
- Go to: [https://discord.com/developers/applications](https://discord.com/developers/applications)
- Click **"New Application"**
- Name it whatever you like

### 2. Set Up OAuth2 and Invite the Bot
- In the left sidebar, go to **OAuth2 → URL Generator**
- Select:
  - ✅ `bot`
- Under **Bot Permissions**, choose:
  - ✅ `Administrator`
- Copy the generated link and open it to invite the bot to your server

> 💡 *If the bot doesn’t get all permissions automatically, go to the Bot tab and manually set "Administrator" under Bot Permissions.*

### 3. Enable Intents
Go to the **"Bot"** tab and enable the following:
- ✅ Message Content Intent
- ✅ Presence Intent *(optional, for future features)*

---

## 🛠️ Configure the Bot

Open the `IdeaFlow.py` file and:

- **Line 6**: Replace `INPUT_CHANNEL_ID` with your input channel's ID (where trade messages are sent)
- **Line 7**: Replace `OUTPUT_CHANNEL_ID` with your output channel's ID (where the embed is posted)
- **Line 55**: Replace `YOUR_BOT_TOKEN_HERE` with your actual bot token

---

## ▶️ Run the Bot

Make sure Python 3.13+ is installed, then install dependencies:

```bash
pip install discord.py
```

Run the bot with:
```
python IdeaFlow.py
```

---



