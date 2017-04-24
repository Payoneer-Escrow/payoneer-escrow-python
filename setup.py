try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description': 'An SDK for working with the Payoneer Escrow API',
    'author': 'Adam J Hartz',
    'url': 'URL to get it at.',
    'download_url': 'Where to download it.',
    'author_email': 'adamha@payoneer.com',
    'version': '0.1',
    'install_requires': ['nose'],
    'packages': ['payoneer_escrow_sdk', 'payoneer_escrow_sdk.api'],
    'scripts': [],
    'name': 'Payoneer Escrow SDK'
}

setup(**config)
