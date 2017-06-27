import telegram
import subprocess
import random
from telegram.ext import Updater

#enable logging
import logging
logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

TOKEN = "redacted" # i should learn to use os env variables

# you have an updater class, and a dispatcher class.
updater = Updater(token=TOKEN)
dispatcher = updater.dispatcher

# respond to /start
def start(bot, update):
    bot.sendMessage(chat_id=update.message.chat_id, text="hi! thanks for helping me out with this project.")
    bot.sendMessage(chat_id=update.message.chat_id, text="i'm using markov chains to generate real-sounding messages.")
    bot.sendMessage(chat_id=update.message.chat_id, text="please pick which of the four sounds the most real!")
    bot.sendMessage(chat_id=update.message.chat_id, text="send a /next when you're ready!")
    # bot.sendMessage(chat_id=myChatID, text=update.message.from_user.first_name+":"+str(update.message.chat_id)+": "+"ran /start")

from telegram.ext import CommandHandler
start_handler = CommandHandler('start', start)
dispatcher.add_handler(start_handler)
#

# respond to /next
def nextf(bot, update):
    f = open(str(update.message.from_user.first_name)+'.txt','a' )
    bot.sendMessage(chat_id=update.message.chat_id, text="HERE WE GO:\n-----")
    # call out to other scripts to get their string
    # randomly stuff them into boxes
    # have user tap box
    # store:
        # markov: msg
        # markov-mine: msg
        # markov-ify: msg
        # real: msg
        # chosen: whichever
    # as json dumped into a file

    markovnaive = str( subprocess.check_output(["python", "../message-generating/markov-naive.py"]),'utf-8').strip()
    markovmine = str( subprocess.check_output(["python", "../message-generating/markov-mine.py"]),'utf-8').strip()
    markovify = str( subprocess.check_output(["python", "../message-generating/markov-ify.py"]),'utf-8').strip()

    def random_line(afile):
        line = next(afile)
        for num, aline in enumerate(afile):
          if random.randrange(num + 2): continue
          line = aline
        return line

    with open("../output/my-messages-only/xFF5353.txt",'r') as read_random_line_file:
        real = random_line(read_random_line_file)

    messages = [("naive",markovnaive),
                    ("mine",markovmine),
                    ("ify",markovify),
                    ("real",real)]
    random.shuffle(messages)

    for msg in messages:
        bot.sendMessage(chat_id=update.message.chat_id, text=msg[1])
        f.write(str(msg))
        f.write("\n")

    custom_keyboard = [["/1 "+messages[0][1], "/2 "+messages[1][1]], 
                       ["/3 "+messages[2][1], "/4 "+messages[3][1]]]

    reply_markup = telegram.ReplyKeyboardMarkup(custom_keyboard)
    bot.send_message(chat_id=update.message.chat_id, 
                     text="-----\nCHOOSE!", 
                     reply_markup=reply_markup)


from telegram.ext import CommandHandler
nextHandler = CommandHandler('next', nextf)
dispatcher.add_handler(nextHandler)
#

def respond(bot, update, reply_markup):
    filename = str(update.message.from_user.first_name)+'.txt'
    answer = str( subprocess.check_output(["./get-last-real.sh", filename]),'utf-8').strip()
    custom_keyboard = [["/next"]]
    reply_markup = telegram.ReplyKeyboardMarkup(custom_keyboard)
    bot.send_message(chat_id=update.message.chat_id, 
                     text="THE CORRECT ANSWER WAS "+answer+" /next", 
                     reply_markup=reply_markup)

# /1
def one(bot, update):
    f = open(str(update.message.from_user.first_name)+'.txt','a' )
    f.write(update.message.text)
    f.write("\n\n")
    reply_markup = telegram.ReplyKeyboardRemove()
    respond(bot,update,reply_markup)

from telegram.ext import CommandHandler
oneHandler = CommandHandler('1', one)
dispatcher.add_handler(oneHandler)
#

# /2
def two(bot, update):
    f = open(str(update.message.from_user.first_name)+'.txt','a' )
    f.write(update.message.text)
    f.write("\n\n")
    reply_markup = telegram.ReplyKeyboardRemove()
    respond(bot,update,reply_markup)

from telegram.ext import CommandHandler
twoHandler = CommandHandler('2', two)
dispatcher.add_handler(twoHandler)
#

# /3
def three(bot, update):
    f = open(str(update.message.from_user.first_name)+'.txt','a' )
    f.write(update.message.text)
    f.write("\n\n")
    reply_markup = telegram.ReplyKeyboardRemove()
    respond(bot,update,reply_markup)

from telegram.ext import CommandHandler
threeHandler = CommandHandler('3', three)
dispatcher.add_handler(threeHandler)
#

# /4
def four(bot, update):
    f = open(str(update.message.from_user.first_name)+'.txt','a' )
    f.write(update.message.text)
    f.write("\n\n")
    reply_markup = telegram.ReplyKeyboardRemove()
    respond(bot,update,reply_markup)

from telegram.ext import CommandHandler
fourHandler = CommandHandler('4', four)
dispatcher.add_handler(fourHandler)
#

# warning: there can only be one! per-filter i think
# respond to any msg != start
def standardMessage(bot, update):
    return

from telegram.ext import MessageHandler, Filters
standardMessageHandler = MessageHandler(Filters.text, standardMessage)
dispatcher.add_handler(standardMessageHandler)
#

###############################################################################
# poll for messages (seems to be standard structure for most bots)
updater.start_polling()
updater.idle()
