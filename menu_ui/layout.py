from telebot import types

def login_menu():
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add(types.KeyboardButton("🔐 MAM KOD DOSTĘPU"))
    return markup

def auth_menu():
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add(types.KeyboardButton("🆔 Uwierzytelnij konto"), types.KeyboardButton("↩️ Wróć"))
    return markup

def main_menu():
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    row1 = [types.KeyboardButton("🛒 SKLEP"), types.KeyboardButton("📦 MAGAZYN"), types.KeyboardButton("👤 MOJE KONTO")]
    row2 = [types.KeyboardButton("🛡 ADMIN"), types.KeyboardButton("🤖 BOT"), types.KeyboardButton("📢 OGŁOSZENIA")]
    row3 = [types.KeyboardButton("📘 PORADY"), types.KeyboardButton("⚙️ USTAWIENIA")]
    markup.row(*row1)
    markup.row(*row2)
    markup.row(*row3)
    return markup
# === 📂 WZÓR PODMENU DLA KAŻDEJ KATEGORII ===
def submenu_template(title: str, buttons: list):
    """
    Uniwersalny szablon do generowania podmenu.
    :param title: nazwa kategorii np. 'SKLEP'
    :param buttons: lista tekstów przycisków
    """
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)

    rows = [types.KeyboardButton(btn) for btn in buttons]
    markup.add(*rows)
    markup.add(types.KeyboardButton("⬅️ Powrót"))
    return markup
