
import requests
import decimal
import json

def jsonfetch(opts):
	if 'headers' not in opts:
		opts['headers'] = {}
	if 'params' not in opts:
		opts['params'] = {}

	r = requests.get(opts['url'], headers=opts['headers'],
			 params=opts['params'], timeout=10)
	if r.status_code != 200:
		return None

	try:
		jval = json.loads(r.text, parse_float=decimal.Decimal)
		# jval = json.loads(r.text)
	except ValueError:
		return None

	return jval

