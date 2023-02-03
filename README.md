# twitter_bot
Tweet stock prices (optional for more data like weekly)

This is used to automatically tweet stock prices. You can change the shorthand companies to whatever companies you want.
Further more what is being done is an analysis of the past 30 days of the specified company and creating a line chart comparing the company's stock prices.

First you need to create a developer account for twitter and recieve your keys
  TAKE NOTE OF THESE KEYS AND SAVE THEM SOMEWHERE

Now you can test the connection by running:

  client = tweepy.Client(...
	
  auth = tweepy.0Auth1UserHandler(...
	
  api = tweepy.API(auth)
	
If these three lines run without error then you know you are connected properly.
The final line in the function tweet() is the message your bot will tweet. There are different parameters for this. In this doc we are showing a text with the prices and uploading a media file (The line graph analysis of the past 30 days).

To change the stocks go to the fucntion get_stocks()

Inside here you can change the companys and the commented out section is for the weekly data if you want to use that. (Create graphs, plots, etc.)

Further more you can change the start and end date for your analysis.
 
