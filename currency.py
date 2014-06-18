import math
from decimal import Decimal, ROUND_05UP


class Currency:
    def __init__(self, name, short, code, symbol, prefix, precision):
        self.name = name
        self.short = short
        self.code = code
        self.symbol = symbol
        self.prefix = prefix
        self.precision = precision
        self.grain_ratio = Decimal('.%s' % '1'.zfill(precision))
        self.grains_per_unit = int(math.pow(10, precision))

    def __repr__(self):
        return "'%s'" % self.short

    def __unicode__(self):
        return self.symbol

    def to_grains(self, amount):
        return int((Decimal(amount).quantize(
            self.grain_ratio, ROUND_05UP))*self.grains_per_unit)


EUR = Currency('Euro', 'EUR', 978, u'\u20AC', False, 2)
GBP = Currency('Pound sterling', 'GBP', 826, u'\u00A3', True, 2)
USD = Currency('United States dollar', 'USD', 840, u'$', True, 2)
DEFAULT = EUR
