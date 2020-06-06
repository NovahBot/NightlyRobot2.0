import random
from telegram.ext import run_async, Filters
from telegram import Message, Chat, Update, Bot, MessageEntity
from tg_bot import dispatcher
from tg_bot.modules.disable import DisableAbleCommandHandler

SFW_STRINGS = (
    "Teri maa ki chut",
    "Ur dad gey bc",
    "MUH ME LEGA KYA BSDK",
    "Stfu bc",
    "Ur mum gey",
    "GTFO bsdkCUnt",
    "Relax your Rear,ders nothing to fear,The Rape train is finally here",
    "Stfu go fuck yourself",
    "you noob",
    "Fuck you hard",
    "You Are such a Asshole",
    "Fuck your self",
    "Suck my dick", 
    "Bhak BC",
    "Bustard",
    "Fuck you hard"
  )

@run_async
def dark(bot: Bot, update: Update):
    bot.sendChatAction(update.effective_chat.id, "typing") # Bot typing before send messages
    message = update.effective_message
    if message.reply_to_message:
      message.reply_to_message.reply_text(random.choice(SFW_STRINGS))
    else:
      message.reply_text(random.choice(SFW_STRINGS))

__help__ = """
- /dark  Abuse 🙂.
"""

__mod_name__ = "Abuse"

DARK_HANDLER = DisableAbleCommandHandler("dark", dark)

dispatcher.add_handler(DARK_HANDLER)
