import random, os
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton


Bot = Client(
    "Password Generator Bot",
    bot_token=os.environ.get("BOT_TOKEN"),
    api_id=int(os.environ.get("API_ID")),
    api_hash=os.environ.get("API_HASH")
)

TEXT = """**Hai {},
Ben Parola Oluşturucu Bot'um. İstediğiniz Sürede Güçlü Şifreler Üretebilirim (Max. 84).**

Daha Fazla Bilgi İçin /help"""

BUTTONS = InlineKeyboardMarkup(
    [
        [
            InlineKeyboardButton("kanal 🔰", url = "https://telegram.me/CyberTurkish"),
            InlineKeyboardButton("Support⭕️", url = "https://telegram.me/muhabbetofkings")
        ],
        [
            InlineKeyboardButton("OWNER 🗂️", url = "https://t.me/bozkurt20"),
            InlineKeyboardButton("DİĞER BOTLAR🗃️", url = "https://t.me/BozkurtRoBot")
        ],
        [
            InlineKeyboardButton("Developer 💡", url = "https://t.me/bozkurt20")
        ]
    ]
)

HELP = """"Hai {}, **Daha Fazla Bilinecek Bir Şey Yok.** - Bana Parolanızın ve Anahtarlarınızın Sınırını Gönderin (isteğe bağlı) Beğen: - `10 abcd1234` `10` - O Sınırın Şifresini Vereceğim **Not :-** • Yalnızca Rakamlara İzin Verilir • 100'e Kadar İzin Verilen Maksimum Basamak (84 Uzunluğundan Fazla Parola Oluşturamıyorum)"""

HELP_BUTTON = InlineKeyboardMarkup(
    [
        [
            InlineKeyboardButton("🧑‍💻 Channel", url = "https://telegram.me/BozkurtRoBot"),
            InlineKeyboardButton("🗃️ Sahip ", url = "bozkurt20")
        ]
    ]
)

ABOUT = """--**About Me**--

** Bot :** Şifre Oluşturucu Bot ** Geliştirici :** [bozkurt20](https://t.Me/bozkurt20) ** Kanal :** @BozkurtRoBot ** Destek :** @muhabbetofkings * * Kaynak Kodu :** [Password Generator Bot](t.Me/muhabbetofkings) ** Dil :** Python 3 ** Çerçeve :** Pyrogram"""


@Bot.on_message(filters.private & filters.command(["start"]))
async def start(bot, update):
    await update.reply_text(
        text=TEXT.format(update.from_user.mention),
        reply_markup=BUTTONS,
        disable_web_page_preview=True,
        quote=True
    )


@Bot.on_message(filters.private & filters.command(["help"]))
async def help(bot, update):
    await update.reply_text(
        text=HELP.format(update.from_user.mention),
        reply_markup=HELP_BUTTON,
        disable_web_page_preview=True,
        quote=True
    )


@Bot.on_message(filters.private & filters.command(["about", "source", "repo"]))
async def about(bot, update):
    await update.reply_text(
        text=ABOUT,
        disable_web_page_preview=True,
        quote=True
    )


@Bot.on_message(filters.private & filters.text)
async def password(bot, update):
    
    message = await message.reply_text('`Processing...`')
    
    try:
        if len(update.text.split()) > 1:
            keys, limit = update.text.split()[1], int(update.text.split()[0])
        else:
            keys = "abcdefghijklmnopqrstuvwxyz"+"1234567890"+"!@#$%^&*()_+".lower()
            limit = int(update.text)
    except:
        await message.edit_text('Something wrong')
        return
    
    if limit > 100 or limit <= 0:
        text = "Sorry... Failed To Create Password, Because Limit is 1 to 100."
    else:
        random_value = "".join(random.sample(password, limit))
        text = f"**Limit :-** `{str(limit)}`.\n**Password :-** `{random_value}`**\n\nJoin @EKBOTZ_UPDATE"
    
    await message.edit_text(text, True)


Bot.run()
