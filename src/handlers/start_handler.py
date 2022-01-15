from telegram.ext import CommandHandler


def start(update, context):
    context.bot.send_message(
        chat_id=update.effective_chat.id,
        text="Hi, i am the hashbot, i don't really know what i do yet :D",
    )


start_handler = CommandHandler("start", start)
