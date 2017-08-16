
from decimal import Decimal

def toEther(wei):
	return Decimal(wei) / Decimal('1000000000000000000')

