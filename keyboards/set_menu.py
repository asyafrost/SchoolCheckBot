from aiogram import Bot, Dispatcher
from aiogram.types import BotCommand
from config import token


# Инициализируем бот и диспетчер
bot: Bot = Bot(token)
dp: Dispatcher = Dispatcher()


# Создаем асинхронную функцию
async def set_main_menu(bot: Bot):

    # Создаем список с командами и их описанием для кнопки menu
    main_menu_commands = [
        BotCommand(command='/start',
                   description='Начать работу с ботом'),
        BotCommand(command='/help',
                   description='Справка по работе бота'),
        BotCommand(command='/check_my_child',
                   description='Проверить, в школе ли ребёнок'),
        BotCommand(command='/authors',
                   description='Авторы бота')]

    await bot.set_my_commands(main_menu_commands)


if __name__ == '__main__':
    # Регистрируем асинхронную функцию в диспетчере,
    # которая будет выполняться на старте бота,
    dp.startup.register(set_main_menu)
    # Запускаем поллинг
    dp.run_polling(bot)