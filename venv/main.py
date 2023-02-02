import tweepy
from yahoo_fin.stock_info import *
from datetime import date
from other import keys

def get_stocks():#Get stock prices and last week price
    tesla_price = ("%.2f" % (get_live_price("TSLA")))
    # tesla_week = get_data('tsla', start_date=(datetime.date.today()-datetime.timedelta(days=7)), end_date=date.today())

    amazon_price = ("%.2f" % (get_live_price("AMZN")))
    # amazon_week = get_data('amzn', start_date=(datetime.date.today()-datetime.timedelta(days=7)), end_date=date.today())

    apple_price = ("%.2f" % (get_live_price("AAPL")))
    # apple_week = get_data('apple', start_date=(datetime.date.today()-datetime.timedelta(days=7)), end_date=date.today())

    alphabet_price = ("%.2f" % (get_live_price("GOOG")))
    # alphabet_week = get_data('goog', start_date=(datetime.date.today()-datetime.timedelta(days=7)), end_date=date.today())

    microsoft_price = ("%.2f" % (get_live_price("MSFT")))
    # microsoft_week = get_data('msft', start_date=(datetime.date.today()-datetime.timedelta(days=7)), end_date=date.today())

    stock_prices = str("Tesla: $"+tesla_price + "\nAmazon: $"+amazon_price + "\nApple: $"+apple_price + "\nAlphabet: $"+alphabet_price+
               "\nMicrosoft: $"+microsoft_price)
    return stock_prices

def tweet(message,prices):
    client = tweepy.Client(keys.bearer_token, keys.api_key, keys.api_secret, keys.access_token,
                           keys.access_token_secret)
    auth = tweepy.OAuth1UserHandler(keys.api_key, keys.api_secret, keys.access_token, keys.access_token_secret)
    api = tweepy.API(auth)
    client.create_tweet(text=message + prices)


if __name__ == '__main__':

    prices = get_stocks()
    tweet("The Top Tech Stock prices today are:\n", prices)
