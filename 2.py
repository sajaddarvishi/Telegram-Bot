from telegram.ext import Updater, CommandHandler
from telegram.ext import MessageHandler, filters, CallbackContext
import logging
import redis
import datetime

updater = Updater(token='1tvKDCRI', use_context=True)
dispatcher = updater.dispatcher
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

# writting functionality of the command
def start(update, context):
    user_id = update.message.from_user.id
    user_name = update.message.from_user.name
    r.set(user_name, user_id)
    message = 'Welcome to the bot' 
    context.bot.send_message(chat_id=update.effective_chat.id, text=message)


# give a name to the command and add it to the dispaatcher
start_handler = CommandHandler('start', start)
dispatcher.add_handler(start_handler)
updater.start_polling() # enable bot to get updates


r = redis.from_url('your_redis_db_url') # connection to the databse
db_keys = r.keys(pattern='*')   # allows us to fetch data


# You can check the list of subscribers any time you want. Create new script users.py:

# import redis
# r = redis.from_url('your_redis_db_url')
# db_keys = r.keys(pattern="*")
# print((len(db_keys)))
# for single in db_keys:
#     chat_id = r.get(single).decode("UTF-8")
#     print(single.decode("UTF-8"), ": ", chat_id)


def echo(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text=update.message.text)

echo_handler = MessageHandler(filters.text & (~filters.command), echo)
dispatcher.add_handler(echo_handler)

# Note: That is not a command and you cannot access it by typing /echo. It is automatical handler 
# that will reply to the user after the user’s text message (with the help of Filters.text)

j = updater.job_queue

def once(context: CallbackContext):
    message = "Hello, this message will be sent only once"
    
    # send message to all users
    for keys in db_keys:
        id = r.get(keys).decode("UTF-8")
        context.bot.send_message(chat_id=id, text=message)

j.run_once(once, 30)

def morning(context: CallbackContext):
    message = "Good Morning! Have a nice day!"
    
    # send message to all users
    for keys in db_keys:
        id = r.get(keys).decode("UTF-8")
        context.bot.send_message(chat_id=id, text=message)
job_daily = j.run_daily(morning, days=(0, 1, 2, 3, 4, 5, 6), time=datetime.time(hour=10, minute=00, second=00))

