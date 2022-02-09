# - *- coding: utf- 8 - *-
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, inline_keyboard


cicada = InlineKeyboardMarkup(row_width=1)
cicada.add(
    InlineKeyboardButton('🔗 Зашифр. Ссылку', callback_data='uurl'),
    InlineKeyboardButton('☑️ Пробив по IP', callback_data='ip'),
    InlineKeyboardButton('🔐 Генератор паролей', callback_data='gen_pass'),
    InlineKeyboardButton('🧰 Генератор ников', callback_data='gen_nick'),
    InlineKeyboardButton('🔝 user!! agent!!', callback_data='gen_agent'),
    InlineKeyboardButton(text='🌐 Генератор прокси', callback_data='gen_proxy')
)

uss = InlineKeyboardMarkup(row_width=1)
uss.add(
    InlineKeyboardButton(text='1️⃣  ANDROID ✅', callback_data='uss_android'),
    InlineKeyboardButton(text='2️⃣  IOS ✅', callback_data='uss_ios'),
    InlineKeyboardButton(text='3️⃣   Linux  ✅', callback_data='uss_linux'),
    InlineKeyboardButton(text='4️⃣    windows   ✅', callback_data='uss_windows'),
)

soglasie = InlineKeyboardMarkup()
soglasie.add(
    InlineKeyboardButton("✅ Да", callback_data="dada"),
    InlineKeyboardButton("❌ Нет", callback_data='nene')
)
soglasie2 = InlineKeyboardMarkup()
soglasie2.add(
    InlineKeyboardButton("✅ Да", callback_data="dada2"),
    InlineKeyboardButton("❌ Нет", callback_data='nene2')
)


gen_ent = InlineKeyboardMarkup(row_width=1)
gen_ent.add(
    InlineKeyboardButton(text='🧬 Сгенерировать', callback_data='gen_agnt'),
    InlineKeyboardButton(text='⚙️ Параметры', callback_data='settings_pass'),
    InlineKeyboardButton(text='◀️ Назад', callback_data='back_gen'),
)
gen_pass = InlineKeyboardMarkup(row_width=1)
gen_pass.add(
    InlineKeyboardButton(text='🧬 Сгенерировать', callback_data='generate_pass'),
    InlineKeyboardButton(text='⚙️ Параметры', callback_data='settings_pass'),
    InlineKeyboardButton(text='◀️ Назад', callback_data='back_gen'),
)


 
gen_pro = InlineKeyboardMarkup(row_width=1)
gen_pro.add(
    InlineKeyboardButton(text='🔄 Сгенерировать', callback_data='generate_proxy'),
    InlineKeyboardButton(text='◀️ Назад', callback_data='back_gen'),
)


cicada3301 = InlineKeyboardMarkup()

cicada3301.row(
    InlineKeyboardButton(text='🏞 Получить id фото:', callback_data='id_foto')
)

podmena2 = InlineKeyboardMarkup()
podmena2.add(
    InlineKeyboardButton('Подробнее', callback_data='pd2')
)
podmena = InlineKeyboardMarkup(row_width=1)
podmena.add(
    InlineKeyboardButton(text='Тарифы', callback_data='tarif'),
    InlineKeyboardButton(text='Видео', callback_data='vid'),
    InlineKeyboardButton(text='Проверим ?', callback_data='proverit'),
    InlineKeyboardButton(text='◀️ Назад', callback_data='tttt')
)

tariff = InlineKeyboardMarkup(row_width=1)
tariff.add(
    InlineKeyboardButton(text='Базовый', callback_data='bazovii'),
    InlineKeyboardButton(text='Расширенный', callback_data='rashir'),
    InlineKeyboardButton(text='VIP', callback_data='vip'),
    InlineKeyboardButton(text='◀️ Назад', callback_data='tttt')
)

tar_baza_back = InlineKeyboardMarkup()
tar_baza_back.add(
    InlineKeyboardButton('Купить', callback_data='baz_chench'),
    InlineKeyboardButton(text='◀️ Назад', callback_data='pd2')
)


tar_rash_back = InlineKeyboardMarkup()
tar_rash_back.add(
    InlineKeyboardButton('Купить', callback_data='rash_chench'),
    InlineKeyboardButton(text='◀️ Назад', callback_data='pd2')
)


tar_vip_back = InlineKeyboardMarkup()
tar_vip_back.add(
    InlineKeyboardButton('Купить', callback_data='vip_chench'),
    InlineKeyboardButton(text='◀️ Назад', callback_data='pd2')
)
oplata = InlineKeyboardMarkup()
oplata.add(
    InlineKeyboardButton("оплатил", callback_data='opt'),
    InlineKeyboardButton(text='◀️ Назад', callback_data='tttt')
)