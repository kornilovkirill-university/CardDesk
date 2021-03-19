import random
from typing import List


class Card:

    _values = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]
    _types_signs = {"diamonds": "\u2666", "hearts": "\u2665", "spades": "\u2660", "clubs": "\u2663"}
    _types_priority = ['\u2665', '\u2666', '\u2663', '\u2660']

    def __init__(self, value, type):
        self._value = self._values.index(str(value).upper())
        self._type = type.lower()

    def to_str(self):
        # return self._values[self._value]+self._type[0:1].lower()
        return self._values[self._value]+self._types_signs[self._type.lower()]

    @staticmethod
    def is_equal_suit(card1, card2):
        return card1.to_str()[1:] == card2.to_str()[1:]

    @classmethod
    def is_more(cls, card1, card2):
        card1_val = cls._values.index(card1.to_str()[0:1])
        card2_val = cls._values.index(card2.to_str()[0:1])
        if card1_val == card2_val:
            return cls._is_suit_more(card1, card2)
        return card1_val > card2_val

    @classmethod
    def is_less(cls, card1, card2):
        card1_val = cls._values.index(card1.to_str()[0:1])
        card2_val = cls._values.index(card2.to_str()[0:1])
        if card1_val == card2_val:
            return cls._is_suit_less(card1, card2)
        return card1_val < card2_val

    @classmethod
    def _is_suit_more(cls, card1, card2):
        suit1 = card1.to_str()[1:]
        suit2 = card2.to_str()[1:]
        suit1_priority = cls._types_priority.index(suit1)
        suit2_priority = cls._types_priority.index(suit2)
        return suit1_priority > suit2_priority

    @classmethod
    def _is_suit_less(cls, card1, card2):
        suit1 = card1.to_str()[1:]
        suit2 = card2.to_str()[1:]
        suit1_priority = cls._types_priority.index(suit1)
        suit2_priority = cls._types_priority.index(suit2)
        return suit1_priority < suit2_priority


class Deck:
    def __init__(self):
        self._cards = []
        for type in ["Hearts", "Diamonds", "Clubs", "Spades"]:
            for i in range(2, 11):
                self._cards.append(Card(i, type))
            self._cards.append(Card("J", type))
            self._cards.append(Card("Q", type))
            self._cards.append(Card("K", type))
            self._cards.append(Card("A", type))

    def show(self):
        if len(self._cards) == 0:
            return "desk[0]"
        res = "desk["+str(len(self._cards))+"]: "
        res = res + self._cards[0].to_str()
        for card in self._cards[1:]:
            res = res + ", " + card.to_str()
        return res

    def draw(self, x) -> List[Card]:
        if x < 0:
            raise IndexError
        result = self._cards[0:x]
        self._cards = self._cards[x:]
        return result

    def shuffle(self):
        random.shuffle(self._cards)


deck = Deck()
for el in deck.draw(10):
    print(el.to_str(), end=" ")
print()
print(deck.show())
deck.shuffle()
print(deck.show())

# print(Card.is_equal_suit(c2, c1))
# print(c1.to_str())

