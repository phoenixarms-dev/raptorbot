import os
import sys
from loguru import logger
from dotenv import load_dotenv
import telebot
from handlers.auth import handle_login
from routers.menu_router import handle_main_menu


# dodaj libs do ścieżki
sys.path.append(os.path.join(os.path.dirname(__file__), "..", "libs"))

# importy modułów
from handlers.auth import handle_login

load_dotenv()

def main():
    logger.info("🚀 RapTOR™ Bot startuje...")

    token = os.getenv("BOT_TOKEN")
    if not token:
        logger.error("❌ Brak BOT_TOKEN w .env")
        return

    bot = telebot.TeleBot(token)

    # logowanie / autoryzacja
    handle_login(bot)
    
    # Menu Router 
    handle_main_menu(bot)


    logger.success("✅ Bot działa i czeka na użytkowników...")
    bot.infinity_polling()


if __name__ == "__main__":
    main()
