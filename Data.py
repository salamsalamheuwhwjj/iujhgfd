from pyrogram.types import InlineKeyboardButton


class Data:
    # Start Message
    START = """
👋 ¦ اهلا عمࢪي  {}
✠━━━━━━━━Ξ𝗜𝗧𝗛𝗢𝗡━━━━━━━━━✠
 📮 ¦ في بوت 📬 {} 
━━━━━━━━━━━━━━━━━━━
🕹 ¦ يعمـل هـذا البـوت لمساعدتـك بطريقـة سهلـه للحصـول على كـود تيرمكـس والبايروجرام تم انشـاء هـذا البـوت بواسطـة : @TTTLL0
✠━━━━━━━━Ξ𝗜𝗧𝗛𝗢𝗡━━━━━━━━━✠

    """

    # Home Button
    home_buttons = [
        [InlineKeyboardButton(" ⚜️¦ بدأ استخراج الكود ", callback_data="generate")],
        [InlineKeyboardButton(text="⚜️¦ رجــوع", callback_data="home")]
    ]

    generate_button = [
        [InlineKeyboardButton(" ⚜️¦ بدأ استخراج الكود ", callback_data="generate")]
    ]

    # Rest Buttons
    buttons = [
        [InlineKeyboardButton(" ⚜️¦ بدأ استخراج الكود ", callback_data="generate")],
        [
            InlineKeyboardButton("⚜️¦ كيف تستخدمني", callback_data="help"),
            InlineKeyboardButton("⚜️¦ حــول", callback_data="about")
        ]
    ]

    # Help Message
    HELP = """
✨ **📬 ¦ كـيف تستخـدمني** ✨

× /about - حول البوت
× /help - لتسوي روحك كلشي متعرف
× /start - حتى تشغل البوت
× /generate - حتى تبدا بأستخراج جلسة
× /cancel - لألغاء الاستخراج
× /restart - اعادة تشغيل البوت
"""

    # About Message
    ABOUT = """
**⚜️¦حـول البـوت** 

- بـوت استخـراج كـود تيرمكـس خـاص بســورس ايـثـون 

- قنـاة السـورس : @EITHON1

كروب السورس : [كروب سورس ايــثــون](https://t.me/eithonsupport)

استخدم البوت : 

»[Pyrogram](docs.pyrogram.org)
🕹
»[Python](www.python.org)

لغة البوت : [بايثون](www.python.org)

🇸🇾 ¦ المطور  : [مٰۭۘـٖۛৣ๋͜͡ﹻٰـحـ᭓͚͊٘͢ـٰ͜͡ـمٰۭٖۘـٖۛৣ๋͜͡ﹻٰـٰډ͢ ༒ آٖب۪ٖؔٛـ࿆ۦ๋ۚۧ͜ـﯡُٖ٘ز۪ۖڰـٖۛৣ๋͜͡ﹻٰـﯡٍ٘ٚࢪٰ۪ؔ༒ ](https://t.me/TTTLL0)
    """
