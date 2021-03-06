#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# (c) @AlbertEinsteinTG

from pyrogram import filters, Client
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, CallbackQuery
from bot import Translation, LOGGER # pylint: disable=import-error
from bot.database import Database # pylint: disable=import-error

db = Database()

@Client.on_message(filters.command(["start"]) & filters.private, group=1)
async def start(bot, update):
    
    try:
        file_uid = update.command[1]
    except IndexError:
        file_uid = False
    
    if file_uid:
        file_id, file_name, file_caption, file_type = await db.get_file(file_uid)
        
        if (file_id or file_type) == None:
            return
        
        caption = file_caption if file_caption != ("" or None) else ("<code>" + file_name + "</code>")
        try:
            await update.reply_cached_media(
                file_id,
                quote=True,
                caption = β€οΈ ππππππ’ππ π΅ππ πππππ πΎππ πππππππ πΏπππππ πππππππ ππ π±π’ πππππππ πΎππ π²ππππππ/πΆππππ π»πππ ππ ππππ π΅ππππππ\n 
 \n
 βππ ππ ππ¦π£ βπππππππ€β \n
\n
π€ Bots for common useπ \n
ππ»(Rename, Group Manager, etc)ππ» \n
https://t.me/bots_showcase \n
π¬ Movie request groupπ \n
https://t.me/mymovieshowcase \n
 π­ Cartoonπ \n
https://t.me/tamil_cartoon_ms \n
πΊ Series request groupπ \n
https://t.me/series_showcase \n
ποΈΚΟΞΉΠΈ ποΈ ΡΠ½Ξ±ΡΡποΈ ΡΟΟΟΟΡΡ
                parse_mode="html",
                reply_markup=InlineKeyboardMarkup(
                    [
                        [
                            InlineKeyboardButton
                                (
                                    'For Feedback', url="https://t.me/ShowcasE_Feedback"
                                )
                        ]
                    ]
                )
            )
        except Exception as e:
            await update.reply_text(f"<b>Error:</b>\n<code>{e}</code>", True, parse_mode="html")
            LOGGER(__name__).error(e)
        return

    buttons = [[
        InlineKeyboardButton('Developers', url='https://t.me/ShowcasE_Feedback'),
        InlineKeyboardButton('Source Code π§Ύ', url ='https://github.com/ShowcaseBoss/Auto_Filter_V2')
    ],[
        InlineKeyboardButton('For More Bots', url='https://t.me/bots_showcase')
    ],[
        InlineKeyboardButton('Help β', callback_data="help")
    ]]
    
    reply_markup = InlineKeyboardMarkup(buttons)
    
    await bot.send_message(
        chat_id=update.chat.id,
        text=Translation.START_TEXT.format(
                update.from_user.first_name),
        reply_markup=reply_markup,
        parse_mode="html",
        reply_to_message_id=update.message_id
    )


@Client.on_message(filters.command(["help"]) & filters.private, group=1)
async def help(bot, update):
    buttons = [[
        InlineKeyboardButton('Home β‘', callback_data='start'),
        InlineKeyboardButton('About π©', callback_data='about')
    ],[
        InlineKeyboardButton('Close π', callback_data='close')
    ]]
    
    reply_markup = InlineKeyboardMarkup(buttons)
    
    await bot.send_message(
        chat_id=update.chat.id,
        text=Translation.HELP_TEXT,
        reply_markup=reply_markup,
        parse_mode="html",
        reply_to_message_id=update.message_id
    )


@Client.on_message(filters.command(["about"]) & filters.private, group=1)
async def about(bot, update):
    
    buttons = [[
        InlineKeyboardButton('Home β‘', callback_data='start'),
        InlineKeyboardButton('Close π', callback_data='close')
    ]]
    reply_markup = InlineKeyboardMarkup(buttons)
    
    await bot.send_message(
        chat_id=update.chat.id,
        text=Translation.ABOUT_TEXT,
        reply_markup=reply_markup,
        disable_web_page_preview=True,
        parse_mode="html",
        reply_to_message_id=update.message_id
    )
