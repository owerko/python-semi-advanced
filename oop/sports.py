from oop.exeptionClass import *


class Player:

    def __init__(self, name: str, ranking: int):
        if len(name) < 3:
            raise NameToShortExeption()
        self.name = name
        if ranking < 100 or ranking > 10000:
            raise WrongRanking()
        self.ranking = ranking

    def description(self):
        return f'My name is {self.name} and my ranking is {self.ranking}.'


class Game:
    def __init__(self, white: Player, black: Player, result: int):
        results = (1, 2)
        if result not in results:
            raise WrongResult()
        self.result = result
        self.white = white
        self.black = black

    def whiteWon(self):
        return self.result == 1

    def blackWon(self):
        return self.result == 2


class Arena:
    def __init__(self):
        self.games = []

    def add_game(self, game: Game):
        self.games.append(game)

    '''
    1. Stwórz Lista zawodników
    2. Stwórz mapę=słownik zawodnik -> lista zwycięst
    3. Posotruj zawodników po ich zwycięstwach
    '''

    def standing(self):
        palyers = []
        scores = []

        for game in self.games:
            white = game.white
            black = game.black

            if white not in palyers:
                palyers.append(white)
                scores.append(0)
            if black not in palyers:
                palyers.append(black)
                scores.append(0)

            if game.whiteWon():
                index = palyers.index(white)
            else:
                index = palyers.index(black)

            scores[index] += 1

        player_score_list = list(zip(palyers, scores))
        player_score_list.sort(reverse=True, key=lambda x: x[1])

        return [pair[0] for pair in player_score_list]
