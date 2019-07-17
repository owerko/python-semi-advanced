'''
nazwa posiłku
godzine złożenie zamowienia
godzine wykoania zamówienia
godzine sobioru zamowinia
'''

from time import time
from datetime import datetime

class Order:

    def __init__(self, name):
        self.name = name
        self.created_at = time()
        self.read_at = None
        self.collected_at = None

    def __str__(self) -> str:
        return f"Order name: {self.name}, zamowienie: {datetime.utcfromtimestamp(self.created_at).strftime('%Y-%m-%d %H:%M:%S')}, " \
            f"odebranie: {datetime.utcfromtimestamp(self.collected_at).strftime('%Y-%m-%d %H:%M:%S')}, " \
            f"gotowe na: {datetime.utcfromtimestamp(self.read_at).strftime('%Y-%m-%d %H:%M:%S')} "
