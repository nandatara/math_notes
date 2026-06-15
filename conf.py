# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'Math Notes'
copyright = '2026, Dr. Tara Nanda'
author = 'Dr. Tara Nanda'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    'sphinx.ext.mathjax',
]

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store', 'lecture_template.rst']

html_theme = 'classic'
html_static_path = ['_static']

# Configure the sidebar layout
html_sidebars = {
    '**': [
        'localtoc.html',     # Table of contents for the current page
        'relations.html',    # Next and Previous page links
        'searchbox.html',    # Quick search box
    ]
}

