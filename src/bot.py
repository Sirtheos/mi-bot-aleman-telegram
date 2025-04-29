import os
from telegram import Update
from telegram.ext import Application, MessageHandler, filters

TOKEN = os.getenv("mi_bot_aleman")  # Asegúrate de que coincide con el nombre de variable en Render

async def handle_message(update: Update, context):
    user_message = update.message.text
    await update.message.reply_text(f"¡Recibí tu mensaje! Escribiste: '{user_message}'")

def main():
    application = Application.builder().token(TOKEN).build()
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))
    application.run_polling()

if __name__ == "__main__":
    print("Bot activo. Presiona Ctrl + C para detenerlo.")
    main()
