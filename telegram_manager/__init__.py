import telegram
from config import settings

bot = telegram.Bot(token=settings.telegram_token)


def send_pic(photo_path: str, text: str) -> bool:
    bot.send_photo(photo=open(photo_path, 'rb'), caption=f"Appena aggiunto {text}!", chat_id=settings.telegram_channel_id)


