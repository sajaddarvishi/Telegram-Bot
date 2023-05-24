import telegram
from telegram.ext import Updater,CommandHandler, JobQueue

token = "tokenno:token"

bot = telegram.Bot(token=token)

def start(update, context):
    context.bot.send_message(chat_id=update.message.chat_id,
                             text="You will now receive msgs!")


def callback_minute(context):
    chat_id = context.job.context

    # Check in DB and send if new msgs exist
    send_msgs_tg(context, chat_id)


def callback_msgs():
    fetch_msgs()


def main():
    JobQueue.run_repeating(callback_msgs, interval=5, first=1, context=None)
    
    updater = Updater(token,use_context=True)
    dp = updater.dispatcher
    dp.add_handler(CommandHandler("start",start, pass_job_queue=True))

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()