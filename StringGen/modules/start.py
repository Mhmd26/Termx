from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message
from StringGen import Anony
from StringGen.utils import add_served_user, keyboard


@Anony.on_message(filters.command("start") & filters.private & filters.incoming)
async def f_start(_, message: Message):
    await message.reply_text(
        text=f"""</b>المستخدم</b> | {message.from_user.first_name}\n</b>مرحبا بك فـي بـوت اسـتـخـراج جلسات العقرب 😁 </b>\n\n</b>✎┊‌ يمكنك استـخـراج التالـي </b>\n</b>✎┊‌ تـلـيـثـون </b>\n</b>✎┊‌ بايـروجـرام </b>\n\n</b>- لبدء الاستخراج اضغط Start bot</b>\n</b>- لمعرفة كيفية الاستخراج اضغط Order bot</b>\n\n</b>✎┊‌ تم انشاء البوت بواسطة: \n @Zo_r0 | @I_e_e_l </b>""",
        reply_markup=keyboard,
        disable_web_page_preview=True,
    )
    await add_served_user(message.from_user.id)
