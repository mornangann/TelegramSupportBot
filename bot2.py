import logging
import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.utils.media_group import MediaGroupBuilder

# Токен бота
TOKEN = "7759560584:AAGLdRQkKSDSORJzwmf0TqQmR8hH0thcFWA"

# ID группы поддержки
SUPPORT_CHAT_ID = -1002528638847

# Логирование
logging.basicConfig(level=logging.INFO)

# Инициализация бота и диспетчера
bot = Bot(token=TOKEN)
dp = Dispatcher()

# Основная клавиатура с проблемами
menu_keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="🖨 Проблемы с принтером")],
        [KeyboardButton(text="💻 Проблемы в работе компьютера")],
        [KeyboardButton(text="📲 Установка")],
        [KeyboardButton(text="🖥 Терминальная станция")],
        [KeyboardButton(text="⚒️ Не работает ИС")],
        [KeyboardButton(text="🔨 Проблемы в работе ИС")],     
#        [KeyboardButton(text="🖊 Проблемы с электронной подписью")],   
        [KeyboardButton(text="❌ Проблема не решена")]
    ],
    resize_keyboard=True
)

# Клавиатура для выбора проблем с принтером
printer_keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="🖨 Принтер не печатает")],
        [KeyboardButton(text="📃 Принтер зажевывает бумагу")],
        [KeyboardButton(text="⁉️ Принтер печататет с дефектами")],
        [KeyboardButton(text="📄 Принтер не захватывает бумагу")],
        [KeyboardButton(text="🔌 Принтер отсутствует в системе")],
        [KeyboardButton(text="🔍 Принтер не отображается")],
        [KeyboardButton(text="🔙 Назад")]
    ],
    resize_keyboard=True
)

# Клавиатура для выбора вариантов установки ПО
installation_keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="💻 Установка ПО Офис")],
        [KeyboardButton(text="📊 Установка ПО МИС Ариадна")],
        [KeyboardButton(text="📈 Установка ПО РИС Ариадна")],
        [KeyboardButton(text="🔬 Установка ПО ЛИС АкроссЛАБ")],
        [KeyboardButton(text="📥 Установка другого ПО")],
        [KeyboardButton(text="🔙 Назад")]
    ],
    resize_keyboard=True
)


# Клавиатура не работает ИС
doesntwork_keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="📊 Не работает МИС Ариадна")],
        [KeyboardButton(text="📈 Не работает РИС Архимед")],
        [KeyboardButton(text="🔬 Не работает ЛИС АкроссЛАБ")],
        [KeyboardButton(text="📥 Не работает другая ИС")],
        [KeyboardButton(text="🔙 Назад")]
    ],
    resize_keyboard=True
)

# Клавиатура проблемы в работе ИС
problemwork_keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="📊 Проблемы в работе МИС Ариадна")],
        [KeyboardButton(text="📈 Проблемы в работе РИС Архимед")],
        [KeyboardButton(text="🔬 Проблемы в работе ЛИС АкроссЛАБ")],
        [KeyboardButton(text="📥 Проблемы в работе другой ИС")],
        [KeyboardButton(text="🔙 Назад")]
    ],
    resize_keyboard=True
)


# терминальная станция
terminalst_keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="💾 Терминальная станция зависла")],
        [KeyboardButton(text="🖥 Терминальная станция не включается")],
        [KeyboardButton(text="🔙 Назад")]
    ],
    resize_keyboard=True
)

# проблемы с компьютером
PKproblem_keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="🎞 Монитор изображение с дефектами")],
        [KeyboardButton(text="🖥 Компьютер не включается")],
        [KeyboardButton(text="⚙️ Компьютер с неисправностями")],
        [KeyboardButton(text="🔙 Назад")]
    ],
    resize_keyboard=True
)

# Эл.подпись
#signature_keyboard = ReplyKeyboardMarkup(
#    keyboard=[
#        [KeyboardButton(text="🖌 Не подписывает документ")],
#        [KeyboardButton(text="🖋 Не высвечивается в контейнере")],
#        [KeyboardButton(text="🖋 Другая система ЛЛО\УМРС\1С\др")],
#        [KeyboardButton(text="🔙 Назад")]
#    ],
#    resize_keyboard=True
#)

# Макет заявки
TEMPLATE_TEXT = (
    "🔹 Скопируйте данное сообщение и заполните все поля:\n\n"
    "**IP Адрес:** \n"
    "**Имя пользователя:** \n"
    "**Имя компьютера:** \n"
    "**MAC Адрес:** \n"
    "**Домен:** \n"
    "**Отделение:** \n"
    "**Опишите вашу проблему или ошибку, появившуюся на экране:** \n\n"
    "Вы также можете добавить одно фото к вашей заявке."
)

# Команда /start
@dp.message(Command("start"))
async def start_command(message: types.Message):
    await message.answer("Выберите пункт в соотвествии с возникшей проблемой.", reply_markup=menu_keyboard)

# Обработчик выбора проблемы с принтером
@dp.message(lambda message: message.text == "🖨 Проблемы с принтером")
async def problem_with_printer(message: types.Message):
    await message.answer("Выберите тип проблемы с принтером:", reply_markup=printer_keyboard)

# Ответы на конкретные проблемы с принтером
@dp.message(lambda message: message.text == "🖨 Принтер не печатает")
async def printer_not_printing(message: types.Message):
    await message.answer("Попробуйте проверить подключение принтера к компьютеру и его статус.")

@dp.message(lambda message: message.text == "📃 Принтер зажевывает бумагу")
async def printer_not_turning_on(message: types.Message):
    await message.answer("Проверьте подключение к сети и работоспособность кнопки включения.")

@dp.message(lambda message: message.text == "⁉️ Принтер печататет с дефектами")
async def printer_defects(message: types.Message):
    await message.answer("Попробуйте перезагрузить компьютер и проверить настройки устройства.")

@dp.message(lambda message: message.text == "📄 Принтер не захватывает бумагу")
async def printer_not_peper(message: types.Message):
    await message.answer("Попробуйте проверить подключение принтера к компьютеру и его статус.")

@dp.message(lambda message: message.text == "🔌 Принтер отсутствует в системе")
async def printer_not_system(message: types.Message):
    await message.answer("Проверьте подключение к сети и работоспособность кнопки включения.")

@dp.message(lambda message: message.text == "🔍 Принтер не отображается")
async def printer_not_displaying(message: types.Message):
    await message.answer("Попробуйте перезагрузить компьютер и проверить настройки устройства.")

# Обработчик выбора на установку ПО
@dp.message(lambda message: message.text == "📲 Установка")
async def mis_ariadna_installation(message: types.Message):
    await message.answer("Выберите то, что нужно установить", reply_markup=installation_keyboard)

# Ответы на установку ПО
@dp.message(lambda message: message.text == "💻 Установка ПО Офис")
async def office_installation(message: types.Message):
    await message.answer("Убедитесь, что у вас есть лицензионный ключ для установки ПО Офис.")

@dp.message(lambda message: message.text == "📊 Установка ПО МИС Ариадна")
async def mis_ariadna_installation(message: types.Message):
    await message.answer("Проверьте, что у вас есть доступ к установочным файлам МИС Ариадна.")

@dp.message(lambda message: message.text == "📈 Установка ПО РИС Ариадна")
async def ris_ariadna_installation(message: types.Message):
    await message.answer("Для установки ПО РИС Ариадна убедитесь, что все необходимые пакеты уже на месте.")

@dp.message(lambda message: message.text == "🔬 Установка ПО ЛИС АкроссЛАБ")
async def lis_acrosslab_installation(message: types.Message):
    await message.answer("Убедитесь, что ваше оборудование совместимо с ПО ЛИС АкроссЛАБ.")

@dp.message(lambda message: message.text == "📥 Установка другого ПО")
async def other_software_installation(message: types.Message):
    await message.answer("Пожалуйста, уточните, какое ПО нужно установить.")

# Обработчик выбора на Не работает ИС
@dp.message(lambda message: message.text == "⚒️ Не работает ИС")
async def mis_dont_work(message: types.Message):
    await message.answer("Выберите то, что нужно починить", reply_markup=doesntwork_keyboard)

# Ответы на Не работает ИС
@dp.message(lambda message: message.text == "📊 Не работает МИС Ариадна")
async def office_installation(message: types.Message):
    await message.answer("Убедитесь, что у вас есть лицензионный ключ для установки ПО Офис.")

@dp.message(lambda message: message.text == "📈 Не работает РИС Архимед")
async def mis_ariadna_installation(message: types.Message):
    await message.answer("Проверьте, что у вас есть доступ к установочным файлам МИС Ариадна.")

@dp.message(lambda message: message.text == "🔬 Не работает ЛИС АкроссЛАБ")
async def ris_ariadna_installation(message: types.Message):
    await message.answer("Для установки ПО РИС Ариадна убедитесь, что все необходимые пакеты уже на месте.")

@dp.message(lambda message: message.text == "📥 Не работает другая ИС")
async def lis_acrosslab_installation(message: types.Message):
    await message.answer("Убедитесь, что ваше оборудование совместимо с ПО ЛИС АкроссЛАБ.")


# Обработчик выбора на проблемы в работе ИС
@dp.message(lambda message: message.text == "🔨 Проблемы в работе ИС")
async def mis_problem_work(message: types.Message):
    await message.answer("Выберите то, что нужно починить", reply_markup=problemwork_keyboard)

# Ответы на Проблемы в работе  ИС
@dp.message(lambda message: message.text == "📊 Проблемы в работе МИС Ариадна")
async def problem_mis_IS(message: types.Message):
    await message.answer("Убедитесь, что у вас есть лицензионный ключ для установки ПО Офис.")

@dp.message(lambda message: message.text == "📈 Проблемы в работе РИС Архимед")
async def problem_ris_IS(message: types.Message):
    await message.answer("Проверьте, что у вас есть доступ к установочным файлам МИС Ариадна.")

@dp.message(lambda message: message.text == "🔬 Проблемы в работе ЛИС АкроссЛАБ")
async def problem_AcrossLAB(message: types.Message):
    await message.answer("Для установки ПО РИС Ариадна убедитесь, что все необходимые пакеты уже на месте.")

@dp.message(lambda message: message.text == "📥 Проблемы в работе другой ИС")
async def problem_other_IC(message: types.Message):
    await message.answer("Убедитесь, что ваше оборудование совместимо с ПО ЛИС АкроссЛАБ.")


# Обработчик выбора терминальная станция
@dp.message(lambda message: message.text == "🖥 Терминальная станция")
async def terminal_station_work(message: types.Message):
    await message.answer("Выберите то, что нужно починить", reply_markup=terminalst_keyboard)

# Ответы на терминальная станция
@dp.message(lambda message: message.text == "💾 Терминальная станция зависла")
async def hungup_terminalst(message: types.Message):
    await message.answer("Убедитесь, что у вас есть лицензионный ключ для установки ПО Офис.")

@dp.message(lambda message: message.text == "🖥 Терминальная станция не включается")
async def doesnt_turn_on_terminalst(message: types.Message):
    await message.answer("Проверьте, что у вас есть доступ к установочным файлам МИС Ариадна.")


# Обработчик выбора проблемы с ПК
@dp.message(lambda message: message.text == "💻 Проблемы в работе компьютера")
async def mis_problem_work(message: types.Message):
    await message.answer("Выберите то, что нужно починить", reply_markup=PKproblem_keyboard)

# Ответы на Проблемы с ПК
@dp.message(lambda message: message.text == "🎞 Монитор изображение с дефектами")
async def problem_picture_def(message: types.Message):
    await message.answer("Убедитесь, что у вас есть лицензионный ключ для установки ПО Офис.")

@dp.message(lambda message: message.text == "🖥 Компьютер не включается")
async def computer_doesnt_work(message: types.Message):
    await message.answer("Проверьте, что у вас есть доступ к установочным файлам МИС Ариадна.")

@dp.message(lambda message: message.text == "⚙️ Компьютер с неисправностями")
async def computer_malfunction(message: types.Message):
    await message.answer("Для установки ПО РИС Ариадна убедитесь, что все необходимые пакеты уже на месте.")



# Кнопка "Назад"
@dp.message(lambda message: message.text == "🔙 Назад")
async def back_to_main_menu(message: types.Message):
    await message.answer("Выберите одну из следующих опций:", reply_markup=menu_keyboard)


# Обработчик кнопки "Проблема не решена"
@dp.message(lambda message: message.text == "❌ Проблема не решена")
async def send_issue_template(message: types.Message):
    await message.answer(TEMPLATE_TEXT, parse_mode="Markdown")

# Проверка заполненности заявки
def is_valid_issue(text: str) -> bool:
    required_fields = ["IP Адрес", "Имя пользователя", "Имя компьютера", "MAC Адрес", "Домен", "Отделение", "Опишите вашу проблему"]
    return all(field in text for field in required_fields)

# Обработчик текстовых заявок
@dp.message(lambda message: message.text and not message.photo)
async def handle_text_issue(message: types.Message):
    """Обрабатывает текстовую заявку"""
    
    if not is_valid_issue(message.text):
        await message.answer("⚠️ Ваше сообщение не соответствует макету! Пожалуйста, заполните все поля и отправьте снова.", parse_mode="Markdown")
        return

    user_info = f"👤 {message.from_user.full_name} (@{message.from_user.username}) отправил заявку:\n\n"
    issue_text = user_info + message.text

    await bot.send_message(SUPPORT_CHAT_ID, issue_text, parse_mode="Markdown")

    # Ответ пользователю
    support_group_link = "https://t.me/+ug7iZf6Jh5E5ZWNi"  
    response_text = (
        "✅ Ваша заявка отправлена в техподдержку. Ожидайте ответа в теме - ТП инфосистем ГМБ.\n\n"
        f"🔗 <a href='{support_group_link}'>Перейти в группу поддержки</a>"
    )
    await message.answer(response_text, parse_mode="HTML")

# Обработчик заявок с фото
@dp.message(lambda message: message.photo)
async def handle_photo_issue(message: types.Message):
    """Обрабатывает заявку с фото"""
    
    if not message.caption or not is_valid_issue(message.caption):
        await message.answer("⚠️ Вы должны отправить фото вместе с заполненным макетом!", parse_mode="Markdown")
        return

    user_info = f"👤 {message.from_user.full_name} (@{message.from_user.username}) отправил заявку:\n\n"
    issue_text = user_info + message.caption

    # Отправляем фото с подписью (макетом)
    photo = message.photo[-1]  # Берем последнее фото из списка
    await bot.send_photo(SUPPORT_CHAT_ID, photo.file_id, caption=issue_text, parse_mode="Markdown")

    # Ответ пользователю
    support_group_link = "https://t.me/+ug7iZf6Jh5E5ZWNi" 
    response_text = (
        "✅ Ваша заявка отправлена в техподдержку. Ожидайте ответа.\n\n"
        f"🔗 <a href='{support_group_link}'>Перейти в группу поддержки</a>"
    )
    await message.answer(response_text, parse_mode="HTML")

# Запуск бота
async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())