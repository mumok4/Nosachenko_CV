# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'toolchain'
copyright = '2023, Artem Vesnin, Albert Nosachenko'
author = 'Artem Vesnin, Albert Nosachenko'
release = '1.0'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = ['myst_parser',
              'sphinx.ext.mathjax',
             'sphinx.ext.autodoc']

templates_path = ['_templates']
exclude_patterns = ['projects/mtracker/*',
                    'README.md']

language = 'ru'

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'alabaster'
html_static_path = ['_static']

source_suffix = {
    '.rst': 'restructuredtext',
    '.txt': 'restructuredtext',
    '.md': 'markdown',
}

# -- Options for PDF output -------------------------------------------------

latex_engine = 'xelatex'
latex_elements = {
    'papersize': 'a4paper',  # Формат бумаги
    'pointsize': '10pt',     # Размер шрифта
    'figure_align': 'htbp',  # Выравнивание изображений
}
