import telegram

from telegram.ext import Updater, MessageHandler, Filters

def welcome(update, context):

    new_member = update.message.new_chat_members[0]

    context.bot.send_message(chat_id=update.effective_chat.id, text=f"Welcome to the group, {new_member.first_name}!")

def main():

    updater = Updater("YOUR_BOT_TOKEN")

    dispatcher = updater.dispatcher

    dispatcher.add_handler(MessageHandler(Filters.status_update.new_chat_members, welcome))

    updater.start_polling()

    updater.idle()

if __name__ == '__main__':

    main()
