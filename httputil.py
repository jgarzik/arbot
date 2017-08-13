
import requests
import decimal
import json
import logging

def jsonfetch(opts):
	if 'headers' not in opts:
		opts['headers'] = {}
	if 'params' not in opts:
		opts['params'] = {}

	r = requests.get(opts['url'], headers=opts['headers'],
			 params=opts['params'], timeout=30)
	if r.status_code != 200:
		logging.warning(opts['url'] + " returned status " + str(r.status_code))
		return None

	try:
		jval = json.loads(r.text, parse_float=decimal.Decimal)
		# jval = json.loads(r.text)
	except ValueError:
		logging.warning(opts['url'] + " failed JSON parse")
		return None

	return jval

