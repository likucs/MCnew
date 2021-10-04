from config import Messages
from time import time, sleep
from pyrogram import Client, filters
from pyrogram.errors import FloodWait
from pyrogram.errors.exceptions.forbidden_403 import ChatWriteForbidden
from pyrogram.errors.exceptions.bad_request_400 import ChatAdminRequired, UserAdminInvalid


START_MSG = "**Hey [{}](tg://user?id={})**\n__I can kick inactive members from group.\nLearn more at /help__"
      
      CREATOR_REQUIRED = "❗ **You have to be the group creator to do that.**"
      
      INPUT_REQUIRED = "❗ **Arguments Required**\n__See /help in personal message for more information.__"
      
      KICKED = "✔️ **Successfully Kicked {} members according to the arguments provided.**"
      
      START_KICK = "🚮**Removing inactive members this may take a while...**"
      
      ADMIN_REQUIRED = "❗**I am not an admin here**\n__Leaving this chat, add me again as admin with ban user permission.__"
      
      DKICK = "✔️ **Kicked {} Deleted Accounts Successfully.**"
      
      FETCHING_INFO = "**Collecting users information...**"
      
      STATUS = "**{}\nChat Member Status**\n\n```recently``` - {}\n```within_week``` - {}\n```within_month``` - {}\n```long_time_ago``` - {}\nDeleted Account - {}\nBot - {}\nUnCached - {}"
   
@Client.on_message(filters.incoming & ~filters.private & filters.command(['inkick']))
def inkick(client, message):
  user = client.get_chat_member(message.chat.id, message.from_user.id)
  if user.status == "creator":
    if len(message.command) > 1:
      input_str = message.command
      sent_message = message.reply_text(Messages.START_KICK)
      count = 0
      for member in client.iter_chat_members(message.chat.id):
        if member.user.status in input_str and not member.status in ('administrator', 'creator'):
          try:
            client.kick_chat_member(message.chat.id, member.user.id, int(time() + 45))
            count += 1
            sleep(1)
          except (ChatAdminRequired, UserAdminInvalid):
            sent_message.edit(Messages.ADMIN_REQUIRED)
            client.leave_chat(message.chat.id)
            break
          except FloodWait as e:
            sleep(e.x)
      try:
        sent_message.edit(Messages.KICKED.format(count))
      except ChatWriteForbidden:
        pass
    else:
      message.reply_text(Messages.INPUT_REQUIRED)
  else:
    sent_message = message.reply_text(Messages.CREATOR_REQUIRED)
    sleep(5)
    sent_message.delete()

@Client.on_message(filters.incoming & ~filters.private & filters.command(['dkick']))
def dkick(client, message):
  user = client.get_chat_member(message.chat.id, message.from_user.id)
  if user.status == "creator":
    sent_message = message.reply_text(Messages.START_KICK)
    count = 0
    for member in client.iter_chat_members(message.chat.id):
      if member.user.is_deleted and not member.status in ('administrator', 'creator'):
        try:
          client.kick_chat_member(message.chat.id, member.user.id, int(time() + 45))
          count += 1
          sleep(1)
        except (ChatAdminRequired, UserAdminInvalid):
          sent_message.edit(Messages.ADMIN_REQUIRED)
          client.leave_chat(message.chat.id)
          break
        except FloodWait as e:
          sleep(e.x)
    try:
      sent_message.edit(Messages.DKICK.format(count))
    except ChatWriteForbidden:
      pass
  else:
    sent_message = message.reply_text(Messages.CREATOR_REQUIRED)
    sleep(5)
    sent_message.delete()

@Client.on_message(filters.incoming & ~filters.private & filters.command(['instatus']))
def instatus(client, message):
  user = client.get_chat_member(message.chat.id, message.from_user.id)
  if user.status in ('administrator', 'creator'):
    sent_message = message.reply_text(Messages.FETCHING_INFO)
    recently = 0
    within_week = 0
    within_month = 0
    long_time_ago = 0
    deleted_acc = 0
    uncached = 0
    bot = 0
    for member in client.iter_chat_members(message.chat.id):
      user = member.user
      if user.is_deleted:
        deleted_acc += 1
      elif user.is_bot:
        bot += 1
      elif user.status == "recently":
        recently += 1
      elif user.status == "within_week":
        within_week += 1
      elif user.status == "within_month":
        within_month += 1
      elif user.status == "long_time_ago":
        long_time_ago += 1
      else:
        uncached += 1
    sent_message.edit(Messages.STATUS.format(message.chat.title, recently, within_week, within_month, long_time_ago, deleted_acc, bot, uncached))
