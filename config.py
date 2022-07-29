import os
from dotenv import load_dotenv

load_dotenv()
BOT_TOKEN = os.getenv('BOT_TOKEN')
TASK_SPREADSHEET = os.getenv('TASK_SPREADSHEET')
# можно засунуть нужные ссылки для бота

print(BOT_TOKEN)
print(TASK_SPREADSHEET)
