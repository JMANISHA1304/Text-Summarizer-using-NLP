import setuptools

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()
    
__version__ = "0.0.0"

REPO_NAME = "Text-Summarizer-using-NLP"
AUTHOR_USER = "ManishaJ"
SRC_REPO="textSummarizer"
AUTHOR_USER = "jmanisha2003@gmail.com"

setuptools.setup(
    name=SRC_REPO,
    version=__version__,
    author=AUTHOR_USER,
    author_email="jmanisha2003@gmail.com",
    description="A text summarizer using Natural Language Processing (NLP)",
    long_description=long_description,
    long_description_content="text/markdown",
    url=f"https://github.com/{AUTHOR_USER}/{REPO_NAME}",
    project_urls={
        "Bug Tracker": "https://github.com/{AUTHOR_USER}/{REPO_NAME}/issues",
    },
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src")
)