from monopoly.tile.base_tile import Tile


class BonusTile(Tile):
    def __init__(self, name: str, type: str, city: str) -> None:
        super().__init__(name, type, city)


    def display_tile(self) -> None:
        pass


    def arrival_message(self) -> None:
        pass