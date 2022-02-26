import telegram

bot = telegram.Bot(token='5258719252:AAEQ3oQCu3e3B_Xnd5JYIcIO4mIHkfm2hwU')


def send_pic(photo_path: str, text: str) -> bool:
    bot.send_photo(photo=open(photo_path, 'rb'), caption=f"Appena aggiunto {text}!", chat_id="-707664914")


