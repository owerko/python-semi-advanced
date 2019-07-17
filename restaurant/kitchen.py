from time import sleep, time

class Kitchen:

    def __init__(self, manager):
        self.manager = manager


    def prepare_meal(self, order):
        print(f'Kuchnia: zaczynam przygotowywać posiłek {order.name}')
        sleep(5)
        self.meal_ready(order)

    def meal_ready(self, order):
        order.ready_at = time()
        self.manager.meal_ready(order)

    @staticmethod
    def log(message):
        with open('kitchen.log', 'a', encoding='utf-8') as f:
            f.write(message + '\n')