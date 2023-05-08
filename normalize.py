import argparse
from pprint import pprint as pp
from pprint import pformat as pf

import mojimoji
import unicodedata

def normalize(text):
    """
    括弧を半角に
    アルファベットを半角に
    普通の数字を半角に
    カタカナは全角に
    """
    #TODO 丸数字を括弧数字に
    text =  mojimoji.zen_to_han(text, kana=False)
    text =  mojimoji.han_to_zen(text, ascii=False, digit=False)
    return text

if __name__ == '__main__':
    parser = argparse.ArgumentParser("This is hogehoge")
    args = parser.parse_args()

    
    text = "「」『』（）｛｝［］(){}[]ABCＡＢＣ123１２３ｱｲｳアイウガｶﾞ"
    text = normalize(text)
    answer = "「」『』(){}[](){}[]ABCABC123123アイウアイウガガ"
    assert text == answer, text
    text = "ガｶﾞ"
    text = normalize(text)
    assert len(text) == 2, text

    print('\033[32m' + 'end' + '\033[0m')

