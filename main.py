from flask import Flask, request
import os
from telegram import Bot, Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import CommandHandler, CallbackQueryHandler, ApplicationBuilder

app = Flask(__name__)

TOKEN = os.environ.get('TELEGRAM_BOT_TOKEN')
bot = Bot(token=TOKEN)

def start(update: Update, context):
    keyboard = [
        [InlineKeyboardButton("Bouton 1", callback_data='1')],
        [InlineKeyboardButton("Bouton 2", callback_data='2')],
        [InlineKeyboardButton("Bouton 3", callback_data='3')]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    update.message.reply_text('Choisissez une option:', reply_markup=reply_markup)

def button(update: Update, context):
    query = update.callback_query
    query.answer()
    query.edit_message_text(text=f"Vous avez cliqué sur le bouton {query.data}")

@app.route('/webhook', methods=['POST'])
def webhook():
    update = Update.de_json(request.get_json(force=True), bot)
    application.update_queue.put(update)
    return "ok"

if __name__ == "__main__":
    application = ApplicationBuilder().token(TOKEN).build()

    application.add_handler(CommandHandler("start", start))
    application.add_handler(CallbackQueryHandler(button))

    application.run_webhook(
        listen="0.0.0.0",
        port=int(os.environ.get('PORT', 5000)),
        url_path=TOKEN,
        webhook_url='https://aljazeera.onrender.com/' + TOKEN
    )

    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))
