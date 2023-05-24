#1. Import the necessary libraries:

import telegram
from telegram.ext import Updater, CommandHandler
import time
import random
import datetime

def get_chat_id(bot_token, username=None,groupname=None):
    bot = telegram.Bot(token=bot_token)
    if username:
        user = bot.get_chat(username=username)
        chat_id = user.id
    elif groupname:
        group = bot.get_chat(chat_id = groupname)
        chat_id = group.id
    return chat_id


#2. Create a function to get a sample message:

def get_sample_message(bot):
    updates = bot.get_updates()
    if updates:
        latest_update = updates[-1]
        message = latest_update.message
        return message.text
    return None

#bot.get_chat_history

#3. Create a function to send messages to different persons and groups at specific times:

# Define a function to send messages repeatedly at a specific interval
def send_messages(bot_token, chat_ids, message, interval, end_time):
    bot = telegram.Bot(token=bot_token)
    while True:
        now = datetime.datetime.now()
        for chat_id in chat_ids:
            bot.send_message(chat_id=chat_id, text=message)
        time.sleep(interval)
        if now.strftime('%m/%d/%Y') <= end_time:
            break

# import datetime
# t = datetime.datetime(2012, 2, 23, 0, 0)
# t.strftime('%m/%d/%Y')
# '05/24/2023'

# def send_messages_at_time(bot, chat_id, message, send_time):
#     while True:
#         now = datetime.datetime.now()
#         if now >= send_time:
#             bot.send_message(chat_id=chat_id, text= message)
#             break
#         time.sleep(60)

#4. Create a function to search for messages with specific words in different groups:

def search_message(bot_token, chat_ids, keywords,id):
    bot = telegram.Bot(token=bot_token)
    for chat_id in chat_ids:
        messages = bot.get_chat_history(chat_id)
        for message in messages:
            for keyword in keywords:
                if keyword in message.text:
                    bot.send_message(chat_id=id, text=message.text)

#5. Create the main function to run the bot:

# Define a command handler for the /search command
def send(update, context):
    # Get the list of chat IDs and keywords from the user's input
    chat_ids = get_chat_id(bot_token,groupname=context.args[0].split(','))
    interval = context.args[1:2].split(',')
    end_time = context.args[2:3].split(',')
    bot = telegram.Bot(token=bot_token)
    # Call the send_messages function to send messages

    send_messages(bot_token,chat_ids,message=get_sample_message(bot),interval=interval, end_time=end_time)

def search(update, context):
    # Get the list of chat IDs and keywords from the user's input
    chat_ids = get_chat_id(bot_token,groupname=context.args[0].split(','))
    keywords = context.args[1:]
    id=update.effective_chat.id
    # Call the search_messages function to search for messages

    search_message(bot_token, chat_ids, keywords, id)

# Define the main function that runs the bot
def main():
    # Create an instance of the Updater class with your bot's API token
    updater = Updater(bot_token, use_context=True)
    # Get the dispatcher to register handlers
    dp = updater.dispatcher
    # Register the search handler for the /search command
    dp.add_handler(CommandHandler("search", search))
    dp.add_handler(CommandHandler("search", send))
    # Start the bot
    updater.start_polling()
    # Run the bot until you press Ctrl-C or the process is stopped
    updater.idle()

if __name__ == '__main__':
    # Replace bot_token with your bot's API token
    bot_token = 'YOUR_BOT_API_TOKEN'
    main()


#########################3
# def main():
#     # Your code to initialize the bot and get the necessary credentials goes here
#     bot = telegram.Bot(token='YOUR_API_KEY')

#     # Get a sample message
#     message = get_sample_message()

#     # Send messages to different persons and groups at specific times
#     chat_ids = ['PERSON_CHAT_ID_1', 'PERSON_CHAT_ID_2', 'GROUP_CHAT_ID_1', 'GROUP_CHAT_ID_2']
#     send_messages(bot, chat_ids, message)

#     # Search for messages with specific words in different groups
#     group_ids = ['GROUP_CHAT_ID_1', 'GROUP_CHAT_ID_2']
#     keyword = 'SOME_KEYWORD'
#     search_messages(bot, group_ids, keyword)


# #6. Call the main function to run the bot:

# if _name_ == '__main__':
#     main()