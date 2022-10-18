# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

from pnwapi import __version__ as version

project = 'pnwapi'
copyright = '2022, Cikmo'
author = 'Cikmo'
release = version

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = ['sphinx.ext.autodoc',
              'autoapi.extension']

templates_path = ['_templates']
exclude_patterns = []

autoapi_type = 'python'
autoapi_dirs = ['../../pnwapi']
autoapi_root = 'api'
autoapi_add_toctree_entry = True


# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']
