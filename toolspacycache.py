import spacy
import toolspacycache

nlp = spacy.load("ja_ginza")
doc_list = toolspacycache.apply_text_list(nlp, text_list)

