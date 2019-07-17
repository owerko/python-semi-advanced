from time import time, sleep

class GiveAway:

    def __init__(self, manager):
        self.manager = manager

    def call_customer(self, order):
        sleep(3)
        self.customer_collected_order(order)

    def customer_collected_order(self, order):
        order.collected_at = time()
        self.manager.customer_collected_order(order)