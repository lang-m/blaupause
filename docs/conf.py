# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
# import os
# import sys
# sys.path.insert(0, os.path.abspath('.'))


# -- Project information -----------------------------------------------------

project = 'blaupause'
copyright = '2020, Martin Lang and Marijan Beg'
author = 'Martin Lang and Marijan Beg'


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = ['sphinx.ext.napoleon',
              'sphinx.ext.mathjax',
              'nbsphinx',
              'sphinx.ext.autodoc',
              'sphinx.ext.autosummary',
              ]

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

autosummary_generate = True
autoclass_content = 'class'  # 'both' to include __init__ docstring
autosummary_imported_members = True

# special methods to include in autosummary
autosummary_context = {
    'included_special_methods': ['__add__', '__radd__', '__repr__']
}

autodoc_inherit_docstrigs = True
autodoc_default_options = {
    'member-order': 'groupwise',
    'exclude-members': '__init__, __weakref__'
}

# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = 'furo'

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']
