"""Check if userbot alive. If you change these, you become the gayest gay such that even the gay world will disown you."""
#IMG CREDITS: @WhySooSerious
import asyncio
from telethon import events
from telethon.tl.types import ChannelParticipantsAdmins
from platform import uname
from userbot import ALIVE_NAME
from userbot.utils import admin_cmd


DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else "Set ALIVE_NAME in config vars in Heroku"
PM_IMG = "https://telegra.ph/file/b2e3b398c2f75c72bebd1.png"
pm_caption = "` Congratulation You Have successfully Deployed \n"
pm_caption += "`Dark_Zino_SuperUser IS:`ONLINE` \n\n"
pm_caption += "Current Sat : `Dark Zino `\n\n"
pm_caption += f"ɧ My Boss ɧ : {DEFAULTUSER} \n\n"
pm_caption += "\n\n"
pm_caption += "\n\n"
pm_caption += " Type .help To Access SuperUser\n\n"
pm_caption += "Copyright : By Dark Zino (GitHub.com/Deepankar-siddharth)\n"
pm_caption += "[Deploy SuperUser Made By @Dark_zino](https://github.com/Deepankar-Siddharth/DarkZino_SuperUser)"
#@command(outgoing=True, pattern="^.alive$")
@borg.on(admin_cmd(pattern=r"alive"))
async def amireallyalive(alive):
    """ For .alive command, check if the bot is running.  """
    await alive.delete() 
    await borg.send_file(alive.chat_id, PM_IMG,caption=pm_caption)
