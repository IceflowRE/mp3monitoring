import sys
from pathlib import Path

import sphinx_rtd_theme

sys.path.insert(0, str(Path('../mp3monitoring').resolve()))
extensions = [
    'sphinx.ext.autodoc',
    'sphinx_autodoc_typehints',
    'sphinx.ext.intersphinx',
    'sphinx.ext.todo',
    'sphinx.ext.coverage',
    'sphinx.ext.viewcode',
]
source_suffix = '.rst'
master_doc = 'index'

project = 'MP3 Monitoring'
author = 'Iceflower S'
copyright = '2017-present, Iceflower S'
title = project + ' Documentation'
version = '2.0.0'
release = '2.0.0'

language = 'english'
pygments_style = 'sphinx'
html_theme = 'sphinx_rtd_theme'
html_theme_path = [sphinx_rtd_theme.get_html_theme_path()]
html_static_path = ['_static']
html_css_files = [
    'css/style.css',
]

inkscape_converter_bin = r'inkscape'

intersphinx_mapping = {
    'python': ('https://docs.python.org/3/', None),
    'urllib3': ('https://urllib3.readthedocs.io/en/latest/', None),
    'packaging': ('https://packaging.pypa.io/en/latest/', None),
}
