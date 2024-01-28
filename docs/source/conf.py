# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information
import sys 
import os

sys.path.insert(0, os.path.abspath('../..')) # Add here any underlying folders!
sys.path.insert(0, os.path.abspath('../../pytools')) # Add here any underlying folders!

project = 'PyTools'
copyright = '2024, Johan Carlsen'
author = 'Johan Carlsen'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    'sphinx.ext.autodoc', 
    'sphinx.ext.napoleon', 
    'numpydoc', 
    'sphinx.ext.autosummary',
    'sphinx_autodoc_typehints',
    'sphinx.ext.viewcode'
]
autosummary_generate = True
autosummary_imported_members = True
templates_path = ['_templates']
exclude_patterns = []

def linkcode_resolve(domain, info):
    if domain != 'py':
        return None
    if not info['module']:
        return None
    filename = (info['module'].replace('.', '/'))
    return "https://github.com/JohanCarlsen/fys-stk4155/%s.py" % filename

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'sphinx_rtd_theme'
# viewcode_enable_epub = True
# html_theme = 'pydata_sphinx_theme'
html_static_path = ['_static']
