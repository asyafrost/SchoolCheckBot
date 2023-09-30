import asyncio
import logging
import config
from heandlers import heandlers, errors
from keyboards.set_menu import set_main_menu
from aiogram import Bot, Dispatcher, types

async def main():
    
    # Инициализируем логгер
    logger = logging.getLogger(__name__)

     # Конфигурируем логирование
    logging.basicConfig(
        level=logging.INFO,
        format='%(filename)s:%(lineno)d #%(levelname)-8s '
               '[%(asctime)s] - %(name)s - %(message)s')

    # Выводим в консоль информацию о начале запуска бота
    logger.info('Starting bot')
    
    # Инициализируем бот и диспетчер
    bot: Bot = Bot(token=config.token)
    dp: Dispatcher = Dispatcher()

    # Регистриуем роутеры в диспетчере
    dp.include_router(heandlers.router)
    dp.include_router(errors.router)

    # Настраиваем кнопку Menu
    await set_main_menu(bot)

    # Пропускаем накопившиеся апдейты и запускаем polling
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())
