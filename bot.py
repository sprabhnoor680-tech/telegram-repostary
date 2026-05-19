import logging
import os
from telegram import Update
from telegram.ext import (
    ApplicationBuilder,
    MessageHandler,
    ContextTypes,
    filters,
)

BOT_TOKEN = os.environ.get("BOT_TOKEN")
if not BOT_TOKEN:
    raise RuntimeError("BOT_TOKEN environment variable is not set")

# KEYWORD REPLIES - edit these as you like
KEYWORD_REPLIES = {
    "hello": "Hello! Welcome to our channel.",
    "hi": "Hi there! How can I help you?",
    "price": "bhai apko 500 mai vip ka access miljayega",
    "buy": "To buy, contact us at @yourusername",
    "help": "Type price, buy, or contact for info.",
    "contact": "Contact us at @yourusername",
    "thanks": "You are welcome!",
}

# DEFAULT reply when no keyword matches
DEFAULT_REPLY = (
    "Thanks for your message! "
    "Type 'help' to see what I can do."
)

logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,
)
logger = logging.getLogger(__name__)


async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_text = update.message.text.lower().strip()
    user_name = update.effective_user.first_name or "there"
    logger.info(f"Message from {user_name}: {user_text}")

    reply = None
    for keyword, response in KEYWORD_REPLIES.items():
        if keyword in user_text:
            reply = response
            break

    if reply is None:
        reply = DEFAULT_REPLY

    await update.message.reply_text(reply)


def main():
    app = ApplicationBuilder().token(BOT_TOKEN).build()
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))
    logger.info("Bot is running...")
    app.run_polling()


if __name__ == "__main__":
    main()
