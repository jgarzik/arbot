
from httputil import jsonfetch

class EtherChain:
	ApiBaseUrl = 'https://etherchain.org/api/'

	def __init__(self):
		pass

	def account(self, id):
		opts = { 'url': self.ApiBaseUrl + 'account/' + id }
		return jsonfetch(opts)

	def basic_stats(self):
		opts = { 'url': self.ApiBaseUrl + 'basic_stats' }
		return jsonfetch(opts)

