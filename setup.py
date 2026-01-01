from setuptools import setup

setup(
    name="tamil_translator",
    py_modules=["add_tamil_translated_titles"],
    install_requires=[
   "indic_transliteration==2.3.75"
]
)
