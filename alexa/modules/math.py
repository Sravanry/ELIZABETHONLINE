from typing import List
import requests
from telegram import Message, Update, Bot, MessageEntity
from telegram.ext import CommandHandler, run_async
from alexa import dispatcher
from alexa.modules.disable import DisableAbleCommandHandler
import pynewtonmath as newton
import math
from alexa.modules.helper_funcs.chat_status import user_admin

def join(args):
    x = ''.join(map(str, args))
    return x

@run_async
@user_admin
def simplify(bot: Bot, update: Update, args: List[str]):
    message = update.effective_message
    message.reply_text(newton.simplify('{}'.format(join(args))))

@run_async
@user_admin
def factor(bot: Bot, update: Update, args: List[str]):
    message = update.effective_message
    message.reply_text(newton.factor('{}'.format(join(args))))

@run_async
@user_admin
def derive(bot: Bot, update: Update, args: List[str]):
    message = update.effective_message
    message.reply_text(newton.derive('{}'.format(join(args))))

@run_async
@user_admin
def integrate(bot: Bot, update: Update, args: List[str]):
    message = update.effective_message
    message.reply_text(newton.integrate('{}'.format(join(args))))

@run_async
@user_admin
def zeroes(bot: Bot, update: Update, args: List[str]):
    message = update.effective_message
    message.reply_text(newton.zeroes('{}'.format(join(args))))

@run_async
@user_admin
def tangent(bot: Bot, update: Update, args: List[str]):
    message = update.effective_message
    message.reply_text(newton.tangent('{}'.format(join(args))))

@run_async
@user_admin
def area(bot: Bot, update: Update, args: List[str]):
    message = update.effective_message
    message.reply_text(newton.area('{}'.format(join(args))))

@run_async
@user_admin
def cos(bot: Bot, update: Update, args):
    message = update.effective_message
    message.reply_text(math.cos(int(args[0])))

@run_async
@user_admin
def sin(bot: Bot, update: Update, args):
    message = update.effective_message
    message.reply_text(math.sin(int(args[0])))

@run_async
@user_admin
def tan(bot: Bot, update: Update, args):
    message = update.effective_message
    message.reply_text(math.tan(int(args[0])))

@run_async
@user_admin
def arccos(bot: Bot, update: Update, args):
    message = update.effective_message
    message.reply_text(math.acos(int(args[0])))

@run_async
@user_admin
def arcsin(bot: Bot, update: Update, args):
    message = update.effective_message
    message.reply_text(math.asin(int(args[0])))

@run_async
@user_admin
def arctan(bot: Bot, update: Update, args):
    message = update.effective_message
    message.reply_text(math.atan(int(args[0])))

@run_async
@user_admin
def abs(bot: Bot, update: Update, args):
    message = update.effective_message
    message.reply_text(math.fabs(int(args[0])))

@run_async
@user_admin
def log(bot: Bot, update: Update, args):
    message = update.effective_message
    message.reply_text(math.log(int(args[0])))

__help__ = """
Solves complex math problems using https://newton.now.sh
 - /simplify: Simplify `/simplify 2^2+2(2)`
 - /factor: Factor `/factor x^2 + 2x`
 - /derive: Derive `/derive x^2+2x`
 - /integrate: Integrate `/integrate x^2+2x`
 - /zeroes: Find 0's `/zeroes x^2+2x`
 - /tangent: Find Tangent `/tangent 2lx^3`
 - /area: Area Under Curve `/area 2:4lx^3`
 - /cos: Cosine `/cos pi`
 - /sin: Sine `/sin 0`
 - /tan: Tangent `/tan 0`
 - /arccos: Inverse Cosine `/arccos 1`
 - /arcsin: Inverse Sine `/arcsin 0`
 - /arctan: Inverse Tangent `/arctan 0`
 - /abs: Absolute Value `/abs -1`
 - /log: Logarithm `/log 2l8`
__Keep in mind__: To find the tangent line of a function at a certain x value, send the request as c|f(x) where c is the given x value and f(x) is the function expression, the separator is a vertical bar '|'. See the table above for an example request.
To find the area under a function, send the request as c:d|f(x) where c is the starting x value, d is the ending x value, and f(x) is the function under which you want the curve between the two x values.
To compute fractions, enter expressions as numerator(over)denominator. For example, to process 2/4 you must send in your expression as 2(over)4. The result expression will be in standard math notation (1/2, 3/4).
"""

__mod_name__ = "Math ➗"

SIMPLIFY_HANDLER = CommandHandler("simplify", simplify, pass_args=True)
FACTOR_HANDLER = CommandHandler("factor", factor, pass_args=True)
DERIVE_HANDLER = CommandHandler("derive", derive, pass_args=True)
INTEGRATE_HANDLER = CommandHandler("integrate", integrate, pass_args=True)
ZEROES_HANDLER = CommandHandler("zeroes", zeroes, pass_args=True)
TANGENT_HANDLER = CommandHandler("tangent", tangent, pass_args=True)
AREA_HANDLER = CommandHandler("area", area, pass_args=True)
COS_HANDLER = CommandHandler("cos", cos, pass_args=True)
SIN_HANDLER = CommandHandler("sin", sin, pass_args=True)
TAN_HANDLER = CommandHandler("tan", tan, pass_args=True)
ARCCOS_HANDLER = CommandHandler("arccos", arccos, pass_args=True)
ARCSIN_HANDLER = CommandHandler("arcsin", arcsin, pass_args=True)
ARCTAN_HANDLER = CommandHandler("arctan", arctan, pass_args=True)
ABS_HANDLER = CommandHandler("abs", abs, pass_args=True)
LOG_HANDLER = CommandHandler("log", log, pass_args=True)

dispatcher.add_handler(SIMPLIFY_HANDLER)
dispatcher.add_handler(FACTOR_HANDLER)
dispatcher.add_handler(DERIVE_HANDLER)
dispatcher.add_handler(INTEGRATE_HANDLER)
dispatcher.add_handler(ZEROES_HANDLER)
dispatcher.add_handler(TANGENT_HANDLER) 
dispatcher.add_handler(AREA_HANDLER)
dispatcher.add_handler(COS_HANDLER)
dispatcher.add_handler(SIN_HANDLER)
dispatcher.add_handler(TAN_HANDLER)
dispatcher.add_handler(ARCCOS_HANDLER)
dispatcher.add_handler(ARCSIN_HANDLER)
dispatcher.add_handler(ARCTAN_HANDLER)
dispatcher.add_handler(ABS_HANDLER)
dispatcher.add_handler(LOG_HANDLER)
