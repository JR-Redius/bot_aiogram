import logging
import mySearchNumber
from typing import Text
from aiogram import Bot, Dispatcher, types, executor
from aiogram.types import ReplyKeyboardRemove, ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton

bot = Bot(token="1966342656:AAEikQMfVsuHureW2I8fJhPJtx4zG64rVvc")
dp=Dispatcher(bot)

logging.basicConfig(level=logging.INFO)

#-------Создание блока клавиатуры-------------------
def getKeyboard():
    buttons =[
        types.InlineKeyboardButton(text='Изменить пароль', callback_data='but_editsecret'),
        types.InlineKeyboardButton(text='Изменить имя', callback_data='but_editfullname'),
        types.InlineKeyboardButton(text='Подтвердить', callback_data='but_accept')
    ]
    keyboard = types.InlineKeyboardMarkup(row_width=2)
    keyboard.add(*buttons)
    return keyboard


#-------Обработка входящего сообщения------------------
@dp.message_handler(content_types=types.ContentTypes.TEXT)
async def getFirstMessage(message: types.Message):
    if len(message.text) == 4 and message.text.isdigit():
        user_info = mySearchNumber.getSearchNumber(message.text)
    await message.answer(f"Информация о пользователя: {user_info['fullname']} \n"
                                        "****************************************\n"
                                        f"Номер телефона: {user_info['name']}\n"
                                        f"Имя пользователя: {user_info['fullname']}\n"
                                        f"Пароль: {user_info['secret']}\n"
                                        f"IP адресс устройства: {user_info['ipaddr']} \n"
                                        f"Модель устройсва: {user_info['useragent']}\n"
                                        "\n****************************************\n", reply_markup=getKeyboard())
    elif 



#-------Запуск бота--------------------------
if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)