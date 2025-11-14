from enum import Enum

class Speaker(Enum):
    """
    発話者のデータクラス
    """
    OP = 0
    CU = 1 # customer first


    def __repr__(self):
        return self.name

    @staticmethod
    def construct(value):
        if type(value) == Speaker:
            return value
        if type(value) == str:
            # ref. https://docs.python.org/ja/3/library/enum.html#enum.EnumType.__members__
            return Speaker.__members__[value]
        raise ValueError(f"can not make Speaker from {value}")

if __name__ == '__main__':
    speacker_op = Speaker(0)

