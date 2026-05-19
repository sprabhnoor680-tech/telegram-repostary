import logging
from telegram import Update
from telegram.ext import (
    ApplicationBuilder,
    MessageHandler,
    ContextTypes,
    filters,
)

# ─────────────────────────────────────────
#  🔑  PUT YOUR BOT TOKEN HERE
# ─────────────────────────────────────────
BOT_TOKEN = "8773270728:AAHWzJ9xkYemp52PtpRJ8EUJXTBQQyIHVD8"

# ─────────────────────────────────────────
#  💬  KEYWORD → REPLY  (edit freely!)
#  Keys are lowercase; matching is case-insensitive.
# ─────────────────────────────────────────
KEYWORD_REPLIES = {
    "hello": "👋 hnji bhai kitna loss hai apka ??",
    "price": "💰 bhai merr vip k liye minimum 500 agar 300 to hack ka access miljayEGA
    "buy": "🛒 To buy, please visit: @uvipandat,
    "help": "🆘 Here are the commands you can use:\n• 'price' – view pricing\n• 'buy' – purchase a plan\n• 'contact' – get our contact info\n• 'hours' – working hours",
    "contact": "📞 You can reach us at:\n• Email: support@example.com\n• Telegram: @yourusername\n• Phone: +91-XXXXXXXXXX",
    "hours": "🕐 We are available:\nMon–Sat: 9 AM – 6 PM IST\nSunday: Closed",
    "thanks": "😊 You're welcome! Let us know if you need anything else.",
    "thank you": "😊 Happy to help! Feel free to ask anytime.",
}

# ─────────────────────────────────────────
#  📝  DEFAULT reply when no keyword matches
# ─────────────────────────────────────────
DEFAULT_REPLY = (
    "🤖 Thanks for your message!\n\n"
    "I'm am manager of jaiclub. Here's what I can help with:\n"
    "• Type 'price' for pricing info\n"
    "• Type 'buy' to make a purchase\n"
    "• Type 'contact' to reach our team\n"
    "• Type 'help' for all options\n\n"
    "Our team will also get back to you soon! 🙏"
)

# ─────────────────────────────────────────
#  ⚙️  Bot logic (no need to edit below)
# ─────────────────────────────────────────
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,
)
logger = logging.getLogger(__name__)


async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_text = update.message.text.lower().strip()
    user_name = update.effective_user.first_name or "there"

    logger.info(f"Message from {user_name}: {user_text}")

    # Check each keyword
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
    logger.info("✅ Bot is running...")
    app.run_polling()


if __name__ == "__main__":
    main()
