
def get_market( SYMBOL , first_date , output_size , data_type ):
	import json
	from alpha_vantage.timeseries import TimeSeries
	from pprint import pprint
	from datetime import date, datetime, timedelta

	APIKEY = "LITMQUQH9NM496K3"


	if first_date == 0:
		now = date.today()
		if output_size <= 100 :
			query_size = 'compact'
		else:
			query_size = 'full'

	else:
		now = first_date
		query_size = 'full'

	if 	data_type == 'close' or data_type =='c':
		lookup_type = unicode('4. close')
	elif data_type == 'volume' or data_type == 'v':
		lookup_type = unicode('5. volume')
	elif data_type == 'high' or data_type == 'h':
		lookup_type = unicode('2. high')
	elif data_type == 'open' or data_type == 'o':
		lookup_type = unicode('1. open')
	elif data_type == 'low' or data_type == 'l':
		lookup_type = unicode('3. low')
	else:
		return -2


	ts = TimeSeries(key=APIKEY )
	data, meta_data = ts.get_daily(symbol=SYMBOL, outputsize=query_size)

	output_values = []
	lookup_date = now
	for i in range(output_size):

		while lookup_date.weekday() == 5 or lookup_date.weekday() == 6:
			lookup_date = lookup_date - timedelta(days=1)

		value = unicode(lookup_date)
		output_values.insert(i,float(data[value][lookup_type]))
		print(output_values[i])
		lookup_date = lookup_date - timedelta(days=1)
	print output_values
	return output_values

	#print data
	#output_file = open(SYMBOL + ".json", "w")
	#output_file.write(str(data))
	#output_file.close()

	print "done"
