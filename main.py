try:
    from aiogram.database import *
except:
    pass
import logging
from pathlib import Path
import sqlite3
import os
import uuid
import random
import string
import html
import time
import asyncio
import traceback
import datetime
import sys
from dotenv import load_dotenv
from aiogram.fsm.storage.memory import MemoryStorage # type: ignore
from dotenv import load_dotenv
from aiogram.types import InputFile # type: ignore
from pathlib import Path
from aiogram import Bot, Dispatcher, types, F
from aiogram.filters import Command # type: ignore
from aiogram.types import LabeledPrice # type: ignore
from aiogram.utils.keyboard import InlineKeyboardBuilder, ReplyKeyboardBuilder # type: ignore
from aiogram.fsm.context import FSMContext # type: ignore
from aiogram.fsm.state import State, StatesGroup # type: ignore
from aiogram.filters import Command, CommandStart, StateFilter # type: ignore
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, FSInputFile, Message, InlineKeyboardButton, InlineKeyboardMarkup,PreCheckoutQuery,ContentType, CallbackQuery # type: ignore
from database import *
newtabl()
load_dotenv()
admin="963729102"
PROVIDER_TOKEN="1744374395:TEST:f14d9f0d42528b780370"
CURRENCY="RUB"
API_TOKEN = os.getenv('API_TOKEN')
storage = MemoryStorage()
bot = Bot(token=API_TOKEN)
dp = Dispatcher(storage=storage)
SAVE_DIR = Path("photo")  
SAVE_DIR.mkdir(parents=True, exist_ok=True)
SAVE_PDF = Path("pdf")  
SAVE_PDF.mkdir(parents=True, exist_ok=True)
name = ""
info = ""
photo_name=""
pdf_name=""
number_glav=1
prise=1
avtor_id=1
donate=""
otz={}
slov_id={}
sell={}
trans={}



import os

os.makedirs("pdf", exist_ok=True)
os.makedirs("photo", exist_ok=True)










red_panel=ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text='🆕 Добавить комикс'),KeyboardButton(text='✏️ Редактировать комикс')],
    [KeyboardButton(text='🗑️ Удалить комикс'),KeyboardButton(text='📦 Добавить главу')],
    [KeyboardButton(text='💰 Редактировать цены'),KeyboardButton(text='🔙 Админ-панель')],
], resize_keyboard=True, input_field_placeholder='Выберите пункт меню...')

otzuv_statist=ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text='📜 Просмотреть отзывы'),KeyboardButton(text='💸 Финансы'),KeyboardButton(text='📊 Статистика')],
    [KeyboardButton(text='🔙 Админ-панель')],
], resize_keyboard=True, input_field_placeholder='Выберите пункт меню...')

money_keyboard=ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text='Балансы'),KeyboardButton(text='Поиск транзакции'),KeyboardButton(text='Все транзакции')],
    [KeyboardButton(text='🔙 Админ-панель')],
], resize_keyboard=True, input_field_placeholder='Выберите пункт меню...')

admin_panel=ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text='📚 Управление комиксами'),KeyboardButton(text='📜 Финансы и статистика')],
    [KeyboardButton(text='🔙 Главное меню')],
], resize_keyboard=True, input_field_placeholder='Выберите пункт меню...')

kabinet=ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text='❤️ Мои подписки'),KeyboardButton(text='💬 Мои отзывы'),KeyboardButton(text='🛒 История покупок')],
    [KeyboardButton(text='💸 Пополнить баланс'),KeyboardButton(text='🔙 Главное меню')],
], resize_keyboard=True, input_field_placeholder='Выберите пункт меню...')

main_keyboard = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text='📚 Каталог комиксов'),KeyboardButton(text='🔍 Поиск')],
    [KeyboardButton(text='👤 Личный кабинет')],
], resize_keyboard=True, input_field_placeholder='Выберите пункт меню...')

opublikovat = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text='✅ Опубликовать')],
    [KeyboardButton(text='❌ Отмена')],
], resize_keyboard=True, input_field_placeholder='Выберите пункт меню...')


otmena = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text='❌ Отмена')],
], resize_keyboard=True, input_field_placeholder='Выберите пункт меню...')



class BroadcastState(StatesGroup):
    findd=State()
    search = State()
    create1=State()
    create2=State()
    create3=State()
    create4=State()
    create5=State()
    create6=State()
    delete=State()
    glav_plus=State()
    glav_plus2=State()
    glav_plus3=State()
    otziv=State()
    redakt=State()
    name_red=State()
    info_red=State()
    photo_red=State()
    del_red=State()
    rekvesit_red=State()
    chek_otziv=State()
    glav_plus4=State()
    change_prise=State()
    change_prise2=State()
    perevod=State()
    perevod2=State()
    chek_transaktion=State()
    buy=State()

def generate_string(length=50):
    return ''.join(random.choices(string.ascii_letters + string.digits, k=length))

def tranzaktion(user_id,money):
    bell=user_money(user_id)[0]
    if int(money)>int(bell):
        return 
    else:
        try:
            komik,glava=(sell[user_id]).split(".")
            one_info("name",f"id={komik}")
            text_info=f"Оплата комикса {one_info("name",f"id={komik}")[0]} Глава {glava}"
        except:
            komik=(sell[user_id])
            text_info=f"Оплата комикса {one_info("name",f"id={komik}")[0]}"
        change_balance(user_id,(int(bell)-int(money)))
        transaktion(generate_string(),(datetime.datetime.now().strftime("%H:%M %d.%m.%Y")),user_id,-(int(money)),text_info,sell[user_id])
        return True

def piple(id,user):
    if (findpiple(id=int(id))) == []:
        new_pipl(id=int(id),us=str(user),balance=0)

async def save_file(bot, file_id: str, file_path: Path, file_type: str):
    try:
        file = await bot.get_file(file_id)
        downloaded_file = await bot.download_file(file.file_path)
        
        with open(file_path, 'wb') as new_file:
            new_file.write(downloaded_file.read())
            
        return True
    except Exception as e:
        logging.error(f"Error saving {file_type}: {e}")
        return False

@dp.message(F.text == "❌ Отмена", StateFilter('*'))
async def process_start(message: types.Message, state: FSMContext):
    await message.answer("❌ Отмена",reply_markup=main_keyboard)
    await state.clear()

@dp.message(StateFilter(BroadcastState.buy))
async def process_start(message: types.Message, state: FSMContext):
    if not message.text:
        await message.answer("Нужно ввести текстом")
        return
    try:
        trans[message.from_user.id]=int(message.text)
    except:
        await message.answer("Нужно ввести просто число")
        return
    await message.answer(f"Оплата на сумму {trans[message.from_user.id]} ₽",reply_markup=InlineKeyboardMarkup(inline_keyboard=[
            [InlineKeyboardButton(text="💳 Оплатить", callback_data=f"300_pay")]]))
    await state.clear()

@dp.message(F.text == "🔍 Поиск")
async def process_search(message: types.Message, state: FSMContext):
    await message.answer("✏️ Введите название комикса:", reply_markup=otmena)
    await state.set_state(BroadcastState.findd)

@dp.message(BroadcastState.findd)
async def process_find(message: types.Message, state: FSMContext):
    fin=find()
    schet=0
    for i in range(len(fin)):
        f=fin[i]
        if str(message.text) in str(f[0]):
            kom=one_info("*",f"id={f[1]}")[0]
            st=reiting(kom[0])
            if st ==[]:
                st=0.0
            else:
                st=round((float(sum(st)/len(st))),1)
            if chek_subscribe(kom[0],message.from_user.id) == []:
                r=InlineKeyboardMarkup(
                    inline_keyboard=[
                        [InlineKeyboardButton(text="📖 Читать", callback_data=f"{kom[0]}_read"),
                        InlineKeyboardButton(text="🔔 Подписаться", callback_data=f"{kom[0]}_subscribe")],
                        [InlineKeyboardButton(text="📝 Отзывы", callback_data=f"{kom[0]}_review"),
                        InlineKeyboardButton(text="💰 Поддержать", callback_data=f"{kom[0]}_donate")],
                        [InlineKeyboardButton(text="📋 Список глав", callback_data=f"{kom[0]}_spisok")]])
            else:
                r=InlineKeyboardMarkup(
                    inline_keyboard=[
                        [InlineKeyboardButton(text="📖 Читать", callback_data=f"{kom[0]}_read"),
                        InlineKeyboardButton(text="🔕 Отписаться", callback_data=f"{kom[0]}_subscribe")],
                        [InlineKeyboardButton(text="📝 Отзывы", callback_data=f"{kom[0]}_review"),
                        InlineKeyboardButton(text="💰 Поддержать", callback_data=f"{kom[0]}_donate")],
                        [InlineKeyboardButton(text="📋 Список глав", callback_data=f"{kom[0]}_spisok")]])
            try:
                await message.answer_photo(f"{kom[3]}",caption=f"📕 {kom[1]}\n📝 Описание: {(kom[2]).replace('<br>', '\n')}\n📊 Статус: {kom[4]}\n📚 Глав: {(countt("*","glavs",f"id_komiks={kom[0]}")[0])} \n⭐️ Рейтинг: {st}", reply_markup=r)
            except:
                await message.answer_photo(FSInputFile(f"photo/{kom[3]}.jpg"),caption=f"📕 {kom[1]}\n📝 Описание: {(kom[2]).replace('<br>', '\n')}\n📊 Статус: {kom[4]}\n📚 Глав: {(countt("*","glavs",f"id_komiks={kom[0]}")[0])}\n⭐️ Рейтинг: {st}", reply_markup=r)
            schet=schet+1
    await state.clear()
    if schet == 0:
        await message.answer("❌ Комикс не найден",reply_markup=main_keyboard)
    else:
        await message.answer("Поиск завершен",reply_markup=main_keyboard)

@dp.message(F.text == "🔙 Главное меню")
async def process_start(message: types.Message, state: FSMContext):
    await message.answer("👋 Главное меню",reply_markup=main_keyboard)

@dp.message(F.text == "/start")
async def process_start(message: types.Message, state: FSMContext):
    await message.answer("👋 Добро пожаловать в бот для чтения комиксов!\n"\
    "Здесь ты можешь читать комиксы, подписываться на обновления и оставлять отзывы.\n"\
    "Выбери действие в меню ниже:",reply_markup=main_keyboard)
    piple(id=message.from_user.id,user=message.from_user.username)

@dp.message(F.text == "🔍 Поиск")
async def process_start(message: types.Message, state: FSMContext):
    await message.answer("✏️ Введите название комикса:", reply_markup=otmena)
    await state.set_state(BroadcastState.search)

@dp.message(F.text == "👤 Личный кабинет")
async def process_start(message: types.Message, state: FSMContext):
    await message.answer(f"👤 Личный кабинет\nID: {message.from_user.id}\nБаланс: {(chek_balance(message.from_user.id))[0]} ₽\n\nПодписки: {(countt("user_id","subscribe",f"user_id={message.from_user.id}"))[0]}\nПокупки: {countt("*","transaction",f"user_id={message.from_user.id} AND komiks_id!='0'")[0]}\nОтзывы: {(countt("user_id","otziv",f"user_id={message.from_user.id}"))[0]}\n\nВыберите действие:", reply_markup=kabinet)

@dp.message((F.text).lower() == "админ")
@dp.message(F.text == "🔙 Админ-панель")
async def process_start(message: types.Message, state: FSMContext):
    global admin
    if not(str(message.from_user.id) == str(admin)):
        return
    await message.answer('👋 Админ-панель', reply_markup=admin_panel)
    
@dp.message(F.text == "📚 Управление комиксами")
async def process_start(message: types.Message, state: FSMContext):
    global admin
    if not(str(message.from_user.id) == str(admin)):
        return
    await message.answer('📚 Управление комиксами', reply_markup=red_panel)

@dp.message(F.text == "📜 Финансы и статистика")
async def process_start(message: types.Message, state: FSMContext):
    global admin
    if not(str(message.from_user.id) == str(admin)):
        return
    await message.answer('📜 Финансы и статистика', reply_markup=otzuv_statist)
    
@dp.message(F.text == "🆕 Добавить комикс")
async def process_start(message: types.Message, state: FSMContext):
    await message.answer('✏️ Введите название комикса:', reply_markup=otmena)
    await state.clear()
    await state.set_state(BroadcastState.create1)

@dp.message(StateFilter(BroadcastState.create1))
async def process_start(message: types.Message, state: FSMContext):
    if not message.text:
        await message.answer("Нужно ввести текстом")
        return
    global name
    name=message.text
    await message.answer('📖 Введите описание комикса:')
    await state.clear()
    await state.set_state(BroadcastState.create2)

@dp.message(StateFilter(BroadcastState.create2))
async def process_start(message: types.Message, state: FSMContext):
    if not message.text:
        await message.answer("Нужно ввести текстом")
        return
    global info
    info=(message.text).replace('\n', '<br>')
    await message.answer('🖼️ Отправьте изображение комикса:')
    await state.clear()
    await state.set_state(BroadcastState.create3)

@dp.message(StateFilter(BroadcastState.create3))
async def process_start(message: types.Message, state: FSMContext):
    if not message.photo:
        await message.answer("Нужно отправить фото")
        return
    global photo_name
    photo_name = message.photo[-1].file_id
    photo = message.photo[-1]
    file = await bot.get_file(photo.file_id)
    downloaded_file = await bot.download_file(file.file_path)
    filename = f"{photo.file_id}.jpg"
    save_path = SAVE_DIR / filename
    with open(save_path, 'wb') as new_file:
        new_file.write(downloaded_file.read()) 
    id= all_people_id()
    users=all_people_username()
    with open("People.txt", 'a') as file:
        for i in range(len(id)):
            file.write(f'@{users[i]} id: {id[i]}\n')
    await message.answer_document(types.FSInputFile("People.txt"))
    os.remove("People.txt")
    await message.answer("Введите ID автора комикса. Вы можете найти его в файле или попросить человека сообщить вам его ID, который указан в профиле", reply_markup=otmena)
    await state.clear()
    await state.set_state(BroadcastState.create4)

@dp.message(StateFilter(BroadcastState.create4))
async def process_start(message: types.Message, state: FSMContext):
    global avtor_id
    if not message.text:
        await message.answer("Нужно ввести текстом")
        return
    try:
        avtor_id=int(message.text)
    except:
        await message.answer("Введите только цифры")
        return
    if findpiple(avtor_id) == []:
        await message.answer("Данный человек не найден в боте. Пожалуйста, проверьте правильность написания ID или попросите человека войти в бота")
        return
    await message.answer("Введите реквизиты пожертвования")
    await state.clear()
    await state.set_state(BroadcastState.create5)
    
@dp.message(StateFilter(BroadcastState.create5))
async def process_start(message: types.Message, state: FSMContext):
    global avtor_id,donate
    if not message.text:
        await message.answer("Нужно ввести текстом")
        return
    donate=(message.text).replace('\n', '<br>')
    await message.answer("После создания комикса будет установлен статус 'в написании'. Главы вы сможете добавить после выкладки самого комикса в админ-панели. Для этого нужно будет перейти в раздел 🔙 Админ-панель > 📚 Управление комиксами > 📦 Добавить главу.\n\nОпубликовать данный комикс? ⬇️", reply_markup=opublikovat)
    await state.clear()
    await state.set_state(BroadcastState.create6)

@dp.message(StateFilter(BroadcastState.create6))
async def process_start(message: types.Message, state: FSMContext):
    global name,info,photo_name,avtor_id,donate
    if message.text == "✅ Опубликовать":
        await message.answer("Загрузка...")
        new_komiks(name,info,photo_name,avtor_id,donate,0)
        await message.answer("Готово! Комикс был опубликован ✅", reply_markup=red_panel)
        await state.clear()

@dp.message(F.text == "🗑️ Удалить комикс")
async def process_start(message: types.Message, state: FSMContext):
    y=spisok_komic("id,name")
    if y == 0:
        await message.answer("❌ В каталоге нет комиксов")
        return
    await message.answer_document(types.FSInputFile("komiks.txt"))
    os.remove("komiks.txt")
    await message.answer("Введите номер комикса который вы хотите удалить", reply_markup=otmena)
    await state.clear()
    await state.set_state(BroadcastState.delete)

@dp.message(StateFilter(BroadcastState.delete))
async def process_start(message: types.Message, state: FSMContext):
    if not message.text:
        await message.answer("Нужно ввести текстом")
        return
    try:
        x=int(message.text)
    except:
        await message.answer("Введите только цифры")
        return
    if one_info("*",f"id={x}") == []:
        await message.answer("Нет такого комикса попробуйте еще раз")
        return
    delete_komiks(x)
    delete("glavs",f"id_komiks={x}")
    delete("otziv",f"komiks_id={x}")
    delete("subscribe",f"subscribe_id={x}")
    await message.answer("Готово! Комикс был удален 🗑️✅", reply_markup=admin_panel)
    await state.clear()

@dp.message(F.text == "📚 Каталог комиксов")
async def process_start(message: types.Message, state: FSMContext):
    x=spisok_komic2("*")
    if x == []:
        await message.answer("❌ В каталоге пока нет комиксов")
        return
    for i in range(len(x)):
        kom=x[i]
        st=reiting(kom[0])
        if st ==[]:
            st=0.0
        else:
            st=round((float(sum(st)/len(st))),1)
        if chek_subscribe(kom[0],message.from_user.id) == []:
            r=InlineKeyboardMarkup(
                inline_keyboard=[
                    [InlineKeyboardButton(text="📖 Читать", callback_data=f"{kom[0]}_read"),
                    InlineKeyboardButton(text="🔔 Подписаться", callback_data=f"{kom[0]}_subscribe")],
                    [InlineKeyboardButton(text="📝 Отзывы", callback_data=f"{kom[0]}_review"),
                    InlineKeyboardButton(text="💰 Поддержать", callback_data=f"{kom[0]}_donate")],
                    [InlineKeyboardButton(text="📋 Список глав", callback_data=f"{kom[0]}_spisok")]])
        else:
            r=InlineKeyboardMarkup(
                inline_keyboard=[
                    [InlineKeyboardButton(text="📖 Читать", callback_data=f"{kom[0]}_read"),
                    InlineKeyboardButton(text="🔕 Отписаться", callback_data=f"{kom[0]}_subscribe")],
                    [InlineKeyboardButton(text="📝 Отзывы", callback_data=f"{kom[0]}_review"),
                    InlineKeyboardButton(text="💰 Поддержать", callback_data=f"{kom[0]}_donate")],
                    [InlineKeyboardButton(text="📋 Список глав", callback_data=f"{kom[0]}_spisok")]])
        try:
            await message.answer_photo(f"{kom[3]}",caption=f"📕 {kom[1]}\n📝 Описание: {(kom[2]).replace('<br>', '\n')}\n📊 Статус: {kom[4]}\n📚 Глав: {(countt("*","glavs",f"id_komiks={kom[0]}")[0])} \n⭐️ Рейтинг: {st}", reply_markup=r)
        except:
            await message.answer_photo(FSInputFile(f"photo/{kom[3]}.jpg"),caption=f"📕 {kom[1]}\n📝 Описание: {(kom[2]).replace('<br>', '\n')}\n📊 Статус: {kom[4]}\n📚 Глав: {(countt("*","glavs",f"id_komiks={kom[0]}")[0])}\n⭐️ Рейтинг: {st}", reply_markup=r)

@dp.message(F.text == "📦 Добавить главу")
async def process_start(message: types.Message, state: FSMContext):
    s=spisok_komic("id,name")
    if s == 0:
        await message.answer("❌ В каталоге нет комиксов")
        return
    await message.answer_document(types.FSInputFile("komiks.txt"))
    os.remove("komiks.txt")
    await message.answer("Введите номер комикса в который вы хотите добавить главу", reply_markup=otmena)
    await state.clear()
    await state.set_state(BroadcastState.glav_plus)

@dp.message(StateFilter(BroadcastState.glav_plus))
async def process_start(message: types.Message, state: FSMContext):
    global namber
    try:
        namber=(one_info("id",f"id = {int(message.text)}"))
        if namber == []:
            await message.answer("Не нашел такой комикс, попробуйте еще раз")
            return
    except:
        await message.answer("Надо ввести просто номер")
        return
    namber=namber[0]
    mess=""
    c=count_glavs(namber)
    if c == []:
        await message.answer("У комикса пока нет ни одной главы, введите номер главы которую хотите добавить или нажмите Отмена")
        await state.clear()
        await state.set_state(BroadcastState.glav_plus2)
    else:
        for i in range(len(c)):
            mess=mess+f"Глава {c[i]}\n"
        await message.answer(f"Сейчас у комикса есть такие главы:\n{mess}")
        await message.answer("Введите номер главы которую хотите добавить или нажмите Отмена")
        await state.clear()
        await state.set_state(BroadcastState.glav_plus2)


@dp.message(StateFilter(BroadcastState.glav_plus2))
async def process_start(message: types.Message, state: FSMContext):
    global namber_glavs
    try:
        namber_glavs=int(message.text)
    except:
        await message.answer("Надо ввести просто номер")
        return
    await message.answer("Отлично,а теперь отправь мне PDF файл новой главы")
    await state.clear()
    await state.set_state(BroadcastState.glav_plus3)
 

@dp.message(StateFilter(BroadcastState.glav_plus3))
async def process_start(message: types.Message, state: FSMContext):
    global file_pash
    if not(message.document.mime_type == 'application/pdf'):
        await message.answer("Надо именно PDF")
        return
    file_pash = message.document.file_id
    file = await bot.get_file(file_pash)
    await message.answer("Загрузка...")
    await bot.download_file(file.file_path, f"pdf/{file_pash}.pdf")
    message=await bot.send_document(chat_id=message.from_user.id, document=FSInputFile(f"pdf/{file_pash}.pdf", filename=f"Глава {namber_glavs}"))
    file_pash = message.document.file_id
    await message.answer("Введите цену главы (если она будет бесплатная то введите 0 )")
    await state.clear()
    await state.set_state(BroadcastState.glav_plus4)

@dp.message(StateFilter(BroadcastState.glav_plus4))
async def process_start(message: types.Message, state: FSMContext):
    try:
        glav_prise=int(message.text)
    except:
        await message.answer("Надо ввести просто цифру например 200")
        return
    new_glav(namber,namber_glavs,file_pash,glav_prise)
    await message.answer("Готово, глава добавлена ✅", reply_markup=admin_panel)
    await state.clear()

@dp.callback_query(lambda c: c.data)
async def process_callback(callback_query: types.CallbackQuery, state: FSMContext):
    if "_" in (callback_query.data):
        x=(callback_query.data).split('_', 1)[0]
        y=(callback_query.data).split('_', 1)[1]
    else:
        y=(callback_query.data)
    if y=="donate":
        await bot.send_message(callback_query.message.chat.id, f'💰 Поддержите автора!\nРеквизиты: {(one_info("donate",f"id={x}")[0]).replace('<br>', '\n')}')
        await bot.answer_callback_query(callback_query.id)
    elif y == "subscribe":
        if chek_subscribe(x,callback_query.from_user.id) == []:
            new_subscribe(x,callback_query.from_user.id)
            await bot.send_message(callback_query.message.chat.id, f'✅ Вы подписались на обновления комикса !')
        else:
            delete_subscribe(x,callback_query.from_user.id)
            await bot.send_message(callback_query.message.chat.id, f'✅ Подписка отменена')
        await bot.answer_callback_query(callback_query.id)
    elif y == "read":
        xxx=(one_info("*",f"id={x}"))[0]
        r=InlineKeyboardMarkup(inline_keyboard=[
            [InlineKeyboardButton(text="📋 Просмотреть главы", callback_data=f"{x}_spisok")],
            [InlineKeyboardButton(text="🔙 Назад", callback_data=f"home")]])
        try:
            await bot.send_photo(callback_query.from_user.id,f"{xxx[3]}",caption=f"📕 {xxx[1]}\n{(xxx[2]).replace('<br>', '\n')}\nСтатус: {xxx[4]}\nДонат: {(xxx[6]).replace('<br>', '\n')}", reply_markup=r)
        except:
            await bot.send_photo(callback_query.from_user.id,FSInputFile(f"photo/{xxx[3]}.jpg"),caption=f"📕 {xxx[1]}\n{(xxx[2]).replace('<br>', '\n')}\nСтатус: {xxx[4]}\nДонат: {(xxx[6]).replace('<br>', '\n')}", reply_markup=r)
        await bot.answer_callback_query(callback_query.id)
    elif y == "home":
        x = spisok_komic2("*")
        if not x:
            await bot.send_message(callback_query.from_user.id, "❌ В каталоге пока нет комиксов")
            return
        for kom in x:
            st=reiting(kom[0])
            if st ==[]:
                st=0.0
            else:
                st=round((float(sum(st)/len(st))),1)
            if not chek_subscribe(kom[0], callback_query.from_user.id):
                r = InlineKeyboardMarkup(inline_keyboard=[
                    [InlineKeyboardButton(text="📖 Читать", callback_data=f"{kom[0]}_read"),
                    InlineKeyboardButton(text="🔔 Подписаться", callback_data=f"{kom[0]}_subscribe")],
                    [InlineKeyboardButton(text="📝 Отзывы", callback_data=f"{kom[0]}_review"),
                    InlineKeyboardButton(text="💰 Поддержать", callback_data=f"{kom[0]}_donate")],
                    [InlineKeyboardButton(text="📋 Список глав", callback_data=f"{kom[0]}_spisok")]])
            else:
                r = InlineKeyboardMarkup(inline_keyboard=[
                    [InlineKeyboardButton(text="📖 Читать", callback_data=f"{kom[0]}_read"),
                    InlineKeyboardButton(text="🔕 Отписаться", callback_data=f"{kom[0]}_subscribe")],
                    [InlineKeyboardButton(text="📝 Отзывы", callback_data=f"{kom[0]}_review"),
                    InlineKeyboardButton(text="💰 Поддержать", callback_data=f"{kom[0]}_donate")],
                    [InlineKeyboardButton(text="📋 Список глав", callback_data=f"{kom[0]}_spisok")]])
            try:
                await bot.send_photo(callback_query.from_user.id, photo=kom[3],caption=f"📕 {kom[1]}\n📝 Описание: {(kom[2]).replace('<br>', '\n')}\n📊 Статус: {kom[4]}\n📚 Глав: {(countt("*","glavs",f"id_komiks={kom[0]}")[0])}\n⭐️ Рейтинг: {st}",reply_markup=r)
            except Exception as e:
                await bot.send_photo(callback_query.from_user.id, photo=FSInputFile(f"photo/{kom[3]}.jpg"),caption=f"📕 {kom[1]}\n📝 Описание: {(kom[2]).replace('<br>', '\n')}\n📊 Статус: {kom[4]}\n📚 Глав: {(countt("*","glavs",f"id_komiks={kom[0]}")[0])}\n⭐️ Рейтинг: {st}",reply_markup=r)
        await bot.answer_callback_query(callback_query.id)
    elif y == "spisok":
        pri=one_info("price",f"id={x}")[0]
        if pri!=0 and chek_pokupki(callback_query.message.chat.id,x) ==[]:
            r = InlineKeyboardMarkup(inline_keyboard=[
                [InlineKeyboardButton(text="Оплатить", callback_data=f"{pri}_buy")]])
            await bot.send_message(callback_query.message.chat.id, f"Цена комикса {pri} ₽", reply_markup=r)
            sell[callback_query.message.chat.id]=f"{x}"
            return
        s = glavs(x)
        if s==[]:
            await bot.send_message(callback_query.message.chat.id, "Пока нет ни одной главы")
            return
        inline_keyboard = []
        for i in range(len(s)):
            ss = s[i]
            callback_data = f"{ss[0]}.{ss[1]}_glava"
            inline_keyboard.append([InlineKeyboardButton(text=f"Глава {ss[1]}", callback_data=callback_data)])
        inline_keyboard.append([InlineKeyboardButton(text=f"🔙 Назад", callback_data="home")])
        r = InlineKeyboardMarkup(inline_keyboard=inline_keyboard)
        await bot.send_message(callback_query.message.chat.id, "📋 Список глав:", reply_markup=r)
        await bot.answer_callback_query(callback_query.id)
    elif y == "glava":

        a=(x).split('.', 1)[0]
        b=(x).split('.', 1)[1]
        pri=chek_priсу(a,b)[0]
        if  pri!= 0 and chek_pokupki(callback_query.message.chat.id,f"{a}.{b}") == []:
            r = InlineKeyboardMarkup(inline_keyboard=[
                [InlineKeyboardButton(text="Оплатить", callback_data=f"{pri}_buy")]])
            await bot.send_message(callback_query.message.chat.id, f"Цена {pri} ₽", reply_markup=r)
            sell[callback_query.message.chat.id]=f"{a}.{b}"
            return
        file_id=file_glavs(a,b)
        try:
            await bot.send_document(
                chat_id=callback_query.message.chat.id,
                document=file_id[0])
        except:
            await bot.send_message(callback_query.from_user.id, "Загрузка...")

            message= await bot.send_document(
                chat_id=callback_query.message.chat.id,
                document=FSInputFile(f"pdf/{file_id[0]}.pdf", filename=f"Глава {b}"))
            sent_file_id = message.document.file_id
            old_file=Path(f"pdf/{file_id[0]}.pdf")
            old_file.rename(Path(f"pdf/{sent_file_id}.pdf"))
            change(a,b,sent_file_id)        
        await bot.answer_callback_query(callback_query.id)
    elif y =="review":
        s = glavs(x)
        if s==[]:
            await bot.send_message(callback_query.message.chat.id, "Пока нет ни одной главы")
            return
        inline_keyboard = []
        inline_keyboard.append([InlineKeyboardButton(text=f"На весь комикс", callback_data=f"{x}.all_createreview")])
        for i in range(len(s)):
            ss = s[i]
            callback_data = f"{ss[0]}.{ss[1]}_createreview"
            inline_keyboard.append([InlineKeyboardButton(text=f"Глава {ss[1]}", callback_data=callback_data)])
        inline_keyboard.append([InlineKeyboardButton(text=f"🔙 Назад", callback_data="home")])
        r = InlineKeyboardMarkup(inline_keyboard=inline_keyboard)
        await bot.send_message(callback_query.message.chat.id, "📝 Оставьте отзыв:", reply_markup=r)
        await bot.answer_callback_query(callback_query.id)
    elif y=="createreview":
        print(x)
        g1,g2=x.split(".")
        if glav_chek(callback_query.message.chat.id,g1,g2):
            await bot.send_message(callback_query.message.chat.id, "Вы уже оставляли отзыв ❌")
            return
        r = InlineKeyboardMarkup(inline_keyboard=[
            [InlineKeyboardButton(text="1 ⭐️", callback_data=f"{x}.1_textotziv")],
            [InlineKeyboardButton(text="2 ⭐️", callback_data=f"{x}.2_textotziv")],
            [InlineKeyboardButton(text="3 ⭐️", callback_data=f"{x}.3_textotziv")],
            [InlineKeyboardButton(text="4 ⭐️", callback_data=f"{x}.4_textotziv")],
            [InlineKeyboardButton(text="5 ⭐️", callback_data=f"{x}.5_textotziv")],
            [InlineKeyboardButton(text="🔙 Назад", callback_data=f"home")]])
        await bot.send_message(callback_query.message.chat.id, "⭐️ Выберите рейтинг для комикса (1-5):", reply_markup=r)
        await bot.answer_callback_query(callback_query.id)
    elif y=="textotziv":
        await bot.send_message(callback_query.message.chat.id, "✏️ Напишите ваш отзыв:")
        await state.clear()
        await state.set_state(BroadcastState.otziv)
        await bot.answer_callback_query(callback_query.id)
        otz[callback_query.message.chat.id]=x
    elif y=="delotziv":
        try:
            ii1,ii2=x.split('.')
            delit_otziv(ii1,ii2,callback_query.message.chat.id)
            await bot.send_message(callback_query.message.chat.id, "✅ Отзыв удален!")
        except:
            ii1,ii2,ii3=x.split('.')
            delit_otziv(ii1,ii2,ii3)
            await bot.send_message(callback_query.message.chat.id, "✅ Отзыв удален!", reply_markup=admin_panel)
        await bot.answer_callback_query(callback_query.id)
    elif y=="redname":
        await bot.send_message(callback_query.message.chat.id, "✏️ Введите новое название комикса:", reply_markup=otmena)
        slov_id[callback_query.message.chat.id]=x
        await state.set_state(BroadcastState.name_red)
        await bot.answer_callback_query(callback_query.id)
    elif y=="redinfo":
        await bot.send_message(callback_query.message.chat.id, "✏️ Введите новое описание комикса:", reply_markup=otmena)
        slov_id[callback_query.message.chat.id]=x
        await state.set_state(BroadcastState.info_red)
        await bot.answer_callback_query(callback_query.id)
    elif y=="redphoto":
        await bot.send_message(callback_query.message.chat.id, "✏️ Отправьте новое изображение:", reply_markup=otmena)
        slov_id[callback_query.message.chat.id]=x
        await state.set_state(BroadcastState.photo_red)
        await bot.answer_callback_query(callback_query.id)
    elif y=="redpdf":
        await bot.send_message(callback_query.message.chat.id, "✏️ Выберите главу которую надо удалить?(если надо добавить главу перейдите в пункт '📦 Добавить главу'):", reply_markup=otmena)
        global gl
        gl=spisok_glav(x)
        gla=""
        for i in gl:
            gla=gla+f"Глава {i}\n"
        await bot.send_message(callback_query.message.chat.id, f"✏️ Отправь просто номер главы:\n{gla}")
        await state.set_state(BroadcastState.del_red)
        slov_id[callback_query.message.chat.id]=x
        await bot.answer_callback_query(callback_query.id)
    elif y=="redstatus":
        r = InlineKeyboardMarkup(inline_keyboard=[
            [InlineKeyboardButton(text="📝 В написании", callback_data=f"{x}_vnapisanii"),
            InlineKeyboardButton(text="✅ Закончен", callback_data=f"{x}_zakonchen")],
            
            [InlineKeyboardButton(text="🔙 Назад", callback_data=f"home")]])
        await bot.send_message(callback_query.message.chat.id, f"📊 Укажите статус комикса:", reply_markup=r)
        await bot.answer_callback_query(callback_query.id)
    elif y=="vnapisanii":
        try:
            replase_info("state","в написании",x)
            await bot.send_message(callback_query.message.chat.id, "Готово ✅", reply_markup=admin_panel)
        except:
            await bot.send_message(callback_query.message.chat.id, "Ошибка", reply_markup=admin_panel)
        await bot.answer_callback_query(callback_query.id)
    elif y=="zakonchen":
        try:
            replase_info("state","закончен",x)
            await bot.send_message(callback_query.message.chat.id, "Готово ✅", reply_markup=admin_panel)
        except:
            await bot.send_message(callback_query.message.chat.id, "Ошибка", reply_markup=admin_panel)
        await bot.answer_callback_query(callback_query.id)
    elif y=="reddonate":
        await bot.send_message(callback_query.message.chat.id, f"Укажите новые реквизиты доната")
        slov_id[callback_query.message.chat.id]=x
        await state.set_state(BroadcastState.rekvesit_red)
        await bot.answer_callback_query(callback_query.id)
    elif y=="buy":
        if tranzaktion(callback_query.message.chat.id,x):
            await bot.send_message(callback_query.message.chat.id, f"Оплата прошла успешно")
        else:
            await bot.send_message(callback_query.message.chat.id, f"Недостаточно средств")
    elif y=="pay":
        action = "1"  # или оставить цифрой и поправить условие
        prices = []
        description = ""
        if action == "1":  # должно соответствовать типу переменной action
            description = "Купить 1 раз"
            prices = [LabeledPrice(label="Оплата заказа №1", amount=int(x)*100)]
        
        if prices:
            await bot.send_invoice(
                chat_id=callback_query.message.chat.id,
                title=f"Покупка {action}",
                description=description,
                payload=f'sub{action}',
                provider_token=PROVIDER_TOKEN,  # исправлено название параметра и переменной
                currency=CURRENCY,
                start_parameter='test',
                prices=prices
            )

# Обработчики
@dp.pre_checkout_query()
async def process_pre_checkout_query(pre_checkout_query: PreCheckoutQuery, bot: Bot):
    await bot.answer_pre_checkout_query(pre_checkout_query.id, ok=True)

@dp.message(F.content_type == ContentType.SUCCESSFUL_PAYMENT)
async def process_successful_payment(message: Message):
    payload_to_message = {
        'sub1': 'Подписка 1'
    }
    response_message = payload_to_message.get(
        message.successful_payment.invoice_payload, 
        "Оплата прошла успешно"
    )
    await message.answer(response_message)

@dp.pre_checkout_query()
async def process_pre_checkout_query(pre_checkout_query:PreCheckoutQuery,bot:Bot) -> None:
    await bot.answer_pre_checkout_query(pre_checkout_query.id , ok=True)

@dp.message(F.successful_payment)
async def process_successful_payment(message:Message) -> None:
    payload_to_message={
        'sub1':'Подписка 1'
    }
    response_message=payload_to_message.get(message.successful_payment.invoice_payload, "Оплата прошла успешно")
    await message.answer(response_message)

@dp.message(StateFilter(BroadcastState.otziv))
async def process_start(message: types.Message, state: FSMContext):
    if not message.text:
        await message.answer("Напишите текстом")
        return
    iddd=str(otz[message.from_user.id])
    iddd1,iddd2,iddd3=iddd.split('.')
    new_otziv(message.from_user.id,iddd1,iddd2,iddd3,(message.text).replace('\n','<br>'))
    await message.answer("✅ Отзыв добавлен!")
    await state.clear()

@dp.message(F.text == "❤️ Мои подписки")
async def process_start(message: types.Message, state: FSMContext):
    my_sub=my_subskr(message.from_user.id)
    if my_sub ==[]:
        await message.answer("❌ У вас нет подписок")
        return
    for i in my_sub:
        print(i[0])
        await message.answer(f"📕 {i[1]}", reply_markup=InlineKeyboardMarkup(inline_keyboard=[
            [InlineKeyboardButton(text="📖 Читать", callback_data=f"{i[2]}_read"),
            InlineKeyboardButton(text="❌", callback_data=f"{i[2]}_subscribe")]]))

@dp.message(F.text == "💬 Мои отзывы")
async def process_start(message: types.Message, state: FSMContext):
    my_otz=my_otzivs(message.from_user.id)
    if my_otz==[]:
        await message.answer("❌ У вас нет отзывов")
        return
    for i in my_otz:
        await message.answer(f"📝 Отзыв о комиксе: {i[3]} ({i[4]} ⭐️) :\n{(i[2]).replace('<br>','\n')}", reply_markup=InlineKeyboardMarkup(inline_keyboard=[
            [InlineKeyboardButton(text="❌ Удалить отзыв", callback_data=f"{i[0]}.{i[1]}_delotziv")]]))

@dp.message(F.text == "✏️ Редактировать комикс")
async def process_start(message: types.Message, state: FSMContext):
    s=spisok_komic("id,name")
    if s == 0:
        await message.answer("❌ В каталоге нет комиксов")
        return
    await message.answer_document(types.FSInputFile("komiks.txt"))
    os.remove("komiks.txt")
    await message.answer("Введите номер комикса", reply_markup=otmena)
    await state.clear()
    await state.set_state(BroadcastState.redakt)

@dp.message(StateFilter(BroadcastState.redakt))
async def process_start(message: types.Message, state: FSMContext):
    try:
        numb=int(message.text)
    except:
        await message.answer("Введите номер комикса")
        return
    s=one_info("name",f"id={numb}")
    if s==[]:
        await message.answer("Данный комикс не найден,попробуйте еще раз")
        return
    await message.answer(f"📕 {s[0]}\nВыберите, что редактировать:", reply_markup=InlineKeyboardMarkup(inline_keyboard=[
            [InlineKeyboardButton(text="✏️ Название", callback_data=f"{numb}_redname")],
            [InlineKeyboardButton(text="📖 Описание", callback_data=f"{numb}_redinfo")],
            [InlineKeyboardButton(text="🖼️ Изображение", callback_data=f"{numb}_redphoto")],
            [InlineKeyboardButton(text="📋 Редактировать главы", callback_data=f"{numb}_redpdf")],
            [InlineKeyboardButton(text="📊 Статус", callback_data=f"{numb}_redstatus")],
            [InlineKeyboardButton(text="💳 Реквизиты доната", callback_data=f"{numb}_reddonate")]]))

@dp.message(StateFilter(BroadcastState.name_red))
async def process_start(message: types.Message, state: FSMContext):
    if not message.text:
        await message.answer("Напишите текстом")
        return
    replase_info("name",(message.text),slov_id[message.from_user.id])
    await message.answer("Готово ✅",reply_markup=admin_panel)
    await state.clear()
 
@dp.message(StateFilter(BroadcastState.info_red))
async def process_start(message: types.Message, state: FSMContext):
    if not message.text:
        await message.answer("Напишите текстом")
        return
    replase_info("info",(message.text).replace("\n","<br>"),slov_id[message.from_user.id])
    await message.answer("Готово ✅",reply_markup=admin_panel)
    await state.clear()
 
@dp.message(StateFilter(BroadcastState.photo_red))
async def process_start(message: types.Message, state: FSMContext):
    if not message.photo:
        await message.answer("Отправьте фотографию")
        return
    photo_id = message.photo[-1].file_id
    photo = message.photo[-1]
    file = await bot.get_file(photo.file_id)
    downloaded_file = await bot.download_file(file.file_path)
    filename = f"{photo.file_id}.jpg"
    save_path = SAVE_DIR / filename
    with open(save_path, 'wb') as new_file:
        new_file.write(downloaded_file.read()) 
    replase_info("photo_name",photo_id,slov_id[message.from_user.id])
    await message.answer("Готово ✅",reply_markup=admin_panel)
    await state.clear()

@dp.message(StateFilter(BroadcastState.del_red))
async def process_start(message: types.Message, state: FSMContext):
    try:
        t=int(message.text)
    except:
        await message.answer("Отправье просто номер главы")
        return
    if t not in gl:
        await message.answer("У комикса нет такой главы")
        return
    try:
        delete("otziv",f"komiks_id={slov_id[message.from_user.id]} AND glav='{t}'")
        delete_glav(slov_id[message.from_user.id],t)
        await message.answer("Готово ✅")
    except Exception as e:
        await message.answer(f"Ошибка:\n{e}")

@dp.message(StateFilter(BroadcastState.rekvesit_red))
async def process_start(message: types.Message, state: FSMContext):
    if not message.text:
        await message.answer("Напишите текстом")
        return
    try:
        replase_info("donate",(message.text).replace("\n","<br>"),slov_id[message.from_user.id])
        await message.answer("Готово ✅")
        await state.clear()
    except:
        await message.answer("Ошибка")
        await state.clear()

@dp.message(F.text == "📜 Просмотреть отзывы")
async def process_start(message: types.Message, state: FSMContext):
    global admin
    if not(str(message.from_user.id) == str(admin)):
        return
    s=spisok_komic("id,name")
    if s == 0:
        await message.answer("❌ В каталоге нет комиксов")
        return
    await message.answer_document(types.FSInputFile("komiks.txt"))
    os.remove("komiks.txt")
    await message.answer("Введи номер комикса для просмотра его отзывов")
    await state.clear()
    await state.set_state(BroadcastState.chek_otziv)

@dp.message(StateFilter(BroadcastState.chek_otziv))
async def process_start(message: types.Message, state: FSMContext):
    if not message.text:
        await message.answer("Напишите текстом")
        return
    try:
        t=int(message.text)
    except:
        await message.answer("Напишите просто число")
        return
    s=one_info("*",f"id={t}")
    if s==[]:
        await message.answer("Данный комикс не найден,попробуйте еще раз")
        return
    s=all_otzivs(t)
    if s==[]:
        await message.answer("Отзывов пока нет")
        return
    ss=[]
    for i in s:
        if i[3]=="None":
            na="Отсутствует"
        else:
            na=f"@{i[3]}"
        await message.answer(f"Имя: {na} {i[1]} ⭐️ Глава: {"Все произведение" if i[0]=="all" else i[0]}\nОтзыв:{(i[2]).replace('<br>','\n')}",reply_markup=InlineKeyboardMarkup(inline_keyboard=[
            [InlineKeyboardButton(text="Удалить отзыв", callback_data=f"{t}.{i[0]}.{i[4]}_delotziv")]]))
    await state.clear()

@dp.message(F.text == "📊 Статистика")
async def process_start(message: types.Message, state: FSMContext):
    statistik_users("*")
    await message.answer_document(types.FSInputFile("users.txt"))
    os.remove("users.txt")

@dp.message(F.text == "🛒 История покупок")
async def process_start(message: types.Message, state: FSMContext):
    his=hostory_pokupok(message.from_user.id)
    if his==[]:
        await message.answer("У вас не было транзакций")
        return
    for i in his:
        await message.answer(f"Номер чека: `{i[0]}`\nВремя {i[1]}\nСумма: {i[2]}₽\nИнформацмя: {i[3]}", parse_mode="Markdown")

@dp.message(F.text == "💰 Редактировать цены")
async def process_start(message: types.Message, state: FSMContext):
    s=spisok_komic("id,name")
    if s == 0:
        await message.answer("❌ В каталоге нет комиксов")
        return
    await message.answer_document(types.FSInputFile("komiks.txt"))
    os.remove("komiks.txt")
    await message.answer("Что бы поменять цену именно комикса напишите просто номер комикса(например 2)\nЕсли хотите поменять цену одной главы то напишите номер комикса и через точку номер главы (например 2.1)", reply_markup=otmena)
    await state.set_state(BroadcastState.change_prise)

@dp.message(StateFilter(BroadcastState.change_prise))
async def process_start(message: types.Message, state: FSMContext):
    if not message.text:
        await message.answer("Нужно ввести текстом")
        return
    try:
        k,g=(message.text).split(".")
        if file_glavs(k,g) == []:
            await message.answer("Данная глава не найдена введите информацию правильно\n\nЧто бы поменять цену именно комикса напишите просто номер комикса(например 2)\nЕсли хотите поменять цену одной главы то напишите номер комикса и через точку номер главы (например 2.1)")
            return
        otz[message.from_user.id]=f"{k}.{g}"
    except:
        k=message.text
        if glavs(k) == []:
            await message.answer("Данный комикс не найден введите информацию правильно\n\nЧто бы поменять цену именно комикса напишите просто номер комикса(например 2)\nЕсли хотите поменять цену одной главы то напишите номер комикса и через точку номер главы (например 2.1)")
            return
        otz[message.from_user.id]=k
    await message.answer("Введите новую цену")
    await state.clear()
    await state.set_state(BroadcastState.change_prise2)

@dp.message(StateFilter(BroadcastState.change_prise2))
async def process_start(message: types.Message, state: FSMContext):
    if not message.text:
        await message.answer("Нужно ввести текстом")
        return
    try:
        m=int(message.text)
    except:
        await message.answer("Нужно ввести просто число")
        return
    if "." in otz[message.from_user.id]:
        k,g=(otz[message.from_user.id]).split(".")
        change_prise("glavs",f"price={m}",f"id_komiks={k} AND number_glavs={g}")
        await message.answer("Готово ✅",reply_markup=admin_panel)
        await state.clear()
    else:
        k=otz[message.from_user.id]
        change_prise("komiks",f"price={m}",f"id={k}")
        await message.answer("Готово ✅",reply_markup=admin_panel)
        await state.clear()

@dp.message(F.text == "💸 Финансы")
async def process_start(message: types.Message, state: FSMContext):
    await message.answer("💸 Финансы:",reply_markup=money_keyboard)

@dp.message(F.text == "Балансы")
async def process_start(message: types.Message, state: FSMContext):
    statistik_users("*")
    await message.answer_document(types.FSInputFile("users.txt"))
    os.remove("users.txt")
    await message.answer("Отправьте ID человека чей баланс хотели бы изменить. ID можно взять из файла или попросить человека отправить его из личного кабинета",reply_markup=otmena)
    await state.clear()
    await state.set_state(BroadcastState.perevod)

@dp.message(StateFilter(BroadcastState.perevod))
async def process_start(message: types.Message, state: FSMContext):
    if not message.text:
        await message.answer("Нужно ввести текстом")
        return
    try:
        m=int(message.text)
    except:
        await message.answer("Нужно ввести просто число")
        return
    if m not in all_people_id():
        await message.answer("ID не найден попробуйте еще раз")
        return
    otz[message.from_user.id]=m
    await message.answer("Пожалуйста, введите сумму. Если хотите пополнить счет, укажите положительное число (например, 100). Если хотите снять деньги, укажите число с минусом в начале (например, -100)")
    await state.clear()
    await state.set_state(BroadcastState.perevod2)

@dp.message(StateFilter(BroadcastState.perevod2))
async def process_start(message: types.Message, state: FSMContext):
    if not message.text:
        await message.answer("Нужно ввести текстом")
        return
    try:
        m=int(message.text)
    except:
        await message.answer("Нужно ввести просто число")
        return
    change_balance(otz[message.from_user.id],int(user_money(otz[message.from_user.id])[0])+m)
    transaktion(generate_string(),(datetime.datetime.now().strftime("%H:%M %d.%m.%Y")),otz[message.from_user.id],m,f"Админ ({m})",0)
    await message.answer("Готово ✅",reply_markup=admin_panel)
    await state.clear()

@dp.message(F.text == "Поиск транзакции")
async def process_start(message: types.Message, state: FSMContext):
    await message.answer("Введите номер/чек транзакции он должен выклядеть примерно так PiYXtVyT7kbmbseghNWQp95CG4jTY0SFE4g236zkxYgfzs3uRb",reply_markup=otmena)
    await state.clear()
    await state.set_state(BroadcastState.chek_transaktion)

@dp.message(StateFilter(BroadcastState.chek_transaktion))
async def process_start(message: types.Message, state: FSMContext):
    if not message.text:
        await message.answer("Нужно ввести текстом")
        return
    i=chek_transaktion(message.text)
    if i==[]:
        await message.answer("Транзакция не найдена")
        return
    i=i[0]
    await message.answer(f"Номер чека: `{i[0]}`\nВремя {i[1]}\nСумма: {i[2]}₽\nИнформацмя: {i[3]}", parse_mode="Markdown",reply_markup=admin_panel)
    await state.clear()

@dp.message(F.text == "Все транзакции")
async def process_start(message: types.Message, state: FSMContext):
    tran=all_transaktion()
    if tran==[]:
        await message.answer("Транзакций не найдено")
        return
    print(tran)
    with open("transaktion.txt", 'a') as file:
        for i in tran:
            file.write(f"Номер чека: {i[0]}\nВремя {i[1]}\nСумма: {i[2]}₽\nИнформацмя: {i[3]}\n\n")
    await message.answer_document(types.FSInputFile("transaktion.txt"))
    os.remove("transaktion.txt")

@dp.message(F.text == "💸 Пополнить баланс")
async def process_start(message: types.Message, state: FSMContext):
    await message.answer("Введите сумму для пополнения:",reply_markup=otmena)
    await state.clear()
    await state.set_state(BroadcastState.buy)



async def main():
    await dp.start_polling(bot)
    

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print('\nБот успешно выключен')
        