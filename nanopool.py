
from httputil import jsonfetch

class Nanopool:
	ApiBaseUrl = 'https://api.nanopool.org'

	def __init__(self):
		pass

	def balance(self, address):
		opts = {
			'url': self.ApiBaseUrl + '/v1/eth/balance/' + address,
		}
		return jsonfetch(opts)

