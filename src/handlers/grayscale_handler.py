from telegram.ext import (
    CommandHandler,
    MessageHandler,
    Filters,
    ConversationHandler,
)
import requests
import cv2

PHOTO = range(1)

def grayscale(update, context) -> int:
    """Starts the conversation and asks the user for a photo to apply the grayscale."""

    update.message.reply_text(
        'Hi! Send me a photo and i will send you the grayscale version back',
    )

    return PHOTO

def process_photo(update, context) -> int:
    """Receives and process photo"""

    photo_file = update.message.photo[-1].get_file()
    file_path=photo_file["file_path"]
    name=file_path.split("/")[-1]
    photo_request = requests.get(file_path, timeout = 15)
    binary_photo = photo_request.content
    local_path=f"img/{name}"
    with open(local_path,"wb") as fin:
        fin.write(binary_photo)

    grayscale_photo=cv2.imread(local_path,cv2.IMREAD_GRAYSCALE)
    gray_local_path=f"img/gray_{name}"
    cv2.imwrite(gray_local_path,grayscale_photo)

    update.message.reply_text(
        'There you go',
    )
    context.bot.send_photo(chat_id=update.effective_chat.id, photo=open(gray_local_path, 'rb'))
    
    return ConversationHandler.END

def cancel(update, context) -> int:
    """Cancels and ends the conversation."""
    update.message.reply_text(
        'Okay, cancelling grayscale operation D:'
    )

    return ConversationHandler.END

grayscale_handler = ConversationHandler(
    entry_points=[CommandHandler('grayscale', grayscale)],
    states={
        PHOTO: [MessageHandler(Filters.photo, process_photo)],
    },
    fallbacks=[CommandHandler('cancel', cancel)],
)