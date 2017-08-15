
import json
from decimal import Decimal, ROUND_FLOOR, getcontext

class DecimalEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, Decimal):
            return float(o)
        return super(DecimalEncoder, self).default(o)

def decimalstr(d):
	s = '{0:f}'.format(d)
	return s

def decimaltrunc(d, n):
	s = decimalstr(d)
	before_dec, after_dec = s.split('.')
	truncStr = '.'.join((before_dec, after_dec[0:n]))
	return Decimal(truncStr)

def jsonDumps(obj):
	return json.dumps(obj, cls=DecimalEncoder)

def jsonLoads(s):
	return json.loads(s, parse_float=Decimal)

