try:
    from setuptools import setup
except ImportError as e:
    from distutils.core import setup

config = {
        'description': 'Morbi - Online Dating Application',
        'author': 'Harshul Jain',
        'url': 'https://blog.harshulja.in/introducing-morbi',
        'download_url': 'https://blog.harshulja.in/introducing-morbi',
        'author_email': '',
        'version': '0.2',
        'install_requires': [

        ],
        'packages': ['morbi'],
        'scripts': [],
        'name': 'morbi',
        'entry_points' : {
            'console_scripts': ['morbi-cli=morbi.run:run'],
        }
    }

setup(**config)
