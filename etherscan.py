
from decimal import Decimal
from httputil import jsonfetch
from ethunits import toEther

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
		wei = jval['result']
		retobj = {
			'ether': toEther(wei),
			'wei': wei,
		}
		return retobj

