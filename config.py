from os import getenv

class Config(object):
      API_HASH = getenv("21562655")
      API_ID = int(getenv("82a353e4cf209ae679b537c1fff17c9c", 0))      
      BOT_TOKEN = getenv("6820240200:AAGBVWRJJyn82CYv8R6mzJFQtPm8APKCjjU", "")
      CHANNEL = list(x for x in getenv("CHANNEL_ID", "").replace("\n", " ").split(' '))
