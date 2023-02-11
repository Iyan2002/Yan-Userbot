""" Userbot module for other small commands. """
from userbot import CMD_HANDLER as cmd
from userbot import CMD_HELP
from userbot.utils import edit_or_reply, man_cmd


@man_cmd(pattern="ihelp$")
async def usit(event):
    me = await event.client.get_me()
    await edit_or_reply(
        event,
        f"**ʜᴀʟʟᴏ, ᴋᴇɴᴀʟɪɴ ɢᴡ ɪʏᴀɴ ᴀsᴀʟ ᴊᴀᴡᴀ ʙᴀʀᴀᴛ. sᴀʟᴀᴍ ᴋᴇɴᴀʟ ʏᴀ.** \n"
        f"✣ **sᴜᴘᴘᴏʀᴛ ɢʀᴏᴜᴘ :** [Sharing Userbot](t.me/Publik_Virtual)\n"
        f"✣ **ᴄʜᴀɴɴᴇʟ ɪʏᴀɴ :** [Lunatic0de](t.me/bang_iyan)\n"
        f"✣ **ᴛᴇʟᴇɢʀᴀᴍ :** [Risman](@A_iyan)\n"
        f"✣ **ʀᴇᴘᴏ :** [Man-Userbot](https://github.com/mrismanaziz/Man-Userbot)\n",
    )


@man_cmd(pattern="listvar$")
async def var(event):
    await edit_or_reply(
        event,
        "**Daftar Lengkap Vars Dari Man-Userbot:** [KLIK DISINI](https://telegra.ph/List-Variabel-Heroku-untuk-Man-Userbot-09-22)",
    )


CMD_HELP.update(
    {
        "helper": f"**Plugin : **`helper`\
        \n\n  •  **Syntax :** `{cmd}ihelp`\
        \n  •  **Function : **Bantuan Untuk Man-Userbot.\
        \n\n  •  **Syntax :** `{cmd}listvar`\
        \n  •  **Function : **Melihat Daftar Vars.\
        \n\n  •  **Syntax :** `{cmd}repo`\
        \n  •  **Function : **Melihat Repository Man-Userbot.\
        \n\n  •  **Syntax :** `{cmd}string`\
        \n  •  **Function : **Link untuk mengambil String Man-Userbot.\
    "
    }
)
