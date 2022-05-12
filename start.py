from main import dp

dict_sample = {
    'привет' : 'Привет я бот',
    'твое имя' : 'R2D2'
}


@dp.message_handler(content_types=['text'])
async def start(message):
    key = message.text
    if key in dict_sample.keys():
        await message.answer(dict_sample[key])
    else:
        await message.answer('Ответ не найден')