import matplotlib.pyplot as plt
import pandas.io.data as web
import datetime

start = datetime.datetime(2014, 5, 25)
end = datetime.datetime(2015, 5, 24)

skt = web.DataReader('017670.KS', 'yahoo', start, end)
kt_g = web.DataReader('033780.KS', 'yahoo', start, end)


plt.figure(1)
plt.subplot(2,1,1)
plt.plot(skt.index, skt['Close'], 'r')
plt.grid(True)
plt.title('SKT')

plt.subplot(2,1,2)
plt.plot(kt_g.index, kt_g['Close'], 'g')
plt.grid(True)
plt.title('KT&G')

plt.show()
