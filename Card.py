'''
Class card 
    attributes:
        suite
        number
        toString
        get int
        get suite
'''

class Card:
    def __init__(self, new_suite, new_value):
        assert new_suite in ['hearts', 'spades', 'diamonds', 'clubs', 'special'], 'wrong suite given'
        assert new_value in range(1, 14) or new_value == -1, 'wrong value given'
        self.suite = new_suite
        self.value = new_value

    def get_suite(self):
        return self.suite

    def get_value(self):
        return self.value

    def __str__(self):
        if self.value == 1:
            return f"Ace of {self.suite}"
        elif 1 < self.value < 11:
            return f"{self.get_value()} of {self.get_suite()}"
            #ret_str = str(self.get_value()) + " of " + self.get_suite()
            #return ret_str
        elif self.value == 11:
            return f"Jack of {self.suite}"
        elif self.value == 12:
            return f"Queen of {self.get_suite()}"
        elif self.value == 13:
            return f"King of {self.get_suite()}"
        elif self.value == -1:
            return f"Joker"

    def __eq__(self, right):
        if (type(right) != Card):
            return False
        return self.get_suite() == right.get_suite() and self.get_value() == right.get_value()

if __name__ == "__main__":
    newCard = Card('hearts', 11)
    newCard2 = Card('hearts', 11)
    print(newCard == newCard2)
