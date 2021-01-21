from abc import abstractmethod, ABC


class Clothes(ABC):

    @abstractmethod
    def tissue(self):
        pass


class Coat(Clothes):
    coat_cnt = 0

    def __init__(self, size):
        self.size = size
        self.formula = round(self.size / 6.5 + 0.5, 2)
        Coat.coat_cnt += self.formula

    @property
    def tissue(self):
        print(f'На пальто понадобится {self.formula}м ткани')


class Suit(Clothes):
    suit_cnt = 0

    def __init__(self, rise):
        self.rise = rise
        self.formula = round(2 * self.rise + 0.3, 2)
        Suit.suit_cnt += self.formula

    @property
    def tissue(self):
        print(f'На костюм понадобится {self.formula}м ткани')


class CountTissue:
    def calculating():
        print(f'Расход ткани на всю одежду: {Coat.coat_cnt + Suit.suit_cnt}м')


coat1 = Coat(48)
coat1.tissue

suit1 = Suit(170)
suit1.tissue

suit2 = Suit(180)
suit2.tissue

CountTissue.calculating()
