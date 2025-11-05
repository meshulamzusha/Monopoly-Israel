class Tile:
    def __init__(self, name: str, type: str, city: str) -> None:
        self.name = name
        self.type = type
        self.city = city
        self.payment_required = False


    def display_tile(self) -> None:
        pass


    def arrival_message(self) -> None:
        pass
