from telegram.ext import Updater, CommandHandler

# Обработчик команды /limba
def limba(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Лимба топ")

def main():
    # Ваш токен бота
    token = '7259745980:AAGlcxRDHT2T6KqYwlICFa4B6Tnn6qQ3fDk'

    # Инициализация бота
    updater = Updater(token=token, use_context=True)
    dp = updater.dispatcher

    # Регистрация обработчика команды
    dp.add_handler(CommandHandler("limba", limba))

    # Запуск бота
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
