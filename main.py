from aiogram import executor
from loader import dp
import start

if __name__ == '__main__':
    executor.start_polling(dp, on_startup=print("Бот запущен"))