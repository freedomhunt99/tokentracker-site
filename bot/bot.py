import asyncio
from aiogram import Bot, Dispatcher, F
from aiogram.enums import ParseMode
from aiogram.types import Message, ReplyKeyboardMarkup, KeyboardButton, FSInputFile
from aiogram.utils.keyboard import ReplyKeyboardBuilder
from aiogram.client.default import DefaultBotProperties
from aiogram.filters import Command
from aiogram.filters.command import CommandObject

TOKEN = "7935011116:AAFNde-V4vbtl_uk3ZjAZM3uPS36-OaDgus"  # 🔁 Заміни на свій токен
ADMIN_ID = 8187961356  # 🔁 Заміни на свій Telegram user_id

bot = Bot(
    token=TOKEN,
    default=DefaultBotProperties(parse_mode=ParseMode.HTML)
)

dp = Dispatcher()

def main_keyboard() -> ReplyKeyboardMarkup:
    kb = ReplyKeyboardBuilder()
    kb.button(text="⚙️ Как работает TokenTracker") 
    kb.button(text="🚀 Возможности")
    kb.button(text="🧪 Бета-доступ")   
    kb.button(text="💬 Поддержка")
    kb.button(text="🌐 Вебсайт")
    kb.adjust(2)
    return kb.as_markup(resize_keyboard=True)

@dp.message(F.text == "/start")
async def start(msg: Message):
    banner = FSInputFile("assets/banner.png")
    await msg.answer_photo(
        photo=banner,
        caption=(
            "👋 <b>Добро пожаловать в TokenTracker</b>\n\n"
            "🧠 Это больше, чем трекер токенов.\n"
            "Это твой персональный инструмент для:\n"
            "• Анализа китов и балансов\n"
            "• AI-обработки данных без логинов\n"
            "• Мониторинга телеграма и медиа\n"
            "• Реального отслеживания разработчиков\n\n"
            "⚙️ Работает локально. Никаких утечек. Никаких фейков.\n\n"
            "⬇️ Выбери, с чего начать:"
        ),
        reply_markup=main_keyboard()
    )

@dp.message(F.text == "🚀 Возможности")
async def features(msg: Message):
    await msg.answer(
        "<b>🚀 Что умеет TokenTracker:</b>\n\n"
        "🐋 <b>Анализ китов</b>\nТрекинг крупных кошельков: входы, выходы, накопления.\n\n"
        "👨‍💻 <b>Мониторинг девелопера</b>\nПроверка контрактов, свапов, действий разработчика.\n\n"
        "⚖️ <b>Разведка по балансу</b>\nДвижения холдеров, аномалии, рост/падение балансов.\n\n"
        "🧠 <b>Локальный AI-анализ</b>\nОбработка данных на ПК — без API и логинов. Мозг на базе Genspark LLM.\n\n"
        "📈 <b>Аналитика TVL</b>\nИзменения ликвидности токенов в реальном времени. Дашборды.\n\n"
        "📣 <b>Telegram мониторинг</b>\nАнализ упоминаний токенов в чатах. Настроения, активность, волны обсуждений.\n\n"
        "🔔 <b>Алёрты по медиа</b>\nРезкие всплески на Cointelegraph, X/Twitter, Reddit — сразу в уведомления.\n\n"
        "🧾 <b>Трекинг разработчиков</b>\nGitHub, Discord, Notion, изменения смарт-контрактов и документации.\n\n"
        "🎒 <b>Кастомный портфель</b>\nДобавляй свои токены и кошельки — отслеживай активность персонально."
    )

@dp.message(F.text == "⚙️ Как работает TokenTracker")
async def how_it_works(msg: Message):
    await msg.answer(
        "<b>⚙️ Как работает TokenTracker:</b>\n\n"
        "1️⃣ <b>Вводишь адрес токена</b>\nИли выбираешь из популярных. Работает с Ethereum, BNB, Arbitrum, Solana и др.\n\n"
        "2️⃣ <b>Получаешь дашборд</b>\nКрупные кошельки, транзакции, балансы, активность разработчиков.\n\n"
        "3️⃣ <b>Настраиваешь алерты</b>\nЗакупки китов, выводы, подозрительная активность.\n\n"
        "🧠 Все данные обрабатываются локально, без API."
    )

@dp.message(F.text == "🧪 Бета-доступ")
async def beta_start(msg: Message):
    kb = ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text="📱 Поделиться номером", request_contact=True)]
        ],
        resize_keyboard=True,
        one_time_keyboard=True
    )
    await msg.answer(
        "🧪 Для участия в бета-доступе нужно подтвердить себя.\n\nНажми кнопку ниже, чтобы поделиться номером телефона:",
        reply_markup=kb
    )

@dp.message(F.contact)
async def handle_contact(msg: Message):
    phone = msg.contact.phone_number
    user = msg.from_user
    print(f"User {user.full_name} ({user.id}) поделился номером: {phone}")

    await msg.answer(
        "✅ Спасибо! Доступ к бета-версии открыт.\n\n🔽 Ссылка на загрузку: https://example.com/download",
        reply_markup=main_keyboard()
    )

@dp.message(F.text == "💬 Поддержка")
async def support_intro(msg: Message):
    await msg.answer(
        "📨 Напиши свой вопрос сюда. Мы ответим как можно скорее.\n\n✍️ Просто отправь сообщение — и оно попадёт в поддержку."
    )


@dp.message(Command("ответ"))
async def reply_to_user(msg: Message, command: CommandObject):
    print("[DEBUG] /ответ активовано")

    if not command.args:
        await msg.answer("⚠️ Формат: /ответ <user_id> <текст>")
        return

    parts = command.args.split(maxsplit=1)
    if len(parts) < 2:
        await msg.answer("⚠️ Формат: /ответ <user_id> <текст>")
        return

    user_id, reply_text = parts
    try:
        await bot.send_message(chat_id=int(user_id), text=f"💬 <b>Ответ поддержки:</b>\n\n{reply_text}")
        await msg.answer("✅ Ответ отправлен.")
        print(f"[LOG] Відповідь надіслано користувачу {user_id}")
    except Exception as e:
        await msg.answer(f"❌ Ошибка: {e}")
        print(f"[ERROR]: {e}")


@dp.message(F.text & ~F.chat.type.in_({"channel"}))
async def forward_to_admin(msg: Message):
    if msg.from_user.id == ADMIN_ID:
        return

    text = (
        f"📩 <b>Новое сообщение:</b>\n"
        f"<b>Имя:</b> {msg.from_user.full_name}\n"
        f"<b>ID:</b> <code>{msg.from_user.id}</code>\n\n"
        f"{msg.text}"
    )
    await bot.send_message(ADMIN_ID, text)
    await msg.answer("✅ Ваше сообщение передано в поддержку.")

@dp.message(F.text == "🌐 Вебсайт")
async def website(msg: Message):
    await msg.answer("🌐 Наш сайт: https://example.com")


@dp.message(F.text)
async def fallback(msg: Message):
    if msg.text.startswith("/"):
        return
    await msg.answer("❓ Выбери команду из меню ниже 👇", reply_markup=main_keyboard())

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())