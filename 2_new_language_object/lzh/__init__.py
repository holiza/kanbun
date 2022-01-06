from importlib.resources import read_text

from spacy.lang.zh import ChineseTokenizer, Segmenter
from spacy.language import Language
from spacy.util import load_config_from_str, registry

from .lex_attrs import LEX_ATTRS
from .stop_words import STOP_WORDS


# For now, just extend the default Chinese tokenizer
class KanbunTokenizer(ChineseTokenizer):
    pass


# Without a model, just segment by character
# https://spacy.io/api/tokenizer
@registry.tokenizers("spacy.lzh.KanbunTokenizer")
def create_kanbun_tokenizer():
    def kanbun_tokenizer_factory(nlp: Language):
        return KanbunTokenizer(nlp.vocab, segmenter=Segmenter.char)

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
    config = load_config_from_str(read_text(__name__, "config.cfg"))
    lex_attr_getters = LEX_ATTRS
    stop_words = STOP_WORDS
    writing_system = {"direction": "ltr", "has_case": False, "has_letters": False}


# https://spacy.io/api/language#class-attributes
@registry.languages("lzh")
class Kanbun(Language):
    lang = "lzh"
    Defaults = KanbunDefaults


__all__ = ["Kanbun"]
