import asyncio
import telegram
import os
from dotenv import load_dotenv

load_dotenv()
api_token = os.environ.get('TELEGRAM_API_TOKEN')
chat_id = os.environ.get('MY_CHAT_ID')

async def main():
    bot = telegram.Bot(api_token)
    async with bot:
        await bot.send_message(text='Hi Bianca!', chat_id=chat_id)

if __name__ == '__main__':
    asyncio.run(main())