__help__ = """
 - /adminlist | /admins: list of admins in the chat
 - /users: list all the users in the chat
 - /pin | /unpin: pins/unpins the message in the chat
 - /invitelink: gets invitelink
 - /promote: promotes a user 
 - /demote: demotes a user
 - /zombies: count the number of deleted account in your group
 - /kickthefools: kicks all members inactive from 1 week
 - /report <reason> | @admin: reply to a message to report it to admins(non-admin only)
 - /reports <on/off>: change report setting
 - /ban: bans a user 
 - /tban <d/h/m> : temporarily bans a user from your chat
 - /unban: unbans a user 
 - /sban: silently bans a user
 - /mute: mute a user 
 - /tmute <d/h/m>: temporarily mute a user
 - /unmute: unmutes a user
 - /kick: kicks a user 
 - /connect | /connect <chatid> in PM: connects a chat to PM 
 - /connection: list connected chats 
 - /disconnect: disconnect from a chat
 - /helpconnect: list available commands that can be done remotely 
 - /setflood <number/off>: set the number of messages to take action on a user for flooding
 - /setfloodmode <mute/ban/kick/tban/tmute>: select the valid action eg. /setfloodmode tmute 5m.
 - /flood: gets the current antiflood settings
 - /addblacklist <trigger> : blacklists the trigger it will get removed everytime someone types it
 - /unblacklist <trigger> | /rmblacklist <trigger> : stop blacklisting a certain blacklist trigger
 - /blacklist: list all active blacklist filters
 - /addblacklist "the admins suck": This will remove the text everytime someone types it
 - /addblacklist "bit.ly/*": This will remove the link everytime someone sends it matching bit.ly
 - /filter <word> <message>: Every time someone says "word", the bot will reply with "message"
 - /stop <word>: stop that filter.
 - /filters: list all active filters in this chat.
 - /lock <item(s)>: lock the usage of "item" for non-admins
 - /unlock <item(s)>: unlock "item". Everyone can use them again
 - /locks: list the lock status in the chat
 - /locktypes: gets a list of all things that can be locked
 - /setlog: set a log channel.
 - /unsetlog: unset the log channel.
 - /logchannel: get the log channel info
 - /purge: deletes all messages from the message you replied to
 - /purge X: deletes X messages after the message you replied to 
 - /del: deletes the message you replied to.
 - /save <word> <sentence>: Save that sentence to the note called "word"
 - /get <word> | #<word> : get the note registered to that word
 - /clear <word>: delete the note called "word"
 - /notes | /saved: List all notes in the chat
 - /setrules <rules>: set the rules for this chat
 - /clearrules: clear the rules for this chat
 - /rules: get the rules for this chat
 - /addurl <url>: Add a domain to the blacklist, the bot will automatically parse the url
 - /delurl <url>: Remove url from the blacklist
 - /warn <userhandle>: warn a user
 - /resetwarn @username: reset the warnings for a user
 - /addwarn <word> <message>: set a warning filter on a certain word
 - /nowarn <word>: stop a warning filter
 - /warnlimit <num>: set the max warning limit
 - /warns <userhandle>: get a user's number, and reason, of warnings
 - /warnlist: list of all current warning filters
"""
__mod_name__ = "Admin👩‍✈️"
