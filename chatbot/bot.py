import os
import logging
from dotenv import load_dotenv
from telegram import Update, Message
from telegram.ext import (
    ApplicationBuilder,
    CommandHandler,
    MessageHandler,
    filters,
    ConversationHandler,
    ContextTypes,
)
import httpx

# load .env from project root (one level above chatbot/)
env_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), ".env")
load_dotenv(env_path)

BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
BACKEND_URL = os.getenv("BACKEND_URL")

if not BOT_TOKEN:
    raise SystemExit("TELEGRAM_BOT_TOKEN not set in .env")

if not BACKEND_URL:
    raise SystemExit("BACKEND_URL not set in .env")

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Conversation states
NAME, YEARS, LOCATION, REVENUE, PHONE = range(5)

# Start command
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    assert update.message is not None, "update.message is None"
    assert context.user_data is not None, "context.user_data is None"

    await update.message.reply_text(
        "👋 Welcome to MSME Credit Agent!\nLet's get your business onboarded.\n\nWhat is your *business name*?",
        parse_mode="Markdown",
    )
    return NAME

# Step 1: Business name
async def get_name(update: Update, context: ContextTypes.DEFAULT_TYPE):
    assert update.message is not None, "update.message is None"
    assert context.user_data is not None, "context.user_data is None"

    context.user_data["name"] = update.message.text.strip()
    await update.message.reply_text("How many *years* has your business been operating? (enter a whole number)")
    return YEARS

# Step 2: Years operating
async def get_years(update: Update, context: ContextTypes.DEFAULT_TYPE):
    assert update.message is not None, "update.message is None"
    assert context.user_data is not None, "context.user_data is None"

    text = update.message.text.strip()
    try:
        years = int(text)
        if years < 0:
            raise ValueError("negative")
        context.user_data["years_operating"] = years
        await update.message.reply_text("Where is your business *located*?")
        return LOCATION
    except Exception:
        await update.message.reply_text("Please enter a valid whole number for years (e.g., 3).")
        return YEARS

# Step 3: Location
async def get_location(update: Update, context: ContextTypes.DEFAULT_TYPE):
    assert update.message is not None, "update.message is None"
    assert context.user_data is not None, "context.user_data is None"

    context.user_data["location"] = update.message.text.strip()
    await update.message.reply_text("What is your *average monthly revenue* (in ETB)? (e.g., 25000)")
    return REVENUE

# Step 4: Monthly revenue
async def get_revenue(update: Update, context: ContextTypes.DEFAULT_TYPE):
    assert update.message is not None, "update.message is None"
    assert context.user_data is not None, "context.user_data is None"

    text = update.message.text.strip().replace(",", "")
    try:
        revenue = float(text)
        if revenue < 0:
            raise ValueError("negative")
        context.user_data["monthly_revenue"] = revenue
        await update.message.reply_text("Finally, please share your *phone number* (e.g., +2519XXXXXXX).")
        return PHONE
    except Exception:
        await update.message.reply_text("Please enter a valid number for monthly revenue (e.g., 25000).")
        return REVENUE

# Step 5: Phone number → Send to backend (async HTTP)
async def get_phone(update: Update, context: ContextTypes.DEFAULT_TYPE):
    assert update.message is not None, "update.message is None"
    assert context.user_data is not None, "context.user_data is None"

    context.user_data["phone"] = update.message.text.strip()

    data = {
        "name": context.user_data.get("name"),
        "owner_name": "Telegram User",
        "phone": context.user_data.get("phone"),
        "years_operating": context.user_data.get("years_operating"),
        "monthly_revenue": context.user_data.get("monthly_revenue"),
    }

    try:
        async with httpx.AsyncClient(timeout=10.0) as client:
            resp = await client.post(BACKEND_URL, json=data)
            if 200 <= resp.status_code < 300:
                await update.message.reply_text("✅ Business onboarded successfully!\n\nThank you! 🎉")
            else:
                logger.error("Backend error: %s %s", resp.status_code, resp.text)
                await update.message.reply_text(f"⚠️ Backend error ({resp.status_code}): {resp.text}")
    except Exception as e:
        logger.exception("Failed to call backend")
        await update.message.reply_text(f"❌ Could not connect to backend: {e}")

    return ConversationHandler.END

# Cancel command
async def cancel(update: Update, context: ContextTypes.DEFAULT_TYPE):
    assert update.message is not None, "update.message is None"
    await update.message.reply_text("❌ Onboarding canceled.")
    return ConversationHandler.END

# Main function
def main():
    app = ApplicationBuilder().token(BOT_TOKEN).build()

    conv_handler = ConversationHandler(
        entry_points=[CommandHandler("start", start)],
        states={
            NAME: [MessageHandler(filters.TEXT & ~filters.COMMAND, get_name)],
            YEARS: [MessageHandler(filters.TEXT & ~filters.COMMAND, get_years)],
            LOCATION: [MessageHandler(filters.TEXT & ~filters.COMMAND, get_location)],
            REVENUE: [MessageHandler(filters.TEXT & ~filters.COMMAND, get_revenue)],
            PHONE: [MessageHandler(filters.TEXT & ~filters.COMMAND, get_phone)],
        },
        fallbacks=[CommandHandler("cancel", cancel)],
    )

    app.add_handler(conv_handler)
    logger.info("🤖 Bot is running...")
    app.run_polling()

if __name__ == "__main__":
    main()