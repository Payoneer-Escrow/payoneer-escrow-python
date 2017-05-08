import codecs
import os
try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup


here = os.path.abspath(os.path.dirname(__file__))


def read(*parts):
    # Intentionally *not* adding an encoding option to open
    return codecs.open(os.path.join(here, *parts), 'r').read()


long_description = read('README.md')

config = {
    'name': 'Payoneer Escrow SDK',
    'version': '0.1',
    'description': 'An SDK for working with the Payoneer Escrow API',
    'long_description': long_description,
    'author': 'Adam J Hartz',
    'author_email': 'adamha@payoneer.com',
    'url': 'https://github.com/Payoneer-Escrow/payoneer-escrow-python',
    'packages': ['payoneer_escrow_sdk', 'payoneer_escrow_sdk.api'],
    'install_requires': ['requests'],
    'license': 'MIT',
    'tests_require': ['nose'],
    }

setup(**config)
