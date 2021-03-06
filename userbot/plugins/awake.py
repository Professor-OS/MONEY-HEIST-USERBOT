import time

from telethon import version

from LEGENDBOT.utils import admin_cmd, edit_or_reply, sudo_cmd
from userbot import LEGENDversion, StartTime
from userbot.cmdhelp import CmdHelp

from . import *


async def reply_id(event):
    reply_to_id = None
    if event.sender_id in Config.SUDO_USERS:
        reply_to_id = event.id
    if event.reply_to_msg_id:
        reply_to_id = event.reply_to_msg_id
    return reply_to_id


LEGEND_IMG = Config.AWAKE_PIC
CUSTOM_ALIVE_TEXT = Config.ALIVE_MSG or "PROFESSOR AGORA"
CUSTOM_YOUR_GROUP = Config.YOUR_GROUP or "@MM_Userbot"


def get_readable_time(seconds: int) -> str:
    count = 0
    ping_time = ""
    time_list = []
    time_suffix_list = ["s", "m", "h", "days"]

    while count < 4:
        count += 1
        if count < 3:
            remainder, result = divmod(seconds, 60)
        else:
            remainder, result = divmod(seconds, 24)
        if seconds == 0 and remainder == 0:
            break
        time_list.append(int(result))
        seconds = int(remainder)

    for x in range(len(time_list)):
        time_list[x] = str(time_list[x]) + time_suffix_list[x]
    if len(time_list) == 4:
        ping_time += time_list.pop() + ", "

    time_list.reverse()
    ping_time += ":".join(time_list)

    return ping_time


uptime = get_readable_time((time.time() - StartTime))


@bot.on(admin_cmd(outgoing=True, pattern="awake$"))
@bot.on(sudo_cmd(pattern="awake$", allow_sudo=True))
async def amireallyalive(event):
    if event.fwd_from:
        return
    reply_to_id = await reply_id(event)

    if LEGEND_IMG:
        LEGEND_caption = f"**{legend_mention}**\n"

        LEGEND_caption += f"~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n"
        LEGEND_caption += f"     π°πΌπΎπ½π΄π π·π΄πΈππ πΈπ π°ππ°πΊπ΄π°\n"
        LEGEND_caption += f"β’π₯β’ πΌπΎπ½π΄π π·π΄πΈππ π±πΎπ : Ξ½3.0\n"
        LEGEND_caption += f"β’π₯β’ ππ΄π»π΄ππ·πΎπ½: `{version.__version__}`\n"
        LEGEND_caption += f"β’π₯β’ ππΏππΈπΌπ΄: `{uptime}`\n" 
        LEGEND_caption += f"β’π₯β’ πΏππΎπ΅π΄πππΎπ: `[π°πΆπΎππ°](t.me/prof_agora)\n" 
        LEGEND_caption += f"β’π₯β’ ππΏπ°πΌ: `[ππΏπ°πΌ](t.me/mm_ub_updates)\n"
        LEGEND_caption += f"β’π₯β’ πΆππΎππΏ: `[πΆππΎππΏ](t.me/MM_USERBOT)\n"

        await event.client.send_file(
            event.chat_id, LEGEND_IMG, caption=LEGEND_caption, reply_to=reply_to_id
        )
        await event.delete()
    else:
        await edit_or_reply(
            awake,
            f"**{CUSTOM_ALIVE_TEXT}**\n\n"
            f"~~~~~~~~~~~~~~~~~~~~~~~ \n"
            f"       πΌπΎπ½π΄π π·π΄πΈππ π±πΎπ πππ°πππ\n"
            f"β’β‘β’ ππ΄π»π΄ππ·πΎπ½       : `{version.__version__}`\n"
            f"β’π°β’ πΌπΎπ½π΄ππ·π΄πΈπππ±πΎπ  : `{LEGENDversion}`\n"
            f"β’π₯β’ ππΏππΈπΌπ΄         : `{uptime}`\n"
            f"β’π°β’ πΌπ°πππ΄π         : {mention}\n"
            f"β’π¨βπ«β’ πΎππ½π΄π          : [πΏππΎπ΅π΄πππΎπ](t.me/PROF_AGORA)\n",
        )


CmdHelp("awake").add_command("awake", None, "ΟΡΡ Ξ±ΠΈβ ΡΡΡ").add_info(
    "Same Like Alive"
).add_type("Official").add()
