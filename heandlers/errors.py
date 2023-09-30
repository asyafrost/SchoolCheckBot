from aiogram import Router
from aiogram.types import Message
from dictionary import dict_ru

router: Router = Router()


# Хэндлер для сообщений, которые не попали в другие хэндлеры
@router.message()
async def send_answer(message: Message):
    await message.answer(text=dict_ru['other'])