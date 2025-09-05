import asyncio
import logging
from info import *
from pyrogram import Client
from Jisshu.util.config_parser import TokenParser
from . import multi_clients, work_loads, JisshuBot

async def initialize_clients():
    multi_clients[0] = JisshuBot
    work_loads[0] = 0

    all_tokens = TokenParser().parse_from_env()
    if not all_tokens:
        print("No additional clients found, using default client")
        return

    async def start_client(client_id, token):
        try:
            print(f"Starting - Client {client_id}")
            if client_id == len(all_tokens):
                await asyncio.sleep(2)
                print("This will take some time, please wait...")

            # 🛠 Create Client instance first
            client = Client(
                name=str(client_id),
                api_id=API_ID,
                api_hash=API_HASH,
                bot_token=token,
                sleep_threshold=SLEEP_THRESHOLD,
                no_updates=True,
                in_memory=True
            )

            # ✅ Start within the same event loop
            await client.start()
            work_loads[client_id] = 0
            return client_id, client

        except Exception:
            logging.error(f"Failed starting Client - {client_id} Error:", exc_info=True)

    # Use asyncio.gather to run all clients concurrently
    clients = await asyncio.gather(
        *[start_client(i, token) for i, token in all_tokens.items()],
        return_exceptions=False  # Optional: catch errors manually if needed
    )

    multi_clients.update(dict(filter(None, clients)))

    if len(multi_clients) != 1:
        print("Multi-Client Mode Enabled")
    else:
        print("No additional clients were initialized, using default client")
