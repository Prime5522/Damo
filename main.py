from pyrogram import Client, filters
from pyrogram.types import Message
from flask import Flask
from threading import Thread
import os
from dotenv import load_dotenv

# .env ফাইল লোড করা
load_dotenv()

# API ID, API HASH, এবং BOT TOKEN সেটআপ
API_ID = int(os.getenv("API_ID"))
API_HASH = os.getenv("API_HASH")
BOT_TOKEN = os.getenv("BOT_TOKEN")

# Pyrogram বট সেটআপ
bot = Client(
    "ServiceDownBot",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN,
)

# Flask HTTP সার্ভার সেটআপ
app = Flask(__name__)

@app.route('/')
def home():
    return "Bot is running!"

# Flask HTTP সার্ভার চালানোর জন্য থ্রেড
def run():
    app.run(host="0.0.0.0", port=int(os.getenv("PORT", 8080)))

# যে কোন মেসেজ পেলেই উত্তর দেওয়া
@bot.on_message(filters.all)
async def handle_all_messages(client: Client, message: Message):
    try:
        await message.reply_text(
            "⚠️ দুঃখিত! এই বটের সার্ভিসে কিছু প্রবলেম হয়েছে।\n\n"
            "➡️ নতুন সার্ভিস ব্যবহার করতে অনুগ্রহ করে এই বটটি ব্যবহার করুন: @iPapkornPrimeBot"
        )
    except Exception as e:
        # যদি কোনো সমস্যা হয়, তাহলে লগ করে জানিয়ে দেব
        print(f"Error while handling message: {e}")

# বট এবং Flask HTTP সার্ভার চালু করা
if __name__ == "__main__":
    try:
        print("Bot is running...")
        Thread(target=run).start()  # Flask HTTP সার্ভার চালানো
        bot.run()  # Pyrogram বট চালানো
    except Exception as e:
        print(f"Error while starting bot or server: {e}")
