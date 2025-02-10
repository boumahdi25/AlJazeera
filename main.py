from flask import Flask, request
import os
from telegram import Bot, Update
from telegram.ext import CommandHandler, CallbackContext, Updater

app = Flask(__name__)

TOKEN = os.environ.get('TELEGRAM_BOT_TOKEN')
bot = Bot(token=TOKEN)

def start(update: Update, context: CallbackContext):
    update.message.reply_text("Hello! Welcome to the bot.")

@app.route('/webhook', methods=['POST'])
def webhook():
    update = Update.de_json(request.get_json(force=True), bot)
    dispatcher.process_update(update)
    return "ok"

if __name__ == "__main__":
    updater = Updater(token=TOKEN, use_context=True)
    dispatcher = updater.dispatcher
    dispatcher.add_handler(CommandHandler('start', start))
    updater.start_webhook(listen="0.0.0.0",
                          port=int(os.environ.get('PORT', 5000)),
                          url_path=TOKEN)
    updater.bot.setWebhook('https://aljazeera.onrender.com/' + TOKEN)
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))
