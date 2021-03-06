import os
from . import handlers
import logging
from telegram.ext import Updater, Filters, CallbackContext
from telegram.ext import CommandHandler, ConversationHandler, MessageHandler
from tg.telegram_consts import WELCOME_MESSAGE
from telegram import ReplyKeyboardMarkup, Update


def start(update: Update, context: CallbackContext):
    reply_keyboard = [['Get contact', 'Add contact'], ['Delete contact', 'Get all contacts']]
    update.message.reply_text(WELCOME_MESSAGE,
                              reply_markup=ReplyKeyboardMarkup(
                                  reply_keyboard, one_time_keyboard=False, input_field_placeholder='Select action'
                              ),
                              )


def start_bot() -> None:
    updater = Updater(token=os.environ['TOKEN'], use_context=True)
    dispatcher = updater.dispatcher
    logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                        level=logging.INFO)

    get_contact_handler = ConversationHandler(
        entry_points=[MessageHandler(Filters.regex("Get contact"), handlers.start_get_contact)],
        states={
            handlers.NAME: [MessageHandler(Filters.text & ~Filters.command & ~Filters.regex(
                '^(Get contact|Add contact|Get all contacts|Delete contact|)$'), handlers.find_contact)],
        },
        allow_reentry=True,
        fallbacks=[CommandHandler('cancel', handlers.cancel)],
    )

    add_contact_handler = ConversationHandler(
        entry_points=[MessageHandler(Filters.regex("Add contact"), handlers.start_add_contact)],
        states={
            handlers.NAME: [MessageHandler(Filters.text & ~Filters.command & ~Filters.regex(
                '^(Get contact|Add contact|Get all contacts|Delete contact|)$'), handlers.add_name)],
            handlers.PHONE: [MessageHandler(Filters.text & ~Filters.command & ~Filters.regex(
                '^(Get contact|Add contact|Get all contacts|Delete contact|)$'), handlers.add_phone)]
        },
        allow_reentry=True,
        fallbacks=[CommandHandler('cancel', handlers.cancel)],
    )

    delete_contact_handler = ConversationHandler(
        entry_points=[MessageHandler(Filters.regex('Delete contact'), handlers.start_delete_contact)],
        states={
            handlers.NAME: [MessageHandler(Filters.text & ~Filters.command & ~Filters.regex(
                '^(Get contact|Add contact|Get all contacts|Delete contact|)$'), handlers.delete_one)],
        },

        allow_reentry=True,
        fallbacks=[CommandHandler('cancel', handlers.cancel)],
    )
    get_all_contacts = MessageHandler(Filters.regex('Get all contacts'), handlers.get_all)

    json_handler = CommandHandler('json', handlers.json_handler)

    dispatcher.add_handler(get_contact_handler)
    dispatcher.add_handler(add_contact_handler)
    dispatcher.add_handler(get_all_contacts)
    dispatcher.add_handler(delete_contact_handler)
    dispatcher.add_handler(json_handler)

    start_handler = CommandHandler('start', start)
    dispatcher.add_handler(start_handler)
    updater.start_polling()
    updater.idle()
