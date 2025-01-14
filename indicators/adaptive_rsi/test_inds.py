from __future__ import (absolute_import, division, print_function,
                        unicode_literals)

import backtrader as bt
from adaptive_rsi_ind import AdaptiveRsiIndicator
import datetime


class TestStrategy(bt.Strategy):
    params = dict(
        period = 10
    )

    def __init__(self):
        self.acc_ind = AdaptiveRsiIndicator(self.data,period = self.p.period)
        self.sma_ind = bt.indicators.MovingAverageSimple(self.data.close, period = self.p.period)

    def next(self):
        print(self.sma_ind[0])
        print(self.acc_ind[0])

if __name__ == "__main__":
    cerebro = bt.Cerebro()

    from_date = datetime.datetime(2006, 1, 1)
    to_date = datetime.datetime(2006, 12, 31)

    data = bt.feeds.BacktraderCSVData(
        dataname="../../datas/2006-day-001.txt",
        fromdate=from_date,
        todate=to_date)

    cerebro.adddata(data)
    cerebro.addstrategy(TestStrategy,period = 10)
    cerebro.run()
    cerebro.plot()

