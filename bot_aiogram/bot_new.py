from typing import Text
from aiogram import Bot, Dispatcher, types, executor
from aiogram.types import ReplyKeyboardRemove, ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton

def get_keyboard():
    buttons = [
        types.InlineKeyboardButton(text='Изменить пароль', callback_data='edit_secret'),
        types.InlineKeyboardButton(text='Изменить имя', callback_data='edit_fullname')
    ]
    