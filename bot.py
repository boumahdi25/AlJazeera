import os
from telegram import Bot, Update
from telegram.ext import CommandHandler, CallbackContext, Updater

# Votre fonction de démarrage de bot
def start(update: Update, context: CallbackContext):
    update.message.reply_text('Hello! Bot is running.')

# Configurez le bot avec votre token
TOKEN = os.getenv('7963739930:AAGLR3reZEHliOWOG6lshDZ02miBzkSOAdg')
bot = Bot(token=TOKEN)

# Configurez l'updater et dispatcher
updater = Updater(bot=bot, use_context=True)
dispatcher = updater.dispatcher

# Ajoutez des handlers
dispatcher.add_handler(CommandHandler('start', start))

# Utilisez le port spécifié par Render
PORT = int(os.environ.get('PORT', '8443'))

# Démarrez le bot avec webhook
updater.start_webhook(listen="0.0.0.0", port=PORT, url_path=TOKEN)
updater.bot.setWebhook(f"https://{os.getenv('RENDER_EXTERNAL_HOSTNAME')}/{TOKEN}")

updater.idle()
