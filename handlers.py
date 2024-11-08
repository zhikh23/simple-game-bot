from aiogram import Router
from aiogram.types import Message
from aiogram.filters import Command
from dotenv import load_dotenv
from os import getenv


router = Router()
load_dotenv(dotenv_path=".env")


@router.message(Command("start"))
@router.message(Command("help"))
async def start_handler(msg: Message,):
    await msg.answer('Введите код.')


@router.message()
async def other_handler(msg: Message):
    tg_user_id = msg.from_user.id
    path = getenv('PATH_TO_FILE')
    with open(path, 'r', encoding='utf-8') as file:
        for line in file:
            if tg_user_id == int(line.strip()):
                await msg.answer('Вы уже разгадали код.')
                return

    secret_key = getenv('SECRET_KEY')
    if msg.text.strip() == secret_key:
        with open(path, 'a', encoding='utf-8') as file:
            file.write(str(tg_user_id)+'\n')
        await msg.answer('Код введен успешно.')
        return
    await msg.answer('Код неверен')
