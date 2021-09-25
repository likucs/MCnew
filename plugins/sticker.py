from pyrogram import Client, filters

# Sticker ID
@Client.on_message(
    filters.private
    & ~filters.forwarded
    & ~filters.command(["start", "about", "help", "id"])
)
async def stickers(idbot, msg):
    if msg.sticker:
        await msg.reply(f"This Sticker's ID is <code>{msg.sticker.file_id}</code>", quote=True)
