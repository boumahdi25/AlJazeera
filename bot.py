import os
from dotenv import load_dotenv
from telegram import Bot, Update
from telegram.ext import CommandHandler, CallbackContext, Updater

# Charger les variables d'environnement
load_dotenv()

# Récupérer le token depuis le fichier .env
TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
if not TOKEN:
    raise ValueError("Token Telegram manquant. Vérifie ton fichier .env.")

bot = Bot(token=TOKEN)

# Fonction de démarrage du bot
def start(update: Update, context: CallbackContext):
    update.message.reply_text("Hello! Bot is running.")

# Configuration de l'updater et du dispatcher
updater = Updater(bot=bot, use_context=True)
dispatcher = updater.dispatcher

# Ajouter le handler pour la commande /start
dispatcher.add_handler(CommandHandler("start", start))

# Utilisation du port et webhook
PORT = int(os.environ.get("PORT", 8443))
updater.start_webhook(listen="0.0.0.0", port=PORT, url_path=TOKEN)
updater.bot.setWebhook(f"https://{os.getenv('RENDER_EXTERNAL_HOSTNAME')}/{TOKEN}")

updater.idle()

