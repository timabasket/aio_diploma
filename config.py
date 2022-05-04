import os
from dotenv import load_dotenv

load_dotenv()
BOT_TOKEN = os.getenv('BOT_TOKEN')
# можно засунуть нужные ссылки для бота

print(BOT_TOKEN)