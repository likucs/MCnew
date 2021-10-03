import os
import re
import io
import pyrogram
from pyrogram import filters, Client
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from info import ADMINS

from wasim_faris.filter_db import add_filter
from wasim_faris.filter_db import find_filter
from wasim_faris.filter_db import get_filters
from wasim_faris.filter_db import delete_filter
from wasim_faris.filter_db import count_filters

from wasim_faris.connect_db import add_connection
from wasim_faris.connect_db import all_connections
from wasim_faris.connect_db import if_active
from wasim_faris.connect_db import delete_connection
from wasim_faris.connect_db import active_connection
from plugins.main_filter.Helpers import parser,split_quotes


NOT_FOR_U ="CAACAgIAAxkBAAIE5WFWnf7I8uPvrlnpp7fj41548xlPAAIiDgACsX2wSyUIjTPiUHFVHgQ",
STICKER = "CAACAgUAAxkBAAIHDGFYELSFHihhbW6SM5re-FhegHR5AAIhAwAC_EcZVKinu1GWDbtpHgQ"
#-------------------------------------------------------------------------------------------------------------------------------------------------
@Client.on_message(filters.command(["add"]))
async def addfilter(client, message):
      
    userid = message.from_user.id
    chat_type = message.chat.type
    args = message.text.html.split(None, 1)

    if chat_type == "private":
        
        grpid = await active_connection(str(userid))
        if grpid is not None:
            grp_id = grpid
            try:
                chat = await client.get_chat(grpid)
                title = chat.title
            except:
                await message.reply_text("__Make sure I'm present in your group.!!__", quote=True)
                return
        else:
            await message.reply_text("__I'm not connected to any groups.!__", quote=True)
            return

    elif (chat_type == "group") or (chat_type == "supergroup"):
        grp_id = message.chat.id
        title = message.chat.title

    else:
        return

    st = await client.get_chat_member(grp_id, userid)
    if not ((st.status == "administrator") or (st.status == "creator") or (str(userid) in ADMINS)):
        return
        

    if len(args) < 2:
        await message.reply_text("__Command Is Incomplete...__", quote=True)
        return
    
    extracted = split_quotes(args[1])
    text = extracted[0].lower()
   
    if not message.reply_to_message and len(extracted) < 2:
        await message.reply_text("Add some content to save your filter!", quote=True)
        return

    if (len(extracted) >= 2) and not message.reply_to_message:
        reply_text, btn, alert = parser(extracted[1], text)
        fileid = None
        if not reply_text:
            await message.reply_text("__You cannot have buttons alone, give some text to go with it..__", quote=True)
            return

    elif message.reply_to_message and message.reply_to_message.reply_markup:
        try:
            rm = message.reply_to_message.reply_markup
            btn = rm.inline_keyboard
            msg = message.reply_to_message.document or\
                  message.reply_to_message.video or\
                  message.reply_to_message.photo or\
                  message.reply_to_message.audio or\
                  message.reply_to_message.animation or\
                  message.reply_to_message.sticker
            if msg:
                fileid = msg.file_id
                reply_text = message.reply_to_message.caption.html
            else:
                reply_text = message.reply_to_message.text.html
                fileid = None
            alert = None
        except:
            reply_text = ""
            btn = "[]" 
            fileid = None
            alert = None

    elif message.reply_to_message and message.reply_to_message.photo:
        try:
            fileid = message.reply_to_message.photo.file_id
            reply_text, btn, alert = parser(message.reply_to_message.caption.html, text)
        except:
            reply_text = ""
            btn = "[]"
            alert = None

    elif message.reply_to_message and message.reply_to_message.video:
        try:
            fileid = message.reply_to_message.video.file_id
            reply_text, btn, alert = parser(message.reply_to_message.caption.html, text)
        except:
            reply_text = ""
            btn = "[]"
            alert = None

    elif message.reply_to_message and message.reply_to_message.audio:
        try:
            fileid = message.reply_to_message.audio.file_id
            reply_text, btn, alert = parser(message.reply_to_message.caption.html, text)
        except:
            reply_text = ""
            btn = "[]"
            alert = None
   
    elif message.reply_to_message and message.reply_to_message.document:
        try:
            fileid = message.reply_to_message.document.file_id
            reply_text, btn, alert = parser(message.reply_to_message.caption.html, text)
        except:
            reply_text = ""
            btn = "[]"
            alert = None

    elif message.reply_to_message and message.reply_to_message.animation:
        try:
            fileid = message.reply_to_message.animation.file_id
            reply_text, btn, alert = parser(message.reply_to_message.caption.html, text)
        except:
            reply_text = ""
            btn = "[]"
            alert = None

    elif message.reply_to_message and message.reply_to_message.sticker:
        try:
            fileid = message.reply_to_message.sticker.file_id
            reply_text, btn, alert =  parser(extracted[1], text)
        except:
            reply_text = ""
            btn = "[]"
            alert = None

    elif message.reply_to_message and message.reply_to_message.text:
        try:
            fileid = None
            reply_text, btn, alert = parser(message.reply_to_message.text.html, text)
        except:
            reply_text = ""
            btn = "[]"
            alert = None

    else:
        return
    
    await add_filter(grp_id, text, reply_text, btn, fileid, alert)

    await message.reply_text(
        f"Filter for `{text}` added in **{title}**",
        quote=True,
        parse_mode="md"
    )
#-------------------------------------------------------------------------------------------------------------------------------------------------
@Client.on_message(filters.command(["view"]))
async def get_all(client, message):    
    chat_type = message.chat.type
    user_id = message.from_user.id

    if chat_type == "private":
        
        grpid = await active_connection(str(user_id))
        if grpid is not None:
            grp_id = grpid
            try:
                chat = await client.get_chat(grpid)
                title = chat.title
            except:
                await message.reply_text("Make sure I'm present in your group!!", quote=True)
                return
        else:
            await message.reply_text("__I'm not connected to any groups.!!__", quote=True)
            return

    elif (chat_type == "group") or (chat_type == "supergroup"):
        grp_id = message.chat.id
        title = message.chat.title

    else:
        return

    st = await client.get_chat_member(grp_id, user_id)
    if not ((st.status == "administrator") or (st.status == "creator") or (str(userid) in ADMINS)):
        return

    texts = await get_filters(grp_id)
    count = await count_filters(grp_id)
    if count:
        filterlist = f"Total filters in **{title}**: `{count}`\n\n"

        for text in texts:
            keywords = "• `{}`\n".format(text)
            
            filterlist += keywords

        if len(filterlist) > 4096:
            with io.BytesIO(str.encode(filterlist.replace("`", ""))) as keyword_file:
                keyword_file.name = "keywords.txt"
                await message.reply_document(
                    document=keyword_file,
                    quote=True
                )
            return
    else:
        filterlist = f"There are no active filters in **{title}**"

    await message.reply_text(
        text=filterlist,
        quote=True,
        parse_mode="md"
    )
#-------------------------------------------------------------------------------------------------------------------------------------------------        
@Client.on_message(filters.command(["delfilter"]))
async def deletefilter(client, message):
    userid = message.from_user.id
    chat_type = message.chat.type

    if chat_type == "private":
       
        grpid  = await active_connection(str(userid))
        if grpid is not None:
            grp_id = grpid
            try:
                chat = await client.get_chat(grpid)
                title = chat.title
            except:
                await message.reply_text("__Make sure I'm present in your group.!!__", quote=True)
                return
        else:
            await message.reply_text("__I'm not connected to any groups.!!__", quote=True)

    elif (chat_type == "group") or (chat_type == "supergroup"):
        grp_id = message.chat.id
        title = message.chat.title

    else:
        return

    st = await client.get_chat_member(grp_id, userid)
    if not ((st.status == "administrator") or (st.status == "creator") or (str(userid) in ADMINS)):
        return

    try:
        cmd, text = message.text.split(" ", 1)
    except:
        await message.reply_text("__Mention the filter name which you wanna delete..!__", quote=False)
        return

    query = text.lower()

    await delete_filter(message, query, grp_id)
#-------------------------------------------------------------------------------------------------------------------------------------------------
@Client.on_message(filters.command(["delall_filters"]))
async def delallconfirm(client, message):
    userid = message.from_user.id
    chat_type = message.chat.type
    await message.reply_sticker(STICKER)
#-------------------------------------------------------------------------------------------------------------------------------------------------
@Client.on_message((filters.private | filters.group) & filters.command(["connect"]))
async def addconnection(client,message):
    userid = message.from_user.id
    chat_type = message.chat.type

    if chat_type == "private":
        
        try:
            cmd, group_id = message.text.split(" ", 1)
        except:
            await message.reply_text(
                "<b>Enter in correct format.!</b>\n\n"
                "<code>/connect groupid</code>\n\n"
                "<i>Get your Group id by adding this bot to your group and use  <code>/id</code></i>",
                quote=True
            )
            return

    elif (chat_type == "group") or (chat_type == "supergroup"):
        group_id = message.chat.id

    try:
        st = await client.get_chat_member(group_id, userid)
        if (st.status == "administrator") or (st.status == "creator") or (str(userid) in ADMINS):
            pass
        else:
            await message.reply_text("__You should be an admin in Given group.!!__", quote=True)
            return
    except Exception as e:
        print(e)
        await message.reply_text(
            "**Invalid Group ID**\n\n__If correct, Make sure I'm present in your group.!!__",
            quote=True
        )
        return


    try:
        st = await client.get_chat_member(group_id, "me")
        if st.status == "administrator":
            ttl = await client.get_chat(group_id)
            title = ttl.title

            addcon = await add_connection(str(group_id), str(userid))
            if addcon:
                await message.reply_text(
                    f"Sucessfully connected to **{title}**\nNow manage your group from my pm !",
                    quote=True,
                    parse_mode="md"
                )
                if (chat_type == "group") or (chat_type == "supergroup"):
                    await client.send_message(
                        userid,
                        f"Connected to **{title}** !",
                        parse_mode="md"
                    )
            else:
                await message.reply_text(
                    "__You're already connected to this chat.!__",
                    quote=True
                )

        else:
            await message.reply_text("Add me as an admin in group", quote=True)
    except Exception as e:
        print(e)
        await message.reply_text(
            "Some error occured! Try again later.",
            quote=True
        )
        return


@Client.on_message((filters.private | filters.group) & filters.command(["disconnect"]))
async def deleteconnection(client,message):
    userid = message.from_user.id
    chat_type = message.chat.type

    if chat_type == "private":
        
        await message.reply_text("Run /connections to view or disconnect from groups!", quote=True)

    elif (chat_type == "group") or (chat_type == "supergroup"):
        group_id = message.chat.id

        st = await client.get_chat_member(group_id, userid)
        if not ((st.status == "administrator") or (st.status == "creator") or (str(userid) in ADMINS)):
            return

        delcon = await delete_connection(str(userid), str(group_id))
        if delcon:
            await message.reply_text("Successfully disconnected from this chat", quote=True)
        else:
            await message.reply_text("This chat isn't connected to me!\nDo /connect to connect.", quote=True)


@Client.on_message(filters.group & filters.text)
async def give_filter(client,message):
    group_id = message.chat.id
    name = message.text

    keywords = await get_filters(group_id)
    for keyword in reversed(sorted(keywords, key=len)):
        pattern = r"( |^|[^\w])" + re.escape(keyword) + r"( |$|[^\w])"
        if re.search(pattern, name, flags=re.IGNORECASE):
            reply_text, btn, alert, fileid = await find_filter(group_id, keyword)

            if reply_text:
                reply_text = reply_text.replace("\\n", "\n").replace("\\t", "\t")

            if btn is not None:
                try:
                    if fileid == "None":
                        if btn == "[]":
                            await message.reply_text(reply_text, disable_web_page_preview=True)
                        else:
                            button = eval(btn)
                            await message.reply_text(
                                reply_text,
                                disable_web_page_preview=True,
                                reply_markup=InlineKeyboardMarkup(button)
                            )
                    else:
                        if btn == "[]":
                            await message.reply_cached_media(
                                fileid,
                                caption=reply_text or ""
                            )
                        else:
                            button = eval(btn) 
                            await message.reply_cached_media(
                                fileid,
                                caption=reply_text or "",
                                reply_markup=InlineKeyboardMarkup(button)
                            )
                except Exception as e:
                    print(e)
                    pass
                break 
