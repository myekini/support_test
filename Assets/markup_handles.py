from aiogram.types import ReplyKeyboardMarkup, ReplyKeyboardRemove, KeyboardButton
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


keyboard_markup = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton('Chat', callback_data='ChatCallbackdata')],
        [InlineKeyboardButton('Read our FAQ\'s', callback_data='faqCallbackdata')],
        [InlineKeyboardButton('Emails', callback_data='EmailCallbackdata')]
    ]

)



