import webbrowser
import os
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler

# Ouvre automatiquement index.html dans le navigateur
webbrowser.open(f'file://{os.path.abspath("index.html")}')

# Fonction de démarrage pour la commande /start
async def start(update: Update, context) -> None:
    await update.message.reply_text('Bienvenue au Puzzle Game! Jouez ici: https://boumahdi25.github.io/PuzzleGame')

# Fonction principale qui lance le bot
def main() -> None:
    # Remplacez 'VOTRE_TOKEN_D_ACCES' par le token de votre bot Telegram
    token = "8165761277:AAH-dafuWHa61Trd005X_839YgiCO9xaZJw"


    # Création de l'application avec le token
    app = ApplicationBuilder().token(token).build()

    # Ajouter un gestionnaire de commande pour la commande /start
    app.add_handler(CommandHandler("start", start))

    # Démarrer le bot
    app.run_polling()

if __name__ == '__main__':
    main()
