import os
import asyncio
import logging

from aiogram import Bot, Dispatcher, F
from aiogram.types import Message, CallbackQuery
from aiogram.filters import CommandStart
from aiogram.enums import ParseMode
from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram.client.default import DefaultBotProperties

logging.basicConfig(level=logging.INFO)

WELCOME_TEXT = (
"JUZ40 білім беру орталығының GENIUS бөлімінің CALL-CENTER қош келдіңіз!❤️\n\n"
"Өзіңіздің комбинацияңызды таңдау арқылы сұрағыңызды жолдай аласыз👇🏻"
)

PRICES_TEXT = (
"🏆 НЕГІЗГІ БАҒА\n"
"VIP — ТЕГІН\n"
"PREMIUM — 35 000 тг\n"
"STANDARD — 45 000 тг\n\n"
"🎯 IELTS\n"
"VIP — ТЕГІН\n"
"PREMIUM — 27 000 тг\n"
"STANDARD — 34 000 тг"
)

RESPONSIBLES = {

"djtangl":
"ДЖТАНГЛ/ГЕОАНГЛ комбинациялары бойынша сұрақтарыңызды осы жауапты маманнан сұрай аласыз: @dgadamir",

"adebtil":
"ӘДЕБТІЛ/РУСЛИТ комбинациялары бойынша сұрақтарыңызды осы жауапты маманнан сұрай аласыз: @atrlzere",

"geodjt":
"ГЕОДЖТ/ДЖТҚҰҚЫҚ комбинациялары бойынша сұрақтарды осы жауапты маманнан сұрай аласыз: @wqa1ad",

"biohim":
"БИОХИМ комбинациясы бойынша сұрақтарды осы жауапты маманнан сұрай аласыз: @uldanasssss",

"fizmat":
"ФИЗМАТ комбинациясы бойынша сұрақтарды осы жауапты маманнан сұрай аласыз: @physmatharu",

"infomat":
"ИНФОМАТ комбинациясы бойынша сұрақтарды осы жауапты маманнан сұрай аласыз: @zhantoreinfomath",

"geomath":
"ГЕОМАТ комбинациясы бойынша сұрақтарды осы жауапты маманнан сұрай аласыз: @geomathzhuka",

"geobio":
"БИОГЕО комбинациясы бойынша сұрақтарды осы жауапты маманнан сұрай аласыз: @soleanar",

"prices": PRICES_TEXT
}


def main_keyboard():

    kb = InlineKeyboardBuilder()

    kb.button(text="ДЖТАНГЛ/ГЕОАНГЛ",callback_data="djtangl")
    kb.button(text="ӘДЕБТІЛ/РУСЛИТ",callback_data="adebtil")

    kb.button(text="ГЕОДЖТ/ДЖТҚҰҚЫҚ",callback_data="geodjt")
    kb.button(text="БИОХИМ",callback_data="biohim")

    kb.button(text="ФИЗМАТ",callback_data="fizmat")
    kb.button(text="ИНФОМАТ",callback_data="infomat")

    kb.button(text="ГЕОМАТ",callback_data="geomath")
    kb.button(text="ГЕОБИО",callback_data="geobio")

    kb.button(text="БАҒАЛАР",callback_data="prices")

    kb.adjust(2,2,2,2,1)

    return kb.as_markup()


def back_keyboard():

    kb = InlineKeyboardBuilder()

    kb.button(text="⬅️ Артқа",callback_data="back")

    return kb.as_markup()


async def main():

    token = os.getenv("BOT_TOKEN")

    if not token:
        raise RuntimeError("BOT_TOKEN Railway Variables ішіне қой.")

    bot = Bot(
        token=token,
        default=DefaultBotProperties(parse_mode=ParseMode.HTML)
    )

    dp = Dispatcher()


    @dp.message(CommandStart())
    async def start(message: Message):

        await message.answer(
            WELCOME_TEXT,
            reply_markup=main_keyboard()
        )


    @dp.callback_query(F.data == "back")
    async def back(callback: CallbackQuery):

        await callback.answer()

        await callback.message.edit_text(
            WELCOME_TEXT,
            reply_markup=main_keyboard()
        )


    @dp.callback_query(F.data.in_(RESPONSIBLES.keys()))
    async def handlers(callback: CallbackQuery):

        await callback.answer()

        text = RESPONSIBLES[callback.data]

        await callback.message.edit_text(
            text,
            reply_markup=back_keyboard()
        )


    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
