from pyrogram import Client, filters

@Client.on_message(filters.command("start") & filters.private)
async def start(client, message):
    await message.reply_text("👋 Hello! I am your Movie Filter Bot.\n\nSend me a movie name to get download links.")
