from app import bot,dp
from airogram import Message
from config import admin_id, todo, HELP
import time

async def send_to_admin(dp):
  await bot.send_message(chat_is = admin_id, text = "Бот запущен!")