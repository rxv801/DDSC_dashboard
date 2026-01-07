import os
import discord
from dotenv import load_dotenv
import csv
from pathlib import Path

load_dotenv()
token = os.getenv("DISCORD_TOKEN") or ""

# Set up CSV path
project_root = Path(__file__).parent.parent.parent
csv_path = project_root / "data" / "discord_messages.csv"
csv_path.parent.mkdir(exist_ok=True)

intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)

# List of channel IDs to monitor
CHANNEL_IDS = [1344078615419031664, 1344079770706776185, 1339189911303098384]


@client.event
async def on_ready():
    print(f"Logged in as {client.user}")

    # Get last message ID from CSV
    last_id = None
    try:
        with open(csv_path, "r", encoding="utf-8") as f:
            reader = csv.DictReader(f)
            for row in reader:
                message_id = row.get("message_id")
                if message_id:
                    last_id = int(message_id)
    except FileNotFoundError:
        pass

    # Loop through all channels
    for channel_id in CHANNEL_IDS:
        channel = client.get_channel(channel_id)

        if channel and hasattr(channel, "history"):
            print(f"Fetching history from {channel.name}...")
            after_obj = discord.Object(id=last_id) if last_id is not None else None

            async for message in channel.history(limit=1000, after=after_obj):  # type: ignore
                with open(csv_path, "a", newline="", encoding="utf-8") as f:
                    writer = csv.writer(f)
                    if f.tell() == 0:
                        writer.writerow(
                            ["message_id", "timestamp", "author", "channel", "message"]
                        )

                    writer.writerow(
                        [
                            message.id,
                            message.created_at.isoformat(),
                            str(message.author),
                            str(message.channel),
                            message.content,
                        ]
                    )

    print("All history fetched!")


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    # Save new message to CSV
    with open(csv_path, "a", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        if f.tell() == 0:
            writer.writerow(["message_id", "timestamp", "author", "channel", "message"])

        writer.writerow(
            [
                message.id,
                message.created_at.isoformat(),
                str(message.author),
                str(message.channel),
                message.content,
            ]
        )

    if message.content.startswith("$hello"):
        await message.channel.send("Hello")


client.run(token)
