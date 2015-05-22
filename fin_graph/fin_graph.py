import matplotlib.pyplot as plt
import pandas.io.data as web
import datetime

start = datetime.datetime(2014, 5, 25)
end = datetime.datetime(2015, 5, 24)

stocks = ['017670.KS', '033780.KS', '002960.KS']
stocks_name = ['SK텔레콤', 'KT&G', '한국쉘석유']
stocks_data = []

for stock in stocks:
	stocks_data.append(web.DataReader(stock, 'yahoo', start, end))

plt.figure(1)

for i in range(len(stocks)):
	plt.subplot(len(stocks),1,i+1)
	plt.plot(stocks_data[i].index, stocks_data[i]['Close'])
	plt.grid(True)
	plt.title(stocks_name[i])

plt.show()
