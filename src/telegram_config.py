from telegram.ext import Updater

from settings import settings

updater = Updater(token=settings.telegram_token)

dispatcher = updater.dispatcher
