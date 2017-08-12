
import requests

def jsonfetch(opts):
	if 'headers' not in opts:
		opts['headers'] = {}

	r = requests.get(opts['url'], headers=opts['headers'], timeout=10)
	if r.status_code != 200:
		return None
	
	return r.json()

