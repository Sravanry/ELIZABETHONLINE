import random, re, string, io, asyncio
from PIL import Image
from io import BytesIO
import base64
from spongemock import spongemock
from zalgo_text import zalgo
import os
from pathlib import Path
import glob

import nltk # shitty lib, but it does work
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')

from typing import Optional, List
from telegram import Message, Update, Bot, User
from telegram import MessageEntity
from telegram.ext import Filters, MessageHandler, run_async, CommandHandler
from deeppyer import deepfry

from alexa import dispatcher, DEEPFRY_TOKEN, LOGGER
from alexa.modules.disable import DisableAbleCommandHandler, DisableAbleRegexHandler
from alexa.modules.helper_funcs.chat_status import user_admin

WIDE_MAP = dict((i, i + 0xFEE0) for i in range(0x21, 0x7F))
WIDE_MAP[0x20] = 0x3000

# D A N K modules by @deletescape vvv


@run_async
@user_admin
def owo(bot: Bot, update: Update):
    message = update.effective_message
    if not message.reply_to_message:
        message.reply_text("I need a message to meme.")
    else:
        faces = ['(・`ω´・)',';;w;;','owo','UwU','>w<','^w^','\(^o\) (/o^)/','( ^ _ ^)∠☆','(ô_ô)','~:o',';____;', '(*^*)', '(>_', '(♥_♥)', '*(^O^)*', '((+_+))']
        reply_text = re.sub(r'[rl]', "w", message.reply_to_message.text)
        reply_text = re.sub(r'[ｒｌ]', "ｗ", message.reply_to_message.text)
        reply_text = re.sub(r'[RL]', 'W', reply_text)
        reply_text = re.sub(r'[ＲＬ]', 'Ｗ', reply_text)
        reply_text = re.sub(r'n([aeiouａｅｉｏｕ])', r'ny\1', reply_text)
        reply_text = re.sub(r'ｎ([ａｅｉｏｕ])', r'ｎｙ\1', reply_text)
        reply_text = re.sub(r'N([aeiouAEIOU])', r'Ny\1', reply_text)
        reply_text = re.sub(r'Ｎ([ａｅｉｏｕＡＥＩＯＵ])', r'Ｎｙ\1', reply_text)
        reply_text = re.sub(r'\!+', ' ' + random.choice(faces), reply_text)
        reply_text = re.sub(r'！+', ' ' + random.choice(faces), reply_text)
        reply_text = reply_text.replace("ove", "uv")
        reply_text = reply_text.replace("ｏｖｅ", "ｕｖ")
        reply_text += ' ' + random.choice(faces)
        message.reply_to_message.reply_text(reply_text)

@run_async
@user_admin
def copypasta(bot: Bot, update: Update):
    message = update.effective_message
    if not message.reply_to_message:
        message.reply_text("I need a message to meme.")
    else:
        emojis = ["😂", "😂", "👌", "✌", "💞", "👍", "👌", "💯", "🎶", "👀", "😂", "👓", "👏", "👐", "🍕", "💥", "🍴", "💦", "💦", "🍑", "🍆", "😩", "😏", "👉👌", "👀", "👅", "😩", "🚰"]
        reply_text = random.choice(emojis)
        b_char = random.choice(message.reply_to_message.text).lower() # choose a random character in the message to be substituted with 🅱️
        for c in message.reply_to_message.text:
            if c == " ":
                reply_text += random.choice(emojis)
            elif c in emojis:
                reply_text += c
                reply_text += random.choice(emojis)
            elif c.lower() == b_char:
                reply_text += "🅱️"
            else:
                if bool(random.getrandbits(1)):
                    reply_text += c.upper()
                else:
                    reply_text += c.lower()
        reply_text += random.choice(emojis)
        message.reply_to_message.reply_text(reply_text)


@run_async
@user_admin
def bmoji(bot: Bot, update: Update):
    message = update.effective_message
    if not message.reply_to_message:
        message.reply_text("I need a message to meme.")
    else:
        b_char = random.choice(message.reply_to_message.text).lower() # choose a random character in the message to be substituted with 🅱️
        reply_text = message.reply_to_message.text.replace(b_char, "🅱️").replace(b_char.upper(), "🅱️")
        message.reply_to_message.reply_text(reply_text)


@run_async
@user_admin
def clapmoji(bot: Bot, update: Update):
    message = update.effective_message
    if not message.reply_to_message:
        message.reply_text("I need a message to meme.")
    else:
        reply_text = "👏 "
        reply_text += message.reply_to_message.text.replace(" ", " 👏 ")
        reply_text += " 👏"
        message.reply_to_message.reply_text(reply_text)



@run_async
@user_admin
def stretch(bot: Bot, update: Update):
    message = update.effective_message
    if not message.reply_to_message:
        message.reply_text("I need a message to meme.")
    else:
        count = random.randint(3, 10)
        reply_text = re.sub(r'([aeiouAEIOUａｅｉｏｕＡＥＩＯＵ])', (r'\1' * count), message.reply_to_message.text)
        message.reply_to_message.reply_text(reply_text)


@run_async
@user_admin
def vapor(bot: Bot, update: Update, args: List[str]):
    message = update.effective_message
    if not message.reply_to_message:
        if not args:
            message.reply_text("I need a message to convert to vaporwave text.")
        else:
            noreply = True
            data = message.text.split(None, 1)[1]
    elif message.reply_to_message:
        noreply = False
        data = message.reply_to_message.text
    else:
        data = ''

    reply_text = str(data).translate(WIDE_MAP)
    if noreply:
        message.reply_text(reply_text)
    else:
        message.reply_to_message.reply_text(reply_text)

# D A N K modules by @deletescape ^^^
# Less D A N K modules by @skittles9823 # holi fugg I did some maymays vvv


@run_async
@user_admin
def zalgotext(bot: Bot, update: Update):
    message = update.effective_message
    if message.reply_to_message:
        data = message.reply_to_message.text
    else:
        data = str('Insolant human, you must reply to something to zalgofy it!')

    reply_text = zalgo.zalgo().zalgofy(data)
    message.reply_text(reply_text)

# Less D A N K modules by @skittles9823 # holi fugg I did some maymays ^^^
# shitty maymay modules made by @divadsn vvv

@run_async
@user_admin
def forbesify(bot: Bot, update: Update):
    message = update.effective_message
    if message.reply_to_message:
        data = message.reply_to_message.text
    else:
        data = ''

    data = data.lower()
    accidentals = ['VB', 'VBD', 'VBG', 'VBN']
    reply_text = data.split()
    offset = 0

    # use NLTK to find out where verbs are
    tagged = dict(nltk.pos_tag(reply_text))

    # let's go through every word and check if it's a verb
    # if yes, insert ACCIDENTALLY and increase offset
    for k in range(len(reply_text)):
        i = reply_text[k + offset]
        if tagged.get(i) in accidentals:
            reply_text.insert(k + offset, 'accidentally')
            offset += 1

    reply_text = string.capwords(' '.join(reply_text))
    message.reply_to_message.reply_text(reply_text)


@run_async
@user_admin
def deepfryer(bot: Bot, update: Update):
    message = update.effective_message
    if message.reply_to_message:
        data = message.reply_to_message.photo
        data2 = message.reply_to_message.sticker
    else:
        data = []
        data2 = []

    # check if message does contain media and cancel when not
    if not data and not data2:
        message.reply_text("What am I supposed to do with this?!")
        return

    # download last photo (highres) as byte array
    if data:
        photodata = data[len(data) - 1].get_file().download_as_bytearray()
        image = Image.open(io.BytesIO(photodata))
    elif data2:
        sticker = bot.get_file(data2.file_id)
        sticker.download('sticker.png')
        image = Image.open("sticker.png")

    # the following needs to be executed async (because dumb lib)
    loop = asyncio.new_event_loop()
    loop.run_until_complete(process_deepfry(image, message.reply_to_message, bot))
    loop.close()

async def process_deepfry(image: Image, reply: Message, bot: Bot):
    # DEEPFRY IT
    image = await deepfry(
        img=image,
        token=DEEPFRY_TOKEN,
        url_base='westeurope'
    )

    bio = BytesIO()
    bio.name = 'image.jpeg'
    image.save(bio, 'JPEG')

    # send it back
    bio.seek(0)
    reply.reply_photo(bio)
    if Path("sticker.png").is_file():
        os.remove("sticker.png")

# shitty maymay modules made by @divadsn ^^^


@run_async
@user_admin
def shout(bot: Bot, update: Update, args):
    if len(args) == 0:
        update.effective_message.reply_text("Where is text?")
        return

    msg = "```"
    text = " ".join(args)
    result = []
    result.append(' '.join([s for s in text]))
    for pos, symbol in enumerate(text[1:]):
        result.append(symbol + ' ' + '  ' * pos + symbol)
    result = list("\n".join(result))
    result[0] = text[0]
    result = "".join(result)
    msg = "```\n" + result + "```"
    return update.effective_message.reply_text(msg, parse_mode="MARKDOWN")


# no help string
__help__ = """
Some memes command, find it all out yourself!

 - /owo: OWO de text
 - /stretch: STRETCH de text
 - /clapmoji: Type in reply to a message and see magic
 - /bmoji: Type in reply to a message and see magic
 - /copypasta: Type in reply to a message and see magic
 - /vapor: owo vapor dis
 - /shout: Write anything that u want it to should
 - /zalgofy: reply to a message to g̫̞l̼̦i̎͡tͫ͢c̘ͭh̛̗ it out!
 - /table : get flip/unflip :v.
 - /decide : Randomly answers yes/no/maybe
 - /toss : Tosses A coin
 - /abuse : Abuses the cunt
 - /insult : Insult the cunt
 - /slap : Slaps the cunt
 - /roll : Roll a dice.
 - /rlg : Join ears,nose,mouth and create an emo ;-;
 - /react : Check on your own
 - /happy : Check on your own
 - /amgery : Check on your own
 - /cowsay | /tuxsay | /milksay | /kisssay | /wwwsay | /defaultsay | /bunnysay | /moosesay | /sheepsay | /rensay | /cheesesay | /ghostbusterssay | /skeletonsay <text>: Returns a stylish art text from the given text	
 - /deepfry: Type this in reply to an image/sticker to roast the image/sticker	
 - /figlet: Another Style art	
 - /dice: Roll A dice	
 - /dart: Throw a dart and try your luck
 - /basketball: Try your luck if you can enter the ball in the ring
 - /type <text>: Make the bot type something for you in a professional way
 - /carbon <text>: Beautifies your text and enwraps inside a terminal image [ENGLISH ONLY]
 - /stickerid: Gives the ID of the sticker you've replied to
 - /getsticker: Uploads the .png of the sticker you've replied to
 - /kang <emoji for sticker>: Reply to a sticker to add it to your pack or makes a new one if it doesn't exist
 - /sticklet <text>: Turn a text into a sticker, you'll get a random colour from a rainbow(out of 7 colours)
 - /fortune: gets a random fortune quote
 - /quotly: An alternative to @QuotlyBot, type /quotly in reply to a message
"""

__mod_name__ = "Memes 💢"

COPYPASTA_HANDLER = CommandHandler("copypasta", copypasta)
CLAPMOJI_HANDLER = CommandHandler("clapmoji", clapmoji)
BMOJI_HANDLER = CommandHandler("bmoji", bmoji)
OWO_HANDLER = CommandHandler("owo", owo)
STRETCH_HANDLER = CommandHandler("stretch", stretch)
VAPOR_HANDLER = CommandHandler("vapor", vapor, pass_args=True)
ZALGO_HANDLER = CommandHandler("zalgofy", zalgotext)
FORBES_HANDLER = CommandHandler("forbes", forbesify)
DEEPFRY_HANDLER = CommandHandler("deepfry", deepfryer)
SHOUT_HANDLER = CommandHandler("shout", shout, pass_args=True)
#FORBES_HANDLER = CommandHandler("forbesify", forbesify)

dispatcher.add_handler(COPYPASTA_HANDLER)
dispatcher.add_handler(CLAPMOJI_HANDLER)
dispatcher.add_handler(BMOJI_HANDLER)
dispatcher.add_handler(SHOUT_HANDLER)
dispatcher.add_handler(OWO_HANDLER)
#dispatcher.add_handler(FORBES_HANDLER)
dispatcher.add_handler(STRETCH_HANDLER)
dispatcher.add_handler(VAPOR_HANDLER)
dispatcher.add_handler(ZALGO_HANDLER)
dispatcher.add_handler(FORBES_HANDLER)
dispatcher.add_handler(DEEPFRY_HANDLER)
