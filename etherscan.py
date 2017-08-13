
from decimal import Decimal
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
		wei = Decimal(jval['result'])
		ethBalance = wei / Decimal('1000000000000000000')
		retobj = {
			'ether': ethBalance,
			'wei': jval['result'],
		}
		return retobj

