import requests
from telegram.ext import Updater, CommandHandler, CallbackContext, MessageHandler
from telegram.update import Update
import settings
from telegram.ext.filters import Filters
updater = Updater(token=settings.TELEGRAM_TOKEN)


def start(update: Update, context: CallbackContext):
    update.message.\
        reply_text("Assalomu Aleykum. Vikipediadan maʼlumot qidiruvchi botga Xush kelibsiz. "
                   "Qidirish uchun /search va so‘rovingizni qoldiring. "
                   "Misol uchun: /search Amir Temur")


def search(update: Update, context: CallbackContext):
    args = context.args
    if len(args) == 0:
        update.message.reply_text('Hech bo‘lmaganda biron nima kiriting Masalan: /search Amir Temur')
        pass
    else:
        search_text = ' '.join(args)
        response = requests.get('https://uz.wikipedia.org/w/api.php', {
            'action': 'opensearch',
            'search': search_text,
            'limit': 1,
            'namespace': 0,
            'format': 'json',
        })
        result = response.json()
        link = result[3]
        if len(link):
            update.message.reply_text("Sizning so'rovingiz bo'yicha ilova: " + link[0])

        else:
            update.message.reply_text("Sizning so'rovingiz bo'yicha hech nima topilmadi.")


dispatcher = updater.dispatcher
dispatcher.add_handler(CommandHandler('start', start))
dispatcher.add_handler(CommandHandler('search', search))
dispatcher.add_handler(MessageHandler(Filters.all, start))

print("Bot starting...")
updater.start_polling()
updater.idle()
