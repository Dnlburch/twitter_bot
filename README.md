# twitter_bot
Tweet stock prices (optional for more data like weekly)

This is used to automatically tweet stock prices. You can change the shorthand companies to whatever companies you want.

First you need to create a developer account for twitter and recieve your keys
  TAKE NOTE OF THESE KEYS AND SAVE THEM SOMEWHERE

Now you can test the connection by running:
  client = tweepy.Client(...
  auth = tweepy.0Auth1UserHandler(...
  api = tweepy.API(auth)
If these three lines run without error then you know you are connected properly.
The final line in the function tweet() is the message your bot will tweet. There are different parameters for this. In this doc we are showing a simple text

To change the stocks go to the fucntion get_stocks()
Inside here you can change the companys and the commented out section is for the weekly data if you want to use that. (Create graphs, plots, etc.)
 
