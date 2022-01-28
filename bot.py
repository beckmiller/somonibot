
import config
import logging
from banks.eskhata import somoni_rub
from predictions import predict
from aiogram import Bot, Dispatcher, executor, types

from sql_db import SQLighter

from aiogram.types import ReplyKeyboardRemove, \
    ReplyKeyboardMarkup, KeyboardButton, \
    InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.dispatcher.filters import Text


#setting log level
logging.basicConfig(level=logging.INFO)

#initializing bot
bot = Bot(token=config.API_TOKEN)
dp = Dispatcher(bot)

#initializing db connection
db = SQLighter('db.db')

#command to activate subscription
@dp.message_handler(commands=['subscribe'])
async def subscribe(message: types.Message):
	if(not db.subscriber_exists(message.from_user.id)):
		#if user doesnt exist   
		db.add_subscriber(message.from_user.id)
	else:
		#if exists then updating status
		db.update_subscription(message.from_user.id, True)

	await message.answer('You succefully subscribed')

#command to unsubscribe
@dp.message_handler(commands=['unsubscribe'])
async def unsubscribe(message: types.Message):
	if(not db.subscriber_exists(message.from_user.id)):
		#if user doesnt exist we'll add user but with inactive subscription
		db.add_subscriber(message.from_user.id)
		await message.answer('You already unsubscribed')
	else:
		db.update_subscription(message.from_user.id, False)
		await message.answer('You unsubscribed')


    
@dp.message_handler(commands=['kurs'])
async def kurs(message: types.Message):
	curr = somoni_rub()
	await message.answer(curr)


@dp.message_handler(commands="start")
async def cmd_start(message: types.Message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    buttons = ["Узнать курс", 'Прогноз'] # 'Orienbank'
    keyboard.add(*buttons)
    await message.answer("Хотите узнать курс или прогноз на завтра?", reply_markup=keyboard)

#обработка кнопки, если Эсхата
@dp.message_handler(Text(equals="Узнать курс"))
async def with_puree(message: types.Message):
	curr = somoni_rub()
	await message.reply(curr)

@dp.message_handler(Text(equals="Прогноз"))
async def with_puree(message: types.Message):
	await message.reply(predict)


@dp.message_handler()
async def echo_message(msg: types.Message):
	if msg.text.lower() == 'курс' or msg.text.lower()=='kurs':
		curr = somoni_rub()
		await bot.send_message(msg.from_user.id, curr)


# run log poll
if __name__ == '__main__':
	executor.start_polling(dp, skip_updates=True)
