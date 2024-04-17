import asyncio
import logging
from aiogram import Bot, Dispatcher, types
from aiogram.filters.command import Command
from aiogram.types import FSInputFile
from aiogram.utils.markdown import hlink
import os

import config
import markups
import messages
import prog


logging.basicConfig(level=logging.INFO)

bot = Bot(token=config.TOKEN)

dp = Dispatcher()


@dp.message(Command("start"))
async def start(message):
    await message.answer(
        messages.message_main,
        parse_mode="html",
        reply_markup=markups.markup_main.as_markup()
        )
    

@dp.callback_query()
async def answer(call: types.CallbackQuery):
    global msg_edit

    if call.data == "back":
        await call.message.edit_text(
            messages.message_main,
            parse_mode="html",
            reply_markup=markups.markup_main.as_markup()
            )

    if call.data == "ipconfig":
        msg_edit = await call.message.edit_text(
            "<b>Введите IP</b>",
            parse_mode="html",
            reply_markup=markups.markup_back.as_markup()
        )

        config.next_step = call.data

@dp.message()
async def get_msg(message: types.Message):
    if config.next_step == "ipconfig":
        data = prog.get_info_by_ip(message.text)

        await msg_edit.edit_reply_markup()

        if data != "Error":
            with open("ip.txt", "w") as f:
                f.write(data)
                
            await message.answer_document(
                document=FSInputFile(r"ip.txt")
                )

            os.remove("ip.txt")

        else:
            await message.answer("Что-то пошло не так, попробуй ещё раз")

        await message.answer(
            messages.message_main,
            parse_mode="html",
            reply_markup=markups.markup_main.as_markup()
        )

        config.next_step = ""

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())