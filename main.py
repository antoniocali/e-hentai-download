from telegram.ext import CommandHandler, CallbackContext
from telegram.ext import Updater
from telegram import Update
from telegram_manager import telegram_download
from config import settings
import logging

from download_manager import get_info
from utils import check_ehentai

base_path = settings.base_path

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO
)
logger = logging.getLogger(__name__)


def main():
    updater = Updater(token=settings.telegram_token, use_context=True)
    dispatcher = updater.dispatcher
    download_handler = CommandHandler("download", callback=accept_comics)
    dispatcher.add_handler(download_handler)
    updater.start_polling()
    updater.idle()


def accept_comics(update: Update, context: CallbackContext):
    comics = [c for c in update.message.text.split(" ")[1:] if check_ehentai(c)]
    for comic in comics:
        info = get_info(comic)
        update.message.reply_text(f"Starting to download {info.title}")
        telegram_download(bot=context.bot, base_path=base_path, info=info)


if __name__ == '__main__':
    main()
