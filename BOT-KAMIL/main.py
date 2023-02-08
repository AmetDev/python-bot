import logging
 
from aiogram import Bot, Dispatcher, executor, types
from aiogram.types.message import ContentType
 
# log
logging.basicConfig(level=logging.INFO)
# Оплата 
PRICE = types.LabeledPrice(label='бронь', amount = 100*100)
# Объект бота
bot = Bot(token="5812078222:AAHLp8IoHMYDJVrVuGStrxAjALUUZXd1h6g")
# Диспетчер
dp = Dispatcher(bot) 
#массив с данными о парковках

#на команду /start
@dp.message_handler(commands=["start"])
async def cmd_start(message: types.Message):
    kb = [
        [types.KeyboardButton(text="Узнать кол-во свободных мест")],
        [types.KeyboardButton(text="Забронировать место")]
    ]
    keyboard = types.ReplyKeyboardMarkup(keyboard=kb)
    await message.answer("Здравствуйте! Это телеграм бот проекта simfparking!\nЯ помогу вам узнать количество свободных мест и забронировать безналичным рассчетом.", reply_markup=keyboard)

#свободные места
@dp.message_handler(text=["Узнать кол-во свободных мест"])
async def cmd_free(message: types.Message):
    await message.answer( "Cвободные места:" )#ячейкамассива1 ячейкамассива2 итд


#задаем параметры окна покупкі
@dp.message_handler(text=['Забронировать место'])
async def process_buy_command(message: types.Message):
    await bot.send_invoice(
    message.chat.id,
    title="Бронь места",
    description="Сейчас вы можете забронировать место на парковке, чтобы это сделать, вам надо заплатить 100 рублей в качестве залога :)",
    provider_token='381764678:TEST:49573',
    currency='rub',
    photo_url='https://media.istockphoto.com/vectors/car-parking-illustration-vector-id876792570?k=20&m=876792570&s=612x612&w=0&h=A0yUvnBbN0EFKpW1uYajpa1ycSHI0pGAGSqNHRd-GQo=',
    photo_height=512,
    photo_width=512,
    photo_size=512,
    is_flexible=False, 
    prices=[PRICE],
    start_parameter='time-machine-example',
    payload='some-invoice-payload-for-our-internal-use'
)

#препроверка
@dp.pre_checkout_query_handler()
async def process_pre_checkout_query(pre_checkout_query: types.PreCheckoutQuery):
    await bot.answer_pre_checkout_query(pre_checkout_query.id, ok=True)

#конечная обработка платежа(можно задать действия по совершению платежа!!)
@dp.message_handler(content_types=ContentType.SUCCESSFUL_PAYMENT)
async def successful_payment(message: types.Message):
    print("SUCCESSFUL PAYMENT:")
    payment_info = message.successful_payment.to_python()
    for k, v in payment_info.items():
        print(f"{k} = {v}")
 
    await bot.send_message(message.chat.id,
                           f"Платёж на сумму {message.successful_payment.total_amount // 100} {message.successful_payment.currency} прошел успешно!!!")


# Запуск процесса поллинга новых апдейтов
if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=False)
