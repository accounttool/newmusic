#
# Copyright (C) 2021-2022 by TeamYukki@Github, < https://github.com/TeamYukki >.
#
# This file is part of < https://github.com/TeamYukki/YukkiMusicBot > project,
# and is released under the "GNU v3.0 License Agreement".
# Please see < https://github.com/TeamYukki/YukkiMusicBot/blob/master/LICENSE >
#
# All rights reserved.

HELP_1 = """â**<u>ð«ðªð¼ð²ð¬ ð¬ð¸ð¶ð¶ðªð·ð­ð¼:</u>**

**c** stands for channel play.

/pause or /cpause - ð³ð¸ð²ð· @ðªð¬ð¬ð¸ð¾ð·ð½ð½ð¸ð¸ðµPause the playing music. 
/resume or /cresume- Resume the paused music.
/mute or /cmute- Mute the playing music.
/unmute or /cunmute- Unmute the muted music.
/skip or /cskip- Skip the current playing music.
/stop or /cstop- Stop the playing music.
/shuffle or /cshuffle- Randomly shuffles the queued playlist.
/seek or /cseek - Forward Seek the music to your duration
/seekback or /cseekback - Backward Seek the music to your duration
/restart - Restart bot for your chat .


â<u>**ð¼ð¹ð®ð¬ð²ð¯ð´ ð¼ð´ð²ð¹:**</u>
/skip or /cskip [Number(example: 3)] 
    - Skips music to a the specified queued number. Example: /skip 3 will skip music to third queued music and will ignore 1 and 2 music in queue.

â<u>**ðµð¸ð¸ð¹ ð¹ðµðªð:**</u>
/loop or /cloop [enable/disable] or [Numbers between 1-10] 
    - When activated, bot loops the current playing music to 1-10 times on voice chat. Default to 10 times.

â<u>**ðªð¾ð½ð± ð¾ð¼ð®ð»ð¼:**</u>
Auth Users can use admin commands without admin rights in your chat.

/auth [Username] - Add a user to AUTH LIST of the group.
/unauth [Username] - Remove a user from AUTH LIST of the group.
/authusers - Check AUTH LIST of the group."""


HELP_2 = """â<u>**ð¹ðµðªð ð¬ð¸ð¶ð¶ðªð·ð­ð¼:**</u>

Available Commands = play , vplay , cplay ð³ð¸ð²ð· @ðªð¬ð¬ð¸ð¾ð·ð½ð½ð¸ð¸ðµ

ForcePlay Commands = playforce , vplayforce , cplayforce

**c** stands for channel play.
**v** stands for video play.
**force** stands for force play.

/play or /vplay or /cplay  - Bot will start playing your given query on voice chat or Stream live links on voice chats.

/playforce or /vplayforce or /cplayforce -  **Force Play** stops the current playing track on voice chat and starts playing the searched track instantly without disturbing/clearing queue.

/channelplay [Chat username or id] or [Disable] - Connect channel to a group and stream music on channel's voice chat from your group.


â**<u>ð«ð¸ð½ ð¼ð®ð»ð¿ð®ð» ð¹ðµð¼ððµð²ð¼ð½:</u>**
/playlist  - Check Your Saved Playlist On Servers.
/deleteplaylist - Delete any saved music in your playlist
/play  - Start playing Your Saved Playlist from Servers."""


HELP_3 = """â<u>**ð¶ð ð¬ð¸ð¶ð¶ðªð·ð­ð¼:**</u>

/stats - Get Top 10 Tracks Global Stats, Top 10 Users of bot, Top 10 Chats on bot, Top 10 Played in a chat etc etc.

/sudolist - Check Sudo Users of Yukki Music Bot

/lyrics [Music Name] - Searches Lyrics for the particular Music on web.

/song [Track Name] or [YT Link] - Download any track from youtube in mp3 or mp4 formats.

/player -  Get a interactive Playing Panel.

**c** stands for channel play.

/queue or /cqueue- Check Queue List of Music."""

HELP_4 = """â<u>**ðªð·ð¸ð½ð±ð®ð» ð¬ð¸ð¶ð¶ðªð·ð­ð¼:**</u>
/start - Start the Music Bot. ð«ð¸ð½ ð«ð @nati_sam223
/help  - Get Commands Helper Menu with detailed explanations of commands.
/ping- Ping the Bot and check Ram, Cpu etc stats of Bot.

â<u>**Group Settings:**</u>
/settings - Get a complete group's settings with inline buttons

ð **ð¸ð¹ð½ð²ð¸ð·ðªðµ ð¼ð®ð½ð½ð²ð·ð°:**

1ï¸â£ You can set **Audio Quality** you want to stream on voice chat.

2ï¸â£ You can set **Video Quality** you want to stream on voice chat.

3ï¸â£ **Auth Users**:- You can change admin commands mode from here to everyone or admins only. If everyone, anyone present in you group will be able to use admin commands(like /skip, /stop etc)

4ï¸â£ **Clean Mode:** When enabled deletes the bot's messages after 5 mins from your group to make sure your chat remains clean and good.

5ï¸â£ **Command Clean** : When activated, Bot will delete its executed commands (/play, /pause, /shuffle, /stop etc) immediately.

6ï¸â£ **Play Settings:**

/playmode - Get a complete play settings panel with buttons where you can set your group's play settings. 

<u>Options in playmode:</u>

1ï¸â£ **Search Mode** [Direct or Inline] - Changes your search mode while you give /play mode. 

2ï¸â£ **Admin Commands** [Everyone or Admins] - If everyone, anyone present in you group will be able to use admin commands(like /skip, /stop etc)

3ï¸â£ **Play Type** [Everyone or Admins] - If admins, only admins present in group can play music on voice chat."""

HELP_5 = """ð°**<u>ð±ð®ð ð«ð»ð¸ ðªð­ð­ ð¼ð¾ð­ð¸ ð¾ð¼ð®ð»ð¼  :</u>**
/addsudo [Username or Reply to a user]
/delsudo [Username or Reply to a user]

ð**<u>HEROKU:</u>**
/usage - Dyno Usage.

ð**<u>CONFIG VARS:</u>**
/get_var - Get a config var from Heroku or .env.
/del_var - Delete any var on Heroku or .env.
/set_var [Var Name] [Value] - Set a Var or Update a Var on heroku or .env. Seperate Var and its Value with a space.

ð¤**<u>BOT COMMANDS:</u>**
/reboot - Reboot your Bot. 
/update - Update Bot.
/speedtest - Check server speeds
/maintenance [enable / disable] 
/logger [enable / disable] - Bot logs the searched queries in logger group.
/get_log [Number of Lines] - Get log of your bot from heroku or vps. Works for both.
/autoend [enable|disable] - Enable Auto stream end after 3 mins if no one is listening.

ð**<u>STATS COMMANDS:</u>**
/activevoice - Check active voice chats on bot.
/activevideo - Check active video calls on bot.
/stats - Check Bots Stats

â ï¸**<u>BLACKLIST CHAT FUNCTION:</u>**
/blacklistchat [CHAT_ID] - Blacklist any chat from using Music Bot
/whitelistchat [CHAT_ID] - Whitelist any blacklisted chat from using Music Bot
/blacklistedchat - Check all blacklisted chats.

ð¤**<u>BLOCKED FUNCTION:</u>**
/block [Username or Reply to a user] - Prevents a user from using bot commands.
/unblock [Username or Reply to a user] - Remove a user from Bot's Blocked List.
/blockedusers - Check blocked Users Lists

ð¤**<u>GBAN FUNCTION:</u>**
/gban [Username or Reply to a user] - Gban a user from bot's served chat and stop him from using your bot.
/ungban [Username or Reply to a user] - Remove a user from Bot's gbanned List and allow him for using your bot
/gbannedusers - Check Gbanned Users Lists

ð¥**<u>VIDEOCALLS FUNCTION:</u>**
/set_video_limit [Number of Chats] - Set a maximum Number of Chats allowed for Video Calls at a time. Default to 3 chats.
/videomode [download|m3u8] - If download mode is enabled, Bot will download videos instead of playing them in M3u8 form. ByDefault to M3u8. You can use download mode when any query doesnt plays in m3u8 mode.

â¡ï¸**<u>PRIVATE BOT FUNCTION:</u>**
/authorize [CHAT_ID] - Allow a chat for using your bot.
/unauthorize [CHAT_ID] - Disallow a chat from using your bot.
/authorized - Check all allowed chats of your bot.

ð**<u>BROADCAST FUNCTION:</u>**
/broadcast [Message or Reply to a Message] - Broadcast any message to Bot's Served Chats.

<u>options for broadcast:</u>
**-pin** : This will pin your message 
**-pinloud** : This will pin your message with loud notification
**-user** : This will broadcast your message to the users who have started your bot.
**-assistant** : This will broadcast your message from assistant account of your bot.
**-nobot** : This will force your bot to not broadcast message

**Example:** `/broadcast -user -assistant -pin Hello Testing`

"""
