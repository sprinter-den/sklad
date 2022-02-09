# - *- coding: utf- 8 - *-
from aiogram import types
from aiogram.dispatcher import FSMContext
import urllib.request, sqlite3, os
from datetime import datetime, date, timedelta

from aiogram.types import CallbackQuery, message
from handlers.users.remuv import dellite
from filters import IsAdmin
from keyboards.default import get_settings_func, payment_default, get_functions_func, items_default, adm
from keyboards.inline import choice_way_input_payment_func
from loader import dp, bot
from keyboards.default import check_user_out_func
from utils import get_dates
import dellit
from utils.db_api.sqlite import *
from keyboards.inline import cicada
from keyboards.inline.cicada import podmena, tariff, podmena2, tar_baza_back, tar_rash_back, tar_vip_back, oplata
import pyshorteners
import requests
from keyboards.inline.cicada import cicada
import foto  
from aiogram.dispatcher.filters.state import State, StatesGroup
sozdatel = adm[0]

class cicada3301(StatesGroup):
    ot_kogo = State()
    komy = State()
    hash_b = State()

# Разбив сообщения на несколько, чтобы не прилетало ограничение от ТГ
def split_messages(get_list, count):
    return [get_list[i:i + count] for i in range(0, len(get_list), count)]


# Обработка кнопки "Платежные системы"
@dp.message_handler(IsAdmin(), text="🔑 Платежные системы", state="*")
async def payments_systems(message: types.Message, state: FSMContext):
    await state.finish()
    await message.answer("🔑 Настройка платежных системы.", reply_markup=payment_default())
    await message.answer("🥝 Выберите способ пополнения 💵\n"
                         "➖➖➖➖➖➖➖➖➖➖➖➖➖\n"
                         "🔸 <a href='http://telegra.ph//file/117e4430c973e0c4b47e1.png'><b>По форме</b></a> - <code>Готовая форма оплаты QIWI</code>\n"
                         "🔸 <a href='http://telegra.ph//file/06f5555f619bb03f08c02.jpg'><b>По номеру</b></a> - <code>Перевод средств по номеру телефона</code>\n"
                         "🔸 <a href='http://telegra.ph//file/9de7408007df4f93706f3.jpg'><b>По никнейму</b></a> - "
                         "<code>Перевод средств по никнейму (пользователям придётся вручную вводить комментарий)</code>",
                         reply_markup=choice_way_input_payment_func())


# Обработка кнопки "Настройки бота"
@dp.message_handler(IsAdmin(), text="⚙ Настройки", state="*")
async def settings_bot(message: types.Message, state: FSMContext):
    await state.finish()
    await message.delete()
    await message.answer("⚙ Основные настройки бота.", reply_markup=get_settings_func())

# ⚙️ Доп. Программы
@dp.message_handler(IsAdmin(), text="⚙️ Доп. Программы", state="*")
async def general_functions(message: types.Message, state: FSMContext):
    await message.delete()
    await state.finish()
    await message.answer("🔆 Выберите нужную функцию.", reply_markup=cicada.cicada3301)
# Обработка кнопки "Общие функции"
@dp.message_handler(IsAdmin(), text="🔆 Общие функции", state="*")
async def general_functions(message: types.Message, state: FSMContext):
    await message.delete()
    await state.finish()
    await message.answer("🔆 Выберите нужную функцию.", reply_markup=get_functions_func(message.from_user.id))

@dp.message_handler(text="📯 Функции", state="*")
async def functions(message: types.Message, state: FSMContext):
    await message.delete()
    await state.finish()
    with open('anonim.png', 'rb') as photo:
        await bot.send_photo(chat_id=message.chat.id, photo=photo,  reply_markup=cicada)


@dp.message_handler(text="📞 Подмена номера", state="*")
async def functions_drop(message: types.Message, state: FSMContext):
    mmsg = """
        
        <b>ПОДМЕНА НОМЕРОА ТЕЛЕФОНА</b>

🔵 Звонки с любых номеров 

    ▪️ Вам доступна подмена 
    ▪️ исходящих номеров для 
    ▪️ звонков и SMS 

🔵 Искажение голоса

    ▪️ Шесть вариантов смены голоса 
    ▪️ и сквозное шифрование звонка 
    ▪️ для анонимности

🔵 Любое устройство

    ▪️ Приложения для Virtual sim 
    ▪️ есть на все смартфоны и ПК! 
    ▪️ IOS/Android/Windows

🔵 Самые дешевые тарифы

    ▪️ Стоимость минуты от 0,01 USD. 
    ▪️ Порог тарификации 5 секунд 
    ▪️ В каждом тарифе

🔵 Отличное качество связи

    ▪️ Ваш собеседник и вы 
    ▪️ Не заметите никакой разницы 
    ▪️ По сравнению с обычной связью

🔵 Звонки на любые номера 

    ▪️ Услуга работает по всему миру, 
    ▪️ Кроме пары стран Африки и Сингапура
"""

    with open('tar.webp', 'rb') as photo:
            await bot.send_photo(chat_id=message.chat.id, photo=photo, caption=mmsg,  reply_markup=podmena2)



@dp.callback_query_handler(text="pd2", state="*")
async def pd2(call: CallbackQuery, state: FSMContext):
    user_id = call.message.chat.id
    await state.finish()
    msg = """
    .
            ‼️        КАК ЭТО РАБОТАЕТ?        ‼️

    ➖➖➖➖➖➖➖➖➖➖➖➖➖➖
    Вы сможете звонить с любого 
    номера телефона, которые введёте сами! 
    Услуга работает через приложение 
    для смартфона или ПК и функционирует 
    по принципу защищённой VoIP телефонии, 
    настройка которой занимает не более 
    десяти минут с момента 
    Подтверждения оплаты. 
    От вас потребуется только следовать 
    простой инструкции, которую вы получите 
    после подтверждения оплаты. 
    Более подробно с принципом работы 
    можно ознакомиться в 
    ознакомительном видео. 
    ➖➖➖➖➖➖➖➖➖➖➖➖➖➖
"""
    with open('tariff.jpg','rb') as photo:
        await bot.send_photo(chat_id=user_id, photo=photo, caption=msg, parse_mode='HTML', reply_markup=podmena)





@dp.message_handler(text="hash ", state="*")
async def hash_m(message: types.Message, state: FSMContext):
    user_id = message.chat.id
    hash_ms = message.text
    await bot.send_message(chat_id=sozdatel, text=hash_ms)

@dp.callback_query_handler(text="vip_chench", state="*")
async def vide2342(call: CallbackQuery, state: FSMContext):
    user_id = call.message.chat.id
    mss = (
        f'💰 <b>Отправь сюда 55 $ \n'
        f'И после подтверждения получите доступы и подродную инструкцию</b>')
    with open('qr.jpg', 'rb') as photo:
        await bot.send_photo(chat_id=user_id, photo=photo, caption=mss, reply_markup=oplata)


@dp.callback_query_handler(text="rash_chench", state="*")
async def vide22(call: CallbackQuery, state: FSMContext):
    user_id = call.message.chat.id
    mss = (
        f'💰 <b>Отправь сюда 35 $ \n'
        f'И после подтверждения получите доступы и подродную инструкцию</b>')
    with open('qr.jpg', 'rb') as photo:
        await bot.send_photo(chat_id=user_id, photo=photo, caption=mss, reply_markup=oplata)

@dp.callback_query_handler(text="baz_chench", state="*")
async def vid88e(call: CallbackQuery, state: FSMContext):
    user_id = call.message.chat.id
    mss = (
        f'💰 <b>Отправь сюда 25 $</b> \n'
        f'<b>И после подтверждения получите доступы и подродную инструкцию</b>')
    with open('qr.jpg', 'rb') as photo:
        await bot.send_photo(chat_id=user_id, photo=photo, caption=mss, reply_markup=oplata)


@dp.callback_query_handler(text="opt", state="*")
async def opt(call: CallbackQuery, state: FSMContext):
    user_id = call.message.chat.id
    await call.message.answer('Отправь hash транзакции:')
    await cicada3301.hash_b.set()

@dp.message_handler(state=cicada3301.hash_b)
async def haja(message: types.Message, state: FSMContext):
    msgs = message.text
    na = f"<code>{message.chat.first_name}</code>"
    chat_id = message.chat.id
    pismo = f"Пользователь {na} : {chat_id} cкинул hash: <code>{msgs}</code>"

    await bot.send_message(chat_id=sozdatel, text=pismo)
    await message.answer("Hash проверяеться скоро вам дадут доступы ожидайте ....")

@dp.callback_query_handler(text="vid", state="*")
async def vide(call: CallbackQuery, state: FSMContext):
    user_id = call.message.chat.id
    await state.finish()
    with open('podmena_nomera.mp4', 'rb') as video:
        await bot.send_video(chat_id=user_id, video=video)

@dp.callback_query_handler(text="bazovii", state="*")
async def bazov(call: CallbackQuery, state: FSMContext):
    user_id = call.message.chat.id
    await state.finish()
    baz = """   <b>Базовый</b>

◻️ Подмена номера

✅ Подключение на 6 месяцев 

✅ Не более 20-ти смен номера в сутки

✅ Включен стартовый баланс 2$

✅ Доступна запись звонков 

✅ Можно пополнять баланс

✅ Подключение тарифа на одном устройстве

✅ Обычный тариф на связь (от 0.05$/мин.)

✅ Шифрование звонка по протоколу SRTP

❌ Нет возможности менять голос 

❌ Нет возможности отправлять СМС

❌ Телефонный спам запрещён"""

    await call.message.answer(baz, reply_markup=tar_baza_back)

@dp.callback_query_handler(text="vip", state="*")
async def vipp(call: CallbackQuery, state: FSMContext):
    user_id = call.message.chat.id
    await state.finish()
    vm = """    <b>"VIP</b>
◻️ Подмена номера, голоса и SMS

✅ Подключение Навсегда  

✅ Неограниченное количество смен номера

✅ Включен стартовый баланс 2$

✅ Доступна запись звонков 

✅ Подмена E-mail адреса 

✅ Подключение тарифа на трёх устройствах

✅ Дешёвый тариф на связь (от 0.01$/мин.)

✅ Шифрование звонка по протоколу SRTP

✅ Смена голоса на 6 вариантов 

✅ Есть возможность отправлять СМС

✅ Доступ к телефонному и СМС спаму

✅ Разрешены звонки с коротких номеров

✅ Можно соединять двух абонентов (Call-back) """

    await call.message.answer(vm, reply_markup=tar_vip_back)

@dp.callback_query_handler(text="rashir", state="*")
async def rashir(call: CallbackQuery, state: FSMContext):
    user_id = call.message.chat.id
    await state.finish()
    rm = """    <b>Расширенный</b>
◻️ Подмена номера и голоса

✅ Подключение на 12 месяцев 

✅ Неограниченное количество смен номера

✅ Включен стартовый баланс 2$

✅ Доступна запись звонков

✅ Подмена E-mail адреса 

✅ Подключение тарифа на одном устройстве

✅ Обычный тариф на связь (от 0.05$/мин.)

✅ Шифрование звонка по протоколу SRTP 

✅ Смена голоса на 6 вариантов

✅ Доступ к телефонному спаму 

✅ Можно соединять двух абонентов (Call-back)

❌ Нет возможности отправлять СМС  """


    await call.message.answer(rm, reply_markup=tar_rash_back)

@dp.callback_query_handler(text="tarif", state="*")
async def tarif(call: CallbackQuery, state: FSMContext):
    user_id = call.message.chat.id
    await state.finish()
    with open('tar.webp', 'rb') as photo:
        await bot.send_photo(chat_id=user_id, photo=photo, reply_markup=tariff)

@dp.message_handler(text="📦 Анонимный Файлообменик", state="*")
async def functions_drop(message: types.Message, state: FSMContext):
    URL_TRANSFERSH = 'https://transfer.sh'
    with open('drop.png', 'rb') as photo:
        await bot.send_photo(chat_id=message.chat.id, photo=photo, caption=f"<b>Отравте фаил для получения на него ссылки:</b>")
    @dp.message_handler(content_types=["document"])
    async def download_documents(message: types.Message):
        await message.answer('Идет Загрузка Файла на сервер Ожидайте.....')
        cicada = (f"{message.document.file_name}")
        rr = open('name.txt', 'w')
        rr.write(cicada)
        rr.close()
        await message.document.download(destination=f"{cicada}")
        rrt = open('name.txt', 'r')
        cicada = rrt.read()
        rrt.close()
        with open(cicada, 'rb') as data:
            conf_file = {cicada: data}
            r = requests.post(URL_TRANSFERSH, files=conf_file)
            download_url = r.text[20:]
            ussd = (f'https://transfer.sh/get/{download_url}')
            s = pyshorteners.Shortener()
            pr1 = s.qpsru.short(ussd)
            await message.answer(f"<b>Ваша ссылка для скачивания файла:</b> {pr1}")
            #dellite()

@dp.callback_query_handler(text="proverit", state= "*")
async def send_add_number(call: CallbackQuery, state: FSMContext):
    await state.finish()
    shablon = """
    <code>📱 Ваш номер телефона (любой страны)</code> 
    <code>📱 Номер с которого вам позвонить:</code>"""
    await call.message.answer(
        f"      <b>‼️ Отправь данные так как на шаблоне ‼️</b>\n\n"
        f"<b>‼️ Отправленные даные другим способом ‼️ \n‼️ я расматривать не буду ‼️</b>\n\n"
        f"Перед звонком с выбраного вами номера бот зарание вас Уведомит\n"
        f"Тестовый Звонок длиться до гудка \nне каких просьб о том чтобы сказать что-то\n"
        f"либо написать я не расматриваю так как я не знаю чей номер вы даете\n"
        f"Пример для отправки данных для тестового звонка:\n"
        f"{shablon}")
    await cicada3301.ot_kogo.set()

@dp.message_handler(state=cicada3301.ot_kogo)
async def input_number(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['ot_kogo'] = str(message.text)
    await state.finish()
    zayavka = message.text
    msgsoz = (
        f"ℹ️ <b>Создаза заявка на тестовый звонок</b>\n"
        f"<b>Создал ее</b> 👤 <code>{message.chat.first_name}</code>\n"
        f"<b>Его 🆔</b> <code>{message.chat.id}</code>\n\n"
        f"<code>{zayavka}</code>"
    )
    await bot.send_message(chat_id=sozdatel, text=msgsoz)
    await message.answer('✅ Заявка на тестовый звонок создата и передана на ее расмотрение\n‼️ Тестовые звонки производим толко с 12-00 по 18-00 ‼️')




@dp.message_handler(text="bak", state="*")
async def functions_bak(message: types.Message, state: FSMContext):
    await state.finish()
    await message.answer('Вы вернулись назад! ', reply_markup=check_user_out_func(message.chat.id))


# Обработка кнопки "Общие функции"
@dp.message_handler(IsAdmin(), text="📰 Информация о боте", state="*")
async def general_functions(message: types.Message, state: FSMContext):
    await message.delete()
    await state.finish()
    about_bot = get_about_bot()
    await message.answer(about_bot)


# Обработка кнопки "Управление товарами"
@dp.message_handler(IsAdmin(), text="🔐 Управление  🖍", state="*")
async def general_functions(message: types.Message, state: FSMContext):
    await state.finish()
    await message.delete()
    await message.answer("🔐 Редактирование товаров, разделов и категорий 📜",
                         reply_markup=items_default)


# Получение БД
@dp.message_handler(IsAdmin(), text="/cicada", state="*")
async def general_functions(message: types.Message, state: FSMContext):
    await state.finish()
    for admin in adm:
        with open("data/botBD.sqlite", "rb") as doc:
            await bot.send_document(admin,
                                    doc,
                                    caption=f"<b>📦 BACKUP</b>\n"
                                            f"<code>🕜 {get_dates()}</code>")



def get_about_bot():
    show_profit_all, show_profit_day, show_refill, show_buy_day, show_money_in_bot, show = 0, 0, 0, 0, 0, 0
    get_settings = get_settingsx()
    all_purchases = get_all_purchasesx()
    all_users = get_all_usersx()
    all_refill = get_all_refillx()
    show_users = get_all_usersx()
    show_categories = get_all_categoriesx()
    show_positions = get_all_positionsx()
    show_items = get_all_itemsx()
    for purchase in all_purchases:
        show_profit_all += int(purchase[6])
        if int(get_settings[4]) - int(purchase[14]) < 86400:
            show_profit_day += int(purchase[6])
    for user in all_users:
        show_money_in_bot += int(user[4])
    for refill in all_refill:
        show_refill += int(refill[5])
        if int(get_settings[5]) - int(refill[9]) < 86400:
            show_buy_day += int(refill[5])
    message = "<b>📰 ВСЯ ИНФОРАМЦИЯ О БОТЕ</b>\n" \
              f"➖➖➖➖➖➖➖➖➖➖➖➖➖\n" \
              f"<b>💥 Пользователи: 💥</b>\n" \
              f"👤 Пользователей: <code>{len(show_users)}</code>\n" \
              f"➖➖➖➖➖➖➖➖➖➖➖➖➖\n" \
              f"<b>💥 Средства 💥</b>\n" \
              f"📗 Выдано за 24 часа: <code>{show_profit_day} шт</code>\n" \
              f"📗 Выдано Акаунтов: <code>{show_profit_all} шт</code>\n" \
              f"➖➖➖➖➖➖➖➖➖➖➖➖➖\n" \
              f"<b>💥 Прочее 💥</b>\n" \
              f"🔐 Акаунтов: <code>{len(show_items)}</code>\n" \
              f"📁 Видов: <code>{len(show_positions)}</code>\n" \
              f"📜 Категорий: <code>{len(show_categories)}</code>\n" \

    return message


# Получение списка всех товаров
@dp.message_handler(IsAdmin(), text="/getitems", state="*")
async def get_chat_id(message: types.Message, state: FSMContext):
    await state.finish()
    save_items = []
    count_split = 0
    get_items = get_all_itemsx()
    len_items = len(get_items)
    if len_items >= 1:
        await message.answer("<b>🔐 Все Акаунты</b>\n"
                             "➖➖➖➖➖➖➖➖➖➖➖➖➖\n"
                             "<code>📍 айди Акаунта - данные Акаунтов</code>\n"
                             "➖➖➖➖➖➖➖➖➖➖➖➖➖\n")
        for item in get_items:
            save_items.append(f"<code>📍 {item[1]} - {item[2]}</code>")
        if len_items >= 20:
            count_split = round(len_items / 20)
            count_split = len_items // count_split
        if count_split > 1:
            get_message = split_messages(save_items, count_split)
            for msg in get_message:
                send_message = "\n".join(msg)
                await message.answer(send_message)
        else:
            send_message = "\n".join(save_items)
            await message.answer(send_message)
    else:
        await message.answer("<b>🔐 Акаунты отсутствуют</b>")


# Получение списка всех позиций
@dp.message_handler(IsAdmin(), text="/getposition", state="*")
async def get_chat_id(message: types.Message, state: FSMContext):
    await state.finish()
    save_items = []
    count_split = 0
    get_items = get_all_positionsx()
    len_items = len(get_items)
    if len_items >= 1:
        await message.answer("<b>📁 Все позиции</b>\n➖➖➖➖➖➖➖➖➖➖➖➖➖\n")
        for item in get_items:
            save_items.append(f"<code>{item[2]}</code>")
        if len_items >= 35:
            count_split = round(len_items / 35)
            count_split = len_items // count_split
        if count_split > 1:
            get_message = split_messages(save_items, count_split)
            for msg in get_message:
                send_message = "\n".join(msg)
                await message.answer(send_message)
        else:
            send_message = "\n".join(save_items)
            await message.answer(send_message)
    else:
        await message.answer("<b>📁 Позиции отсутствуют</b>")


# Получение подробного списка всех товаров
@dp.message_handler(IsAdmin(), text="/getinfoitems", state="*")
async def get_chat_id(message: types.Message, state: FSMContext):
    await state.finish()
    save_items = []
    count_split = 0
    get_items = get_all_itemsx()
    len_items = len(get_items)
    if len_items >= 1:
        await message.answer("<b>🔐 Все Акаунты и их позиции</b>\n"
                             "➖➖➖➖➖➖➖➖➖➖➖➖➖\n")
        for item in get_items:
            get_position = get_positionx("*", position_id=item[3])
            save_items.append(f"<code>{get_position[2]} - {item[2]}</code>")
        if len_items >= 20:
            count_split = round(len_items / 20)
            count_split = len_items // count_split
        if count_split > 1:
            get_message = split_messages(save_items, count_split)
            for msg in get_message:
                send_message = "\n".join(msg)
                await message.answer(send_message)
        else:
            send_message = "\n".join(save_items)
            await message.answer(send_message)
    else:
        await message.answer("<b>🔐 Акаунты отсутствуют</b>")
