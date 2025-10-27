from telebot import types
from menu_ui.layout import login_menu, auth_menu, main_menu
from loguru import logger

# Prosty system sesji (tymczasowy)
user_sessions = {}

def handle_login(bot):
    @bot.message_handler(commands=['start'])
    def start(msg):
        user_id = msg.from_user.id
        logger.info(f"User {user_id} wystartował bota")
        bot.send_message(msg.chat.id,
                         "🦅 Witaj w *RapTOR Secure Access Panel*\n\n"
                         "Wybierz jedną z opcji:",
                         parse_mode="Markdown",
                         reply_markup=login_menu())

    @bot.message_handler(func=lambda m: m.text == "🔐 MAM KOD DOSTĘPU")
    def ask_password(msg):
        bot.send_message(msg.chat.id, "🔑 Podaj hasło dostępu:")
        bot.register_next_step_handler(msg, verify_password)


    def verify_password(msg):
        password = msg.text.strip()
        # Dla testu – hasło z .env albo "admin123"
        import os
        from dotenv import load_dotenv
        load_dotenv()

        expected = os.getenv("ACCESS_PASS", "admin123")
        if password == expected:
            user_sessions[msg.from_user.id] = True
            bot.send_message(msg.chat.id, "✅ Dostęp przyznany!", reply_markup=main_menu())
            logger.success(f"User {msg.from_user.username} zalogowany")
        else:
            bot.send_message(msg.chat.id, "❌ Błędne hasło! Spróbuj ponownie.", reply_markup=login_menu())
            logger.warning(f"User {msg.from_user.id} błędne hasło")
