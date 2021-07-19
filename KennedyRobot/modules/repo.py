from pyrogram import filters
from JisooX import pbot

__help__ = """
 ❍ /repos*:* To Get My Github Repository Link And Support Group Link
"""

__mod_name__ = "REPO"


@pbot.on_message(filters.command("repos") & ~filters.edited)
async def repos(_, message):
    await message.reply_text(
        "[GitHub](https://github.com/ferikunn/JisooXRobot)"
        + " | [Group](https://t.me/JisooSupport)",
        disable_web_page_preview=True,
    )
