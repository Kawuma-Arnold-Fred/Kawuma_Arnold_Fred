import asyncio
import os
import logging
import traceback
from telegram import Update
from telegram.ext import (
    Application,
    CommandHandler,
    ContextTypes,
)
import randfacts
from dotenv import load_dotenv

load_dotenv()


# Logging setup with more detailed formatting
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
logger = logging.getLogger(__name__)

# Your bot token and channel/group ID
TOKEN = os.getenv('TELEGRAM_BOT_TOKEN')
CHAT_ID = int(os.getenv('TELEGRAM_CHAT_ID', '0'))

# Global variable to store the application instance
app = None

# /start command handler
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    chat_info = f"Chat ID: {update.effective_chat.id}, Type: {update.effective_chat.type}"
    logger.info(f"Start command received in {chat_info}")
    
    try:
        await update.message.reply_text(
            f"Hey there! Bot is up and running.\n"
            f"Current chat ID: `{update.effective_chat.id}`\n"
            f"Chat type: {update.effective_chat.type}\n"
            f"I'll be posting random facts every minute to chat ID: `{CHAT_ID}`",
            parse_mode='Markdown'
        )
    except Exception as e:
        logger.error(f"Error in start command: {e}")

# /post command handler for manual posting
async def post_now(update: Update, context: ContextTypes.DEFAULT_TYPE):
    logger.info(f"Manual post requested by user {update.effective_user.id}")
    try:
        fact = randfacts.get_fact()
        await context.bot.send_message(
            chat_id=CHAT_ID, 
            text=f"**Random Fact:**\n\n{fact}",
            parse_mode='Markdown'
        )
        await update.message.reply_text("Done! Posted a fact to the target chat.")
        logger.info("Manual fact posted successfully")
    except Exception as e:
        logger.error(f"Error in manual posting: {e}")
        await update.message.reply_text(f"Oops, something went wrong: {e}")

#  /info command to check bot status 
async def info(update: Update, context: ContextTypes.DEFAULT_TYPE):
    chat_info = (
        f"**Bot Information:**\n"
        f"Current chat ID: `{update.effective_chat.id}`\n"
        f"Current chat type: {update.effective_chat.type}\n"
        f"Target posting chat ID: `{CHAT_ID}`\n"
        f"Your user ID: `{update.effective_user.id}`\n"
        f"Chat title: {update.effective_chat.title or 'Not available'}"
    )
    try:
        await update.message.reply_text(chat_info, parse_mode='Markdown')
    except Exception as e:
        logger.error(f"Error in info command: {e}")


# Function to post random fact automatically
async def post_random_fact():
    global app
    try:
        fact = randfacts.get_fact()
        message = await app.bot.send_message(
            chat_id=CHAT_ID, 
            text=f"**Random Fact:**\n\n{fact}",
            parse_mode='Markdown'
        )
        logger.info(f"Posted scheduled fact successfully. Message ID: {message.message_id}")
    except Exception as e:
        logger.error(f"Error posting scheduled fact: {e}")
        logger.error(f"Full traceback: {traceback.format_exc()}")

#  Background task for periodic posting 
async def periodic_poster():
    logger.info("Starting periodic poster...")
    await asyncio.sleep(30)  # Wait 30 seconds before first post
    
    while True:
        try:
            await post_random_fact()
            await asyncio.sleep(60)  # Wait 60 seconds between posts
        except Exception as e:
            logger.error(f"Error in periodic poster: {e}")
            await asyncio.sleep(60)  # Wait before retrying

#  Main function
async def main():
    global app
    
    if not TOKEN or TOKEN == 'YOUR_BOT_TOKEN_HERE':
        logger.error("Please set your bot token in the TOKEN variable!")
        return
    
    logger.info("Starting Telegram bot...")
    
    # Create application
    app = Application.builder().token(TOKEN).build()
    
    # Add handlers
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("post", post_now))
    app.add_handler(CommandHandler("info", info))
    
    
    try:
        # Initialize and start the application
        await app.initialize()
        await app.start()
        
        # Test bot connection
        bot_info = await app.bot.get_me()
        logger.info(f"Bot connected successfully: @{bot_info.username}")
        
        # Start the periodic posting task
        asyncio.create_task(periodic_poster())
        
        # Start polling for updates
        await app.updater.start_polling()
        
        logger.info("Bot is now running and listening for commands...")
        logger.info(f"Will post facts to chat ID: {CHAT_ID}")
        
        # Keep the bot running until interrupted
        try:
            # This will wait indefinitely until the program is interrupted
            while True:
                await asyncio.sleep(1)
        except KeyboardInterrupt:
            logger.info("Received shutdown signal")
        finally:
            # Clean shutdown
            await app.updater.stop()
            await app.stop()
            await app.shutdown()
        
    except Exception as e:
        logger.error(f"Failed to start bot: {e}")
        logger.error(traceback.format_exc())

# Entry point 
if __name__ == "__main__":
    import sys
    
    # Handle Windows event loop policy for Python 3.8+
    if sys.platform.startswith('win') and sys.version_info >= (3, 8):
        asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
    
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        logger.info("Bot stopped by user")
    except Exception as e:
        logger.error(f"Bot crashed: {e}")
        logger.error(traceback.format_exc())