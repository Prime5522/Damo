from pyrogram import Client, filters
from pyrogram.types import Message
import os
from dotenv import load_dotenv

# লোড .env ফাইল
load_dotenv()

# API ID, API HASH এবং BOT TOKEN সেটআপ
API_ID = int(os.getenv("API_ID"))
API_HASH = os.getenv("API_HASH")
BOT_TOKEN = os.getenv("BOT_TOKEN")

# Pyrogram Bot সেটআপ
bot = Client(
    "ServiceDownBot",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN,
)

# Start Command Handler
@bot.on_message(filters.command("start") & filters.private)
async def start_message(client: Client, message: Message):
    await message.reply_text(
        "⚠️ দুঃখিত! এই বটের সার্ভিসে কিছু প্রবলেম হয়েছে।\n\n"
        "➡️ নতুন সার্ভিস ব্যবহার করতে অনুগ্রহ করে এই বটটি ব্যবহার করুন: @iPapkornPrimeBot"
    )

# General Message Handler
@bot.on_message(filters.text & filters.private)
async def handle_message(client: Client, message: Message):
    await message.reply_text(
        "⚠️ দুঃখিত! এই বটের সার্ভিসে কিছু প্রবলেম হয়েছে।\n\n"
        "➡️ নতুন সার্ভিস ব্যবহার করতে অনুগ্রহ করে এই বটটি ব্যবহার করুন: @iPapkornPrimeBot"
    )

# বট চালু করুন
if __name__ == "__main__":
    print("Bot is running...")
    bot.run()
