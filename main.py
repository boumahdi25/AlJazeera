from flask import Flask, request
import os
from telegram import Bot, Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import CommandHandler, CallbackQueryHandler, ApplicationBuilder, ContextTypes

app = Flask(__name__)

TOKEN = os.environ.get('TELEGRAM_BOT_TOKEN')
if not TOKEN:
    raise ValueError("TELEGRAM_BOT_TOKEN is not set")

bot = Bot(token=TOKEN)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton("🔵 Bouton 1", callback_data='1')],
        [InlineKeyboardButton("🔴 Bouton 2", callback_data='2')],
        [InlineKeyboardButton("🟢 Bouton 3", callback_data='3')]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text('Choisissez une option:', reply_markup=reply_markup)

async def button(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    if query.data == '1':
        await query.edit_message_text(text="Voici le puzzle : https://boumahdi25.github.io/AlJazeera/")
    elif query.data == '2':
        await query.edit_message_text(text="Vous avez cliqué sur le bouton 2")
    elif query.data == '3':
        await query.edit_message_text(text="Vous avez cliqué sur le bouton 3")

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




