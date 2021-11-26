from telegram.ext import Updater, CallbackContext, CommandHandler, CallbackQueryHandler
import logging
from telegram.replymarkup import ReplyMarkup
from query_lib import query_lib
from settings import TOKEN
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from datetime import datetime

# Setup

updater = Updater(token=TOKEN, use_context=True)
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
dispatcher = updater.dispatcher



# Methods
inline_kb = [
    [InlineKeyboardButton("Li Ka Shing Library", callback_data=0)],
    [InlineKeyboardButton("Kwa Geok Choo Law Library", callback_data=1)]
]
markup = InlineKeyboardMarkup(inline_kb)

def start(update: Update, context: CallbackContext):
    update.message.reply_text(text="Welcome to the SMU Capacity bot! Where are you headed?", reply_markup=markup)

def button_click(update: Update, context: CallbackContext):
    query = update.callback_query
    occupancy = query_lib(query.data)
    print(occupancy)

    lib_string = ""
    if query.data == "0":
        lib_string = "Lee Ka Shing Library"
    elif query.data == "1":
        lib_string = "Kwa Geok Choo Law Library"
    now = datetime.now()

    query.answer()
    query.edit_message_text(f"Occupancy for: {lib_string}\nAt datetime: {now.strftime('%m/%d/%Y, %H:%M:%S')}:\n\n{occupancy['current']} / {occupancy['max']}", reply_markup=markup)

# Init handlers and launch

start_handler = CommandHandler('start', start)
dispatcher.add_handler(start_handler)
dispatcher.add_handler(CallbackQueryHandler(button_click))
updater.start_polling()
updater.idle()

