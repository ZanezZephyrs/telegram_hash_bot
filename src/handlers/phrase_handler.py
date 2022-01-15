from telegram.ext import CommandHandler
import random

def phrase(update, context):
    number = random.randint(1,3)

    if number == 1:
        context.bot.send_message(
            chat_id=update.effective_chat.id,
            text=update.message.chat.first_name + ", great things are done by a series of small things brought together – Vincent Van Gogh",
        )
    elif number == 2:
        context.bot.send_message(
            chat_id=update.effective_chat.id,
            text=update.message.chat.first_name + ", you can waste your lives drawing lines. Or you can live your life crossing them - Shonda Rhimes",
        )
    else:
        context.bot.send_message(
            chat_id=update.effective_chat.id,
            text= update.message.chat.first_name + ", in a gentle way, you can shake the world – Mahatma Gandhi",
        )


phrase_handler = CommandHandler("phrase", phrase)
