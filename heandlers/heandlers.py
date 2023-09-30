from servises import get_update_from_external_program
from aiogram import Router, Bot, types
from aiogram.filters import Command, CommandStart, Text
import config


bot: Bot = Bot(token=config.token)
router: Router = Router()

@router.message(CommandStart())
async def start_command(message: types.Message):
    # Отправка приветственного сообщения
    await message.answer("Привет! Я буду сообщать тебе, когда твой ребёнок приходит в школу и уходит из неё.")

@router.message(Command(commands=['help']))
async def start_command(message: types.Message):
    # Отправка приветственного сообщения
    await message.answer("Этот бот будет присылать оповещение, когда кто-то из детей пришел в школу или вышел из неё.\n"
                        "Чтобы узнать, находится ли твой ребёнок сейчас в школе, воспользуйся командой 'check_my_child'.")

@router.message(Command(commands=['check_my_child']))
async def start_command(message: types.Message):
    # Отправка приветственного сообщения
    await message.answer("Напиши фамилию и имя своего ребёнка")
    update_command(message)

async def update_command(message: types.Message):
    # Получение обновлений от внешней программы
    first_name, last_name = message.text.split()
    update = get_update_from_external_program()  # Функция, которую нужно реализовать
    # Отправка обновлений родителям
    await message.reply(update)


