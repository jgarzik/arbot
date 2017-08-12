
from httputil import jsonfetch

class EthChain:
	ApiUrl = 'https://etherchain.org/api/basic_stats'

	def __init__(self):
		pass

	def basic_stats(self):
		opts = { 'url': self.ApiUrl }
		return jsonfetch(opts)

