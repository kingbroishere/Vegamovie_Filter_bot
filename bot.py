import sys
import glob
import importlib
import logging
import logging.config
import asyncio
from pathlib import Path
from datetime import date, datetime

import pytz
from aiohttp import web
from pyrogram import Client, __version__, idle
from pyrogram.raw.all import layer

# Project imports
from Jisshu.bot import JisshuBot
from Jisshu.bot.clients import initialize_clients
from Jisshu.util.keepalive import ping_server
from database.ia_filterdb import Media
from database.users_chats_db import db
from info import *
from utils import temp
from Script import script
from plugins import web_server

# Setup logging
logging.config.fileConfig('logging.conf', disable_existing_loggers=False)
logging.getLogger().setLevel(logging.INFO)
logging.getLogger("pyrogram").setLevel(logging.ERROR)
logging.getLogger("aiohttp").setLevel(logging.ERROR)
logging.getLogger("aiohttp.web").setLevel(logging.ERROR)

# Minimum channel ID (to support large ID formats)
import pyrogram.utils
pyrogram.utils.MIN_CHANNEL_ID = -1009147483647

# Glob plugins
plugin_files = glob.glob("plugins/*.py")

# ---------------- Main Bot Function ----------------

async def Jisshu_start():
    print('\n🚀 Initializing Jisshu Filter Bot...')

    # Get bot info
    bot_info = await JisshuBot.get_me()
    JisshuBot.username = bot_info.username

    # Initialize user clients (multi-client)
    await initialize_clients()

    # Load plugins dynamically
    for plugin_path in plugin_files:
        plugin_name = Path(plugin_path).stem
        spec = importlib.util.spec_from_file_location(f"plugins.{plugin_name}", plugin_path)
        mod = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(mod)
        sys.modules[f"plugins.{plugin_name}"] = mod
        print(f"✅ Loaded plugin: {plugin_name}")

    # Ping Heroku/Web server
    if ON_HEROKU:
        asyncio.create_task(ping_server())

    # Get banned users/chats from DB
    temp.BANNED_USERS, temp.BANNED_CHATS = await db.get_banned()

    # Ensure indexes for DB
    await Media.ensure_indexes()

    # Set basic bot info in temp
    me = await JisshuBot.get_me()
    temp.ME = me.id
    temp.U_NAME = me.username
    temp.B_NAME = me.first_name
    temp.B_LINK = me.mention

    # Logging start info
    logging.info(f"🤖 Bot: {me.first_name} | Username: @{me.username}")
    logging.info(f"💾 Pyrogram v{__version__} | Layer {layer}")
    logging.info(script.LOGO)

    # Send startup messages
    tz = pytz.timezone('Asia/Kolkata')
    now = datetime.now(tz)
    today = date.today()
    time = now.strftime("%H:%M:%S %p")

    await JisshuBot.send_message(chat_id=LOG_CHANNEL, text=script.RESTART_TXT.format(me.mention, today, time))
    await JisshuBot.send_message(chat_id=SUPPORT_GROUP, text=f"<b>{me.mention} ʀᴇsᴛᴀʀᴛᴇᴅ 🤖</b>")

    # Start web server (API or ping)
    app_runner = web.AppRunner(await web_server())
    await app_runner.setup()
    await web.TCPSite(app_runner, "0.0.0.0", PORT).start()

    # Keep bot alive
    await idle()

    # Notify admins
    for admin_id in ADMINS:
        await JisshuBot.send_message(chat_id=admin_id, text=f"<b>{me.mention} ʙᴏᴛ ʀᴇsᴛᴀʀᴛᴇᴅ ✅</b>")


# ---------------- Entrypoint ----------------

if __name__ == "__main__":
    try:
        # Only run — don't call .start() manually
        JisshuBot.run(Jisshu_start())
    except KeyboardInterrupt:
        logging.info("🚪 Bot Stopped Manually. Goodbye 👋")
        
