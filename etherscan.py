
from httputil import jsonfetch

class Etherscan:
	ApiUrl = 'https://api.etherscan.io/api'

	def __init__(self):
		pass

	def balance(self, address, apikey):
		opts = {
			'url': self.ApiUrl,
			'params': {
				'module': 'account',
				'action': 'balance',
				'address': address,
				'tag': 'latest',
				'apikey': apikey,
			}
		}
		jval = jsonfetch(opts)
		wei = float(jval['result'])
		ethBalance = wei / 1000000000000000000
		return ethBalance

