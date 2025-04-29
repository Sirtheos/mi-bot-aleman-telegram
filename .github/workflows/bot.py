from telegram import Update
from telegram.ext import Application, MessageHandler, filters

# Configuración (usa TU token aquí)
TOKEN = "7691643184:AAHPnSlXBasf9fsGu_IhLNNOVjm6IU05RwM"

# Función que responde a los mensajes
async def handle_message(update: Update, context):
    user_message = update.message.text
    await update.message.reply_text(f"¡Recibí tu mensaje! Escribiste: '{user_message}'")

# Iniciar el bot
def main():
    application = Application.builder().token(TOKEN).build()
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))
    application.run_polling()

if __name__ == "__main__":
    print("Bot activo. Presiona Ctrl + C para detenerlo.")
    main()