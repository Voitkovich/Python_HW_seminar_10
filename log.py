import aiohttp
import time
import logging
from aiogram import Bot, Dispatcher, executor, types


# 'UTF-8-sig'
logging.basicConfig(level=logging.INFO, filename="log.csv", filemode="w",
                    format="%(asctime)s: %(levelname)s %(funcName)s-%(lineno)d %(message)s")