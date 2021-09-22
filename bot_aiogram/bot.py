from typing import Text
from aiogram import Bot, Dispatcher, types, executor
from aiogram.types import ReplyKeyboardRemove, ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton

bot = Bot(token="1966342656:AAEikQMfVsuHureW2I8fJhPJtx4zG64rVvc")
dp=Dispatcher(bot)


#---inlineButton---

editFullname = InlineKeyboardButton("Изменить имя аккаунта", callback_data='editfullname')
editSecret = InlineKeyboardButton("Изменить пароль аккаунта", callback_data='editsecret')
btn_editFullname = InlineKeyboardMarkup().add(editFullname)
btn_editSecret = InlineKeyboardMarkup().add(editSecret)


@dp.message_handler()
async def echo(message: types.Message):
    if len(message.text) == 4:
        if message.text.isdigit():
            await message.answer('-#-'*10)
            await message.answer('Название:  ' + message.text, reply_markup=btn_editFullname)
            await message.answer('Пароль: ' + message.text, reply_markup=btn_editSecret)
        else:
            await message.reply('Стррока состоит не из цифр')

    else:
        await message.reply('Стррока имеет длину боьлше 4 символов')


@dp.callback_query_handler(text='editsecret')
async def my_editsecret(call: types.CallbackQuery):
    #await call.message.answer('Нажата кнопка изменения пароля!')
    await call.answer(text='Нажата кнопка изменения пароля', show_alert=True)

@dp.callback_query_handler(text='editfullname')
async def my_editFullname(call: types.CallbackQuery):
    #await call.message.answer('Нажата кнопка изменения имени')
    await call.answer(text='Нажата кнопка изменения имени', show_alert=True)

if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)