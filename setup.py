from codecs import open
from os import path
try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup


here = path.abspath(path.dirname(__file__))


def read(*parts):
    # Intentionally *not* adding an encoding option to open
    return open(path.join(here, *parts), 'r').read()

long_description = read('README.rst')

config = {
    'name': 'payoneer-escrow-sdk',
    'version': '0.1.0',
    'description': 'An SDK for working with the Payoneer Escrow API',
    'long_description': long_description,
    'author': 'Adam J Hartz',
    'author_email': 'adamha@payoneer.com',
    'url': 'https://github.com/Payoneer-Escrow/payoneer-escrow-python',
    'packages': ['payoneer_escrow_sdk', 'payoneer_escrow_sdk.api'],
    'install_requires': ['requests'],
    'license': 'MIT',
    'classifiers': [
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 3',
        'Topic :: Office/Business :: Financial',
        'Topic :: Software Development',
        ],
    'extras_require': {
        'tests': ['nose'],
        }
    }

setup(**config)
