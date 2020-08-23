import subprocess
import html
import json
import random
from random import randrange
import time
from telethon.tl.types import ChannelParticipantsAdmins
import re
import html
import wikipedia
import html
from typing import Optional, List
from telethon import events
import datetime
from telethon.tl.functions.users import GetFullUserRequest
from telethon.tl.types import MessageEntityMentionName
from datetime import timedelta
from telethon.tl.types import UserStatusEmpty, UserStatusLastMonth, UserStatusLastWeek, UserStatusOffline, UserStatusOnline, UserStatusRecently, ChannelParticipantsKicked, ChatBannedRights
from telethon.tl import functions, types
from time import sleep
import asyncio
from telegram import Message, Chat, Update, Bot, User, ParseMode
from telegram.error import BadRequest
from telegram.ext import run_async, Filters
from telegram.utils.helpers import mention_html
from alexa import dispatcher, LOGGER, CHROME_DRIVER, GOOGLE_CHROME_BIN
from alexa.modules.disable import DisableAbleCommandHandler
from alexa.modules.helper_funcs.chat_status import bot_admin, user_admin, is_user_ban_protected, can_restrict, \
    is_user_admin, is_user_in_chat
from alexa.modules.helper_funcs.extraction import extract_user_and_text
from alexa.modules.helper_funcs.string_handling import extract_time
from alexa.modules.log_channel import loggable
from alexa.modules.translations.strings import tld
import re
from pyDownload import Downloader
import datetime
import time
import os
from alexa.modules.helper_funcs.telethon.chat_status import user_is_ban_protectedd, user_is_adminn, is_user_adminn, alexa_is_adminn, is_user_in_chatt, can_delete_messagess, can_change_infoo, can_ban_userss, can_invite_userss, can_add_adminss, can_pin_messagess
from telethon.tl.functions.users import GetFullUserRequest
from telethon.tl.types import MessageEntityMentionName
import pytz
from io import BytesIO 
from time import sleep
from typing import Optional, List
from telegram import TelegramError, Chat, Message
from telegram import Update, Bot, User
from telegram import ParseMode
from telegram.error import BadRequest
from telegram.ext import MessageHandler, Filters, CommandHandler
from telegram.ext.dispatcher import run_async
from telegram.utils.helpers import escape_markdown
from alexa.modules.helper_funcs.chat_status import is_user_ban_protected, user_admin
import random
import telegram
import alexa.modules.sql.users_sql as sql
from alexa import dispatcher, OWNER_ID, SUDO_USERS, SUPPORT_USERS, LOGGER, OCR_SPACE_API_KEY, IBM_WATSON_CRED_URL, IBM_WATSON_CRED_PASSWORD
from alexa.modules.helper_funcs.filters import CustomFilters
from alexa.modules.disable import DisableAbleCommandHandler
USERS_GROUP = 4
import os
import re
import requests
from alexa.modules.helper_funcs.chat_status import bot_admin, can_promote, user_admin, can_pin
import urllib
from urllib.request import urlopen
from urllib.error import URLError, HTTPError
from bs4 import BeautifulSoup
from typing import List
from telegram import ParseMode, InputMediaPhoto, Update, Bot, TelegramError
from telegram.ext import run_async
from alexa import dispatcher
from alexa.modules.disable import DisableAbleCommandHandler
from googleapiclient.discovery import build
import requests 
import urllib.request
from alexa.modules.helper_funcs.chat_status import user_admin, is_user_admin

from telethon.errors import (BadRequestError, ChatAdminRequiredError,
                             ImageProcessFailedError, PhotoCropSizeSmallError,
                             UserAdminInvalidError)
from telethon.errors.rpcerrorlist import (UserIdInvalidError,
                                          MessageTooLongError)
from telethon.tl.functions.channels import (EditAdminRequest,
                                            EditBannedRequest,
                                            EditPhotoRequest)
from telethon.tl.functions.messages import UpdatePinnedMessageRequest
from telethon.tl.types import (PeerChat, PeerChannel,
                               ChannelParticipantsAdmins, ChatAdminRights,
                               ChatBannedRights, MessageEntityMentionName,
                               MessageMediaPhoto, ChannelParticipantsBots)
from telethon import events
from telethon.errors import YouBlockedUserError
import asyncio
import datetime
import time
from telethon import events
import pytz
import pyfiglet
from urllib.parse import quote_plus
from urllib.error import HTTPError
from telethon import events, functions
import sys
import datetime
import asyncio
import os
import subprocess
import datetime
import os
import time
from bs4 import BeautifulSoup as bs 
import requests
from telethon import events
import asyncio
from telegraph import Telegraph
from googleapiclient.errors import HttpError
import asyncio
import shutil
from bs4 import BeautifulSoup
import re
from time import sleep
from html import unescape
from re import findall
from urllib.parse import quote_plus
from urllib.error import HTTPError
from gtts import gTTS
from wikipedia import summary
from wikipedia.exceptions import DisambiguationError, PageError
import os
import time
import math
import asyncio
import shutil
from youtube_dl import YoutubeDL
from youtube_dl.utils import (DownloadError, ContentTooShortError,
                              ExtractorError, GeoRestrictedError,
                              MaxDownloadsReached, PostProcessingError,
                              UnavailableVideoError, XAttrMetadataError)
from html import unescape
from typing import Optional, List
import os
from gtts import gTTS, gTTSError
import requests
from requests import get
from telegram import Message, Chat, Update, Bot
from telegram.ext import run_async
from alexa import dispatcher, updater
from alexa.modules.disable import DisableAbleCommandHandler
from telegram import ChatAction
from telegram import Message, Chat, Update, Bot, MessageEntity
from telegram import Message, Update, Bot, User, Chat
from telegram import ParseMode, ReplyKeyboardRemove, InlineKeyboardMarkup, InlineKeyboardButton
from telegram.ext import CommandHandler, run_async, Filters
from telegram.utils.helpers import escape_markdown, mention_html
from telegram.error import BadRequest

from alexa import dispatcher, OWNER_ID, SUDO_USERS, SUPPORT_USERS, WHITELIST_USERS, tbot, OPENWEATHERMAP_ID, YOUTUBE_API_KEY, TEMP_DOWNLOAD_DIRECTORY
from alexa.__main__ import GDPR
from alexa.__main__ import STATS, USER_INFO
from alexa.modules.disable import DisableAbleCommandHandler
from alexa.modules.helper_funcs.extraction import extract_user
from alexa.modules.translations.strings import tld
from alexa.events import register
from requests import get
from telethon import events
from telethon.errors import YouBlockedUserError
import asyncio
from re import findall
from shutil import rmtree
from urllib.error import HTTPError
from wikipedia import summary
import asyncio
from telethon.errors import FloodWaitError
from alexa import tbot
from alexa.events import register
from wikipedia.exceptions import DisambiguationError, PageError
import os
import time
import math
import asyncio
import shutil
import requests
from telegram import Message, Chat, Update, Bot, MessageEntity
from telegram import ParseMode, ReplyKeyboardRemove, InlineKeyboardMarkup, InlineKeyboardButton
from telegram.ext import CommandHandler, run_async, Filters
from telegram.utils.helpers import escape_markdown, mention_html
from telegram.error import BadRequest
from alexa import dispatcher, OWNER_ID, SUDO_USERS, SUPPORT_USERS, WHITELIST_USERS
from alexa.__main__ import GDPR
from alexa.__main__ import STATS, USER_INFO
from alexa.modules.disable import DisableAbleCommandHandler
from alexa.modules.helper_funcs.extraction import extract_user
from alexa.modules.translations.strings import tld
from requests import get
from youtube_dl import YoutubeDL
from youtube_dl.utils import (DownloadError, ContentTooShortError,
                              ExtractorError, GeoRestrictedError,
                              MaxDownloadsReached, PostProcessingError,
                              UnavailableVideoError, XAttrMetadataError)
from asyncio import sleep
from telethon.tl.types import DocumentAttributeAudio
from collections import deque
from googleapiclient.discovery import build
from html import unescape
import requests

BANNED_RIGHTS = ChatBannedRights(
    until_date=None,
    view_messages=True,
    send_messages=True,
    send_media=True,
    send_stickers=True,
    send_gifs=True,
    send_games=True,
    send_inline=True,
    embed_links=True,
)

UNBAN_RIGHTS = ChatBannedRights(
    until_date=None,
    send_messages=None,
    send_media=None,
    send_stickers=None,
    send_gifs=None,
    send_games=None,
    send_inline=None,
    embed_links=None,
)

MUTE_RIGHTS = ChatBannedRights(until_date=None, send_messages=True)

UNMUTE_RIGHTS = ChatBannedRights(until_date=None, send_messages=False)
# ==================================#
from random import randint
from datetime import datetime
from typing import Optional, List
from typing import Optional, List
from hurry.filesize import size
import requests
from telegram import Message, Chat, Update, Bot, MessageEntity
from telegram import ParseMode, ReplyKeyboardRemove, ReplyKeyboardMarkup, InlineKeyboardMarkup, InlineKeyboardButton
from telegram.ext import CommandHandler, run_async, Filters
from telegram.utils.helpers import escape_markdown, mention_html
from alexa import dispatcher, OWNER_ID, SUDO_USERS, SUPPORT_USERS, WHITELIST_USERS, BAN_STICKER
from alexa.__main__ import GDPR
from alexa.__main__ import STATS, USER_INFO
from alexa.modules.disable import DisableAbleCommandHandler
from alexa.modules.helper_funcs.extraction import extract_user
from alexa.modules.helper_funcs.filters import CustomFilters
from alexa.modules.rextester.api import Rextester, CompilerError
from alexa.modules.rextester.langs import languages
from alexa.modules.sql.translation import prev_locale
from alexa.modules.translations.strings import tld
from requests import get
from telethon.tl.types import *

async def is_register_admin(chat, user):
    if isinstance(chat, (types.InputPeerChannel, types.InputChannel)):
        return isinstance(
            (await tbot(functions.channels.GetParticipantRequest(chat, user))).participant,
            (types.ChannelParticipantAdmin, types.ChannelParticipantCreator)
        )
    elif isinstance(chat, types.InputPeerChat):
        ui = await tbot.get_peer_id(user)
        ps = (await tbot(functions.messages.GetFullChatRequest(chat.chat_id))) \
            .full_chat.participants.participants
        return isinstance(
            next((p for p in ps if p.user_id == ui), None),
            (types.ChatParticipantAdmin, types.ChatParticipantCreator)
        )
    else:
        return None

async def is_register_banful(chat, user):
    if isinstance(chat, (types.InputPeerChannel, types.InputChannel)):
        return isinstance(
            (await tbot(functions.channels.GetParticipantRequest(chat, user))).participant,
            (types.ChannelParticipantAdmin, types.ChatAdminRights(ban_users=True))
        )
    elif isinstance(chat, types.InputPeerChat):
        ui = await tbot.get_peer_id(user)
        ps = (await tbot(functions.messages.GetFullChatRequest(chat.chat_id))) \
            .full_chat.participants.participants
        return isinstance(
            next((p for p in ps if p.user_id == ui), None),
            (types.ChatParticipantAdmin, types.ChatAdminRights(ban_users=True))
        )
    else:
        return None

@user_admin
@run_async
def runs(bot: Bot, update: Update):
    chat = update.effective_chat  # type: Optional[Chat]
    update.effective_message.reply_text(random.choice(tld(chat.id, "RUNS-K")))

@user_admin
@run_async
def slap(bot: Bot, update: Update, args: List[str]):
    chat = update.effective_chat  # type: Optional[Chat]
    msg = update.effective_message  # type: Optional[Message]

    # reply to correct message
    reply_text = msg.reply_to_message.reply_text if msg.reply_to_message else msg.reply_text

    # get user who sent message
    if msg.from_user.username:
        curr_user = "@" + escape_markdown(msg.from_user.username)
    else:
        curr_user = "[{}](tg://user?id={})".format(msg.from_user.first_name, msg.from_user.id)

    user_id = extract_user(update.effective_message, args)
    if user_id:
        slapped_user = bot.get_chat(user_id)
        user1 = curr_user
        if slapped_user.username:
            user2 = "@" + escape_markdown(slapped_user.username)
        else:
            user2 = "[{}](tg://user?id={})".format(slapped_user.first_name,
                                                   slapped_user.id)

    # if no target found, bot targets the sender
    else:
        user1 = "[{}](tg://user?id={})".format(bot.first_name, bot.id)
        user2 = curr_user

    temp = random.choice(tld(chat.id, "SLAP_TEMPLATES-K"))
    item = random.choice(tld(chat.id, "ITEMS-K"))
    hit = random.choice(tld(chat.id, "HIT-K"))
    throw = random.choice(tld(chat.id, "THROW-K"))
    itemp = random.choice(tld(chat.id, "ITEMP-K"))
    itemr = random.choice(tld(chat.id, "ITEMR-K"))

    repl = temp.format(user1=user1, user2=user2, item=item, hits=hit, throws=throw, itemp=itemp, itemr=itemr)
    #user1=user1, user2=user2, item=item_ru, hits=hit_ru, throws=throw_ru, itemp=itemp_ru, itemr=itemr_ru

    reply_text(repl, parse_mode=ParseMode.MARKDOWN)
    
@user_admin
@run_async
def get_id(bot: Bot, update: Update, args: List[str]):
    user_id = extract_user(update.effective_message, args)
    chat = update.effective_chat  # type: Optional[Chat]
    if user_id:
        if update.effective_message.reply_to_message and update.effective_message.reply_to_message.forward_from:
            user1 = update.effective_message.reply_to_message.from_user
            user2 = update.effective_message.reply_to_message.forward_from
            update.effective_message.reply_text(tld(chat.id,
                "The original sender, {}, has an ID of `{}`.\nThe forwarder, {}, has an ID of `{}`.").format(
                    escape_markdown(user2.first_name),
                    user2.id,
                    escape_markdown(user1.first_name),
                    user1.id),
                parse_mode=ParseMode.MARKDOWN)
        else:
            user = bot.get_chat(user_id)
            update.effective_message.reply_text(tld(chat.id, "{}'s id is `{}`.").format(escape_markdown(user.first_name), user.id),
                                                parse_mode=ParseMode.MARKDOWN)
    else:
        chat = update.effective_chat  # type: Optional[Chat]
        if chat.type == "private":
            update.effective_message.reply_text(tld(chat.id, "Your id is `{}`.").format(chat.id),
                                                parse_mode=ParseMode.MARKDOWN)

        else:
            update.effective_message.reply_text(tld(chat.id, "This group's id is `{}`.").format(chat.id),
                                                parse_mode=ParseMode.MARKDOWN)
@run_async
def stats(bot: Bot, update: Update):
    update.effective_message.reply_text("Current stats:\n" + "\n".join([mod.__stats__() for mod in STATS]))

@user_admin
@run_async
def info(bot: Bot, update: Update, args: List[str]):
    msg = update.effective_message  # type: Optional[Message]
    user_id = extract_user(update.effective_message, args)
    chat = update.effective_chat  # type: Optional[Chat]

    if user_id:
        user = bot.get_chat(user_id)

    elif not msg.reply_to_message and not args:
        user = msg.from_user

    elif not msg.reply_to_message and (not args or (
            len(args) >= 1 and not args[0].startswith("@") and not args[0].isdigit() and not msg.parse_entities(
        [MessageEntity.TEXT_MENTION]))):
        msg.reply_text(tld(chat.id, "I can't extract a user from this."))
        return

    else:
        return

    text =  tld(chat.id, "<b>User info</b>:")
    text += "\nID: <code>{}</code>".format(user.id)
    text += tld(chat.id, "\nFirst Name: {}").format(html.escape(user.first_name))

    if user.last_name:
        text += tld(chat.id, "\nLast Name: {}").format(html.escape(user.last_name))

    if user.username:
        text += tld(chat.id, "\nUsername: @{}").format(html.escape(user.username))

    text += tld(chat.id, "\nUser link: {}\n").format(mention_html(user.id, "link"))

    if user.id == OWNER_ID:
        text += tld(chat.id, "\n\nAy, This guy is my owner. I would never do anything against him!")
    else:
        if user.id in SUDO_USERS:
            text += tld(chat.id, "\nThis person is one of my sudo users! " \
            "Nearly as powerful as my owner - so watch it.")
        else:
            if user.id in SUPPORT_USERS:
                text += tld(chat.id, "\nThis person is one of my support users! " \
                        "Not quite a sudo user, but can still gban you off the map.")

            if user.id in WHITELIST_USERS:
                text += tld(chat.id, "\nThis person has been whitelisted! " \
                        "That means I'm not allowed to ban/kick them.")

    for mod in USER_INFO:
        mod_info = mod.__user_info__(user.id, chat.id).strip()
        if mod_info:
            text += "\n\n" + mod_info

    update.effective_message.reply_text(text, parse_mode=ParseMode.HTML)

@user_admin
@run_async
def echo(bot: Bot, update: Update):
    args = update.effective_message.text.split(None, 1)
    message = update.effective_message
    if message.reply_to_message:
        message.reply_to_message.reply_text(args[1])
    else:
        message.reply_text(args[1], quote=False)
    message.delete()

@user_admin
@run_async 
def reply_keyboard_remove(bot: Bot, update: Update):
    reply_keyboard = []
    reply_keyboard.append([
        ReplyKeyboardRemove(
            remove_keyboard=True
        )
    ])
    reply_markup = ReplyKeyboardRemove(
        remove_keyboard=True
    )
    old_message = bot.send_message(
        chat_id=update.message.chat_id,
        text='Bot Keyboard removed successfully !',
        reply_markup=reply_markup,
        reply_to_message_id=update.message.message_id
    )
    bot.delete_message(
        chat_id=update.message.chat_id,
        message_id=old_message.message_id
    )

@user_admin
@run_async
def gdpr(bot: Bot, update: Update):
    update.effective_message.reply_text(tld(update.effective_chat.id, "Deleting identifiable data..."))
    for mod in GDPR:
        mod.__gdpr__(update.effective_user.id)

    update.effective_message.reply_text(tld(update.effective_chat.id, "send_gdpr"), parse_mode=ParseMode.MARKDOWN)

@user_admin
@run_async
def markdown_help(bot: Bot, update: Update):
    chat = update.effective_chat  # type: Optional[Chat]
    update.effective_message.reply_text(tld(chat.id, "MARKDOWN_HELP-K"), parse_mode=ParseMode.HTML)
    
@run_async
@user_admin
def github(bot: Bot, update: Update):
    message = update.effective_message
    text = message.text[len('/git '):]
    usr = get(f'https://api.github.com/users/{text}').json()
    if usr.get('login'):
        reply_text = f"""*Name:* `{usr['name']}`
*Username:* `{usr['login']}`
*Account ID:* `{usr['id']}`
*Account type:* `{usr['type']}`
*Location:* `{usr['location']}`
*Bio:* `{usr['bio']}`
*Followers:* `{usr['followers']}`
*Following:* `{usr['following']}`
*Hireable:* `{usr['hireable']}`
*Public Repos:* `{usr['public_repos']}`
*Public Gists:* `{usr['public_gists']}`
*Email:* `{usr['email']}`
*Company:* `{usr['company']}`
*Website:* `{usr['blog']}`
*Last updated:* `{usr['updated_at']}`
*Account created at:* `{usr['created_at']}`
"""
    else:
        reply_text = "User not found. Make sure you entered valid username!"
    message.reply_text(reply_text, parse_mode=ParseMode.MARKDOWN)


@user_admin
@run_async
def repo(bot: Bot, update: Update, args: List[str]):
    message = update.effective_message
    text = message.text[len('/repo '):]
    usr = get(f'https://api.github.com/users/{text}/repos?per_page=300').json()
    reply_text = "*Repo*\n"
    for i in range(len(usr)):
        reply_text += f"[{usr[i]['name']}]({usr[i]['html_url']})\n"
    message.reply_text(reply_text,
                       parse_mode=ParseMode.MARKDOWN,
                       disable_web_page_preview=True)


BASE_URL = 'https://del.dog'

@user_admin
@run_async
def paste(bot: Bot, update: Update, args: List[str]):
    message = update.effective_message

    if message.reply_to_message:
        data = message.reply_to_message.text
    elif len(args) >= 1:
        data = message.text.split(None, 1)[1]
    else:
        message.reply_text("What am I supposed to do with this?!")
        return

    r = requests.post(f'{BASE_URL}/documents', data=data.encode('utf-8'))

    if r.status_code == 404:
        update.effective_message.reply_text('Failed to reach dogbin')
        r.raise_for_status()

    res = r.json()

    if r.status_code != 200:
        update.effective_message.reply_text(res['message'])
        r.raise_for_status()

    key = res['key']
    if res['isUrl']:
        reply = f'Shortened URL: {BASE_URL}/{key}\nYou can view stats, etc. [here]({BASE_URL}/v/{key})'
    else:
        reply = f'{BASE_URL}/{key}'
    update.effective_message.reply_text(reply, parse_mode=ParseMode.MARKDOWN, disable_web_page_preview=True)

@user_admin
@run_async
def get_paste_content(bot: Bot, update: Update, args: List[str]):
    message = update.effective_message

    if len(args) >= 1:
        key = args[0]
    else:
        message.reply_text("Please supply a paste key!")
        return

    format_normal = f'{BASE_URL}/'
    format_view = f'{BASE_URL}/v/'

    if key.startswith(format_view):
        key = key[len(format_view):]
    elif key.startswith(format_normal):
        key = key[len(format_normal):]

    r = requests.get(f'{BASE_URL}/raw/{key}')

    if r.status_code != 200:
        try:
            res = r.json()
            update.effective_message.reply_text(res['message'])
        except Exception:
            if r.status_code == 404:
                update.effective_message.reply_text('Failed to reach dogbin')
            else:
                update.effective_message.reply_text('Unknown error occured')
        r.raise_for_status()

    update.effective_message.reply_text('```' + escape_markdown(r.text) + '```', parse_mode=ParseMode.MARKDOWN)

@user_admin
@run_async
def get_paste_stats(bot: Bot, update: Update, args: List[str]):
    message = update.effective_message

    if len(args) >= 1:
        key = args[0]
    else:
        message.reply_text("Please supply a paste key!")
        return

    format_normal = f'{BASE_URL}/'
    format_view = f'{BASE_URL}/v/'

    if key.startswith(format_view):
        key = key[len(format_view):]
    elif key.startswith(format_normal):
        key = key[len(format_normal):]

    r = requests.get(f'{BASE_URL}/documents/{key}')

    if r.status_code != 200:
        try:
            res = r.json()
            update.effective_message.reply_text(res['message'])
        except Exception:
            if r.status_code == 404:
                update.effective_message.reply_text('Failed to reach dogbin')
            else:
                update.effective_message.reply_text('Unknown error occured')
        r.raise_for_status()

    document = r.json()['document']
    key = document['_id']
    views = document['viewCount']
    reply = f'Stats for **[/{key}]({BASE_URL}/{key})**:\nViews: `{views}`'
    update.effective_message.reply_text(reply, parse_mode=ParseMode.MARKDOWN)


@register(pattern="^/tts (.*)")
async def _(event):
    if event.fwd_from:
        return
    if event.is_group:
     if not (await is_register_admin(event.input_chat, event.message.sender_id)):
       await event.reply("")
       return
    input_str = event.pattern_match.group(1)
    reply_to_id = event.message.id
    if event.reply_to_msg_id:
        previous_message = await event.get_reply_message()
        text = previous_message.message
        lan = input_str
    elif "|" in input_str:
        lan, text = input_str.split("|")
    else:
        await event.reply("Invalid Syntax\nFormat `/tts lang | text`\nFor eg: `/tts en | hello`")
        return
    text = text.strip()
    lan = lan.strip()
    try:
        tts = gTTS(text, tld='com', lang=lan)
        tts.save("k.mp3") 
    except AssertionError:
        await event.reply('The text is empty.\n'
                         'Nothing left to speak after pre-precessing, '
                         'tokenizing and cleaning.')
        return
    except ValueError:
        await event.reply('Language is not supported.')
        return
    except RuntimeError:
        await event.reply('Error loading the languages dictionary.')
        return
    except gTTSError:
        await event.reply('Error in Google Text-to-Speech API request !')
        return
    with open("k.mp3", "r"):
        await event.client.send_file(event.chat_id, "k.mp3", voice_note=True, reply_to=reply_to_id)
        os.remove("k.mp3")

@register(pattern=r"^/wiki (.*)")
async def wiki(wiki_q):
    """ For .google command, fetch content from Wikipedia. """
    if wiki_q.is_group:
     if not (await is_register_admin(wiki_q.input_chat, wiki_q.message.sender_id)):
       await wiki_q.reply("")
       return
    match = wiki_q.pattern_match.group(1)
    try:
        summary(match)
    except DisambiguationError as error:
        await wiki_q.reply(f"Disambiguated page found.\n\n{error}")
        return
    except PageError as pageerror:
        await wiki_q.reply(f"Page not found.\n\n{pageerror}")
        return
    result = summary(match)
    if len(result) >= 4096:
        file = open("output.txt", "w+")
        file.write(result)
        file.close()
        await wiki_q.client.send_file(
            wiki_q.chat_id,
            "output.txt",
            reply_to=wiki_q.id,
            caption="`Output too large, sending as file`",
        )
        if os.path.exists("output.txt"):
            os.remove("output.txt")
        return
    await wiki_q.reply("**Search:**\n`" + match + "`\n\n**Result:**\n" + result)

import asyncio
import os
import requests
from bs4 import BeautifulSoup
from datetime import datetime
#from google_images_download import google_images_download
import sys
import shutil
from re import findall
import html2text

@register(pattern="^/google (.*)") 
async def _(event):
    if event.fwd_from:
        return
    if event.is_group:
     if not (await is_register_admin(event.input_chat, event.message.sender_id)):
       await event.reply("")
       return
    # SHOW_DESCRIPTION = False
    input_str = event.pattern_match.group(1) # + " -inurl:(htm|html|php|pls|txt) intitle:index.of \"last modified\" (mkv|mp4|avi|epub|pdf|mp3)"
    input_url = "https://bots.shrimadhavuk.me/search/?q={}".format(input_str)
    headers = {"USER-AGENT": "UniBorg"}
    response = requests.get(input_url, headers=headers).json()
    output_str = " "
    for result in response["results"]:
        text = result.get("title")
        url = result.get("url")
        description = result.get("description")
        last = html2text.html2text(description)
        output_str += "[{}]({})\n{}\n".format(text, url, last)       
    await event.reply("{}".format(output_str), link_preview=False, parse_mode='Markdown')

import aiohttp
import io
import time
from datetime import tzinfo, datetime


@register(pattern="^/weather (.*)")
async def _(event):
    if event.fwd_from:
        return
    if event.is_group:
     if not (await is_register_admin(event.input_chat, event.message.sender_id)):
       await event.reply("")
       return
    sample_url = "https://api.openweathermap.org/data/2.5/weather?q={}&APPID={}&units=metric"
    input_str = event.pattern_match.group(1)
    async with aiohttp.ClientSession() as session:
        response_api_zero = await session.get(sample_url.format(input_str, OPENWEATHERMAP_ID))
    response_api = await response_api_zero.json()
    if response_api["cod"] == 200:
        country_code = response_api["sys"]["country"]
        country_time_zone = int(response_api["timezone"])
        sun_rise_time = int(response_api["sys"]["sunrise"]) + country_time_zone
        sun_set_time = int(response_api["sys"]["sunset"]) + country_time_zone
        await event.reply(
            """**Location**: {}
**Temperature**: {}°С
    __minimium__: {}°С
    __maximum__ : {}°С
**Humidity**: {}%
**Wind**: {}m/s
**Clouds**: {}hpa
**Sunrise**: {} {}
**Sunset**: {} {}""".format(
                input_str,
                response_api["main"]["temp"],
                response_api["main"]["temp_min"],
                response_api["main"]["temp_max"],
                response_api["main"]["humidity"],
                response_api["wind"]["speed"],
                response_api["clouds"]["all"],
                # response_api["main"]["pressure"],
                time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime(sun_rise_time)),
                country_code,
                time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime(sun_set_time)),
                country_code
            )
        )
    else:
        await event.reply(response_api["message"])


@register(pattern="^/wttr (.*)")
async def _(event):
    if event.fwd_from:
        return
    if event.is_group:
     if not (await is_register_admin(event.input_chat, event.message.sender_id)):
       await event.reply("")
       return
    sample_url = "https://wttr.in/{}.png"
    # logger.info(sample_url)
    input_str = event.pattern_match.group(1)
    async with aiohttp.ClientSession() as session:
        response_api_zero = await session.get(sample_url.format(input_str))
        # logger.info(response_api_zero)
        response_api = await response_api_zero.read()
        with io.BytesIO(response_api) as out_file:
            await event.reply(
                file=out_file)
            

 
@register(pattern="^/figlet (.*)")
async def figlet(event):
    if event.fwd_from:
        return
    if event.is_group:
     if not (await is_register_admin(event.input_chat, event.message.sender_id)):
       await event.reply("")
       return
    input_str = event.pattern_match.group(1)
    result = pyfiglet.figlet_format(input_str)
    await event.respond("`{}`".format(result))


# MADE BY @AyushChatterjee

# from alexa.google_imgs import googleimagesdownload
import os
import shutil
from re import findall
from bing_image_downloader import downloader
import os
import cv2

@register(pattern="^/img (.*)")
async def img_sampler(event):
     if event.fwd_from:
        return
     if event.is_group:
       if not (await is_register_admin(event.input_chat, event.message.sender_id)):
          await event.reply("")
          return
     query = event.pattern_match.group(1)
     jit = f'"{query}"'
     downloader.download(query, limit=5, output_dir='outimages', adult_filter_off=False, force_replace=False, timeout=60)
     images = []
     for filename in os.listdir('./outimages/{jit}'):
        img = cv2.imread(os.path.join('./outimages/{jit}',filename))
        if img is not None:
            images.append(img)
     await event.client.send_file(event.chat_id, images, reply_to=event.id)
     os.system('rm -rf outimages')


@run_async
@user_admin
def shrug(bot: Bot, update: Update):
    default_msg = "¯\_(ツ)_/¯"
    message = update.effective_message
    if message.reply_to_message:
        message.reply_to_message.reply_text(default_msg)
    else:
        message.reply_text(default_msg)
        
from PyDictionary import PyDictionary
dictionary=PyDictionary()

@run_async
def define(bot: Bot, update: Update):
  message = update.effective_message
  text = message.text[len('/define '):]
  word = f"{text}"
  let = dictionary.meaning(word)
  set = str(let)
  jet = set.replace("{","")
  net = jet.replace("}","")
  got = net.replace("'", "")
  message.reply_text(got)

@run_async
def synonyms(bot: Bot, update: Update):
  message = update.effective_message
  text = message.text[len('/define '):]
  word = f"{text}"
  let = dictionary.synonym(word)
  set = str(let)
  jet = set.replace("{","")
  net = jet.replace("}","")
  got = net.replace("'", "")
  message.reply_text(got)

@run_async
def antonyms(bot: Bot, update: Update):
  message = update.effective_message
  text = message.text[len('/define '):]
  word = f"{text}"
  let = dictionary.antonym(word)
  set = str(let)
  jet = set.replace("{","")
  net = jet.replace("}","")
  got = net.replace("'", "")
  message.reply_text(got)

@register(pattern="^/yt (.*)")
async def yts_search(video_q):
    # For .yts command, do a YouTube search from Telegram.
    if video_q.is_group:
     if not (await is_register_admin(video_q.input_chat, video_q.message.sender_id)):
       await video_q.reply("")
       return
    query = video_q.pattern_match.group(1)
    result = ''

    if not YOUTUBE_API_KEY:
        await video_q.reply(
            "`Error: YouTube API key missing! Add it to environment vars or config.env.`"
        )
        return

   
    full_response = await youtube_search(query)
    videos_json = full_response[1]

    for video in videos_json:
        title = f"{unescape(video['snippet']['title'])}"
        link = f"https://youtu.be/{video['id']['videoId']}"
        result += f"{title}\n{link}\n\n"

    reply_text = f"**Search Query:**\n`{query}`\n\n**Results:**\n\n{result}"

    await video_q.reply(reply_text, link_preview=False)


async def youtube_search(query,
                         order="relevance",
                         token=None,
                         location=None,
                         location_radius=None):
    """ Do a YouTube search. """
    youtube = build('youtube',
                    'v3',
                    developerKey=YOUTUBE_API_KEY,
                    cache_discovery=False)
    search_response = youtube.search().list(
        q=query,
        type="video",
        pageToken=token,
        order=order,
        part="id,snippet",
        maxResults=10,
        location=location,
        locationRadius=location_radius).execute()

    videos = []

    for search_result in search_response.get("items", []):
        if search_result["id"]["kind"] == "youtube#video":
            videos.append(search_result)
    try:
        nexttok = search_response["nextPageToken"]
        return (nexttok, videos)
    except HttpError:
        nexttok = "last_page"
        return (nexttok, videos)
    except KeyError:
        nexttok = "KeyError, try again."
        return (nexttok, videos)

"""Get Administrators of any Chat*
Syntax: .userlist"""
from telethon import events
from telethon.tl.types import ChannelParticipantsAdmins, ChannelParticipantAdmin, ChannelParticipantCreator
from telethon.errors.rpcerrorlist import (UserIdInvalidError, MessageTooLongError, ChatAdminRequiredError)
                                                                                    
@register(pattern="^/users$")
async def get_users(show):
        if not show.is_group:
            await show.reply("Are you sure this is a group?")
            return
        if show.is_group:
         if not (await is_register_admin(show.input_chat, show.message.sender_id)):
          await show.reply("")
          return
        info = await show.client.get_entity(show.chat_id)
        title = info.title if info.title else "this chat"
        mentions = "Users in {}: \n".format(title)
        async for user in show.client.iter_participants(show.chat_id):
                  if not user.deleted:
                     mentions += f"\n[{user.first_name}](tg://user?id={user.id}) {user.id}"
                  else:
                      mentions += f"\nDeleted Account {user.id}"
        file = open("userslist.txt", "w+")
        file.write(mentions)
        file.close()
        await show.client.send_file(
                show.chat_id,
                "userslist.txt",
                caption='Users in {}'.format(title),
                reply_to=show.id,
                )
        os.remove("userslist.txt")


import requests
import bs4 
import re
from telethon import *

@register(pattern="^/app (.*)")
async def apk(e):
    if e.is_group:
     if not (await is_register_admin(e.input_chat, e.message.sender_id)):
          await e.reply("")
          return
    try:
        app_name = e.pattern_match.group(1)
        remove_space = app_name.split(' ')
        final_name = '+'.join(remove_space)
        page = requests.get("https://play.google.com/store/search?q="+final_name+"&c=apps")
        lnk = str(page.status_code)
        soup = bs4.BeautifulSoup(page.content,'lxml', from_encoding='utf-8')
        results = soup.findAll("div","ZmHEEd")
        app_name = results[0].findNext('div', 'Vpfmgd').findNext('div', 'WsMG1c nnK0zc').text
        app_dev = results[0].findNext('div', 'Vpfmgd').findNext('div', 'KoLSrc').text
        app_dev_link = "https://play.google.com"+results[0].findNext('div', 'Vpfmgd').findNext('a', 'mnKHRc')['href']
        app_rating = results[0].findNext('div', 'Vpfmgd').findNext('div', 'pf5lIe').find('div')['aria-label']
        app_link = "https://play.google.com"+results[0].findNext('div', 'Vpfmgd').findNext('div', 'vU6FJ p63iDd').a['href']
        app_icon = results[0].findNext('div', 'Vpfmgd').findNext('div', 'uzcko').img['data-src']
        app_details = "<a href='"+app_icon+"'>📲&#8203;</a>"
        app_details += " <b>"+app_name+"</b>"
        app_details += "\n\n<code>Developer :</code> <a href='"+app_dev_link+"'>"+app_dev+"</a>"
        app_details += "\n<code>Rating :</code> "+app_rating.replace("Rated ", "⭐ ").replace(" out of ", "/").replace(" stars", "", 1).replace(" stars", "⭐ ").replace("five", "5")
        app_details += "\n<code>Features :</code> <a href='"+app_link+"'>View in Play Store</a>"
        app_details += "\n\n===> @AlexaFamilyBot <==="
        await e.reply(app_details, link_preview = True, parse_mode = 'HTML')
    except IndexError:
        await e.reply("No result found in search. Please enter **Valid app name**")
    except Exception as err:
        await e.reply("Exception Occured:- "+str(err))

import asyncio
from telethon import events
from cowpy import cow

@register(pattern=r"^/(\w+)say (.*)")
async def univsaye(cowmsg):
    if cowmsg.is_group:
     if not (await is_register_admin(cowmsg.input_chat, cowmsg.message.sender_id)):
          await cowmsg.reply("")
          return
    """ For .cowsay module, uniborg wrapper for cow which says things. """
    if not cowmsg.text[0].isalpha() and cowmsg.text[0] not in ("#", "@"):
        arg = cowmsg.pattern_match.group(1).lower()
        text = cowmsg.pattern_match.group(2)

        if arg == "cow":
            arg = "default"
        if arg not in cow.COWACTERS:
            return
        cheese = cow.get_cow(arg)
        cheese = cheese()

        await cowmsg.reply(f"`{cheese.milk(text).replace('`', '´')}`")
 

@register(pattern="^/zombies(?: |$)(.*)")
async def rm_deletedacc(show):
    """ For .delusers command, list all the ghost/deleted accounts in a chat. """
    con = show.pattern_match.group(1).lower()
    del_u = 0
    del_status = "`No deleted accounts found, Group is cleaned as Hell`"
    chat = await show.get_chat()
    admin = chat.admin_rights
    creator = chat.creator
    
    if show.is_private:
        await show.reply("You can use this command in groups but not in PM's")
        return

    if show.is_group:
     if not (await is_register_admin(show.input_chat, show.message.sender_id)):
          await show.reply("")
          return

    if con != "clean":
        await show.reply("`Searching for zombie accounts...`")
        async for user in show.client.iter_participants(show.chat_id):
            if user.deleted:
                del_u += 1
         
        if del_u > 0:
            del_status = f"Found **{del_u}** deleted account(s) in this group,\
            \nclean them by using `/zombies clean`"

        await show.reply(del_status)
        return

    # Here laying the sanity check

    # Well
    if not admin and not creator:
        await show.reply("`I am not an admin here!`")
        return

    await show.reply("`Deleting deleted accounts...`")
    del_u = 0
    del_a = 0

    async for user in show.client.iter_participants(show.chat_id):
        if user.deleted:
            try:
                await show.client(
                    EditBannedRequest(show.chat_id, user.id, BANNED_RIGHTS))
            except ChatAdminRequiredError:
                await show.reply("`I don't have ban rights in this group`")
                return
            except UserAdminInvalidError:
                del_u -= 1
                del_a += 1
            await show.client(
                EditBannedRequest(show.chat_id, user.id, UNBAN_RIGHTS))
            del_u += 1

    if del_u > 0:
        del_status = f"Cleaned **{del_u}** deleted account(s)"

    if del_a > 0:
        del_status = f"Cleaned **{del_u}** deleted account(s) \
        \n**{del_a}** deleted admin accounts are not removed"

    await show.reply(del_status)


import json
import os
from PIL import Image
import requests


def ocr_space_file(filename, overlay=False, api_key=OCR_SPACE_API_KEY, language='eng'):
    payload = {'isOverlayRequired': overlay,
               'apikey': api_key,
               'language': language,
               }
    with open(filename, 'rb') as f:
        r = requests.post('https://api.ocr.space/parse/image',
                          files={filename: f},
                          data=payload,
                          )
    return r.json()


def ocr_space_url(url, overlay=False, api_key=OCR_SPACE_API_KEY, language='eng'):
    payload = {'url': url,
               'isOverlayRequired': overlay,
               'apikey': api_key,
               'language': language,
               }
    r = requests.post('https://api.ocr.space/parse/image',
                      data=payload,
                      )
    return r.json()


def progress(current, total):
    logger.info("Downloaded {} of {}\nCompleted {}".format(
        current, total, (current / total) * 100))


@register(pattern="^/img2textlang")
async def get_ocr_languages(event):
    if event.fwd_from:
        return
    if event.is_group:
     if not (await is_register_admin(event.input_chat, event.message.sender_id)):
          await event.reply("")
          return
    languages = {}
    languages["English"] = "eng"
    languages["Arabic"] = "ara"
    languages["Bulgarian"] = "bul"
    languages["Chinese (Simplified)"] = "chs"
    languages["Chinese (Traditional)"] = "cht"
    languages["Croatian"] = "hrv"
    languages["Czech"] = "cze"
    languages["Danish"] = "dan"
    languages["Dutch"] = "dut"
    languages["Finnish"] = "fin"
    languages["French"] = "fre"
    languages["German"] = "ger"
    languages["Greek"] = "gre"
    languages["Hungarian"] = "hun"
    languages["Korean"] = "kor"
    languages["Italian"] = "ita"
    languages["Japanese"] = "jpn"
    languages["Polish"] = "pol"
    languages["Portuguese"] = "por"
    languages["Russian"] = "rus"
    languages["Slovenian"] = "slv"
    languages["Spanish"] = "spa"
    languages["Swedish"] = "swe"
    languages["Turkish"] = "tur"
    a = json.dumps(languages, sort_keys=True, indent=4)
    await event.reply(str(a))


@register(pattern="^/img2text (.*)")
async def parse_ocr_space_api(event):
    if event.fwd_from:
        return
    if event.is_group:
     if not (await is_register_admin(event.input_chat, event.message.sender_id)):
          await event.reply("")
          return
    await event.reply("Processing ...")
    if not os.path.isdir(TEMP_DOWNLOAD_DIRECTORY):
        os.makedirs(TEMP_DOWNLOAD_DIRECTORY)
    lang_code = event.pattern_match.group(1)
    downloaded_file_name = await event.client.download_media(
        await event.get_reply_message(),
        TEMP_DOWNLOAD_DIRECTORY)
    if downloaded_file_name.endswith((".webp")):
        downloaded_file_name = conv_image(downloaded_file_name)
    test_file = ocr_space_file(filename=downloaded_file_name, language=lang_code)
    ParsedText = "hmm"
    try:
        ParsedText = test_file["ParsedResults"][0]["ParsedText"]
        ProcessingTimeInMilliseconds = str(int(test_file["ProcessingTimeInMilliseconds"]) // 1000)
    except Exception as e:
        await event.reply("Error :\n `{}`\nReport This to @AlexaSupport\n\n`{}`".format(str(e), json.dumps(test_file, sort_keys=True, indent=4)))
    else:
        await event.reply("Read Document in {} seconds. \n{}".format(ProcessingTimeInMilliseconds, ParsedText))
    os.remove(downloaded_file_name)
   



def conv_image(image):
    im = Image.open(image)
    im.save(image, "PNG")
    new_file_name = image + ".png"
    os.rename(image, new_file_name)
    return new_file_name



import asyncio
from getpass import getuser
from os import remove
from sys import executable
from alexa.events import register


"""Speech to Text
Syntax: .stt <Language Code> as reply to a speech message"""
from telethon import events
import requests
import os
import datetime

@register(pattern="^/stt")
async def _(event):
    if event.fwd_from:
        return
    if event.is_group:
     if not (await is_register_admin(event.input_chat, event.message.sender_id)):
          await event.reply("")
          return
    start = datetime.datetime.now()
    if not os.path.isdir(TEMP_DOWNLOAD_DIRECTORY):
        os.makedirs(TEMP_DOWNLOAD_DIRECTORY)
    await event.reply("Downloading to Alexa's server for Analysis ...")
    if event.reply_to_msg_id:
        previous_message = await event.get_reply_message()
        required_file_name = await event.client.download_media(previous_message, TEMP_DOWNLOAD_DIRECTORY)
        if IBM_WATSON_CRED_URL is None or IBM_WATSON_CRED_PASSWORD is None:
            await event.reply("You need to set the required ENV variables for this module. \nModule stopping")
        else:
            await event.reply("Starting analysis")
            headers = {
                "Content-Type": previous_message.media.document.mime_type,
            }
            data = open(required_file_name, "rb").read()
            response = requests.post(
                IBM_WATSON_CRED_URL + "/v1/recognize",
                headers=headers,
                data=data,
                auth=("apikey", IBM_WATSON_CRED_PASSWORD)
            )
            r = response.json()
            if "results" in r:
                # process the json to appropriate string format
                results = r["results"]
                transcript_response = ""
                transcript_confidence = ""
                for alternative in results:
                    alternatives = alternative["alternatives"][0]
                    transcript_response += " " + str(alternatives["transcript"]) 
                    transcript_confidence += " " + str(alternatives["confidence"]) + " + "
                end = datetime.datetime.now()
                ms = (end - start).seconds
                if transcript_response != "":
                    string_to_show = "Language: `English`\nTRANSCRIPT: `{}`\nTime Taken: {} seconds\nConfidence: `{}`".format(transcript_response, ms, transcript_confidence)
                else:
                    string_to_show = "Language: `English`\nTime Taken: {} seconds\n**No Results Found**".format(ms)
                await event.reply(string_to_show)
            else:
                await event.reply(r["error"])
            # now, remove the temporary file
            os.remove(required_file_name)
    else:
        await event.reply("Reply to a voice message, to get the text out of it.")

from telethon import events
import os
import requests
import json
import bs4
from bs4 import BeautifulSoup as soup
from urllib.request import urlopen


@register(pattern="^/news")
async def _(event):
  if event.is_group:
     return
  if event.fwd_from:
     return
 
  news_url="https://news.google.com/rss?hl=en-IN&gl=IN&ceid=IN:en"
  Client=urlopen(news_url)
  xml_page=Client.read()
  Client.close()
  soup_page=soup(xml_page,"xml")
  news_list=soup_page.findAll("item")
  for news in news_list:
       title = news.title.text
       text = news.link.text
       date = news.pubDate.text
       seperator = "-"*50
       l = "\n"
       lastisthis = title+l+text+l+date+l+seperator
       await event.reply(lastisthis)


from telethon.tl.types import InputMediaDice

@register(pattern="^/dice")
async def _(event):
    if event.fwd_from:
        return
    if event.is_group:
     if not (await is_register_admin(event.input_chat, event.message.sender_id)):
          await event.reply("")
          return
    input_str = print(randrange(7))
    r = await event.reply(file=InputMediaDice(''))
    if input_str:
        try:
            required_number = int(input_str)
            while not r.media.value == required_number:
                await r.delete()
                r = await event.reply(file=InputMediaDice(''))
        except:
            pass

@register(pattern="^/basketball")
async def _(event):
    if event.fwd_from:
        return
    if event.is_group:
     if not (await is_register_admin(event.input_chat, event.message.sender_id)):
          await event.reply("")
          return
    input_str = print(randrange(6))
    r = await event.reply(file=InputMediaDice('🏀'))
    if input_str:
        try:
            required_number = int(input_str)
            while not r.media.value == required_number:
                await r.delete()
                r = await event.reply(file=InputMediaDice('🏀'))
        except:
            pass


@register(pattern="^/dart")
async def _(event):
    if event.fwd_from:
        return
    if event.is_group:
     if not (await is_register_admin(event.input_chat, event.message.sender_id)):
          await event.reply("")
          return
    input_str = print(randrange(7))
    r = await event.reply(file=InputMediaDice('🎯'))
    if input_str:
        try:
            required_number = int(input_str)
            while not r.media.value == required_number:
                await r.delete()
                r = await event.reply(file=InputMediaDice('🎯'))
        except:
            pass

import datetime
from typing import List

import requests
from telegram import Bot, Update, ParseMode
from telegram.ext import run_async

from alexa import dispatcher, TIME_API_KEY
from alexa.modules.disable import DisableAbleCommandHandler

def generate_time(to_find: str, findtype: List[str]) -> str:
    data = requests.get(f"http://api.timezonedb.com/v2.1/list-time-zone"
                        f"?key={TIME_API_KEY}"
                        f"&format=json"
                        f"&fields=countryCode,countryName,zoneName,gmtOffset,timestamp,dst").json()

    for zone in data["zones"]:
        for eachtype in findtype:
            if to_find in zone[eachtype].lower():
                country_name = zone['countryName']
                country_zone = zone['zoneName']
                country_code = zone['countryCode']

                if zone['dst'] == 1:
                    daylight_saving = "Yes"
                else:
                    daylight_saving = "No"

                date_fmt = r"%d-%m-%Y"
                time_fmt = r"%H:%M:%S"
                day_fmt = r"%A"
                gmt_offset = zone['gmtOffset']
                timestamp = datetime.datetime.now(datetime.timezone.utc) + datetime.timedelta(seconds=gmt_offset)
                current_date = timestamp.strftime(date_fmt)
                current_time = timestamp.strftime(time_fmt)
                current_day = timestamp.strftime(day_fmt)

                break

    try:
        result = (f"<b>🌍Country :</b> <code>{country_name}</code>\n"
                  f"<b>⏳Zone Name :</b> <code>{country_zone}</code>\n"
                  f"<b>🗺Country Code :</b> <code>{country_code}</code>\n"
                  f"<b>🌞Daylight saving :</b> <code>{daylight_saving}</code>\n"
                  f"<b>🌅Day :</b> <code>{current_day}</code>\n"
                  f"<b>⌚Current Time :</b> <code>{current_time}</code>\n"
                  f"<b>📆Current Date :</b> <code>{current_date}</code>")
    except:
        result = None

    return result


@run_async
@user_admin
def gettime(bot: Bot, update: Update):
    message = update.effective_message

    try:
        query = message.text.strip().split(" ", 1)[1]
    except:
        message.reply_text("Provide a country name/abbreviation/timezone to find.")
        return
    send_message = message.reply_text(f"Finding timezone info for <b>{query}</b>", parse_mode=ParseMode.HTML)

    query_timezone = query.lower()
    if len(query_timezone) == 2:
        result = generate_time(query_timezone, ["countryCode"])
    else:
        result = generate_time(query_timezone, ["zoneName", "countryName"])

    if not result:
        send_message.edit_text(f"Timezone info not available for <b>{query}</b>", parse_mode=ParseMode.HTML)
        return

    send_message.edit_text(result, parse_mode=ParseMode.HTML)



# Simple lyrics module using tswift by @TheRealPhoenix

from tswift import Song
from telegram import Bot, Update, Message, Chat
from telegram.ext import run_async
from alexa import dispatcher
from alexa.modules.disable import DisableAbleCommandHandler


@run_async
@user_admin
def lyrics(bot: Bot, update: Update, args):
    msg = update.effective_message
    query = " ".join(args)
    song = ""
    if not query:
        msg.reply_text("You haven't specified which song to look for!")
        return
    else:
        song = Song.find_song(query)
        if song:
            if song.lyrics:
                reply = song.format()
            else:
                reply = "Couldn't find any lyrics for that song!"
        else:
            reply = "Song not found!"
        if len(reply) > 4090:
            with open("lyrics.txt", 'w') as f:
                f.write(f"{reply}\n\n\nOwO UwU OwO")
            with open("lyrics.txt", 'rb') as f:
                msg.reply_document(document=f,
                caption="Message length exceeded max limit! Sending as a text file.")
        else:
            msg.reply_text(reply)

# Made by @Ayushchatterjee

import wolframalpha 
from alexa import WOLFRAM_ID

@register(pattern=r"^/elizabeth(?: |$)([\s\S]*)")
async def _(event):
    if event.fwd_from:
        return
    if event.is_group:
     if not (await is_register_admin(event.input_chat, event.message.sender_id)):
          await event.reply("")
          return
    if not event.reply_to_msg_id:
       app_id =  WOLFRAM_ID
       client = wolframalpha.Client(app_id) 
       question = event.pattern_match.group(1)
       res = client.query(question) 
       answer = next(res.results).text 
       await event.reply(f'**{question}**\n\n' + answer, parse_mode='Markdown')
        
    if event.reply_to_msg_id:
        previous_message = await event.get_reply_message()
        required_file_name = await event.client.download_media(previous_message, TEMP_DOWNLOAD_DIRECTORY)
        if IBM_WATSON_CRED_URL is None or IBM_WATSON_CRED_PASSWORD is None:
            await event.reply("You need to set the required ENV variables for this module. \nModule stopping")
        else:
            headers = {
                "Content-Type": previous_message.media.document.mime_type,
            }
            data = open(required_file_name, "rb").read()
            response = requests.post(
                IBM_WATSON_CRED_URL + "/v1/recognize",
                headers=headers,
                data=data,
                auth=("apikey", IBM_WATSON_CRED_PASSWORD)
            )
            r = response.json()
            if "results" in r:
                # process the json to appropriate string format
                results = r["results"]
                transcript_response = ""
                transcript_confidence = ""
                for alternative in results:
                    alternatives = alternative["alternatives"][0]
                    transcript_response += " " + str(alternatives["transcript"]) 
                if transcript_response != "":
                    string_to_show = "{}".format(transcript_response)           
                    app_id =  WOLFRAM_ID
                    client = wolframalpha.Client(app_id)
                    res = client.query(string_to_show)
                    answer = next(res.results).text
                    try:
                       tts = gTTS(answer, tld='com', lang='en')
                       tts.save("results.mp3")
                    except AssertionError: 
                      return
                    except ValueError:    
                      return
                    except RuntimeError:        
                      return
                    except gTTSError:
                      return
                    with open("results.mp3", "r"):
                        await event.client.send_file(event.chat_id, "results.mp3", voice_note=True, reply_to=event.id)
                    os.remove("results.mp3")
                else:                   
                    try:
                       answer = "Sorry I can't recognise your query"
                       tts = gTTS(answer, tld='com', lang='en')
                       tts.save("results.mp3")
                    except AssertionError: 
                      return
                    except ValueError:    
                      return
                    except RuntimeError:        
                      return
                    except gTTSError:
                      return
                    with open("results.mp3", "r"):
                        await event.client.send_file(event.chat_id, "results.mp3", voice_note=True, reply_to=event.id)
                    os.remove("results.mp3")
            else:
                await event.reply("API Failure !")
                os.remove(required_file_name)


from bs4 import BeautifulSoup as bs 
import requests
from telethon import events
from alexa.events import register
import asyncio
import subprocess
import telegraph
telegraph = Telegraph()
telegraph.create_account(short_name='Alexa')

@register(pattern="^/torrent (.*)")
async def tor_search(event):
   if event.fwd_from:
      return 
   if event.is_group:
    if not (await is_register_admin(event.input_chat, event.message.sender_id)):
          await event.reply("")
          return
   str = event.pattern_match.group(1)
   let = f'"{str}"'
   jit = subprocess.check_output(["we-get", "-s", let, "-J"])   
   proc = jit.decode()
   sit = proc.replace("{", "")
   pit = sit.replace("}", "")
   op = pit.replace(",", "")
   seta = f"Magnets for {str} are below:"
   response = telegraph.create_page(seta, html_content=op)
   await event.reply('Magnet Links for {}:\n\nhttps://telegra.ph/{}'.format(str,response['path']), link_preview=False) 

@register(pattern="^/fortune")
async def fortunate(event):
   if event.fwd_from:
      return 
   if event.is_group:
    if not (await is_register_admin(event.input_chat, event.message.sender_id)):
          await event.reply("")
          return
   jit = subprocess.check_output(["python", "fortune"])
   pit = jit.decode()
   await event.reply(pit)

from alexa import *

@register(pattern="^/helptorrent")
async def helptorrent(event):
 if event.fwd_from or event.is_group:
    return 
 else:
   topa = "./alexa/Tutorial_For_Torrent.mp4"
   file = await event.client.upload_file(topa) 
   await event.client.send_file(event.chat_id, file, caption="Tutorial For Torrent Module", reply_to=event.id)
   
@register(pattern="^/helpcamscanner")
async def helpcam(event):
 if event.fwd_from or event.is_group:
    return 
 else:
   topa = "./alexa/Tutorial for Camscanner.mp4"
   file = await event.client.upload_file(topa) 
   await event.client.send_file(event.chat_id, file, caption="Tutorial For Camscanner Module", reply_to=event.id)
   


import sys
import requests
import json
import time
import urllib
import os

@register(pattern=r'^/phone (.*)')
async def phone(event): 
    if event.is_group:
     if not (await is_register_admin(event.input_chat, event.message.sender_id)):
          await event.reply("")
          return
    information = event.pattern_match.group(1)
    number = information
    key = "fe65b94e78fc2e3234c1c6ed1b771abd" 
    api = "http://apilayer.net/api/validate?access_key=" + key + "&number=" + number + "&country_code=&format=1"
    output = requests.get(api)
    content = output.text
    obj = json.loads(content)
    country_code = obj['country_code']
    country_name = obj['country_name']
    location = obj['location']
    carrier = obj['carrier']
    line_type = obj['line_type']	
    validornot = obj['valid']	
    aa = "Valid: "+str(validornot)
    a = "Phone number: "+str(number)
    b = "Country: " +str(country_code)
    c = "Country Name: " +str(country_name)
    d = "Location: " +str(location)
    e = "Carrier: " +str(carrier)
    f = "Device: " +str(line_type)
    g = f"{aa}\n{a}\n{b}\n{c}\n{d}\n{e}\n{f}"
    await event.reply(g)


@register(pattern="^/ping")
async def pingme(pong):
    if pong.is_group:
     if not (await is_register_admin(pong.input_chat, pong.message.sender_id)):
          await pong.reply("")
          return
    """ FOr .pingme command, ping the userbot from any chat.  """
    start = datetime.datetime.now()
    up = await pong.reply("`Pong!`")
    end = datetime.datetime.now()
    duration = (end - start).microseconds / 1000
    await up.edit("`Pong!\n%sms`" % (duration))


from telethon import events
from telethon.tl.types import UserStatusEmpty, UserStatusLastMonth, UserStatusLastWeek, UserStatusOffline, UserStatusOnline, UserStatusRecently, ChannelParticipantsKicked, ChatBannedRights
from telethon.tl import functions, types
from time import sleep
import asyncio
from telethon import *
from telethon.tl.functions.channels import (EditAdminRequest,
                                            EditBannedRequest,
                                            EditPhotoRequest)
                                           
@register(pattern="^/kickthefools")
async def _(event):
    if event.fwd_from:
        return
    
    if event.is_private:
        await event.reply("You can use this command in groups but not in PM's")
        return

    chat = await event.get_chat()
    admin = chat.admin_rights
    sender = await event.get_sender()
    
    if not event.chat.admin_rights.ban_users:
       await event.reply("I don't have sufficient permissions")
       return

    if event.is_group:
     if not (await is_register_admin(event.input_chat, event.message.sender_id)):
       return

    c = 0
    KICK_RIGHTS = ChatBannedRights(until_date=None, view_messages=True)
    await event.reply("Searching Participant Lists...")
    async for i in event.client.iter_participants(event.chat_id):
        print(i) #optional
        if isinstance(i.status, UserStatusLastMonth):
            status = await event.client(EditBannedRequest(event.chat_id, i, KICK_RIGHTS))
            if not status:
               return
            else:
               c = c + 1
                    
        if isinstance(i.status, UserStatusLastWeek):
            status = await event.client(EditBannedRequest(event.chat_id, i, KICK_RIGHTS))
            if not status:
               return
            else:
               c = c + 1                 

    required_string = "Successfully Kicked **{}** users"
    await event.reply(required_string.format(c))

      
import os
import sys

@register(pattern="^/camscanner")
async def asciiart(event):
  if event.fwd_from:
     return  
  if not event.from_id:
     await event.reply("Reply To A Image Plox..")
     return
  if event.is_group:
   if not (await is_register_admin(event.input_chat, event.message.sender_id)):
          await event.reply("")
          return
  directory = "./"
  test = os.listdir(directory)
  for item in test:
    if item.endswith(".jpg"):
        os.remove(os.path.join(directory, item))
    elif item.endswith(".png"):
        os.remove(os.path.join(directory, item))
    elif item.endswith(".jpeg"):
        os.remove(os.path.join(directory, item))
  reply_msg = await event.get_reply_message()
  downloaded_file_name = await event.client.download_media(reply_msg, './')
  let = f"{downloaded_file_name}"
  subprocess.run(["python", "scan", "--image", let])
  fuck = await event.client.upload_file("./scanned.jpg")
  await event.client.send_file(event.chat_id, fuck)
  directory = "./"
  test = os.listdir(directory)
  for item in test:
    if item.endswith(".jpg"):
        os.remove(os.path.join(directory, item))
    elif item.endswith(".png"):
        os.remove(os.path.join(directory, item))
    elif item.endswith(".jpeg"):
        os.remove(os.path.join(directory, item))
    

import asyncio
import barcode
import os
import time
from barcode.writer import ImageWriter
import datetime
from alexa.events import register
from telethon import events


@register(pattern="^/barcode ?(.*)")
async def _(event):
    if event.fwd_from:
        return
    if event.is_group:
       if not (await is_register_admin(event.input_chat, event.message.sender_id)):
          await event.reply("")
          return
    start = datetime.datetime.now()
    input_str = event.pattern_match.group(1)
    message = "SYNTAX: `.barcode <long text to include>`"
    reply_msg_id = event.message.id
    if input_str:
        message = input_str
    elif event.reply_to_msg_id:
        previous_message = await event.get_reply_message()
        reply_msg_id = previous_message.id
        if previous_message.media:
            downloaded_file_name = await event.client.download_media(
                previous_message,
                Config.TEMP_DOWNLOAD_DIRECTORY,
            )
            m_list = None
            with open(downloaded_file_name, "rb") as fd:
                m_list = fd.readlines()
            message = ""
            for m in m_list:
                message += m.decode("UTF-8") + "\r\n"
            os.remove(downloaded_file_name)
        else:
            message = previous_message.message
    else:
        message = "SYNTAX: `.barcode <long text to include>`"
    bar_code_type = "code128"
    try:
        bar_code_mode_f = barcode.get(bar_code_type, message, writer=ImageWriter())
        filename = bar_code_mode_f.save(bar_code_type)
        await event.client.send_file(
            event.chat_id,
            filename,
            caption=message,
            reply_to=reply_msg_id,
        )
        os.remove(filename)
    except Exception as e:
        await event.reply(str(e))
        return
    end = datetime.now()
    ms = (end - start).seconds
    await event.reply("Created BarCode in {} seconds".format(ms))


@register(pattern="^/unbanall")
async def _(event):
    if event.is_private:
       return
    if event.is_group: 
       sender = event.message.sender_id
       if not sender.ChatAdminRights(ban_users=True):
           return
    done = await event.reply("Searching Participant Lists.")
    p = 0
    async for i in event.client.iter_participants(event.chat_id, filter=ChannelParticipantsKicked, aggressive=True):
            rights = ChatBannedRights(
                until_date=0,
                view_messages=False
            )
            try:
                await tbot(functions.channels.EditBannedRequest(event.chat_id, i, rights))
            except FloodWaitError as ex:
                logger.warn("sleeping for {} seconds".format(ex.seconds))
                sleep(ex.seconds)
            except Exception as ex:
                await event.reply(str(ex))
            else:
                p += 1
            await done.edit("{}: {} unbanned".format(event.chat_id, p))

@register(pattern="^/unmuteall")
async def _(event):
    if event.fwd_from:
        return
    if event.is_private:
       return 
    if event.is_group:
       if not (await is_register_banful(event.chat, event.message.sender_id)):
          await event.reply("")
          return
    done = await event.reply("Searching Participant Lists.")
    p = 0
    async for i in event.client.iter_participants(event.chat_id, filter=ChannelParticipantsKicked, aggressive=True):
            rights = ChatBannedRights(MUTE_RIGHTS)
            try:
                await tbot(functions.channels.EditBannedRequest(event.chat_id, i, rights))
            except FloodWaitError as ex:
                logger.warn("sleeping for {} seconds".format(ex.seconds))
                sleep(ex.seconds)
            except Exception as ex:
                await event.reply(str(ex))
            else:
                p += 1
            await done.edit("{}: {} unbanned".format(event.chat_id, p))


@register(pattern="^/smsbomb (.*) (.*)")
async def sms_hack(event):
   if event.fwd_from:
      return 
   if event.is_group:
    if not (await is_register_admin(event.input_chat, event.message.sender_id)):
          await event.reply("")
          return
   str = event.pattern_match.group(1)
   ptr = event.pattern_match.group(2)
   subprocess.run(["python3", "Bomber.py", "--proxy", "--sms", "500", "-T", "30", "-c", f"{str}", f"{ptr}"])
   await event.reply(f"**ATTACK SUCCESSFULL ON TARGET:** `+{str}{ptr}`")

# Oringinal Source from Nicegrill: https://github.com/erenmetesar/NiceGrill/
# Ported to Lynda by: @pokurt
from PIL import Image, ImageDraw, ImageFont, ImageOps
from telethon.tl import types, functions
from fontTools.ttLib import TTFont 
from fontTools.unicode import Unicode 
import emoji
import textwrap
import urllib
import logging
import random
import json
import os
import re

COLORS = [
    "#F07975", "#F49F69", "#F9C84A", "#8CC56E", "#6CC7DC", "#80C1FA", "#BCB3F9", "#E181AC"]

async def process(msg, user, client, reply, replied=None):
        if not os.path.isdir("resources"):
            os.mkdir("resources", 0o755)
            urllib.request.urlretrieve(
                'https://github.com/erenmetesar/modules-repo/raw/master/Roboto-Regular.ttf',
                'resources/Roboto-Regular.ttf')
            urllib.request.urlretrieve(
                'https://github.com/erenmetesar/modules-repo/raw/master/Quivira.otf',
                'resources/Quivira.otf')
            urllib.request.urlretrieve(
                'https://github.com/erenmetesar/modules-repo/raw/master/Roboto-Medium.ttf',
                'resources/Roboto-Medium.ttf')
            urllib.request.urlretrieve(
                'https://github.com/erenmetesar/modules-repo/raw/master/DroidSansMono.ttf',
                'resources/DroidSansMono.ttf')
            urllib.request.urlretrieve(
                'https://github.com/erenmetesar/modules-repo/raw/master/Roboto-Italic.ttf',
                'resources/Roboto-Italic.ttf')

        # Importıng fonts and gettings the size of text
        font = ImageFont.truetype("resources/Roboto-Medium.ttf", 43, encoding="utf-16")
        font2 = ImageFont.truetype("resources/Roboto-Regular.ttf", 33, encoding="utf-16")
        mono = ImageFont.truetype("resources/DroidSansMono.ttf", 30, encoding="utf-16")
        italic = ImageFont.truetype("resources/Roboto-Italic.ttf", 33, encoding="utf-16")
        fallback = ImageFont.truetype("resources/Quivira.otf", 43, encoding="utf-16")

        # Splitting text
        maxlength = 0
        width = 0
        text = []
        for line in msg.split("\n"):
            length = len(line)
            if length > 43:
                text += textwrap.wrap(line, 43)
                maxlength = 43
                if width < fallback.getsize(line[:43])[0]:
                    if "MessageEntityCode" in str(reply.entities):
                        width = mono.getsize(line[:43])[0] + 30
                    else:
                        width = fallback.getsize(line[:43])[0]
                next
            else:
                text.append(line + "\n")
                if width < fallback.getsize(line)[0]:
                    if "MessageEntityCode" in str(reply.entities):
                        width = mono.getsize(line)[0] + 30
                    else:
                        width = fallback.getsize(line)[0]
                if maxlength < length:
                    maxlength = length

        title = ""
        try:
            details = await client(functions.channels.GetParticipantRequest(reply.chat_id, user.id))
            if isinstance(details.participant, types.ChannelParticipantCreator):
                title = details.participant.rank if details.participant.rank else "Creator"
            elif isinstance(details.participant, types.ChannelParticipantAdmin):
                title = details.participant.rank if details.participant.rank else "Admin"
        except TypeError:
            pass
        titlewidth = font2.getsize(title)[0]

        # Get user name
        lname = "" if not user.last_name else user.last_name
        tot = user.first_name + " " + lname

        namewidth = fallback.getsize(tot)[0] + 10

        if namewidth > width:
            width = namewidth
        width += titlewidth + 30 if titlewidth > width - namewidth else -(titlewidth - 30)
        height = len(text) * 40

        # Profile Photo BG
        pfpbg = Image.new("RGBA", (125, 600), (0, 0, 0, 0))

        # Draw Template
        top, middle, bottom = await drawer(width, height)
        # Profile Photo Check and Fetch
        yes = False
        color = random.choice(COLORS)
        async for photo in client.iter_profile_photos(user, limit=1):
            yes = True
        if yes:
            pfp = await client.download_profile_photo(user)
            paste = Image.open(pfp)
            os.remove(pfp)
            paste.thumbnail((105, 105))

            # Mask
            mask_im = Image.new("L", paste.size, 0)
            draw = ImageDraw.Draw(mask_im)
            draw.ellipse((0, 0, 105, 105), fill=255)

            # Apply Mask
            pfpbg.paste(paste, (0, 0), mask_im)
        else:
            paste, color = await no_photo(user, tot)
            pfpbg.paste(paste, (0, 0))

        # Creating a big canvas to gather all the elements
        canvassize = (
            middle.width + pfpbg.width, top.height + middle.height + bottom.height)
        canvas = Image.new('RGBA', canvassize)
        draw = ImageDraw.Draw(canvas)

        y = 80
        if replied:
            # Creating a big canvas to gather all the elements
            replname = "" if not replied.sender.last_name else replied.sender.last_name
            reptot = replied.sender.first_name + " " + replname
            replywidth = font2.getsize(reptot)[0]
            if reply.sticker:
                sticker = await reply.download_media()
                stimg = Image.open(sticker)
                canvas = canvas.resize((stimg.width + pfpbg.width, stimg.height + 160))
                top = Image.new("RGBA", (200 + stimg.width, 300), (29, 29, 29, 255))
                draw = ImageDraw.Draw(top)
                await replied_user(draw, reptot, replied.message.replace("\n", " "), 20)
                top = top.crop((135, 70, top.width, 300))
                canvas.paste(pfpbg, (0,0))
                canvas.paste(top, (pfpbg.width + 10, 0))
                canvas.paste(stimg, (pfpbg.width + 10, 140))
                os.remove(sticker)
                return True, canvas
            canvas = canvas.resize((canvas.width + 60, canvas.height + 120))
            top, middle, bottom = await drawer(middle.width + 60, height + 105)
            canvas.paste(pfpbg, (0, 0))
            canvas.paste(top, (pfpbg.width, 0))
            canvas.paste(middle, (pfpbg.width, top.height))
            canvas.paste(bottom, (pfpbg.width, top.height + middle.height))
            draw = ImageDraw.Draw(canvas)
            if replied.sticker:
                replied.text = "Sticker"
            elif replied.photo:
                replied.text = "Photo"
            elif replied.audio:
                replied.text = "Audio"
            elif replied.voice:
                replied.text = "Voice Message"
            elif replied.document:
                replied.text = "Document"
            await replied_user(draw, reptot, replied.message.replace("\n", " "), maxlength + len(title), len(title))
            y = 200
        elif reply.sticker:
            sticker = await reply.download_media()
            stimg = Image.open(sticker)
            canvas = canvas.resize((stimg.width + pfpbg.width + 30, stimg.height + 10))
            canvas.paste(pfpbg, (0,0))
            canvas.paste(stimg, (pfpbg.width + 10, 10))
            os.remove(sticker)
            return True, canvas
        elif reply.document and not reply.audio and not reply.audio:
            docname = ".".join(reply.document.attributes[-1].file_name.split(".")[:-1])
            doctype = reply.document.attributes[-1].file_name.split(".")[-1].upper()
            if reply.document.size < 1024:
                docsize = str(reply.document.size) + " Bytes"
            elif reply.document.size < 1048576:
                docsize = str(round(reply.document.size / 1024, 2)) + " KB "
            elif reply.document.size < 1073741824:
                docsize = str(round(reply.document.size / 1024**2, 2)) + " MB "
            else:
                docsize = str(round(reply.document.size / 1024**3, 2)) + " GB "
            docbglen = font.getsize(docsize)[0] if font.getsize(docsize)[0] > font.getsize(docname)[0] else font.getsize(docname)[0]
            canvas = canvas.resize((pfpbg.width + width + docbglen, 160 + height))
            top, middle, bottom = await drawer(width + docbglen, height + 30)
            canvas.paste(pfpbg, (0, 0))
            canvas.paste(top, (pfpbg.width, 0))
            canvas.paste(middle, (pfpbg.width, top.height))
            canvas.paste(bottom, (pfpbg.width, top.height + middle.height))
            canvas = await doctype(docname, docsize, doctype, canvas)
            y = 80 if text else 0
        else:
            canvas.paste(pfpbg, (0, 0))
            canvas.paste(top, (pfpbg.width, 0))
            canvas.paste(middle, (pfpbg.width, top.height))
            canvas.paste(bottom, (pfpbg.width, top.height + middle.height))
            y = 85

        # Writing User's Name
        space = pfpbg.width + 30
        namefallback = ImageFont.truetype("resources/Quivira.otf", 43, encoding="utf-16")
        for letter in tot:
            if letter in emoji.UNICODE_EMOJI:
                newemoji, mask = await emoji_fetch(letter)
                canvas.paste(newemoji, (space, 24), mask)
                space += 40
            else:
                if not await fontTest(letter):
                    draw.text((space, 20), letter, font=namefallback, fill=color)
                    space += namefallback.getsize(letter)[0]
                else:
                    draw.text((space, 20), letter, font=font, fill=color)
                    space += font.getsize(letter)[0]

        if title:
            draw.text((canvas.width - titlewidth - 20, 25), title, font=font2, fill="#898989")

        # Writing all separating emojis and regular texts
        x = pfpbg.width + 30
        bold, mono, italic, link = await get_entity(reply)
        mdlength = 0
        index = 0
        emojicount = 0
        textfallback = ImageFont.truetype("resources/Quivira.otf", 33, encoding="utf-16")
        textcolor = "white"
        for line in text:
            for letter in line:
                index = msg.find(letter) if emojicount == 0 else msg.find(letter) + emojicount
                for offset, length in bold.items():
                    if index in range(offset, length):
                        font2 = ImageFont.truetype("resources/Roboto-Medium.ttf", 33, encoding="utf-16")
                        textcolor = "white"
                for offset, length in italic.items():
                    if index in range(offset, length):
                        font2 = ImageFont.truetype("resources/Roboto-Italic.ttf", 33, encoding="utf-16")
                        textcolor = "white"
                for offset, length in mono.items():
                    if index in range(offset, length):
                        font2 = ImageFont.truetype("resources/DroidSansMono.ttf", 30, encoding="utf-16")
                        textcolor = "white"
                for offset, length in link.items():
                    if index in range(offset, length):
                        font2 = ImageFont.truetype("resources/Roboto-Regular.ttf", 30, encoding="utf-16")
                        textcolor = "#898989"
                if letter in emoji.UNICODE_EMOJI:
                    newemoji, mask = await emoji_fetch(letter)
                    canvas.paste(newemoji, (x, y - 2), mask)
                    x += 45
                    emojicount += 1
                else:
                    if not await fontTest(letter):
                        draw.text((x, y), letter, font=textfallback, fill=textcolor)
                        x += textfallback.getsize(letter)[0]
                    else:
                        draw.text((x, y), letter, font=font2, fill=textcolor)
                        x += font2.getsize(letter)[0]
                msg = msg.replace(letter, "¶", 1)
            y += 40
            x = pfpbg.width + 30
        return True, canvas

async def drawer(width, height):
        # Top part
        top = Image.new('RGBA', (width, 20), (0,0,0,0))
        draw = ImageDraw.Draw(top)
        draw.line((10, 0, top.width - 20, 0),  fill=(29, 29, 29, 255), width=50)
        draw.pieslice((0, 0, 30, 50), 180, 270, fill=(29, 29, 29, 255))
        draw.pieslice((top.width - 75, 0, top.width, 50), 270, 360, fill=(29, 29, 29, 255))

        # Middle part
        middle = Image.new("RGBA", (top.width, height + 75), (29, 29, 29, 255))
        
        # Bottom part
        bottom = ImageOps.flip(top)

        return top, middle, bottom

async def fontTest(letter):
        test = TTFont("resources/Roboto-Medium.ttf")
        for table in test['cmap'].tables:
            if ord(letter) in table.cmap.keys():
                return True

async def get_entity(msg):
        bold = {0: 0}
        italic = {0: 0}
        mono = {0: 0}
        link = {0: 0}
        if not msg.entities:
            return bold, mono, italic, link
        for entity in msg.entities:
            if isinstance(entity, types.MessageEntityBold):
                bold[entity.offset] = entity.offset + entity.length
            elif isinstance(entity, types.MessageEntityItalic):
                italic[entity.offset] = entity.offset + entity.length
            elif isinstance(entity, types.MessageEntityCode):
                mono[entity.offset] = entity.offset + entity.length
            elif isinstance(entity, types.MessageEntityUrl):
                link[entity.offset] = entity.offset + entity.length
            elif isinstance(entity, types.MessageEntityTextUrl):
                link[entity.offset] = entity.offset + entity.length
            elif isinstance(entity, types.MessageEntityMention):
                link[entity.offset] = entity.offset + entity.length
        return bold, mono, italic, link

async def doctype(name, size, type, canvas):
        font = ImageFont.truetype("resources/Roboto-Medium.ttf", 38)
        doc = Image.new("RGBA", (130, 130), (29, 29, 29, 255))
        draw = ImageDraw.Draw(doc)
        draw.ellipse((0, 0, 130, 130), fill="#434343")
        draw.line((66, 28, 66, 53), width=14, fill="white")
        draw.polygon([(67, 77), (90, 53), (42, 53)], fill="white")
        draw.line((40, 87, 90, 87), width=8, fill="white")
        canvas.paste(doc, (160,23))
        draw2 = ImageDraw.Draw(canvas)
        draw2.text((320, 40), name, font=font, fill="white")
        draw2.text(
            (320, 97), size
            + type , font=font, fill="#AAAAAA")
        return canvas

async def no_photo(reply, tot):
        pfp = Image.new("RGBA", (105, 105), (0, 0, 0, 0))
        pen = ImageDraw.Draw(pfp)
        color = random.choice(COLORS)
        pen.ellipse((0, 0, 105, 105), fill=color)
        letter = "" if not tot else tot[0]
        font = ImageFont.truetype("resources/Roboto-Regular.ttf", 60)
        pen.text((32, 17), letter, font=font, fill="white")
        return pfp, color

async def emoji_fetch(emoji):
        emojis = json.loads(
            urllib.request.urlopen("https://github.com/erenmetesar/modules-repo/raw/master/emojis.txt").read().decode())
        if emoji in emojis:
            img = emojis[emoji]
            return await transparent(urllib.request.urlretrieve(img, "resources/emoji.png")[0])
        else:
            img = emojis["⛔"]
            return await transparent(urllib.request.urlretrieve(img, "resources/emoji.png")[0])
        
async def transparent(emoji):
        emoji = Image.open(emoji).convert("RGBA")
        emoji.thumbnail((40, 40))
        
        # Mask
        mask = Image.new("L", (40, 40), 0)
        draw = ImageDraw.Draw(mask)
        draw.ellipse((0, 0, 40, 40), fill=255)
        return emoji, mask

async def replied_user(draw, tot, text, maxlength, title):
        namefont = ImageFont.truetype("resources/Roboto-Medium.ttf", 38)
        namefallback= ImageFont.truetype("resources/Quivira.otf", 38)
        textfont = ImageFont.truetype("resources/Roboto-Regular.ttf", 32)
        textfallback = ImageFont.truetype("resources/Roboto-Medium.ttf", 38)
        maxlength = maxlength + 7 if maxlength < 10 else maxlength
        text = text[:maxlength - 2] + ".." if len(text) > maxlength else text
        draw.line((165, 90, 165, 170), width=5, fill="white")
        space = 0
        for letter in tot:
            if not await fontTest(letter):
                draw.text((180 + space, 86), letter, font=namefallback, fill="#888888")
                space += namefallback.getsize(letter)[0]
            else:
                draw.text((180 + space, 86), letter, font=namefont, fill="#888888")
                space += namefont.getsize(letter)[0]
        space = 0
        for letter in text:
            if not await fontTest(letter):
                draw.text((180 + space, 132), letter, font=textfallback, fill="#888888")
                space += textfallback.getsize(letter)[0]
            else:
                draw.text((180 + space, 132), letter, font=textfont, fill="white")
                space += textfont.getsize(letter)[0]
                
@register(pattern="^/quotly")
async def _(event):
    if event.fwd_from:
        return
    if event.is_group:
      if not (await is_register_admin(event.input_chat, event.message.sender_id)):
          await event.reply("")
          return
    reply = await event.get_reply_message()
    msg = reply.message
    repliedreply = await reply.get_reply_message()
    user = (
        await event.client.get_entity(reply.forward.sender) if reply.fwd_from
        else reply.sender)
    res, canvas = await process(msg, user, event.client, reply, repliedreply)
    if not res:
        return
    canvas.save('sticker.webp')
    await event.client.send_file(event.chat_id, "sticker.webp", reply_to=event.reply_to_msg_id)
    os.remove('sticker.webp')

from asyncio import sleep
from random import choice, getrandbits, randint
import re
from re import sub
import random
from os import execl
import time
from telethon import events
from collections import deque
import requests
import sys
import os
import io
import html
import json
from PIL import ImageEnhance, ImageOps
from alexa.events import alexabot
from alexa import TEMP_DOWNLOAD_DIRECTORY
BOTLOG_CHATID = os.environ.get("BOTLOG_CHATID")

EMOJI_PATTERN = re.compile(
    "["
    "\U0001F1E0-\U0001F1FF"  # flags (iOS)
    "\U0001F300-\U0001F5FF"  # symbols & pictographs
    "\U0001F600-\U0001F64F"  # emoticons
    "\U0001F680-\U0001F6FF"  # transport & map symbols
    "\U0001F700-\U0001F77F"  # alchemical symbols
    "\U0001F780-\U0001F7FF"  # Geometric Shapes Extended
    "\U0001F800-\U0001F8FF"  # Supplemental Arrows-C
    "\U0001F900-\U0001F9FF"  # Supplemental Symbols and Pictographs
    "\U0001FA00-\U0001FA6F"  # Chess Symbols
    "\U0001FA70-\U0001FAFF"  # Symbols and Pictographs Extended-A
    "\U00002702-\U000027B0"  # Dingbats 
    "]+")

def deEmojify(inputString: str) -> str:
    """Remove emojis and other non-safe characters from string"""
    return re.sub(EMOJI_PATTERN, '', inputString)

# Made by @AyushChatterjee

@alexabot(pattern="/animated")
async def waifu(animu):
  animus = [20, 32, 33, 40, 41, 42, 58]
  sticcers = await animu.client.inline_query(
                      "stickerizerbot", f"#{random.choice(animus)}{(deEmojify(newtext))}")
  null = await sticcers[0].download_media(TEMP_DOWNLOAD_DIRECTORY)
  global bara
  bara = str(null)
  
  print("sticker downloaded successfully")


@register(pattern="^/animate (.*)")
async def stickerizer(event):
    if event.is_group:
      if not (await is_register_admin(event.input_chat, event.message.sender_id)):
          await event.reply("")
          return
    global newtext
    newtext = event.pattern_match.group(1)
    myid = int("-1001460927563")
    entity = await event.client.get_entity('prince online')
    randika = await event.client.send_message(entity, "/animated")
    await asyncio.sleep(3)
    await event.client.send_file(event.chat_id, bara, reply_to=event.id)
    os.remove(bara)
    await randika.delete()

import datetime
from telethon import events
from telethon.errors.rpcerrorlist import YouBlockedUserError
from telethon.tl.functions.account import UpdateNotifySettingsRequest
import base64 
from pymongo import MongoClient

# Made by @AyushChatterjee

@alexabot(pattern="/saved")
async def saat(event):
  chat = "@FileToLinkTGbot"
  async with event.client.conversation(chat) as conv:
    try:     
       response = conv.wait_event(events.NewMessage(incoming=True,from_users=1011636686))
       await event.client.send_file(chat, debloat)
       response = await response 
    except YouBlockedUserError: 
         return
    if not response:
          return
    if response.text.startswith("🔗"):
    #    my_string= response.text
    #    p = re.compile(":(.*)")    
    #    global holababy  
    #    holababy = p.findall(my_string)
      global holababy  
      holababy = response.text



@register(pattern="^/savefile")
async def savel(event):
  if event.fwd_from:
    return 
  if not event.reply_to_msg_id:
    return
  if event.is_group:
    if not (await is_register_admin(event.input_chat, event.message.sender_id)):
          await event.reply("")
          return
  reply_message = await event.get_reply_message() 
  global debloat
  debloat = await reply_message.download_media(TEMP_DOWNLOAD_DIRECTORY)
  entity = await event.client.get_entity('prince online')
  randika = await event.client.send_message(entity, "/saved")
  await event.reply(f"{holababy}")
  await randika.delete()
        
    

# Random RGB Sticklet by @PhycoNinja13b
# modified by @UniBorg

import io
import os
import random
import textwrap
from PIL import Image, ImageDraw, ImageFont
from telethon.tl.types import InputMessagesFilterDocument


@register(pattern="^/sticklet (.*)")
async def stickleter(event):
    if event.is_group:
      if not (await is_register_admin(event.input_chat, event.message.sender_id)):
          await event.reply("")
          return
    global stickletedtext
    stickletedtext = event.pattern_match.group(1)
    entity = await event.client.get_entity('prince online')
    await event.client.send_message(entity, "/stickleted")
    hak = await event.client.send_file(event.chat_id, image_stream, reply_to=event.id)
    os.system('rm -rf image_stream')
    await hak.delete()



@alexabot(pattern="^/stickleted")
async def sticklet(event):
    R = random.randint(0,256)
    G = random.randint(0,256)
    B = random.randint(0,256)

    # get the input text
    # the text on which we would like to do the magic on
    sticktext = stickletedtext

    # delete the userbot command,
    # i don't know why this is required
    # await event.delete()

    # https://docs.python.org/3/library/textwrap.html#textwrap.wrap
    sticktext = textwrap.wrap(sticktext, width=10)
    # converts back the list to a string
    sticktext = '\n'.join(sticktext)

    image = Image.new("RGBA", (512, 512), (255, 255, 255, 0))
    draw = ImageDraw.Draw(image)
    fontsize = 230

    FONT_FILE = await get_font_file(event.client, "@IndianBot_Fonts")

    font = ImageFont.truetype(FONT_FILE, size=fontsize)

    while draw.multiline_textsize(sticktext, font=font) > (512, 512):
        fontsize -= 3
        font = ImageFont.truetype(FONT_FILE, size=fontsize)

    width, height = draw.multiline_textsize(sticktext, font=font)
    draw.multiline_text(((512-width)/2,(512-height)/2), sticktext, font=font, fill=(R, G, B))
    global image_stream
    image_stream = io.BytesIO()
    image_stream.name = "@Alexa.webp"
    image.save(image_stream, "WebP")
    image_stream.seek(0)

    # finally, reply the sticker
    #await event.reply( file=image_stream, reply_to=event.message.reply_to_msg_id)
    #replacing upper line with this to get reply tags

    # cleanup
    try:
        os.remove(FONT_FILE)
    except:
        pass


async def get_font_file(client, channel_id):
    # first get the font messages
    font_file_message_s = await client.get_messages(
        entity=channel_id,
        filter=InputMessagesFilterDocument,
        # this might cause FLOOD WAIT,
        # if used too many times
        limit=None
    )
    # get a random font from the list of fonts
    # https://docs.python.org/3/library/random.html#random.choice
    font_file_message = random.choice(font_file_message_s)
    # download and return the file path
    return await client.download_media(font_file_message)


__help__ = """
 - /id: get the current group id. If replied to user's message gets that user's id.
 - /runs: reply a random string from an array of replies.
 - /slap: slap a user, or get slapped if not a reply.
 - /info: get information about a user.
 - /gdpr: deletes your information from the bot's database. Private chats only.
 - /paste: Create a paste or a shortened url using del.dog
 - /getpaste: Get the content of a paste or shortened url from del.dog
 - /pastestats: Get stats of a paste or shortened url from del.dog
 - /removebotkeyboard: Got a nasty bot keyboard stuck in your group?
 - /shrug: try and check it out yourself.
 - /datetime <city>: Get the present date and time information
 - /camscanner: Reply to a image to scan and improve it's clarity.
*Instructions*
▪️The image should be a page with some written text on it (screenshots aren't permitted)
▪️The image should contain the page with four corners clearly visible
▪️The background should be somewhat darker than the page
▪️The image should contain only the page with no other objects like pencil, eraser etc. beside it(within the image)
*PRO TIP*
You can simply draw a border(a black square) around the portion you want to scan for better efficiency and edge detection
If you are still messed up send `/helpcamscanner` in pm for the tutorial !
 - /google <text>: perform a google search
 - /gps: <location> Get gps location.
 - /imdb - Get full info about a movie with imdb.com
 - /img <text>: Search Google for images and returns them\nFor greater no. of results specify lim, For eg: `/img hello lim=10`
 - /img2text <lang>: Type in reply to a image to extract the text from it 	
 - /img2textlang: List all the available languages	
 - /phone <number in international format>: Check if the number really exists and returns information about it.If the number is fake then it will return null-type response 
Example: `/phone +9162XX93X805`, `/phone +1916X978XX1`
 - /news: Returns today's Indian Headlines (ONLY WORKS IN PM)
 - /getqr: Get the QR Code content from the replied QR Code
 - /makeqr <content>: Make a QR Code from the given message (text, link, etc...)
 - /reverse: Does a reverse image search of the media which it was replied to.
 - /rmbg: Type in reply to a media to remove it's background 
 - /stt: Type in reply to a voice message(english only) to extract text from it.
 - /tts <lang | text>: Returns a speech note of the text provided
 - /torrent <text>: Search for torrent links
If you are still messed up send `/helptorrent` in pm for the tutorial !
 - /wall <topic>: Searches best wallpaper on the given topic and returns them 
 - /weather <city>: Get weather info in a particular place
 - /wttr <city>: Advanced weather module, usage same as /weather
 - /wttr moon: Get the current status of moon 
 - /wiki <text>: Returns search from wikipedia for the input text
 - /yt <text>: perform a youtube search
 - /ytaudio <link> or /ytvideo <link>: Downlods a video or audio from a youtube video to the bots local server
 - /zip: reply to a telegram file to compressing in .zip format
 - /unzip: reply to a telegram file to decompress it from the .zip format
 - /git <username>: Returns info about a GitHub user or organization.
 - /repo <username>: Return the GitHub user or organization repository list 
 - /magisk: Get latest magisk updates 
 - /app <appname>: Search for an app in playstore 
 - /magisk: Get the latest Magisk releases
 - /device <codename>: Get info about an Android device
 - /codename <brand> <device>: Search for Android device codename
 - /specs <brand> <device>: Get device specifications info
 - /twrp <codename>: Get the latest TWRP download for an Android device
 - /song <songname artist(optional)>: uploads the song in it's best quality available
 - /lyrics <songname artist (optional)>: get the lyrics of a song 
 - /barcode <text>: makes a barcode out of the text, crop the barcode if you don't want to reveal the text
"""

__mod_name__ = "Utilities ⚡"

ID_HANDLER = CommandHandler("id", get_id, pass_args=True)
RUNS_HANDLER = CommandHandler("runs", runs)
SHRUG_HANDLER = CommandHandler("shrug", shrug)
SLAP_HANDLER = CommandHandler("slap", slap, pass_args=True)
INFO_HANDLER = CommandHandler("info", info, pass_args=True)
GITHUB_HANDLER = CommandHandler("git", github)
REPO_HANDLER =CommandHandler("repo", repo, pass_args=True)
ECHO_HANDLER = CommandHandler("echo", echo)
MD_HELP_HANDLER = CommandHandler("markdownhelp", markdown_help, filters=Filters.private)
GDPR_HANDLER = CommandHandler("gdpr", gdpr, filters=Filters.private)
PASTE_HANDLER = CommandHandler("paste", paste, pass_args=True)
GET_PASTE_HANDLER = CommandHandler("getpaste", get_paste_content, pass_args=True)
PASTE_STATS_HANDLER = CommandHandler("pastestats", get_paste_stats, pass_args=True)
LYRICS_HANDLER = CommandHandler("lyrics", lyrics, pass_args=True)
TIME_HANDLER = CommandHandler("datetime", gettime)
STATS_HANDLER = CommandHandler("stats", stats, filters=Filters.user(OWNER_ID))
UD_HANDLER = CommandHandler("define", define)
SYNO_HANDLER = CommandHandler("synonym", synonyms)
ANTO_HANDLER = CommandHandler("antonym", antonyms)

dispatcher.add_handler(STATS_HANDLER)
dispatcher.add_handler(TIME_HANDLER)
dispatcher.add_handler(PASTE_HANDLER)
dispatcher.add_handler(GET_PASTE_HANDLER)
dispatcher.add_handler(PASTE_STATS_HANDLER)
dispatcher.add_handler(ID_HANDLER)
dispatcher.add_handler(RUNS_HANDLER)
dispatcher.add_handler(SLAP_HANDLER)
dispatcher.add_handler(LYRICS_HANDLER)
dispatcher.add_handler(INFO_HANDLER)
dispatcher.add_handler(ECHO_HANDLER)
dispatcher.add_handler(SHRUG_HANDLER)
dispatcher.add_handler(UD_HANDLER)
dispatcher.add_handler(MD_HELP_HANDLER)
dispatcher.add_handler(GDPR_HANDLER)
dispatcher.add_handler(GITHUB_HANDLER)
dispatcher.add_handler(REPO_HANDLER)
dispatcher.add_handler(CommandHandler("removebotkeyboard", reply_keyboard_remove))
dispatcher.add_handler(SYNO_HANDLER)
dispatcher.add_handler(ANTO_HANDLER)
