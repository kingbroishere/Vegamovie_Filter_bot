import sys
import glob
import importlib
from pathlib import Path
from pyrogram import idle, Client, __version__
from pyrogram.raw.all import layer
from database.ia_filterdb import Media
from database.users_chats_db import db
from info import *
from utils import temp
from typing import Optional
from Script import script
from datetime import date, datetime
import pytz
from aiohttp import web
from plugins import web_server
import pyrogram.utils
import asyncio
import logging
import logging.config

# Setup logging
logging.config.fileConfig('logging.conf', disable_existing_loggers=False)
logging.getLogger().setLevel(logging.INFO)
logging.getLogger("pyrogram").setLevel(logging.ERROR)
logging.getLogger("aiohttp").setLevel(logging.ERROR)

# Fix for Pyrogram channel ID range issue
pyrogram.utils.MIN_CHANNEL_ID = -1009147483647

# Import the bot client
from Jisshu.bot import JisshuBot
from Jisshu.util.keepalive import ping_server
from Jisshu.bot.clients import initialize_clients


async def Jisshu_start():
    print("\n🚀 Initializing Jisshu Filter Bot...")
    
    bot_info = await JisshuBot.get_me()
    JisshuBot.username = bot_info.username

    await initialize_clients()

    # Load all plugin files
    for file in glob.glob("plugins/*.py"):
        plugin_name = Path(file).stem
        spec = importlib.util.spec_from_file_location(f"plugins.{plugin_name}", file)
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
        sys.modules[f"plugins.{plugin_name}"] = module
        print(f"✅ Plugin loaded: {plugin_name}")

    # Heroku/Render keep-alive
    if ON_HEROKU:
        asyncio.create_task(ping_server())

    # Load banned users/chats
    temp.BANNED_USERS, temp.BANNED_CHATS = await db.get_banned()

    # Setup database indexes
    await Media.ensure_indexes()

    me = await JisshuBot.get_me()
    temp.ME = me.id
    temp.U_NAME = me.username
    temp.B_NAME = me.first_name
    temp.B_LINK = me.mention

    logging.info(f"{me.first_name} running Pyrogram v{__version__} (Layer {layer}) on @{me.username}")
    logging.info(script.LOGO)

    # Send restart log
    now = datetime.now(pytz.timezone('Asia/Kolkata'))
    today = date.today()
    time_str = now.strftime("%H:%M:%S %p")
    await JisshuBot.send_message(LOG_CHANNEL, script.RESTART_TXT.format(me.mention, today, time_str))
    await JisshuBot.send_message(SUPPORT_GROUP, f"<b>{me.mention} restarted 🤖</b>")

    # Start web server (if needed for ping or endpoints)
    runner = web.AppRunner(await web_server())
    await runner.setup()
    site = web.TCPSite(runner, "0.0.0.0", int(PORT))
    await site.start()

    # Idle
    await idle()

    # Notify admins
    for admin in ADMINS:
        await JisshuBot.send_message(admin, f"<b>{me.mention} bot restarted ✅</b>")


if __name__ == "__main__":
    try:
        JisshuBot.run(Jisshu_start())
    except KeyboardInterrupt:
        logging.info("🛑 Bot stopped. Bye 👋")
        
