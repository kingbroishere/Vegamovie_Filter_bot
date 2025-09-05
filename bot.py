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
from pyrogram import __version__, idle
from pyrogram.raw.all import layer
import pyrogram.utils

from Jisshu.bot import JisshuBot
from Jisshu.bot.clients import initialize_clients
from Jisshu.util.keepalive import ping_server
from database.ia_filterdb import Media
from database.users_chats_db import db
from info import *
from utils import temp
from Script import script
from plugins import web_server

# Logging setup
logging.config.fileConfig('logging.conf', disable_existing_loggers=False)
logging.getLogger().setLevel(logging.INFO)
logging.getLogger("pyrogram").setLevel(logging.ERROR)
logging.getLogger("aiohttp").setLevel(logging.ERROR)
logging.getLogger("aiohttp.web").setLevel(logging.ERROR)

# Fix for channel ID parsing
pyrogram.utils.MIN_CHANNEL_ID = -1009147483647

# Plugin paths
plugin_files = glob.glob("plugins/*.py")

# ---------------- Main Bot Function ----------------

async def main():
    print('\n🚀 Initializing Jisshu Filter Bot...')

    async with JisshuBot:
        # ✅ Now bot is started, it's safe to call get_me()
        me = await JisshuBot.get_me()
        JisshuBot.username = me.username

        # Initialize clients
        await initialize_clients()

        # Load plugins
        for plugin_path in plugin_files:
            plugin_name = Path(plugin_path).stem
            spec = importlib.util.spec_from_file_location(f"plugins.{plugin_name}", plugin_path)
            mod = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(mod)
            sys.modules[f"plugins.{plugin_name}"] = mod
            print(f"✅ Loaded plugin: {plugin_name}")

        # Ping server (Heroku)
        if ON_HEROKU:
            asyncio.create_task(ping_server())

        # Banned users/chats
        temp.BANNED_USERS, temp.BANNED_CHATS = await db.get_banned()
        await Media.ensure_indexes()

        # Set bot info
        temp.ME = me.id
        temp.U_NAME = me.username
        temp.B_NAME = me.first_name
        temp.B_LINK = me.mention

        # Log
        logging.info(f"🤖 Bot: {me.first_name} | Username: @{me.username}")
        logging.info(f"💾 Pyrogram v{__version__} | Layer {layer}")
        logging.info(script.LOGO)

        # Notify
        tz = pytz.timezone('Asia/Kolkata')
        now = datetime.now(tz)
        today = date.today()
        time = now.strftime("%H:%M:%S %p")

        await JisshuBot.send_message(LOG_CHANNEL, script.RESTART_TXT.format(me.mention, today, time))
        await JisshuBot.send_message(SUPPORT_GROUP, f"<b>{me.mention} ʀᴇsᴛᴀʀᴛᴇᴅ 🤖</b>")

        # Web server
        app_runner = web.AppRunner(await web_server())
        await app_runner.setup()
        await web.TCPSite(app_runner, "0.0.0.0", PORT).start()

        # Idle loop
        await idle()

        # Notify admins
        for admin_id in ADMINS:
            await JisshuBot.send_message(admin_id, f"<b>{me.mention} ʙᴏᴛ ʀᴇsᴛᴀʀᴛᴇᴅ ✅</b>")


# ---------------- Entrypoint ----------------

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        logging.info("🚪 Bot Stopped Manually. Goodbye 👋")
        
