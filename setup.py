from codecs import open
from os import path
import re
from setuptools import setup, find_packages

# Constants

NAME = "markyp-bootstrap4"
ROOT = NAME.replace("-", "_")

# Get the long description from the README file
with open(path.join(path.abspath(path.dirname(__file__)), "README.md"), encoding="utf-8") as f:
    readme = f.read()

# Get the version from the root __init__.py file.
with open(path.join(path.abspath(path.dirname(__file__)), ROOT, "__init__.py"), encoding="utf-8") as f:
    content = f.read()
    _author = re.search("__author__ = \"(.*?)\"", content).group(1)
    _email = re.search("__email__ = \"(.*?)\"", content).group(1)
    _license = re.search("__license__ = \"(.*?)\"", content).group(1)
    _url = re.search("__url__ = \"(.*?)\"", content).group(1)
    _version = re.search("__version__ = \"(.*?)\"", content).group(1)

# Get the requirements from requirements.txt.
req_filename = "requirements.txt"
exp = re.compile("(?P<req>\\w+)\\s*(?P<op>[<>=!~]+)\\s*(?P<ver>[\\w.]+)")
requirements = []
with open(path.join(path.dirname(path.abspath(__file__)), req_filename)) as req_file:
    for line in req_file:
        line = line.split("#", maxsplit=1)[0].strip()
        match = exp.match(line) if line else None
        if match is not None:
            requirements.append(("".join((match["req"], match["op"], match["ver"]))))
requirements.sort(key=lambda s: s.casefold())

setup(
    name=NAME,
    version=_version,
    description="Bootstrap4 components built with markyp-html",
    long_description=readme,
    long_description_content_type="text/markdown",
    url=_url,
    author=_author,
    author_email=_email,
    license=_license,
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Natural Language :: English",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3 :: Only",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Topic :: Internet :: WWW/HTTP :: Dynamic Content",
        "Topic :: Software Development :: Code Generators",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Text Processing :: Markup :: HTML",
        "Topic :: Utilities",
        "Typing :: Typed"
    ],
    keywords="bootstrap html markup generator utility",
    packages=find_packages(exclude=["test"]),
    python_requires=">=3.6",
    install_requires=requirements
)
