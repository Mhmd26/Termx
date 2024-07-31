from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message
from StringGen import Anony
from StringGen.utils import add_served_user, keyboard

# استبدل باسم قناتك
CHANNEL_ID = '@Scorpion_scorp'

# نفترض أن إعدادات Client تحتوي بالفعل على API_TOKEN
app = Client("my_bot")

# وظيفة للتحقق من الاشتراك
async def check_subscription(user_id):
    try:
        chat_member = await app.get_chat_member(CHANNEL_ID, user_id)
        return chat_member.status in ['member', 'administrator', 'creator']
    except Exception as e:
        return False  # إذا حدث خطأ، المستخدم غير مشترك

@app.on_message(filters.command("start") & filters.private & filters.incoming)
async def f_start(_, message: Message):
    user_id = message.from_user.id

    # التحقق من الاشتراك
    if not await check_subscription(user_id):
        await message.reply_text(
            text="الاشتراك إجباري، يرجى الاشتراك في القناة لتتمكن من استخدام البوت.",
            reply_markup=InlineKeyboardMarkup(
                [[InlineKeyboardButton("اشترك في القناة", url=f"https://t.me/{CHANNEL_ID[1:]}")]]
            )
        )
        return

    await message.reply_text(
        text=f"""</b>المستخدم</b> | {message.from_user.first_name}\n</b>مرحبا بك فـي بـوت اسـتـخـراج جلسات العقرب 😁 </b>\n\n</b>✎┊‌ يمكنك استـخـراج التالـي </b>\n</b>✎┊‌ تـلـيـثـون </b>\n</b>✎┊‌ بايـروجـرام </b>\n\n</b>- لبدء الاستخراج اضغط Start bot</b>\n</b>- لمعرفة كيفية الاستخراج اضغط Order bot</b>\n\n</b>✎┊‌ تم انشاء البوت بواسطة: \n @Zo_r0 | @I_e_e_l </b>""",
        reply_markup=keyboard,
        disable_web_page_preview=True,
    )
    await add_served_user(message.from_user.id)

if __name__ == '__main__':
    app.run()
