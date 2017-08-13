
from httputil import jsonfetch

class Poloniex:
	PublicApiUrl = 'https://poloniex.com/public'

	def __init__(self):
		pass

	def ticker(self):
		opts = {
			'url': self.PublicApiUrl,
			'params': { 'command': 'returnTicker' }
		}
		return jsonfetch(opts)

