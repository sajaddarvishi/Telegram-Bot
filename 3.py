from pyrogram import Client, filters
from pyrogram import ChatPermissions
from pyrogram import InlineKeyboardButton, InlineKeyboardMarkup

bot = Client (
    "first message",
    api_id = 1 ,
    api_hash = ",",
    #bot_token = "j"
)

@bot.on_message(filters.command('start') & filters.private) # create a command
def command1(bot, message): 
    bot.send_message(message.chat.id, "Heya, I am a test") # calling a method

@bot.on_message(filters.command('help'))
def command2(bot, message): 
    message.reply_text("reply test") 


#echobot
@bot.on_message(filters.text & filters.private)
def echobot(client, message):
    message.reply_text(message.text)

#welcomebot
GROUP = "name" #Group id/username
WELCOME_MESSAGE = "Heloo, welcome to group"

@bot.on_message(filters.chat(GROUP) & filter.new_chat_members)
def welcomebot(client, message):
    message.reply_text(WELCOME_MESSAGE)

#send_photo
@bot.on_message(filters.command('photo'))
def command3(bot, message): 
    bot.send_photo(message.chat.id, "link of photo") 
    bot.send_photo(message.chat.id, "link of photo2") 


@bot.on_message(filters.audio, filters.private)
def audio(bot, message):
    message.reply(message.audio.file_id) # get file id #document sticker vidro animationvoice

@bot.on_message(filters.command('audio'))
def command4(bot, message): 
    bot.send_audio(message.chat.id, "") # send file

@bot.on_message(filters.text)
def delete_text(bot, message):
    word_list = ["bro", "wtf"]
    if message.text in word_list:
        bot.delete_messages(message.chat_id, message.message_id)
        bot.send_message(message.chat.id, "blackword")

@bot.on_message(filters.command('leave') & filters.group ) 
def leave(bot, message): 
    bot.send_message(message.chat.id, "bye") 
    bot.leave_chat(message.chat.id)

#ban user for ever
@bot.on_message(filters.command('ban') & filters.group ) 
def ban(bot, message): 
    bot.kick_chat_member(message.chat.id, message.reply_to_message.from_user.id)
    bot.send_message(message.chat.id, f"{message.reply_to_message.from_user.mention} banned!") 
    
#ban user for ever
@bot.on_message(filters.command('unban') & filters.group ) 
def unban(bot, message): 
    bot.unban_chat_member(message.chat.id, message.reply_to_message.from_user.id)
    bot.send_message(message.chat.id, f"{message.reply_to_message.from_user.mention} unbanned!") 
    

#mute user
@bot.on_message(filters.command('mute') & filters.group ) 
def mute(bot, message): 
    bot.restrict_chat_member(message.chat.id, message.reply_to_message.from_user.id, ChatPermissions())
    bot.send_message(message.chat.id, f"{message.reply_to_message.from_user.mention} muted!") 
    


print("I AM ALIVE")
bot.run()