import random
from telegram.ext import run_async, Filters
from telegram import Message, Chat, Update, Bot, MessageEntity
from tg_bot import dispatcher
from tg_bot.modules.disable import DisableAbleCommandHandler

SFW_STRINGS = (
      "Sorry!  You're Not Authorized To Use This.",
      "Sorry!  You're Not Authorized To Use This.",
      "Sorry!  You're Not Authorized To Use This.",
      "Sorry!  You're Not Authorized To Use This.",
      "Sorry!  You're Not Authorized To Use This.",
      "Sorry!  You're Not Authorized To Use This.",
      "Sorry!  You're Not Authorized To Use This.",
      "Sorry!  You're Not Authorized To Use This.",
      "Sorry!  You're Not Authorized To Use This.",
      "Sorry!  You're Not Authorized To Use This.",
      "Sorry!  You're Not Authorized To Use This.",
      "Sorry!  You're Not Authorized To Use This.",
      "Sorry!  You're Not Authorized To Use This.",
      "Sorry!  You're Not Authorized To Use This.",
      "Sorry!  You're Not Authorized To Use This.",
      "Sorry!  You're Not Authorized To Use This.",
      "Sorry!  You're Not Authorized To Use This.",
      "Sorry!  You're Not Authorized To Use This.",
      "Sorry!  You're Not Authorized To Use This.",
      "Sorry!  You're Not Authorized To Use This.",
      "Sorry!  You're Not Authorized To Use This.",
      "Sorry!  You're Not Authorized To Use This.",
      "Sorry!  You're Not Authorized To Use This.",
      "Sorry!  You're Not Authorized To Use This.",
      "Sorry!  You're Not Authorized To Use This.",
      "Sorry!  You're Not Authorized To Use This.",
      "Sorry!  You're Not Authorized To Use This.",
      "Sorry!  You're Not Authorized To Use This.",
      "Sorry!  You're Not Authorized To Use This.",
      "Sorry!  You're Not Authorized To Use This.",
      "Sorry!  You're Not Authorized To Use This.",
  )

@run_async
def q(bot: Bot, update: Update):
    bot.sendChatAction(update.effective_chat.id, "typing") # Bot typing before send messages
    message = update.effective_message
    if message.reply_to_message:
      message.reply_to_message.reply_text(random.choice(SFW_STRINGS))
    else:
      message.reply_text(random.choice(SFW_STRINGS))

__help__ = """
- /q  Sorry!  You're Not Authorized To Use This. 
"""

__mod_name__ = "Killing Commands"

Q_HANDLER = DisableAbleCommandHandler("q", q)

dispatcher.add_handler(Q_HANDLER)
