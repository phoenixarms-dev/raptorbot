from telebot import types
from loguru import logger
from menu_ui.layout import main_menu, submenu_template


def handle_main_menu(bot):
    """
    Główny router obsługujący kliknięcia przycisków w panelu RapTOR®.
    """
    @bot.message_handler(func=lambda msg: msg.text in [
        "🏪 SKLEP", "📦 MAGAZYN", "👤 MOJE KONTO",
        "🛡 ADMIN", "🤖 BOT", "📢 OGŁOSZENIA",
        "📚 PORADY", "⚙️ USTAWIENIA", "⬅️ Powrót"
    ])
    def route(msg):
        text = msg.text
        logger.info(f"[MenuRouter] {msg.from_user.username} kliknął: {text}")

        # Obsługa "Powrót"
        if text == "⬅️ Powrót":
            bot.send_message(msg.chat.id, "🔙 Powrót do głównego panelu:", reply_markup=main_menu())
            return

        # === Sekcje główne ===
        if text == "🏪 SKLEP":
            submenu = submenu_template("Sklep", ["🛒 Produkty", "💰 Promocje", "📦 Zamówienia"])
            bot.send_message(msg.chat.id, "🛒 *Panel SKLEPU*", parse_mode="Markdown", reply_markup=submenu)

        elif text == "📦 MAGAZYN":
            submenu = submenu_template("Magazyn", ["📋 Stany", "➕ Dodaj towar", "📤 Wydania"])
            bot.send_message(msg.chat.id, "📦 *Panel MAGAZYNU*", parse_mode="Markdown", reply_markup=submenu)

        elif text == "👤 MOJE KONTO":
            submenu = submenu_template("Konto", ["💳 Status", "🔄 Reset hasła", "📨 Powiadomienia"])
            bot.send_message(msg.chat.id, "👤 *Twoje konto*", parse_mode="Markdown", reply_markup=submenu)

        elif text == "🛡 ADMIN":
            submenu = submenu_template("Admin", ["🧩 Zarządzaj użytkownikami", "🧠 Statystyki", "🧰 Narzędzia"])
            bot.send_message(msg.chat.id, "🛡 *Panel ADMINISTRACYJNY*", parse_mode="Markdown", reply_markup=submenu)

        elif text == "🤖 BOT":
            submenu = submenu_template("Bot", ["⚙️ Ustawienia bota", "🪪 Tokeny", "📈 Logi"])
            bot.send_message(msg.chat.id, "🤖 *Panel BOTA*", parse_mode="Markdown", reply_markup=submenu)

        elif text == "📢 OGŁOSZENIA":
            submenu = submenu_template("Ogłoszenia", ["📣 Nowe ogłoszenie", "📜 Historia"])
            bot.send_message(msg.chat.id, "📢 *Centrum ogłoszeń*", parse_mode="Markdown", reply_markup=submenu)

        elif text == "📚 PORADY":
            submenu = submenu_template("Porady", ["📘 FAQ", "🧩 Instrukcje", "💬 Wsparcie"])
            bot.send_message(msg.chat.id, "📚 *Panel Pomocy*", parse_mode="Markdown", reply_markup=submenu)

        elif text == "⚙️ USTAWIENIA":
            submenu = submenu_template("Ustawienia", ["🌙 Tryb ciemny", "🔔 Powiadomienia", "🌐 Język"])
            bot.send_message(msg.chat.id, "⚙️ *Ustawienia systemowe*", parse_mode="Markdown", reply_markup=submenu)

        else:
            bot.send_message(msg.chat.id, "❓ Nieznana komenda.", reply_markup=main_menu())
