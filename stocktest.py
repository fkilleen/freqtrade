import json
from alpha_vantage.timeseries import TimeSeries
from pprint import pprint
import datetime


APIKEY = "LITMQUQH9NM496K3"
SYMBOL = "V"

now = datetime.datetime.now()
ts = TimeSeries(key=APIKEY )
data, meta_data = ts.get_daily(symbol=SYMBOL, outputsize='compact')

value = "u" + str(now.year) + "-" + str(now.month) + "-" + str(now.day) + "'"
print value
pprint(data[value])

#print data

output_file = open(SYMBOL + ".json", "w")
output_file.write(str(data))
output_file.close()

print "done"
