import tweepy
import plotly.express as px
import kaleido
from yahoo_fin.stock_info import *
from datetime import date
from other import keys

def get_stocks():#Get stock prices and make 30 day graph of stock price
    tesla_price = ("%.2f" % (get_live_price("TSLA")))
    tesla_30days = get_data("tsla",interval="1d", start_date= datetime.date.today()-datetime.timedelta(days=30),
                            end_date=date.today())
    #creating the lists of day-prices
    day_price = []
    for i in range(len(tesla_30days['open'])):
        day = (tesla_30days.index[i])
        price = float(("%.2f" % tesla_30days['open'][i]))
        day_price.append([day, price])

    amazon_price = ("%.2f" % (get_live_price("AMZN")))
    amazon_30days = get_data("amzn",interval="1d", start_date= datetime.date.today()-datetime.timedelta(days=30),
                             end_date=date.today())
    for i in range(len(amazon_30days['open'])):
        price = float(("%.2f" % amazon_30days['open'][i]))
        day_price[i].append(price)

    apple_price = ("%.2f" % (get_live_price("AAPL")))
    apple_30days = get_data("aapl", interval="1d", start_date=datetime.date.today() - datetime.timedelta(days=30),
                             end_date=date.today())
    for i in range(len(apple_30days['open'])):
        price = float(("%.2f" % apple_30days['open'][i]))
        day_price[i].append(price)

    alphabet_price = ("%.2f" % (get_live_price("GOOG")))
    alphabet_30days = get_data("goog", interval="1d", start_date=datetime.date.today() - datetime.timedelta(days=30),
                            end_date=date.today())
    for i in range(len(alphabet_30days['open'])):
        price = float(("%.2f" % alphabet_30days['open'][i]))
        day_price[i].append(price)

    microsoft_price = ("%.2f" % (get_live_price("MSFT")))
    microsoft_30days = get_data("MSFT", interval="1d", start_date=datetime.date.today() - datetime.timedelta(days=30),
                               end_date=date.today())
    for i in range(len(microsoft_30days['open'])):
        price = float(("%.2f" % microsoft_30days['open'][i]))
        day_price[i].append(price)

    #make dataframe off all date and prices of stocks in order -> TSLA, AMZN, AAPL, GOOG, MSFT
    t_30 = pd.DataFrame(data=day_price, columns=['Day', 'TSLA', 'AMZN', 'AAPL', 'GOOG', 'MSFT'])
    t_fig = px.line(t_30, x='Day', y=t_30.columns, title='Past 30 days',
                    width=600, height=400,
                    template='plotly_dark')
    t_fig.write_image("other/t_fig.png")

    #example
    # df = px.data.stocks()
    # fig = px.line(df, x='date', y="GOOG")
    # fig.write_image("other/example.png")

    stock_prices = str("Tesla: $"+tesla_price + "\nAmazon: $"+amazon_price + "\nApple: $"+apple_price + "\nAlphabet: $"+alphabet_price+
               "\nMicrosoft: $"+microsoft_price)
    return stock_prices

def tweet(message,prices):
    client = tweepy.Client(keys.bearer_token, keys.api_key, keys.api_secret, keys.access_token,
                           keys.access_token_secret)
    auth = tweepy.OAuth1UserHandler(keys.api_key, keys.api_secret, keys.access_token, keys.access_token_secret)
    api = tweepy.API(auth)
    image_path = 'other/t_fig.png'
    media = api.media_upload(image_path)
    client.create_tweet(text=message + prices, media_ids=[media.media_id_string])



if __name__ == '__main__':

    prices = get_stocks()
    tweet("The Top Tech Stock prices today are:\n", prices)
