import yfinance as yf
import datetime

# print(ticker.keys())

ticker_name = "SAIL.NS"
ticker = yf.Ticker(ticker_name).info

# stock name
print('Ticker: {}'.format(ticker_name))
# today Price
market_price = ticker['regularMarketPrice']
print('Market Price:', market_price)
# today clsoe Price
previous_close_price = ticker['regularMarketPreviousClose']
print('Previous Close Price:', previous_close_price)
# industry type
print('Industry Type:',ticker['industry'])

# datetime object
datetime_object = datetime.date.today()

# one week
start_date = datetime_object - datetime.timedelta(days=7)
end_date = datetime_object
data = yf.download(ticker_name, start_date, end_date)
print(data.tail())
# one month
# 3 months
# 6 months
# 10 months
# 1 year

'''
todo

'dayHigh': 81.1,
'fiftyTwoWeekLow': 63.6
'fiftyTwoWeekHigh': 131.8
'volume': 11815823,
'dayLow': 77.8,
'fiftyDayAverage': 79.313
'twoHundredDayAverage': 89.2705,
'longName': 'Steel Authority of India Limited'

link ref: https://www.makeuseof.com/stock-price-data-using-python/
link ref: https://finance.yahoo.com/
link ref: https://github.com/ranaroussi/yfinance
'''