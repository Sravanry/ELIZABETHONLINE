from telethon import events
import subprocess
from telethon.errors import MessageEmptyError, MessageTooLongError, MessageNotModifiedError
import io
import asyncio
import time
from haruka.events import register
import glob
import os
import instantmusic,subprocess

@register(pattern="^/song (.*)")
async def _(event):
    if event.fwd_from:
        return
    cmd = event.pattern_match.group(1)
    reply_to_id = event.message.id
    if event.reply_to_msg_id:
        reply_to_id = event.reply_to_msg_id
    os.system("instantmusic -q -s "+cmd)
    bro = 'for f in *.webm; do      mv -- "$f" "${f%.webm}.mp3"; done'
    os.system(bro)
    l = glob.glob("*.mp3")
    loa = l[0]
    await event.reply("sending the song")
    await event.client.send_file(
                eventpp0.chat_id,
                loa,
                force_document=True,
                allow_cache=False,
                caption=cmd,
                reply_to=reply_to_id
            )
    os.system("rm -rf *.mp3")

__help__ = """
 - /song <name>: search download and return a song in the best format
"""
__mod_name__ = "Songs" 
