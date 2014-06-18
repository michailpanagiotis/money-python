from decimal import Decimal, ROUND_05UP
from currency import Currency, DEFAULT


def assert_is_money(an_object):
    if not isinstance(an_object, Money):
        raise TypeError("unsupported operand type(s): 'Money' and '%s'" %
                        type(an_object))


def assert_same_currency(some_money, other_money):
    if not some_money.currency == other_money.currency:
        raise TypeError("unsupported operand currencies(s): '%s' and '%s'"
                        % (str(some_money.currency),
                           str(other_money.currency)))


def lazyprop(fn):
    attr_name = '_lazy_' + fn.__name__

    @property
    def _lazyprop(self):
        if not hasattr(self, attr_name):
            setattr(self, attr_name, fn(self))
        return getattr(self, attr_name)
    return _lazyprop


class Money(object):
    @staticmethod
    def __from_grains__(self, grains, currency=DEFAULT):
        self.grains = grains
        self.currency = currency

    def __init__(self, amount, currency=DEFAULT):
        if not isinstance(currency, Currency):
            raise Exception("expecting a currency as second argument")
        self.set_currency(currency, False)
        self.grains = currency.to_grains(amount)
        self.currency = currency

    # Comparison Operators

    def __eq__(self, other):
        assert_is_money(other)
        assert_same_currency(self, other)
        return self.amount == other.amount

    def __le__(self, other):
        assert_is_money(other)
        assert_same_currency(self, other)
        return self.amount <= other.amount

    def __lt__(self, other):
        assert_is_money(other)
        assert_same_currency(self, other)
        return self.amount < other.amount

    # Arithmetic Operators

    def __abs__(self):
        return Money(abs(self.amount), self.currency)

    def __add__(self, other):
        assert_is_money(other)
        assert_same_currency(self, other)
        return Money(self.amount + other.amount, self.currency)

    def __div__(self, qty):
        return Money(self.amount / Decimal(qty), self.currency)

    def __iadd__(self, other):
        assert_is_money(other)
        assert_same_currency(self, other)
        self.grains += other.grains
        return self

    def __idiv__(self, qty):
        self.grains = int(self.grains / Decimal(qty))
        return self

    def __imul__(self, qty):
        self.grains = int(self.grains * Decimal(qty))
        return self

    def __isub__(self, other):
        assert_is_money(other)
        assert_same_currency(self, other)
        self.grains -= other.grains
        return self

    def __mul__(self, qty):
        return Money(self.amount * Decimal(qty), self.currency)

    def __neg__(self):
        return Money(-self.amount, self.currency)

    def __repr__(self):
        return "Money('%s', %s)" % (self.amount_str, self.currency.__repr__())

    def __sub__(self, other):
        assert_is_money(other)
        assert_same_currency(self, other)
        return Money(self.amount - other.amount, self.currency)

    def __unicode__(self):
        amount = str(self.amount.quantize(
                     self.currency.grain_ratio, ROUND_05UP))
        if self.currency.prefix:
            return self.currency.symbol + amount
        return amount + self.currency.symbol

    @lazyprop
    def amount(self):
        return Decimal(self.grains)/self.currency.grains_per_unit

    @lazyprop
    def amount_str(self):
        return str(self.amount.quantize(self.currency.grain_ratio, ROUND_05UP))

    def set_currency(self, currency, recalc=True):
        if recalc:
            amount = self.amount
        self.currency = currency
        if recalc:
            self.grains = currency.to_grains(amount)


if __name__ == '__main__':
    import currency
    for cur in (currency.EUR, currency.GBP, currency.USD):
        m = Money('200', cur)
        print m, '->', unicode(m)
