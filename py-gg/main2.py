import logging
import requests
import json
import aiohttp
from aiogram import Bot, Dispatcher, executor, types
from aiogram.types.message import ContentType
from aiogram.utils import executor
from aiogram.types import ContentType
import aiogram.utils.exceptions

import time

BASE_URL = "http://45.130.43.65/posts"

async def get_free_spaces():
    new_array = []
    async with aiohttp.ClientSession() as session:
        async with session.get(BASE_URL) as resp:
            let2 = json.loads(await resp.text())
            for elements in let2:
                if(elements.get('index_city') == 95000):
                    new_array.append([
                    elements['User_number_of_free_place_parking'],
                    elements['owner_name_parking'], 
                    elements['owner_free_forinvalid'], 
                    elements["owner_price_parking"],
                    elements['owner_id'],
                    elements["User_number_of_occupied_parking_spaces"]
                 ])
    return new_array
async def decrement_and_update_element(free_spaces, choose_booking):
    for element in free_spaces:
        print("hello")
        if choose_booking == element[1]:
            element[0] -= 1 
            element[5] += 1
            print('element')
            async with aiohttp.ClientSession() as session:
                update_url = BASE_URL + "/" + str(element[4])
                data = {'User_number_of_free_place_parking': element[0]}
                await session.put(update_url, data=json.dumps(data), headers={'Content-Type': 'application/json'})



io=0
# log
logging.basicConfig(level=logging.INFO)
# Оплата 
PRICE = None

# Объект бота
bot = Bot(token="6205423128:AAGGc2H1C29mQqxMkjrrAxC7KbMCgq6TReg")
# Диспетчер
dp = Dispatcher(bot) 
# Переменная брони парковки
choose_booking = 0
#Цена за час
priceperhour=50
myos = False


#на команду /start
@dp.message_handler(commands=["start"])
async def cmd_start(message: types.Message):

    ickb = [
        [types.KeyboardButton(text="Узнать количество свободных мест")],
        [types.KeyboardButton(text="Узнать есть ли льготные места")],
        [types.KeyboardButton(text="Забронировать место")]
    ]

    keyboard = types.ReplyKeyboardMarkup(keyboard=ickb)
    await message.answer("Здравствуйте! Это телеграм бот проекта simfparking!\nЯ помогу вам узнать количество свободных мест и забронировать безналичным рассчетом.", reply_markup=keyboard)


#свободные места
@dp.message_handler(text=["Узнать количество свободных мест"])
async def cmd_free(message: types.Message):
    free_spaces = await get_free_spaces()
   
    for element in free_spaces:
        if(element[2] == True):
            element[2] = 'Доступны'
        else:
            element[2] = 'Не доступны'
        await message.answer(f"Cвободные места: {str(element[0])} на  {str(element[1])} в г.Симферополь.  Цена:{str(element[3])} руб")
#ячейкамассива1 ячейкамассива2 итд

@dp.message_handler(text=["Узнать есть ли льготные места"])
async def cmd_free1(message: types.Message):
    free_spaces = await get_free_spaces()
    for element in free_spaces:
        if(element[2] == True):
            element[2] = 'Доступны'
        else:
            element[2] = 'Не доступны'
        await message.answer(f"Льготные места: {str(element[2])}  на {str(element[1])} в г.Симферополь")



@dp.message_handler(text=['Забронировать место'])
async def cmd_start(message: types.Message):
    await message.answer("На сколько часов требуется парковка?")


async def handle_free_spaces(free_spaces, message):
    freespace = []
    for element in await free_spaces:
        if int(message.text) > 23:
            await message.answer("Вы не можете забронировать место более чем на 23 часа")
            return
        freespace.append([types.KeyboardButton(text=f"{str(element[1])}")])
        io = int(message.text) * int(priceperhour)
        print(io)
    return freespace, io


async def handle_free_spaces_message(message: types.Message):
    global io, choose_booking
    free_spaces = await get_free_spaces()
    for element in free_spaces:
        if element[1] == message.text:
            choose_booking = element
    await bot.send_invoice(chat_id=message.chat.id,
                           title="Бронь парковки",
                           description=f"Забронировано место {choose_booking[1]} на {io} часов",
                           provider_token="381764678:TEST:53438",
                           currency="rub",
                           photo_url='https://media.istockphoto.com/vectors/car-parking-illustration-vector-id876792570?k=20&m=876792570&s=612x612&w=0&h=A0yUvnBbN0EFKpW1uYajpa1ycSHI0pGAGSqNHRd-GQo=',
                           photo_height=256,
                           photo_width=256,
                           photo_size=256,
                           is_flexible=False,  # True если конечная цена зависит от способа доставки
                           prices=[types.LabeledPrice("Бронь", io * 100)],
                           start_parameter='time-machine-example',
                           payload='some-invoice-payload-for-our-internal-use')

@dp.message_handler(lambda message: message.text.isdigit())
async def int_handler(message: types.Message):
    global io
    free_spaces = get_free_spaces()
    freespace, io = await handle_free_spaces(free_spaces, message)
    
    price = types.LabeledPrice(label='бронь', amount=io*100)
    keyboard = types.ReplyKeyboardMarkup(keyboard=freespace)
    await message.answer("Выберите место", reply_markup=keyboard)

@dp.message_handler(lambda message: any(x[1] == message.text for x in get_free_spaces()))
async def handle_message(message: types.Message):
    await handle_free_spaces_message(message)

    # ваш код здесь
    global choose_booking
    free_spaces = get_free_spaces()
    for element in free_spaces:
        if element[1] == message.text:
            choose_booking = element
    await bot.send_invoice(chat_id=message.chat.id,
                           title="Бронь парковки",
                           description=f"Забронировано место {choose_booking[1]} на {io} часов",
                           provider_token="381764678:TEST:53438",
                           currency="rub",
                           photo_url='https://media.istockphoto.com/vectors/car-parking-illustration-vector-id876792570?k=20&m=876792570&s=612x612&w=0&h=A0yUvnBbN0EFKpW1uYajpa1ycSHI0pGAGSqNHRd-GQo=',
                           photo_height=256,
                           photo_width=256,
                           photo_size=256,
                           is_flexible=False,  # True если конечная цена зависит от способа доставки
                           prices=[types.LabeledPrice("Бронь", io * 100)],
                           start_parameter='time-machine-example',
                           payload='some-invoice-payload-for-our-internal-use')

                           


#препроверка
@dp.pre_checkout_query_handler()
async def process_pre_checkout_query(pre_checkout_query: types.PreCheckoutQuery):
    await bot.answer_pre_checkout_query(pre_checkout_query.id, ok=True)


#конечная обработка платежа(можно задать действия по совершению платежа!!)
@dp.message_handler(content_types=ContentType.SUCCESSFUL_PAYMENT)
async def successful_payment(message: types.Message):
    print("SUCCESSFUL PAYMENT:")
    free_spaces = await get_free_spaces()
    await decrement_and_update_element(free_spaces, choose_booking)
    payment_info = message.successful_payment.to_python()
    for k, v in payment_info.items():
        print(f"{k} = {v}")
    await bot.send_message(message.chat.id,
                           f"Платёж на сумму {message.successful_payment.total_amount // 100} {message.successful_payment.currency} по заказу места на "+ choose_booking +" прошел успешно!!!")

# Запуск процесса поллинга новых апдейтов
if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=False)
