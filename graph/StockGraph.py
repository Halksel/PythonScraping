import pandas_datareader.data as web
import datetime
import matplotlib.pyplot as plt

end = datetime.datetime.now()
start = datetime.datetime(end.year - 1, end.month, end.day)

f2 = web.DataReader(['NTDOF', 'CPLLF'], 'morningstar', start, end)

print(f2)
f2_u = f2.unstack(0)
print(f2_u)
f2_u['Close'].plot(title='7974 VS 3668', grid=True)
# plt.show()
plt.savefig('test.png')
