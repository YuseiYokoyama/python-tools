import ginza

def bunsetu_iter(doc):
    for b in ginza.bunsetu_spans(doc):
        print('b', b) # debug

from spacy.tokens import Token

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

