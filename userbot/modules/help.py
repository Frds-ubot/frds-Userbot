# Copyright (C) 2019 The Raphielscape Company LLC.
#
# Licensed under the Raphielscape Public License, Version 1.d (the "License");
# you may not use this file except in compliance with the License.
#
""" Userbot help command """

import asyncio
from userbot import ALIVE_NAME, CMD_HELP
from userbot.events import register
from platform import uname

modules = CMD_HELP

# ================= CONSTANT =================
DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else uname().node
# ============================================


@register(outgoing=True, pattern="^.help(?: |$)(.*)")
async def help(indomie):
    """ For .help command,"""
    args = indomie.pattern_match.group(1).lower()
    if args:
        if args in CMD_HELP:
            await indomie.edit(str(CMD_HELP[args]))
        else:
            await indomie.edit("**`NGETIK YANG BENER NGENTOT!`**")
            await asyncio.sleep(50)
            await indomie.delete()
    else:
        string = ""
        for i in CMD_HELP:
            string += "`" + str(i)
            string += "`\t â¦  "
        await indomie.edit(f"**â¨ List Help [ðððð-ððððððð](https://github.com/frds-ubot/Frds-Userbot):**\n\n"
                           f"**â¨ Êá´á´ á´á´¡É´á´Ê {DEFAULTUSER}**\n**â¨ Má´á´á´Êá´ê± : {len(modules)}**\n\n"
                           "**â¢ Má´ÉªÉ´ Má´É´á´ :**\n"
                           f"â¦ {string}â¦\n\n")
        await indomie.reply(
            "\nâ **É´á´á´á´ê± :** `<.help ping>` **Untuk Informasi Pengunaan.\nJangan Lupa Berdoa Sebelum Mencoba wahahaha...**")

        await asyncio.sleep(50)
        await indomie.delete()
