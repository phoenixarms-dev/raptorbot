import os
import time
import telebot
from telebot import TeleBot, types
from dotenv import load_dotenv

bot = TeleBot("8469658985:AAFBpzqVOgVxgsi6haJX_LIF79hP1Dz6Txo")  # tymczasowo, możesz mieć to globalnie

def animated_startup(chat_id):
    lines = [
        "🧠 Uruchamianie systemu RapTOR®...",
        "🔹 Inicjalizacja modułów...",
        "🔹 Sprawdzanie połączenia z bazą danych...",
        "🔹 Ładowanie interfejsu użytkownika...",
        "✅ System gotowy do pracy."
    ]

    for line in lines:
        if line.strip():  # zabezpieczenie przed pustymi liniami
            bot.send_message(chat_id, line)
            time.sleep(0.6)


# === Główne menu ===
def send_main_menu(chat_id):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    row1 = [types.KeyboardButton("🛒 SKLEP"), types.KeyboardButton("📦 MAGAZYN"), types.KeyboardButton("👤 MOJE KONTO")]
    row2 = [types.KeyboardButton("🛡 ADMIN"), types.KeyboardButton("🤖 BOT"), types.KeyboardButton("📢 OGŁOSZENIA")]
    row3 = [types.KeyboardButton("📘 PORADY"), types.KeyboardButton("⚙️ USTAWIENIA")]
    markup.row(*row1)
    markup.row(*row2)
    markup.row(*row3)

    bot.send_message(chat_id, "📍 *Menu główne RapTOR®*", parse_mode="Markdown", reply_markup=markup)

# === Komenda /start ===
@bot.message_handler(commands=['start'])
def handle_start(message):
    chat_id = message.chat.id
    animated_startup(chat_id)
    send_main_menu(chat_id)

# === Pętla główna ===
def main():
    print("🚀 RapTOR® Bot uruchomiony...")
    bot.infinity_polling()

if __name__ == "__main__":
    main()




