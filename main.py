import keyboard
from tools.Bot import Bot
import time

from tools.Mechanisms import Mechanisms

toggle_key = input('Select toggle key: ')

bot = Bot(1, toggle_key)
keyboard.on_press(bot.handle_keypress)

bot.bot_sequence()
