from gettext import install
from setuptools import setup
from setuptools import find_packages


setup(
    name = "overloading",
    version = "1.0.1",
    url = "https://github.com/toinnn/Python_Overloading",
    packages = find_packages() ,
    license = "LICENSE",
    install_requires = ["certifi>=2021.10.8" , "wincertstore"]
)