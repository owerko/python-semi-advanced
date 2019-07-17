from time import sleep
from time import time
from datetime import datetime

class Kitchen:

    def __init__(self, manager):
        self.manager = manager
        # self.f= open('kitchen.log','a', encoding='utf-8')

    def prepare_meal(self, order):
        info = str(f'Zaczynam przygotowywać posiłek {order.name}')
        self.log(info)
        sleep(1)
        self.meal_ready(order)
        info = str(f"Skonczylem przygotowywac posiłek {order.name} o godzinie {datetime.utcfromtimestamp(time()).strftime('%Y-%m-%d %H:%M:%S')}")
        self.log(info)
        pass

    def meal_ready(self,order):
        order.read_at = time()
        self.manager.meal_ready(order)


    def log(self,message):
        with open('kitchen.log', 'a', encoding='utf-8') as f:
            f.write(message + '\n')
