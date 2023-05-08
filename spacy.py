import spacy

""" MEMO
nlp.pipeline = [
    ('tok2vec', <spacy.pipeline.tok2vec.Tok2Vec object at 0x7fbc3d816440>),
    ('parser', <spacy.pipeline.dep_parser.DependencyParser object at 0x7fbc3d811460>),
    ('ner', <spacy.pipeline.ner.EntityRecognizer object at 0x7fbc3d8114d0>),
    ('morphologizer', <spacy.pipeline.morphologizer.Morphologizer object at 0x7fbc3d8164a0>),
    ('compound_splitter', <ginza.compound_splitter.CompoundSplitter object at 0x7fbc3d842560>),
    ('bunsetu_recognizer', <ginza.bunsetu_recognizer.BunsetuRecognizer object at 0x7fbc3d843fd0>)
]
"""

#TODO loading model is heavy, consult with SWE
exclude = ["ner", "morphologizer", "compound_splitter", ] # "tok2vec" is needed for bunsetu_recognizer
nlp = spacy.load("ja_ginza", exclude=exclude)
doc_list = nlp.pipe(text_list)
