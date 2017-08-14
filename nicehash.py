
from time import sleep
from httputil import jsonfetch
import logging
import json

def nhfetch(opts):
	sleep(2)	# API rate limit is "approx 2s"
	return jsonfetch(opts)

def nhfetchCheck(opts):
	ret = nhfetch(opts)
	result = ret['result']
	if 'success' in result:
		return result

	logging.info("API call failed at url " + opts['url'] + " -- " + json.dumps(result))
	return None

class Nicehash:
	ApiUrl = 'https://api.nicehash.com/api'
	toLocation = {
		'0': 'EU',
		'1': 'US',
	}

	def __init__(self, authDb):
		self.id = authDb['nicehash']['id']
		self.key = authDb['nicehash']['key']

	def balance(self):
		opts = {
			'url': self.ApiUrl,
			'params': {
				'method': 'balance',
				'id': self.id,
				'key': self.key,
			}
		}
		return nhfetch(opts)

	def orders(self, algo, location):
		opts = {
			'url': self.ApiUrl,
			'params': {
				'method': 'orders.get',
				'location': location,
				'algo': algo,
			}
		}
		return nhfetch(opts)

	def myOrders(self, algo, location):
		opts = {
			'url': self.ApiUrl,
			'params': {
				'method': 'orders.get',
				'my': 1,
				'location': location,
				'algo': algo,
				'id': self.id,
				'key': self.key,
			}
		}
		return nhfetch(opts)

	def createOrder(self, params):
		params['method'] = 'orders.create'
		params['id'] = self.id
		params['key'] = self.key
		opts = {
			'url': self.ApiUrl,
			'params': params,
		}
		return nhfetch(opts)

	def orderPriceDec(self, algo, location, orderId, bestPrice):
		params = {
			'method': 'orders.set.price.decrease',
			'id': self.id,
			'key': self.key,
			'location': location,
			'algo': algo,
			'order': orderId,
			# sadly, NH does not take price as input param
		}
		opts = {
			'url': self.ApiUrl,
			'params': params,
		}
		return nhfetchCheck(opts)

	def orderPriceInc(self, algo, location, orderId, bestPrice):
		params = {
			'method': 'orders.set.price',
			'id': self.id,
			'key': self.key,
			'location': location,
			'algo': algo,
			'order': orderId,
			'price': bestPrice,
		}
		opts = {
			'url': self.ApiUrl,
			'params': params,
		}
		return nhfetchCheck(opts)

