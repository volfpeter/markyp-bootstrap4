from codecs import open
from os import path
import re
from setuptools import setup, find_packages

# Get the long description from the README file
with open(path.join(path.abspath(path.dirname(__file__)), "README.md"), encoding="utf-8") as f:
    readme = f.read()

# Get the version from the root __init__.py file.
with open(path.join(path.abspath(path.dirname(__file__)), "src", "markyp_bootstrap4", "__init__.py"), encoding="utf-8") as f:
    match = re.search("__version__ = \"(.*?)\"", f.read())
    version = match.group(1) if match else "0.0.0"

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
    name="markyp-bootstrap4",
    version=version,
    description="Bootstrap4 components built with markyp-html",
    long_description=readme,
    long_description_content_type="text/markdown",
    url="https://github.com/volfpeter/markyp-bootstrap4",
    author="Peter Volf",
    author_email="do.volfp@gmail.com",
    license="MIT",
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
    package_dir={"": "src"},
    packages=find_packages("src", exclude=["test"]),
    python_requires=">=3.6",
    install_requires=requirements
)
