from pyrogram import Client, filters
from pyrogram.types import Message
from flask import Flask
from threading import Thread
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

# Flask HTTP সার্ভার সেটআপ
app = Flask('')

@app.route('/')
def home():
    return "Bot is running!"

def run():
    app.run(host="0.0.0.0", port=int(os.getenv("PORT", 8080)))

# যে কোনো মেসেজ পেলেই উত্তর দেওয়া
@bot.on_message(filters.all)
async def handle_all_messages(client: Client, message: Message):
    await message.reply_text(
        "⚠️ দুঃখিত! এই বটের সার্ভিসে কিছু প্রবলেম হয়েছে।\n\n"
        "➡️ নতুন সার্ভিস ব্যবহার করতে অনুগ্রহ করে এই বটটি ব্যবহার করুন: @iPapkornPrimeBot"
    )

# বট চালু এবং Flask HTTP সার্ভার চালু করুন
if __name__ == "__main__":
    print("Bot is running...")
    Thread(target=run).start()  # Flask HTTP সার্ভার চালানো
    bot.run()
