from telegram.ext import Updater
from telegram.ext import CommandHandler
import logging


def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="I'm a bot, please talk to me!")


def start_bot():
    updater = Updater(token='2022169707:AAG08QHonsEYg11CV9cnyV9780qVzPrpcz4', use_context=True)
    dispatcher = updater.dispatcher
    logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                        level=logging.INFO)


    start_handler = CommandHandler('start', start)
    dispatcher.add_handler(start_handler)
    updater.start_polling()
    updater.idle()
