from aiogram import Router
from aiogram.filters import CommandStart
from aiogram.types import Message

router = Router()

@router.message(CommandStart())
async def command_start_handler(message: Message) -> None:
    await message.answer(f'Hello <b>{message.from_user.username} </b>! How is it going?')

@router.message()
async def echo_handler(message: Message) -> None:
    await message.answer(f'I repeat: <b>{message.text}</b>')