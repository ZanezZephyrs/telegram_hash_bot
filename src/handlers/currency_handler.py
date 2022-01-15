import re
from bs4 import BeautifulSoup
from urllib.request import urlopen,Request
from telegram.ext import CommandHandler


def currency(update, context):
    args=context.args
    if(len(args)!=1):
        message="Please specify the currency, the correct format is /currency <currency name>, for example:\n /currency dollar"
    else:
        try:
            currency=args[0]

            site_url=f"https://www.google.com/search?q={currency}+price"
            headers= {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
                'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
                'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
                'Accept-Encoding': 'none',
                'Accept-Language': 'en-US,en;q=0.8',
                'Connection': 'keep-alive'}
            req = Request(site_url, headers=headers)
            client = urlopen(req)
            html_data = client.read()
            client.close()


            soup = BeautifulSoup(html_data,"html.parser")

            results=soup.body.findAll(text=re.compile('Real brasileiro'))[0]
            value_in_reais=float(results.split()[0].replace(",","."))
            message=f"Now, one {currency} is equivalent to {value_in_reais} reais"
        except Exception:
            message=f"sorry, i was unable to find the currency {currency}"
    context.bot.send_message(
        chat_id=update.effective_chat.id,
        text=message,
    ) 

currency_handler = CommandHandler("currency", currency)
