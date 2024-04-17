from aiogram import types
from aiogram.utils.keyboard import InlineKeyboardBuilder

markup_main, markup_back = InlineKeyboardBuilder(), InlineKeyboardBuilder()

markup_main.row(types.InlineKeyboardButton(text="Пробить", callback_data="ipconfig"))

markup_back.row(types.InlineKeyboardButton(text="Назад", callback_data="back"))
