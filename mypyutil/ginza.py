import spacy
import ginza
from spacy.tokens import Token


def bunsetu_iter(doc):
    for b in ginza.bunsetu_spans(doc):
        print('b', b) # debug

def get_tag(token, num):
    tags = token.tag_.split("-")
    if num < len(tags):
        return tags[num]
    return None

Token.set_extension("tag_0", getter=lambda token: get_tag(token, 0))
Token.set_extension("tag_1", getter=lambda token: get_tag(token, 1))
Token.set_extension("tag_2", getter=lambda token: get_tag(token, 2))
Token.set_extension("tag_3", getter=lambda token: get_tag(token, 3))
# print('token.tag_1', token._.tag_1) # debug

# pos, dep list https://qiita.com/kei_0324/items/400f639b2f185b39a0cf


#TODO looking is not good name
def get_looking(core_token):
    looking = []
    Token.set_extension("flg_looking", default=False)
    for a in core_token.ancestors:
        for t in ginza.bunsetu_span(a):
            t._.flg_looking = True
    for token in doc:
        if token._.flg_looking:
            looking.append(token)
    Token.remove_extension("flg_looking")
    return looking


if __name__ == '__main__':
    from pprint import pprint as pp
    from pprint import pformat as pf

    nlp = spacy.load("ja_ginza")
    text = "10日から調査として16時以降は、可能です。"
    doc = nlp(text)
    print('doc') # debug
    print(doc) # debug
    token = doc[5]
    looking = get_looking(token)
    print('looking') # debug
    pp(looking) # debug

    print('\33[32m' + 'end' + '\033[0m')

