from pyrogram import filters
from KennedyRobot import pbot

__help__ = """
 ❍ /repos*:* To Get My Github Repository Link And Support Group Link
"""

__mod_name__ = "REPO 🕴️"


@pbot.on_message(filters.command("repos") & ~filters.edited)
async def repos(_, message):
    await message.reply_text(
        "[GitHub](https://github.com/KennedyProject/KennedyRobot)"
        + " | [Group](https://t.me/zeusspam)",
        disable_web_page_preview=True,
    )
