from time import time, sleep
from datetime import datetime
class GiveAway:

    def __init__(self, manager):
        self.manager = manager

    def call_customer(self,order):

        sleep(1)
        self.customer_collected_order(order)


    def customer_collected_order(self,order):
        order.collected_at = time()
        self.manager.customer_collected_order(order)
        info = (f"Posiłek do wydania: {order.name} o godzinie  {datetime.utcfromtimestamp(time()).strftime('%Y-%m-%d %H:%M:%S')}")
        self.log(info)

    def log(self,message):
        with open('give_avay.log', 'a', encoding='utf-8') as f:
            f.write(message + '\n')