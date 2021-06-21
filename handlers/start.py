from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton

from config import BOT_NAME as bn




@Client.on_message(filters.command("start") & filters.private & ~filters.channel)
async def start(_, message: Message):
    await message.reply_text(
        f"""**Hey, I'm  {bn}, an open-source bot that lets you play music in your Telegram groups.For Support Join our group @♚𝚒𝐘𝚒♚™🇮🇳 ✦【★ 𝗔 𝗟 ★】✦ ╰❥☯︎ ꧁ঔৣ☠︎Seภ☢ritส☠︎ঔৣ꧂.\n\n The Assistant must be in your group to play music in the voice chat of your group.\n\n /help to know my commands**""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "Support⚡️", url="https://t.me/joinchat/HM2_zumCnDpjYjJl"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "Sk_Inayatullah_17⚡️", url="https://t.me/Sk_Inayatullah_17"
                    ),
                    InlineKeyboardButton(
                        "VENOM_HU_ME⚡️", url="https://t.me/VENOM_HU_ME"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "Add To Your Group⚡️", url="https://t.me/joinchat/HM2_zumCnDpjYjJl?startgroup=true"
                    )
                ]
            ]
        ),
     disable_web_page_preview=True
    )

@Client.on_message(filters.command("start") & ~filters.private & ~filters.channel)
async def gstart(_, message: Message):
      await message.reply_text(
        "💁🏻‍♂️ Do you want to search for a YouTube video?",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "✅ Yes", switch_inline_query_current_chat=""
                    ),
                    InlineKeyboardButton(
                        "No ❌", callback_data="close"
                    )
                ]
            ]
        )
    )
