import logging
#from typing import Text
from aiogram import Bot, Dispatcher, types, executor
#from aiogram.types import ReplyKeyboardRemove, ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton

bot = Bot(token="1966342656:AAEikQMfVsuHureW2I8fJhPJtx4zG64rVvc")
dp=Dispatcher(bot)

logging.basicConfig(level=logging.INFO)


def getKeyboard():
    buttons =[
        types.InlineKeyboardButton(text='Изменить пароль', callback_data='but_editsecret'),
        types.InlineKeyboardButton(text='Изменить имя', callback_data='but_editfullname'),
        types.InlineKeyboardButton(text='Подтвердить', callback_data='but_accept')
    ]
    keyboard = types.InlineKeyboardMarkup(row_width=2)
    keyboard.add(*buttons)
    return keyboard

@dp.message_handler(content_types=types.ContentTypes.TEXT)
async def getFirstMessage(message: types.Message):
    await message.answer(message.text)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)