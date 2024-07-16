from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Updater, CommandHandler, CallbackContext

def start(update: Update, context: CallbackContext) -> None:
    keyboard = [[InlineKeyboardButton("Open Calendar", url="https://your-app-name.vercel.app")]]
    reply_markup = InlineKeyboardMarkup(keyboard)
    update.message.reply_text('Please choose:', reply_markup=reply_markup)

def main():
    updater = Updater("7268516679:AAHn1DvVlkVj3nW2J1CrmqIg9hzcFBy-C4o")

    updater.dispatcher.add_handler(CommandHandler("start", start))

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
