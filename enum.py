from enum import Enum

class Speaker(Enum):
    """
    発話者のデータクラス
    """
    OP = 0
    CU = 1 # customer first


    def __repr__(self):
        return self.name

speaker_conv = {
        "OP": Speaker.OP,
        "CU": Speaker.CU,
        }

