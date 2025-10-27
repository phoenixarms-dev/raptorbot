def register_handlers(bot):
    @bot.message_handler(commands=['menu'])
    def handle_menu(message):
        bot.reply_to(message, "📋 Menu główne (wkrótce interfejs UI).")
