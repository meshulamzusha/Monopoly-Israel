class Game:
    def __init__(self, table, player, aiplayer):
        self.table = table
        self.player = player
        self.dice = Dice()

    def play(self):
        self.print_start_massege()
        turns = 0
        max_turns = 20
        while turns < max_turns and self.player.mony > 0:
            steps = self.dice.rolling_die()
            self.player.set_current_tile(steps)
            new_location = self.player.current_tile()
            self.table.tiles[new_location].display()
            if isinstance(new_location, BiznesTile):
                self.biznes_tile_proces()
            elif isinstance(new_location, (Bonus, Start)):
                self.player.set_mony()
            elif isinstance(new_location, Tax):
                self.tax_proces()
