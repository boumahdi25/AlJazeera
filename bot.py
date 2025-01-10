from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext

def start(update: Update, context: CallbackContext) -> None:
    update.message.reply_text('Bienvenue au Puzzle Game! Jouez ici: https://boumahdi25.github.io/PuzzleGame')

def main() -> None:
    # Remplacez 'VOTRE_TOKEN_D_ACCES' par le token de votre bot Telegram
    updater = Updater(token="7996757034:AAG0U9slaMBKu0SI_FgSHaSa9Zan-qhN6r4")
    dispatcher = updater.dispatcher

    # Ajouter un gestionnaire de commande pour la commande /start
    dispatcher.add_handler(CommandHandler("start", start))

    # Démarrer le bot
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
    
