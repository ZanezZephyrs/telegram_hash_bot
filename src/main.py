import logging

from telegram_config import dispatcher, updater
from handlers.start_handler import start_handler



def main():
    dispatcher.add_handler(start_handler)
    updater.start_polling()


if __name__ == "__main__":
    logging.basicConfig(
        format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
        level=logging.INFO,
    )
    main()
