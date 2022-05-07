from email import message
import config
import markup_handles
from aiogram import Bot, Dispatcher, executor, types


#Support Team message handler
def support_answer(user_id, support_bot, message):
    if message.content_type == 'text':
        first_name = message.from_user.first_name
        support_bot.answer_chat_action(user_id, 'typing')
        support_bot.answer(user_id, \
            config.text_messages[''].format(message.get_chat(user_id).first_name) + f'\n\n{message.text}', parse_mode='Markdown', 
            disable_web_page_preview=True)
    
    elif message.content_type == 'photo':
        support_bot.send_chat_action(user_id, 'upload_photo')
        support_bot.send_photo(user_id, message.photo[-1].file_id,caption=config.text_messages['support_response'].format(support_bot.get_chat(user_id).first_name) + f'\n\n{msgCaption(message)}',parse_mode='Markdown')

    elif message.content_type == 'document':
        support_bot.send_chat_action(user_id, 'upload_document')
        support_bot.send_document(user_id, message.document.file_id,caption=config.text_messages['support_response'].format(support_bot.get_chat(user_id).first_name) + f'\n\n{msgCaption(message)}',parse_mode='Markdown')
    else:
        pass
