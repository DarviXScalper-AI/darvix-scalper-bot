import os
import asyncio
from telegram import Update
from telegram.ext import Application, ContextTypes, MessageHandler, filters

BOT_TOKEN = os.getenv("BOT_TOKEN")


async def handle_channel_post(update: Update, context: ContextTypes.DEFAULT_TYPE):
    message = update.channel_post

    if not message:
        return

    print("=" * 50)
    print("NEW CHANNEL POST RECEIVED")
    print("=" * 50)
    print(f"Channel: {message.chat.title}")
    print(f"Chat ID: {message.chat.id}")
    print(f"Message ID: {message.message_id}")
    print(f"Text:\n{message.text or message.caption}")
    print("=" * 50)


def main():
    if not BOT_TOKEN:
        raise ValueError("BOT_TOKEN environment variable is missing.")

    app = Application.builder().token(BOT_TOKEN).build()

    app.add_handler(
        MessageHandler(
            filters.UpdateType.CHANNEL_POST,
            handle_channel_post
        )
    )

    print("DarviX Signal Bot is running...")
    print("Waiting for new channel posts...")

    app.run_polling(
        allowed_updates=["channel_post"]
    )


if __name__ == "__main__":
    main()
