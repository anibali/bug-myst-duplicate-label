import os
import sys
sys.path.insert(0, os.path.abspath('..'))

project = 'My Project'
copyright = '2023, John Doe'
author = 'John Doe'
extensions = [
    'myst_parser',
    'sphinx.ext.autodoc',
]
