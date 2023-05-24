from telegram.ext import Updater, CommandHandler
from telegram.ext import MessageHandler, filters, CallbackContext, JobQueue
import logging
# import redis
import datetime

updater = Updater(token='1tvKDCRI', use_context=True)
dispatcher = updater.dispatcher
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

# r = redis.from_url('your_redis_db_url') # connection to the databse
# db_keys = r.keys(pattern='*')   # allows us to fetch data

# writting functionality of the command
def start(update, context):
    user_id = update.message.from_user.id
    user_name = update.message.from_user.name
    # r.set(user_name, user_id)
    message = 'Welcome to the bot' 
    context.bot.send_message(chat_id=update.effective_chat.id, text=message)

# give a name to the command and add it to the dispaatcher
start_handler = CommandHandler('start', start)
dispatcher.add_handler(start_handler)


# GROUP = "name" #Group id/username
# WELCOME_MESSAGE = "Heloo, welcome to group"

def get(update):
    global GROUP 
    GROUP = update.message.text

get_handler = CommandHandler('get', get)
dispatcher.add_handler(get_handler)

#welcomebot
# GROUP = "name" #Group id/username
# WELCOME_MESSAGE = "Heloo, welcome to group"

def send(update, context):
    context.bot.send_message(filters.chat(GROUP), text=update.message.text)

send_handler = CommandHandler('send', send)
dispatcher.add_handler(send_handler)

# def echo(update, context):
#     context.bot.send_message(chat_id=update.effective_chat.id, text=update.message.text)

# echo_handler = MessageHandler(filters.text & (~filters.command), echo)
# dispatcher.add_handler(echo_handler)

# j = updater.JobQueue

updater.JobQueue.run_repeating(send, interval=5, first=1, context=None)

updater.start_polling()
updater.idle()



# def once(context: CallbackContext):
#     message = "Hello, this message will be sent only once"
    
#     # send message to all users
#     for keys in db_keys:
#         id = r.get(keys).decode("UTF-8")
#         context.bot.send_message(chat_id=id, text=message)

# j.run_once(once, 30)

# def morning(context: CallbackContext):
#     message = "Good Morning! Have a nice day!"
    
#     # send message to all users
#     for keys in db_keys:
#         id = r.get(keys).decode("UTF-8")
#         context.bot.send_message(chat_id=id, text=message)
# job_daily = j.run_daily(morning, days=(0, 1, 2, 3, 4, 5, 6), time=datetime.time(hour=10, minute=00, second=00))





updater.start_polling() # enable bot to get updates
updater.idle()