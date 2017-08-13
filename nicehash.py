
from httputil import jsonfetch

class Nicehash:
	ApiUrl = 'https://api.nicehash.com/api'

	def __init__(self):
		pass

	def balance(self, authDb):
		opts = {
			'url': self.ApiUrl,
			'params': {
				'method': 'balance',
				'id': authDb['nicehash']['id'],
				'key': authDb['nicehash']['key'],
			}
		}
		return jsonfetch(opts)

	def orders(self, algo, location):
		opts = {
			'url': self.ApiUrl,
			'params': {
				'method': 'orders.get',
				'location': location,
				'algo': algo,
			}
		}
		return jsonfetch(opts)

	def myOrders(self, authDb, algo, location):
		opts = {
			'url': self.ApiUrl,
			'params': {
				'method': 'orders.get',
				'my': 1,
				'location': location,
				'algo': algo,
				'id': authDb['nicehash']['id'],
				'key': authDb['nicehash']['key'],
			}
		}
		return jsonfetch(opts)

