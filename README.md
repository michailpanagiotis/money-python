money-python
=========

money-python is a module for money and currencies. The main difference from other modules is that money-python stores amounts as integer values ('cents') instead of decimal ones and delegates all operations to integer operations. This is very convenient in cases where:

  - you need operations on money which perform as integer operations on cents (e.g. tax calculations)
  - you want to store amounts and perform aggregations on them without the risk introduced by floating point precision


### Testing

To test, use pytest:
```
pip install -U pytest
PYTHONPATH=./ py.test
```
