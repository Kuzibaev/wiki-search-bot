from telegram.ext import Updater, CommandHandler, CallbackContext
from telegram.update import Update
import settings

updater = Updater(token=settings.TELEGRAM_TOKEN)


def start(update: Update, context: CallbackContext):
    print(update)
    update.message.reply_text("Salom!")
    context.bot.send_message(chat_id=update.message.chat_id, text="Salom yana bir bor.")


dispatcher = updater.dispatcher
dispatcher.add_handler(CommandHandler('start', start))


print("Bot starting...")
updater.start_polling()
updater.idle()
