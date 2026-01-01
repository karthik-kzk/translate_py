from setuptools import setup

setup(
    name="tamil_translator",
    py_modules=["add_tamil_translated_titles"],
    install_requires=[
   "googletrans==4.0.0rc1"
]
)
