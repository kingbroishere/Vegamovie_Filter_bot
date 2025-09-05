from flask import Flask, request
import telegram
import os

app = Flask(__name__)

# Load bot token from environment variable or paste directly (not recommended)
TOKEN = os.getenv("BOT_TOKEN")  # Make sure this is set in Render
bot = telegram.Bot(token=TOKEN)

@app.route("/")
def hello_world():
    return "Jisshu bots"

# This route handles POST requests from Telegram
@app.route(f"/{TOKEN}", methods=["POST"])
def webhook():
    update = telegram.Update.de_json(request.get_json(force=True), bot)
    
    # Handle simple start command
    if update.message and update.message.text == "/start":
        chat_id = update.message.chat_id
        bot.send_message(chat_id=chat_id, text="Hello! I'm alive.")
    
    return "OK", 200
