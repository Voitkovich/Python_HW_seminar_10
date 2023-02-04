import time
import logging
from aiogram import Bot, Dispatcher, executor, types
import logging
from log import *
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


MSG = "{}, Выберете пункт меню:"

bot = Bot("6142966797:AAEw4fXUvHUGWX2UbUrZltF549aglLSoTgY")
dp = Dispatcher(bot=bot)

@dp.message_handler(commands=['start'])
async def start_handler(message: types.Message):
    user_id = message.from_user.id
    user_name = message.from_user.first_name
    user_full_name = message.from_user.full_name
    user_bot = message.from_user.is_bot
    user_message = message.text
    logging.info(f'{user_id=} {user_bot=} {user_message=}')
    await message.reply(f"Здравствуйте, {user_full_name}!")
    time.sleep(1)
    btns = types.ReplyKeyboardMarkup(row_width=4)
    btn_why = types.KeyboardButton('/Почему_Raw?')
    btn_image = types.KeyboardButton('/Меню 🍴 ')
    # btn_zakaz = types.KeyboardButton('/Заказать')
    btn_inst = types.KeyboardButton('/Instagramm')
    btns.add(btn_why, btn_image, btn_inst)
    await bot.send_message(user_id, MSG.format(user_name), reply_markup=btns)


urlkb = InlineKeyboardMarkup(row_width=1)
urlButton = InlineKeyboardButton(text='Перейти в мой Instagramm 👉', url='https://instagram.com/cyprus_raw?igshid=Zjc2ZTc4Nzk=')
urlButton2 = InlineKeyboardButton(text='Сделать заказ в WhatsApp 👉', url='https://wa.me/+79046474802')
urlkb.add(urlButton,urlButton2)

 
@dp.message_handler(commands=['Почему_Raw?'])
async def why_raw(message: types.Message):
    with open("venv/raw.JPG", "rb") as f:
       await bot.send_photo(message.chat.id, caption='🎂Холодненький raw-десерт без вредных ингредиентов – приятный и здоровый перекус в любое время. Подходит сыроедам, вегетарианцам, веганам, детям, тем, кто следит за фигурой и просто предпочитает питаться правильно. Такой тортик не содержит сахара и муки, коржи для него не нужно выпекать.🍓🍓🍓 Такой десерт - просто идеальный вариант побаловать себя вкусненьким за чашечкой чая!❤️❤️❤️❤️❤️', photo=f)
               
    
#  bot.send_photo(id, photo, caption='желаемый текст')       
                         
                                                   
@dp.message_handler(commands=['Меню'])
async def cmd_send_image(message):
    with open("venv/авокадо.PNG", "rb") as f:
        await bot.send_photo(message.chat.id, photo=f)
    with open("venv/баунти.JPG", "rb") as f:
        await bot.send_photo(message.chat.id, photo=f)
    with open("venv/вишня.PNG", "rb") as f:
        await bot.send_photo(message.chat.id, photo=f)
    with open("venv/клубника.JPG", "rb") as f:
        await bot.send_photo(message.chat.id, photo=f)
    with open("venv/морковка.PNG", "rb") as f:
        await bot.send_photo(message.chat.id, photo=f)
    with open( "venv/свекла.PNG", "rb") as f:
        await bot.send_photo(message.chat.id, photo=f)
    with open( "venv/тирамису.PNG", "rb") as f:
        await bot.send_photo(message.chat.id, photo=f)
    with open("venv/тыква.PNG", "rb") as f:
        await bot.send_photo(message.chat.id, photo=f)
    with open("venv/цитрус.PNG", "rb") as f:
        await bot.send_photo(message.chat.id, photo=f)     


        
# @dp.message_handler(commands=['Заказать'])
# async def zakaz(message: types.Message):
#     await bot.send_message(message.from_user.id, 'Мой телефон',
#                            reply_markup=types.ReplyKeyboardRemove())        


@dp.message_handler(commands=['Instagramm'])
async def instagramm(message: types.Message):
     await message.answer("Здесь вы можете прочитать интересные рецепты, сделать заказ или  просто пообщаться со мной", reply_markup=urlkb)


if __name__ == '__main__':
    executor.start_polling(dp)

