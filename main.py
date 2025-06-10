import os
import logging
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

TOKEN = os.getenv("BOT_TOKEN")

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("👋 Witaj w Świecie Firos: Magic & Magic!\nRozpocznij swoją przygodę wpisując /quest")

async def quest(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("🧙‍♂️ Rozpoczynasz pierwszy quest...\nZabij szczura w piwnicy!")

def main():
    application = ApplicationBuilder().token(TOKEN).build()
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("quest", quest))
    application.run_polling()

if __name__ == "__main__":
    main()
