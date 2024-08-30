from vkbottle.bot import Bot, Message
from VKconfig import TOKEN
import VKbutton as vbt

bot = Bot(token=TOKEN)


@bot.on.message(text="Вернуться к главному меню")
async def start_message(message: Message):
    await message.answer('''Продолжим знакомство с нашей компанией!🚇
Что еще тебя интересует?👨‍💻''', keyboard=vbt.start_button())

@bot.on.message(text="Начать" or "/start")
async def start_message(message: Message):
    await message.answer('''Добро пожаловать!👤
Я - бот комапнии IPMLogist🚝, буду сопровождать тебя, чтобы рассказать о нашей компании.
Что тебя интересует?👨‍💻''', keyboard=vbt.start_button())

@bot.on.message(text="Наш сайт")
async def weblog(message: Message):
    await message.answer('''🌍Это наш сайт: 
https://ipmlogist.com. 
Ознакомься с тем, чем занимается наша компания🚢''', keyboard=vbt.back_menu())

@bot.on.message(text="Контакты")
async def contacts(message: Message):
    await message.answer('''Контакты для связи с нами:
📧Почта - office@ipmlogist.ru
✅Мы вконтакте - vk.com/ipmlogist
📞Номер телефона - +74953238868
🕙График работы с 9:00 до 20:00
🏢Наш адрес - г. Москва, м. Румянцево, ул. 22 километр Киевское шоссе, вл 4 блок А''', keyboard=vbt.back_menu())

@bot.on.message(text="Презентация компании")
async def presa(message: Message):
    await message.answer('''Это презентация нашей компании📚:
https://ipmlogist.com/ВАКАНСИИ/img_vacancy/Презентация%20FAW%20J7.pdf
Ознакомься, чтобы понимать кто мы такие👥''', keyboard=vbt.back_menu())

@bot.on.message(text="О нас")
async def more(message: Message):
    await message.answer('''История компании:
IPMLogist взяла свой старт 14 июля 2017 года с приобретением первой газели, и с тех пор стабильно следует своим принципам:

- надежность,
- стабильность,
- полный контроль,
- инновации,
- постоянное развитие

IPMLogist сегодня:
Стабильная компания, основанная на высоких стандартах качества обслуживания и надежности
Еще с начала зарождения компании, мы знали, что наша миссия заключается в том, чтобы стать надежным партнером и предложить контрагентам самые лучшие стандарты логистических услуг''', keyboard=vbt.back_menu())


@bot.on.message(text="Закончить знакомство с компанией")
async def log_out(message: Message):
    await message.answer('''Рад был ознакомить с нашей компанией!👨‍🏫
Наши контакты для связи:
📧Почта - office@ipmlogist.ru
✅Мы вконтакте - vk.com/ipmlogist
📞Номер телефона - +74953238868
🕙График работы с 9:00 до 20:00
🏢Наш адрес - г. Москва, м. Румянцево, ул. 22 километр Киевское шоссе, вл 4 блок А''', keyboard=vbt.out_start())
  
if __name__ == "__main__":
  bot.run_forever()
