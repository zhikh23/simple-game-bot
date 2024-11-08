from os import getenv

from aiogram import Router
from aiogram.types import Message
from aiogram.filters import Command

from dotenv import load_dotenv


router = Router()
load_dotenv(dotenv_path=".env")


past_game_users = list()


@router.message(Command("start"))
@router.message(Command("help"))
async def start_handler(msg: Message,):
    await msg.answer("Введите двоичный код.")


@router.message()
async def other_handler(msg: Message):
    tg_user_id = msg.from_user.id
    path = getenv('PATH_TO_FILE')
    with open(path, 'r', encoding='utf-8') as file:
        for line in file:
            if tg_user_id == int(line.strip()):
                return
    if tg_user_id in past_game_users:
        await msg.answer("Вы уже прошли игру.")
        return

    secret_key = getenv("SECRET_KEY")
    if msg.text.strip() == secret_key:
        past_game_users.append(tg_user_id)
        await msg.answer("Вы успешно прошли игру!")
    else:
        await msg.answer("Неверный код, попробуйте снова.")
