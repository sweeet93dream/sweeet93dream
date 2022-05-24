
import logging

from aiogram import Bot, Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from db.database import Database

storage = MemoryStorage()

API_TOKEN = '5285312589:AAEYTN0vs3yLzYVn0R3iKR2xnX5pvCE_p00'

# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot, storage=storage)
db = Database('exlab.db')