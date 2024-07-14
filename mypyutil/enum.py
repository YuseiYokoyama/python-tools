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
            return conv[value]
        raise ValueError(f"can not make Speaker from {value}")

    # Speaker.__members__ # ref. https://docs.python.org/ja/3/library/enum.html#enum.EnumType.__members__

conv = { #NOTE write out of class to avoid Speaker is not defined
        "OP": Speaker.OP,
        "CU": Speaker.CU,
        }

