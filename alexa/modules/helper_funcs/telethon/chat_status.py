from alexa import tbot, SUDO_USERS, WHITELIST_USERS
from telethon.tl.types import ChannelParticipantsAdmins


async def user_is_ban_protectedd(user_id: int, message):
    status = False
    if message.is_private or user_id in (WHITELIST_USERS + SUDO_USERS):
        return True

    async for user in tbot.iter_participants(message.chat_id,
                                             filter=ChannelParticipantsAdmins):
        if user_id == user.id:
            status = True
            break
    return status


async def user_is_adminn(user_id: int, message):
    status = False
    if message.is_private:
        return True

    async for user in tbot.iter_participants(message.chat_id,
                                             filter=ChannelParticipantsAdmins):
        if user_id == user.id or user_id in SUDO_USERS:
            status = True
            break
    return status


async def is_user_adminn(user_id: int, chat_id):
    status = False
    async for user in tbot.iter_participants(chat_id,
                                             filter=ChannelParticipantsAdmins):
        if user_id == user.id or user_id in SUDO_USERS:
            status = True
            break
    return status


async def alexa_is_adminn(chat_id: int):
    status = False
    alexa = await tbot.get_me()
    async for user in tbot.iter_participants(chat_id,
                                             filter=ChannelParticipantsAdmins):
        if alexa.id == user.id:
            status = True
            break
    return status


async def is_user_in_chatt(chat_id: int, user_id: int):
    status = False
    async for user in tbot.iter_participants(chat_id):
        if user_id == user.id:
            status = True
            break
    return status


async def can_delete_messagess(message):
    status = False
    if message.chat.admin_rights:
        status = message.chat.admin_rights.delete_messages
    return status


async def can_change_infoo(message):
    status = False
    if message.chat.admin_rights:
        status = message.chat.admin_rights.change_info
    return status


async def can_ban_userss(message):
    status = False
    if message.chat.admin_rights:
        status = message.chat.admin_rights.ban_users
    return status


async def can_invite_userss(message):
    status = False
    if message.chat.admin_rights:
        status = message.chat.admin_rights.invite_users
    return status


async def can_add_adminss(message):
    status = False
    if message.chat.admin_rights:
        status = message.chat.admin_rights.add_admins
    return status


async def can_pin_messagess(message):
    status = False
    if message.chat.admin_rights:
        status = message.chat.admin_rights.pin_messages
    return status
