import os , glob
from os import error
import logging
import pyrogram
import time
import math
from decouple import config
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from pyrogram.types import User, Message, Sticker, Document

@Client.on_message(filters.command(["ping"]))
async def ping(bot, message):
    start_t = time.time()
    rm = await message.reply_text("Checking")
    end_t = time.time()
    time_taken_s = (end_t - start_t) * 1000
    await rm.edit(f"Pong!\n{time_taken_s:.3f} ms")


@Client.on_message(filters.private & filters.command(["getsticker"]))
async def getstickerasfile(bot, message):  
    tx = await message.reply_text("Checking Sticker")
    await tx.edit("Validating sticker..")
    if message.reply_to_message.sticker is False:
        await tx.edit("Not a Sticker File!!")
    else :
          if message.reply_to_message is None: 
               tx =  await tx.edit("Reply to a Sticker File!")       
          else :
               if message.reply_to_message.sticker.is_animated:
                   try :     
                        tx = await message.reply_text("Downloading...")
                        file_path = DOWNLOAD_LOCATION + f"{message.chat.id}.tgs"
                        await message.reply_to_message.download(file_path)  
                        await tx.edit("Downloaded") 
                    #   zip_path= ZipFile.write("")
                        await tx.edit("Uploading...")
                        start = time.time()
                        await message.reply_document(file_path,caption="©@BugHunterBots")
                        await tx.delete()   
                        os.remove(file_path)
                    #   os.remove(zip_path)
                   except Exception as error:
                        print(error)
 
               elif message.reply_to_message.sticker.is_animated is False:        
                   try : 
                       tx = await message.reply_text("Downloading...")
                       file_path = DOWNLOAD_LOCATION + f"{message.chat.id}.png"
                       await message.reply_to_message.download(file_path)   
                       await tx.edit("Downloaded")
                       await tx.edit("Uploading...")
                       start = time.time()
                       await message.reply_document(file_path,caption="©@BugHunterBots")
                       await tx.delete()   
                       os.remove(file_path)
                   except Exception as error:
                       print(error)

@Client.on_message(filters.private & filters.command(["clearcache"]))
async def clearcache(bot, message):   
    # Found some Files showing error while Uploading, So a method to Remove it !!  
    txt = await message.reply_text("Checking Cache")
    await txt.edit("Clearing cache")
    dir = DOWNLOAD_LOCATION
    filelist = glob.glob(os.path.join(dir, "*"))
    for f in filelist :
           i =1
           os.remove(f)
           i=i+1
    await txt.edit("Cleared "+ str(i) + "File") 
    await txt.delete()
