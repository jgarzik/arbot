
import time
import urllib
import hmac
import hashlib
from httputil import jsonfetch

class Bittrex:
	ApiBaseUrl = 'https://bittrex.com/api'

	def __init__(self):
		pass

	def balances(self, authDb):
		apikey = authDb['bittrex']['key']
		secret = authDb['bittrex']['secret']

		callparams = {
			'apikey': apikey,
			'nonce': int(time.time()),
		}
		qs = urllib.urlencode(callparams)
		callUrl = '/v1.1/account/getbalances?'
		url = self.ApiBaseUrl + callUrl + qs

		mac = hmac.new(str(secret), str(url), digestmod=hashlib.sha512)

		opts = {
			'url': url,
			'headers': {
				'apisign': mac.hexdigest(),
			},
		}
		jval = jsonfetch(opts)
		return jval['result']

