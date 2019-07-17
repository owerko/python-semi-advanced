from time import sleep
from time import time
from datetime import datetime
class CashDesk:

    def __init__(self, manager):
        self.manager = manager

    def new_order(self, order):
        self.manager.new_order(order)
        info = f"Przyjołem zamowienie {order.name} o godzinie  {datetime.utcfromtimestamp(time()).strftime('%Y-%m-%d %H:%M:%S')}"
        self.log(info)

    @staticmethod
    def log(self,message):
        with open('cash_desk.log', 'a', encoding='utf-8') as f:
            f.write(message + '\n')