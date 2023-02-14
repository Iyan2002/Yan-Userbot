from time import sleep

from userbot import CMD_HANDLER as cmd

from userbot import CMD_HELP

from userbot.utils import edit_or_reply, man_cmd

@man_cmd(pattern="iy(?: |$)(.*)")

async def _(event):

    await event.client.send_message(

        event.chat_id,

        "**Assalamualaikum Dulu Biar Sopan**",

        reply_to=event.reply_to_msg_id,

    )

    await event.delete()

@man_cmd(pattern="yi(?: |$)(.*)")

async def _(event):

    await event.client.send_message(

        event.chat_id,

        "**Hadir bang**",

        reply_to=event.reply_to_msg_id,

    )

    await event.delete()

@man_cmd(pattern="bg(?: |$)(.*)")

async def _(event):

    me = await event.client.get_me()

    xx = await edit_or_reply(event, f"**Haii Salken Saya {me.first_name}**")

    sleep(2)

    await xx.edit("**Assalamualaikum...**")

@man_cmd(pattern="an(?: |$)(.*)")

async def _(event):

    await event.client.send_message(

        event.chat_id, "**Wa'alaikumsalam**", reply_to=event.reply_to_msg_id

    )

    await event.delete()

@man_cmd(pattern="ya(?: |$)(.*)")

async def _(event):

    me = await event.client.get_me()

    xx = await edit_or_reply(event, f"**Haii Salken Saya {me.first_name}**")

    sleep(2)

    await xx.edit("**Assalamualaikum**")

@man_cmd(pattern="gb(?: |$)(.*)")

async def _(event):

    xx = await edit_or_reply(event, "**WOYY**")

    sleep(3)

    await xx.edit("**NIMBRUNG TOLOL!!!🔥**")

@man_cmd(pattern="ps(?: |$)(.*)")

async def _(event):

    me = await event.client.get_me()

    xx = await edit_or_reply(event, f"**Hallo KIMAAKK SAYA {me.first_name}**")

    sleep(2)

    await xx.edit("**LU SEMUA NGENTOT 🔥**")

@man_cmd(pattern="na(?: |$)(.*)")

async def _(event):

    xx = await edit_or_reply(event, "**Hallo**")

    sleep(2)

    await xx.edit("**Maaf Telat Nimbrung**")

CMD_HELP.update(

    {

        "salam": f"**Plugin : **`salam`\

        \n\n  •  **Syntax :** `{cmd}iy`\

        \n  •  **Function : **Assalamualaikum Dulu Biar Sopan..\

        \n\n  •  **Syntax :** `{cmd}yi`\

        \n  •  **Function : **salam Kenal dan salam\

        \n\n  •  **Syntax :** `{cmd}an`\

        \n  •  **Function : **Untuk Menjawab salam\

        \n\n  •  **Syntax :** `{cmd}na`\

        \n  •  **Function : **Salam Bahas arab\

        \n\n  •  **Syntax :** `{cmd}sp`\

        \n  •  **Function : **Memberikan Semangat.\

        \n\n  •  **Syntax :** `{cmd}so`\

        \n  •  **Function : **nMenampilkan Sama sama\

        \n\n  •  **Syntax :** `{cmd}os`\

        \n  •  **Function : **Kata I Love You.\

        \n\n  •  **Syntax :** `{cmd}ps`\

        \n  •  **Function : **LU SEMUA NGENTOT 🔥\

        \n\n  •  **Syntax :** `{cmd}gb`\

        \n  •  **Function : **NIMBRUNG GOBLOKK!!!🔥\

    "

    }

)

