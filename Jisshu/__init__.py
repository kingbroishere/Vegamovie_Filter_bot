import time
from pyrogram import Client
from info import API_ID, API_HASH, BOT_TOKEN

StartTime = time.time()
__version__ = 1.1

# ✅ Create your bot client here
JisshuBot = Client(
    name="JisshuBot",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN,
    workers=50,
    plugins=dict(root="plugins")  # Optional: only if you're using plugin support
)
print("BOT_TOKEN:", BOT_TOKEN)
