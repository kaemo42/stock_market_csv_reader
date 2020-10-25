import csv
from datetime import datetime

stock_data_path = "C:/Users/Sully/Downloads/google_stock_data.csv"

stock_data_file = open(stock_data_path, newline= '')

stock_data_reader = csv.reader(stock_data_file)

header = next(stock_data_reader) # The first line is a header (tiltle)

stock_data_list = []


for row in stock_data_reader:
    # header = ['Date', 'Open', 'High', 'Low', 'Close', 'Volume', 'Adj Close']
    # header_types = [date, float, float, float, float, int, float]

    date = datetime.strptime(row[0], '%m/%d/%Y')
    open_price = float(row[1]) # open is a function
    high = float(row[2])
    low = float(row[3])
    close = float(row[4])
    volume = int(row[5])
    adj_close = float(row[6])

    stock_data_list.append([date, open_price, high, low, close, volume, adj_close])


returns_path = "C:/Users/Sully/Downloads/google_returns.csv"
returns_file = open(returns_path, 'w+')
returns_writer = csv.writer(returns_file)
returns_writer.writerow(['Date', 'Time'])


for i in range(len(stock_data_list) - 1):

    todays_row = stock_data_list[i]
    todays_date = todays_row[0]
    todays_date_formatted = todays_date.strftime('%m/%d/%Y')
    todays_price = todays_row[-1]

    yesterdays_row = stock_data_list[i + 1]
    yesterdays_price = yesterdays_row[-1]

    todays_returns = (todays_price / yesterdays_price - 1) * 100
    
    returns_writer.writerow([todays_date_formatted, todays_returns])

