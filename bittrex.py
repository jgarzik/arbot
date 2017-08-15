
import time
import urllib
import hmac
import hashlib
from httputil import jsonfetch

class Bittrex:
	ApiBaseUrl = 'https://bittrex.com/api'

	def __init__(self, authDb):
		self.apikey = authDb['bittrex']['key']
		self.secret = authDb['bittrex']['secret']

	def fetchPub(self, callUrl, qsParams):
		qs = urllib.urlencode(qsParams)
		url = self.ApiBaseUrl + callUrl + '?' + qs

		opts = {
			'url': url,
		}
		jval = jsonfetch(opts)
		return jval['result']

	def fetchPriv(self, callUrl, qsParams):
		qsParams['apikey'] = self.apikey
		qsParams['nonce'] = int(time.time())

		qs = urllib.urlencode(qsParams)
		url = self.ApiBaseUrl + callUrl + '?' + qs

		mac = hmac.new(str(self.secret), str(url),
			       digestmod=hashlib.sha512)

		opts = {
			'url': url,
			'headers': {
				'apisign': mac.hexdigest(),
			},
		}
		jval = jsonfetch(opts)
		return jval['result']

	def balance(self, currency):
		callUrl = '/v1.1/account/getbalance'
		callParams = { 'currency': currency }
		return self.fetchPriv(callUrl, callParams)

	def balances(self):
		callUrl = '/v1.1/account/getbalances'
		return self.fetchPriv(callUrl, {})

	def ticker(self, market):
		callUrl = '/v1.1/public/getticker'
		callParams = { 'market': market }
		return self.fetchPub(callUrl, callParams)

