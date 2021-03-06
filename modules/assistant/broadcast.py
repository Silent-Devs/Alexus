import asyncio 
from main.client import asst
from pyrogram import Client, filters
from pyrogram.types import Dialog, Chat, Message
from pyrogram.errors import UserAlreadyParticipant
from modules import DEV
from main.config import SUDO_ID
# from services.callsmusic import client as USER

@Client.on_message(filters.command(["gcast", "broadcast"]))
async def broadcast(_, message: Message):
    sent=0
    failed=0
    if message.from_user.id not in DEV or SUDO_ID:
        return
    else:   
        wtf = await message.reply("**Broadcast message!!!**")
        if not message.reply_to_message:
            await wtf.edit("**Reply to Message!!!**")
            return
        lmao = message.reply_to_message.text
        async for dialog in asst.iter_dialogs():
            try:
                await USER.send_message(dialog.chat.id, lmao)
                sent = sent+1
                await wtf.edit(f"**Broadcast !!!** \n\n**✔️Sent to:** `{sent}` **Chats** \n**❌  Failed in:** `{failed}` **Chats**")
                await asyncio.sleep(3)
            except:
                failed=failed+1
        await wtf.delete()
        await message.reply_text(f"**Totally Broadcast !!!**\n\n**✔ Sent To:** `{sent}` **Chats**\n**❌  Failed  in* `{failed}` **Chats**")
    
