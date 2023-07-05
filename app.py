# imports from tutorial
import logging
from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler

# additional imports
import os
from dotenv import load_dotenv

load_dotenv()
api_token = os.environ.get('TELEGRAM_API_TOKEN')

# For error logging:
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

# Defining a function that performs some sort of feature
# This function will be called when user uses the '/start' command.
# update parameter: object containing info and data from TG
# context parameter: object containing info and data about status of library itself
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id, text="I'm a bot, please talk to me!")

if __name__ == '__main__':

    # Creating an application object
    application = ApplicationBuilder().token(api_token).build()
    
    # CommandHandler listens for commands
    start_handler = CommandHandler('start', start)
    application.add_handler(start_handler)
    
    # Runs the bot until you cancel out of it.
    application.run_polling()