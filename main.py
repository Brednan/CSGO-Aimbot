import keyboard
from tools.Bot import Bot
import time

from tools.Mechanisms import Mechanisms

mode = input('Select target mode: ')
distance = int(input('Select distance from crosshair: '))

bot = Bot(1, mode, distance)

bot.bot_sequence()
