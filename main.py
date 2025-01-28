from pyrogram import Client, filters
from pyrogram.types import Message
import os
from dotenv import load_dotenv

# সিক্রেট ডেটা লোড
load_dotenv()
API_ID = os.getenv("API_ID")
API_HASH = os.getenv("API_HASH")
BOT_TOKEN = os.getenv("BOT_TOKEN")

# বট ক্লায়েন্ট তৈরি
bot = Client("ServiceDownBot", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)

# স্টার্ট মেসেজ হ্যান্ডলার
@bot.on_message(filters.command("start") & filters.private)
async def start_message(client: Client, message: Message):
    await message.reply_text(
        "⚠️ দুঃখিত! এই বটের সার্ভিসে কিছু প্রবলেম হয়েছে।\n\n"
        "➡️ নতুন সার্ভিস ব্যবহার করতে অনুগ্রহ করে এই বটটি ব্যবহার করুন: @iPapkornPrimeBot"
    )

# সার্চ কমান্ড হ্যান্ডলার (যদি কেউ সার্চ দেয়)
@bot.on_message(filters.text & filters.private)
async def search_message(client: Client, message: Message):
    await message.reply_text(
        "⚠️ দুঃখিত! এই বটের সার্ভিসে কিছু প্রবলেম হয়েছে।\n\n"
        "➡️ নতুন সার্ভিস ব্যবহার করতে অনুগ্রহ করে এই বটটি ব্যবহার করুন: @iPapkornPrimeBot"
    )

# রান করুন
if __name__ == "__main__":
    print("Bot is running...")
    bot.run()
