from itertools import cycle
from typing import Tuple, Optional


class DrawException(Exception):
    pass


class Connect4Game:
    def __init__(
            self, cols: int = 7,
            rows: int = 6,
            players: Tuple[str] = ('A', 'B'),
            win_condition: int = 4,
    ):
        self.players = cycle(players)
        self.cols = cols
        self.rows = rows
        self.win_condition = win_condition
        self.field = [
            [None for col in range(cols)]
            for row in range(rows)
        ]
        self.current_player = next(self.players)

    def show_field(self):
        for row in self.field:
            print(' '.join(col or '_' for col in row))
        print()

    def player_turn(self):
        while True:
            try:
                col = int(input(f'{self.current_player} > ')) - 1
                if col < 0 or col >= self.cols:
                    raise ValueError
                for row in reversed(range(self.rows)):
                    if self.field[row][col] is None:
                        self.field[row][col] = self.current_player
                        self.current_player = next(self.players)
                        return
                raise ValueError
            except ValueError:
                print("Wrong input, please try again")

    def get_winner(self) -> Optional[str]:
        figure, repeats = None, 0
        for row in range(self.rows):
            for col in range(self.cols):
                if self.field[row][col] is None:
                    figure, repeats = None, 0
                else:
                    if self.field[row][col] == figure:
                        repeats += 1
                    else:
                        repeats = 1
                    figure = self.field[row][col]
                    if repeats == self.win_condition:
                        return figure

        for col in range(self.cols):
            for row in range(self.rows):
                if self.field[row][col] is None:
                    figure, repeats = None, 0
                else:
                    if self.field[row][col] == figure:
                        repeats += 1
                    else:
                        repeats = 1
                    figure = self.field[row][col]
                    if repeats == self.win_condition:
                        return figure

        if not any([None in row for row in self.field]):
            raise DrawException

    def run_game(self):
        while True:
            self.show_field()
            self.player_turn()
            try:
                winner = self.get_winner()
                if winner:
                    self.show_field()
                    print(f"Player {winner} wins!")
                    return
            except DrawException:
                print("It's a draw!")
                return


if __name__ == '__main__':
    game = Connect4Game()
    game.run_game()
