from importlib.resources import files, open_text

from spacy.lang.zh import ChineseTokenizer, Segmenter
from spacy.language import Language
from spacy.util import load_config, registry

from .lex_attrs import LEX_ATTRS
from .stop_words import STOP_WORDS


# For now, just extend the default Chinese tokenizer
class KanbunTokenizer(ChineseTokenizer):
    pass


# Without a model, just segment by character
# https://spacy.io/api/tokenizer
@registry.tokenizers("spacy.och.OldChineseTokenizer")
def create_kanbun_tokenizer():
    def kanbun_tokenizer_factory(nlp: Language):
        return KanbunTokenizer(nlp, segmenter=Segmenter.char)

    return kanbun_tokenizer_factory


# TODO: implement UD-Kanbun's tokenizer
# class UDKanbunTokenizer:
#     def __init__(self, vocab, udpipe_model):
#         self.vocab = vocab
#         self.model = ufal.udpipe.Model.load(udpipe_model)
#         self.pipe = ufal.udpipe.Pipeline(
#             self.model,
#             "tokenizer=joint_with_parsing",
#             "tagger=none",
#             "parser=none",
#             "sentencizer=none",
#         )
#
#     def __call__(self, text):
#         words = []
#         spaces = [False] * len(words)
#         return Doc(self.vocab, words=words, spaces=spaces)


# https://spacy.io/api/language#defaults
class KanbunDefaults(Language.Defaults):
    config = load_config(open_text(__name__, "config.cfg"))
    lex_attr_getters = LEX_ATTRS
    stop_words = STOP_WORDS
    writing_system = {"direction": "ltr", "has_case": False, "has_letters": False}


# https://spacy.io/api/language#class-attributes
@registry.languages("lzh")
class Kanbun(Language):
    lang = "lzh"
    Defaults = KanbunDefaults


# Add lookups to the registry
# https://spacy.io/api/lookups
@registry.lookups("och")
def find_lookups():
    return {file.stem[4:]: str(file) for file in files("och.lookups").glob("*.json")}


__all__ = ["Kanbun"]
