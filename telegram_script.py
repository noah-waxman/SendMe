import telegram

my_token = '5475591066:AAFMuPS5p13AAyWcfpSHP41Gg6Tq2E2nfKM'

def send(msg, chat_id, token=my_token):
    """
    Send a mensage to a telegram user specified on chatId
    chat_id must be a number!
    """
    bot = telegram.Bot(token=token)
    bot.sendMessage(chat_id=chat_id, text=msg)
