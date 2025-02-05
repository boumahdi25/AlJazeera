import webbrowser
import os
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, CallbackContext

# Remplacez par le token de votre bot
TOKEN = "7963739930:AAGLR3reZEHliOWOG6lshDZ02miBzkSOAdg"

async def start(update: Update, context: CallbackContext):
    await update.message.reply_text("Bonjour! Je suis votre bot.")

def main():
    app = ApplicationBuilder().token(TOKEN).build()

    # Commande /start
    app.add_handler(CommandHandler("start", start))

    # Lancer le bot
    app.run_polling(drop_pending_updates=True)

if __name__ == '__main__':
    main()

