from setuptools import setup, find_packages

# read the contents of your README file
from os import path
this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

# Needed dependencies
INSTALL_REQUIRES = []

setup(name = 'peax',
      version = '0.0.1',

      url = 'https://github.com/MattiaCinelli/peax',
      description = 'Peax exercise',
      long_description_content_type = 'text/markdown',
      long_description = long_description,
      
      packages = find_packages(),
      install_requires = INSTALL_REQUIRES,
      python_requires = '>=3.7',

      author = 'Mattia Cinelli',
      author_email = '',
      license = '',

      zip_safe = False
      )