from telegram.ext import CallbackContext, ConversationHandler
from actions import get_contact, add_contact, get_all_contacts, delete_contact
from telegram import Update, ReplyKeyboardRemove
import logging
import json

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
    logger.info('add_contact, name: {}, phone: {}'.format(context.user_data['name'], context.user_data['phone']))
    context.user_data.clear()
    update.message.reply_text('New contact added!!!')
    return ConversationHandler.END


def start_delete_contact(update: Update, context: CallbackContext) -> int:
    logger.info('delete_contact, user: {}'.format(update.message.from_user.id))
    update.message.reply_text('Please, enter name of contact')
    return NAME


def delete_one(update: Update, context: CallbackContext) -> int:
    name = update.message.text
    owner = update.message.from_user.id
    result = delete_contact(name, owner)
    logger.info('delete_one_contact, name: {}, owner: {}'.format(name, owner))
    if result:
        update.message.reply_text('Contact deleted!!!')
    update.message.reply_text('No such contact')
    return ConversationHandler.END


def get_all(update: Update, context: CallbackContext) -> int:
    logger.info('get_all_contact, user: {}'.format(update.message.from_user.id))
    all_contacts = ''
    contacts = get_all_contacts(update.message.from_user.id)
    for i in range(len(contacts)):
        all_contacts += '{}. {} - {}\n'.format(i + 1, contacts[i].name, contacts[i].phone)
    update.message.reply_text(all_contacts)


def json_handler(update: Update, context: CallbackContext) -> int:
    logger.info('json, user: {}'.format(update.message.from_user.id))
    with open('{}.json'.format(update.message.from_user.id), 'w') as file:
        contacts = get_all_contacts(update.message.from_user.id)
        contacts_json = {}
        for i in contacts:
            contacts_json[i.id] = {'name': i.name, 'phone': i.phone}
        json_data = json.dumps(contacts_json)
        file.write(json_data)
    filename = '{}.json'.format(update.message.from_user.id)
    update.message.reply_document(document=open(filename))


def cancel(update: Update, context: CallbackContext) -> int:
    user = update.message.from_user
    logger.info("User %s canceled the conversation.", user.first_name)
    context.user_data.clear()
    update.message.reply_text(
        'Bye! I hope we can talk again some day.', reply_markup=ReplyKeyboardRemove()
    )

    return ConversationHandler.END
