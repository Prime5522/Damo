from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from flask import Flask
from threading import Thread
import os
import asyncio  # অটো-ডিলিটের জন্য
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

# যে কোন মেসেজ পেলেই উত্তর দেওয়া এবং ৫ মিনিট পর অটো-ডিলিট করা
@bot.on_message(filters.all)
async def handle_all_messages(client: Client, message: Message):
    try:
        # বটের প্রথম রিপ্লাই পাঠানো
        sent_message = await message.reply_text(
            """📢 গুরুত্বপূর্ণ ঘোষণা – Important Announcement – महत्वपूर्ण सूचना

📢 গুরুতর ঘোষণা!
🔴 কিছু কারিগরি সমস্যার কারণে এই বটটি বন্ধ রয়েছে। তবে, নতুন বটটি আগের মতোই কাজ করবে, তবে কিছু সময়ের জন্য ফাইলগুলো সরাসরি আসবে এবং কোনো অ্যাড থাকবে না!
➡️ নতুন বটের লিঙ্ক: @iPapkornPrimeBot

📌 এটা গ্রুপ এডমিনদের জন্য যারা আমাদের বটকে আপনাদের গ্রুপে এড করেছেন ➕
এডমিনগণ নতুন বটটি গ্রুপে এড করে আগের মতোই ব্যবহার করতে পারবেন। কিছু সময়ের জন্য ফাইলগুলো সরাসরি আসবে, এবং কোনো বিজ্ঞাপন থাকবে না! 🚀

✯  ━━━━━━ ✧  ━━━━━━ ✯

📢 Important Announcement
🔴 Due to technical issues, this bot has been shut down. But the new bot will work the same as before, with files now coming directly for some time, without any ads!
➡️ New bot link: @iPapkornPrimeBot

📌 This is for group admins who added our bot to your group ➕
Admins, add the new bot to your group. For some time, files will come directly, without any ads! 🚀

✯  ━━━━━━ ✧  ━━━━━━ ✯

📢 महत्वपूर्ण सूचना
🔴 कुछ तकनीकी समस्याओं के कारण हमारा बॉट बंद हो गया है। लेकिन नया बोट पहले जैसा ही काम करेगा, केवल कुछ समय के लिए फाइलें सीधे आएंगी, बिना किसी विज्ञापन के!
➡️ नया बोट लिंक: @iPapkornPrimeBot

📌 यह उन ग्रुप एडमिन के लिए है जिन्होंने हमारे बॉट को आपके ग्रुप में जोड़ा है ➕
एडमिन कृपया नए बोट को अपने ग्रुप में जोड़ें। कुछ समय के लिए फाइलें सीधे आएंगी, और कोई विज्ञापन नहीं होगा! 🚀 """,
            reply_markup=InlineKeyboardMarkup(
                [
                    [InlineKeyboardButton("🔗 ɢᴏ ᴛᴏ ɴᴇᴡ ʙᴏᴛ", url="https://t.me/iPapkornPrimeBot")]
                ]
            )
        )

        # ৫ মিনিট (২৫০ সেকেন্ড) অপেক্ষা করা
        await asyncio.sleep(70)

        # প্রথম মেসেজ ডিলিট করা
        await sent_message.delete()

        # নতুন মেসেজ পাঠানো যেখানে লেখা থাকবে "🚨 Message Deleted" এবং একই বাটন থাকবে
        await message.reply_photo(
            photo="https://envs.sh/ars.jpg",  # এখানে আপনার ইমেজ লিংক দিন
            caption="🚨 **Message Deleted Please Join Our New Bot 👇👇.\n\n There's a little problem here, so everyone can use our new bot. 👇**",
            reply_markup=InlineKeyboardMarkup(
                [
                    [InlineKeyboardButton("🔗 ɢᴏ ᴛᴏ ɴᴇᴡ ʙᴏᴛ", url="https://t.me/iPapkornPrimeBot")]
                ]
            )
        )

    except Exception as e:
        print(f"Error while handling message: {e}")

# বট এবং Flask HTTP সার্ভার চালু করা
if __name__ == "__main__":
    try:
        print("Bot is running...")
        Thread(target=run).start()  # Flask HTTP সার্ভার চালানো
        bot.run()  # Pyrogram বট চালানো
    except Exception as e:
        print(f"Error while starting bot or server: {e}")
