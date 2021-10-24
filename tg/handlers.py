from . import tg
from telegram.ext import CallbackContext, ConversationHandler
from actions import get_contact, add_contact
from telegram import Update, ReplyKeyboardRemove
import logging

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO
)

NAME, PHONE = range(2)
logger = logging.getLogger(__name__)


def start_get_contact(update: Update, context: CallbackContext) -> int:
    update.message.reply_text('Please, enter name of contact')
    logger.info("start_one_contact")
    return NAME


def find_contact(update: Update, context: CallbackContext) -> int:
    name = update.message.text
    owner = update.message.from_user.id
    phone = get_contact(name, owner)
    logger.info('get_one_contact, name: {}, owner: {}'.format(name, owner))
    if phone is not None:
        update.message.reply_text('{}: {}'.format(name, phone))
        return
    update.message.reply_text("Cannot find this contact")
    return ConversationHandler.END


def start_add_contact(update: Update, context: CallbackContext) -> int:
    update.message.reply_text('Please, enter name of contact')
    logger.info('start_add_contact')
    return NAME


def add_name(update: Update, context: CallbackContext) -> int:
    context.user_data['name'] = update.message.text
    update.message.reply_text("Please, enter contact number:")
    return PHONE


def add_phone(update: Update, context: CallbackContext) -> int:
    context.user_data['phone'] = update.message.text
    add_contact(context.user_data['name'], context.user_data['phone'], update.message.from_user.id)
    context.user_data.clear()
    update.message.reply_text('New contact added!!!')
    return ConversationHandler.END


def cancel(update: Update, context: CallbackContext) -> int:
    user = update.message.from_user
    logger.info("User %s canceled the conversation.", user.first_name)
    update.message.reply_text(
        'Bye! I hope we can talk again some day.', reply_markup=ReplyKeyboardRemove()
    )

    return ConversationHandler.END
