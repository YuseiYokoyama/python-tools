import ginza

def bunsetu_iter(doc):
    for b in ginza.bunsetu_spans(doc):
        print('b', b) # debug
