import logging
from telegram_config import dispatcher, updater
from handlers.start_handler import start_handler
from handlers.currency_handler import currency_handler
from handlers.phrase_handler import phrase_handler
from handlers.grayscale_handler import grayscale_handler


def main():
    dispatcher.add_handler(start_handler)
    dispatcher.add_handler(currency_handler)
    dispatcher.add_handler(phrase_handler)
    dispatcher.add_handler(grayscale_handler)
    updater.start_polling()


if __name__ == "__main__":
    logging.basicConfig(
        format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
        level=logging.INFO,
    )
    main()
