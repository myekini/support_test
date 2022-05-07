import config
import logging
import emoji
from aiogram import Bot, Dispatcher, executor, types
from Assets import markup_handles as markup

# Configure logging
logging.basicConfig(level=logging.INFO)
# Initialize bot and dispatcher
support_bot = Bot(token=config.bot_token)
dp = Dispatcher(support_bot)


#Callback handler for start command
@dp.callback_query_handler(text=["ChatCallbackdata", "faqCallbackdata", "EmailCallbackdata"])
async def start_answer(call: types.CallbackQuery):
    if call.data == "ChatCallbackdata":
        await call.message.reply("Hi, welcome to MOBI Support! How may i help you \N{FLEXED BICEPS}")
    elif call.data == "faqCallbackdata":
        await call.message.reply(str(config.faqs))

    elif call.data == "EmailCallbackdata":
        await call.message.reply("We are currently not sending emails now. sorry about that \U0001f625")
    await call.answer()

 
# start and help commands 
@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    if message.chat.type == 'private':
        await message.reply(config.text_messages['start'].format(message.from_user.first_name), reply_markup=markup.keyboard_markup, parse_mode='Markdown', disable_web_page_preview=True)
    else:
        pass

#FAQs commands
@dp.message_handler(commands=['faqs'])
async def send_welcome(message: types.Message):
    if message.chat.type == 'private':
        await message.reply(str(config.faqs), parse_mode='Markdown', disable_web_page_preview=True)
    else:
        pass


# Executor commands 
if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)