from setuptools import setup, find_packages

setup(
    name="llm_privacy",
    version="0.1.0",
    packages=find_packages(),
    install_requires=["spacy", "openai"],
)
