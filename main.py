from email import message
import logging
import emoji
import pyqrcode
from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import ReplyKeyboardMarkup, ReplyKeyboardRemove, KeyboardButton
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from random import randint

# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
API_TOKEN = "5323872134:AAEsYNsjhGk5EU_fxMYlVqf3h1rbmG9QjWg"
support_bot = Bot(token=API_TOKEN)
dp = Dispatcher(support_bot)



button1 = KeyboardButton("Hello")
button2 = KeyboardButton("Youtube")
keyboard  = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True).row(button1, button2)
# start and help commands 
@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    """
    This handler will be called when user sends `/start` or `/help` command
    
    """
    name = message.from_user.first_name
    await message.reply(f"Welcome {name} \N{grinning face}\n We're glad to have you here in our city!\n The City of Atlantus!\N{WATER WAVE}\N{WATER WAVE}\N{WATER WAVE}\n\n \N{PUSHPIN}Please go over the pinned messages.All the information on our journey so far and all you need to know is contained in there.\n\n \N{BLACK QUESTION MARK ORNAMENT}If you have further questions, please put them forward, we'll be very glad to give you answers!\N{grinning face}\N{grinning face}\n\n A Rising Tide Lifts All Boats!\N{ANCHOR}\N{WATER WAVE}\N{WATER WAVE}\N{WATER WAVE}", reply_markup=keyboard)


#info command
button3 = KeyboardButton("who are you?", request_contact=True)
button4 = KeyboardButton("where are you from?", request_location=True)
keyboard2 = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True).row(button3,button4)

@dp.message_handler(commands=['info'])
async def info_message(message: types.Message):
    await message.reply('Say something about you!', reply_markup=keyboard2)


   
#Random command
button5 = InlineKeyboardButton(text="Random 1-10", callback_data="randomvalue_of10")
button6 = InlineKeyboardButton(text="Random 1-100", callback_data="randomvalue_of100")
Keyboard3 = InlineKeyboardMarkup().add(button5,button6)

@dp.message_handler(commands=['random'])
async def random_answer(message:types.Message):
    await message.reply("select a range", reply_markup=Keyboard3)   
    
@dp.callback_query_handler(text=["randomvalue_of10", "randomvalue_of100"])
async def random_value(call: types.CallbackQuery):
    if call.data == "randomvalue_of10":
        await call.message.reply(randint(1,10))
    elif call.data == "randomvalue_of100":
        await call.message.reply(randint(1,100))
    await call.answer()
    
    
    
    
@dp.message_handler()
async def kb_answer(message: types.Message):
    if message.text == "Hello":
        await message.answer("Hi, welcome to MOBI Support! How may i help you \N{FLEXED BICEPS}")
    elif message.text == "Youtube":
        await message.answer('www.youtube.com')
    else:
        await message.answer(f'Your message is: {message.text}')

                   
#logo commands   
@dp.message_handler(commands=['logo'])
async def logo(message: types.Message):
    await message.answer_photo("https://avatars.githubusercontent.com/u/44311524?v=4") 
    
    
#QRcodes
@dp.message_handler(commands=['qr'])
async def qr(message: types.Message):
    text = pyqrcode.create(message.text)
    text.png('code.png', scale=5)
    await support_bot.send_photo(chat_id=message.chat.id, photo=open('code.png', 'rb'))    

    



# Executor commands 
if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)