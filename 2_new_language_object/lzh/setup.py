from setuptools import setup

setup(
    name="lzh",
    entry_points={
        "spacy_languages": ["lzh = lzh:Kanbun"],
    },
)
