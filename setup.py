#!/usr/bin/env python

# Work around mbcs bug in distutils.
# http://bugs.python.org/issue10945
import codecs

from setuptools import find_packages, setup

import mp3monitoring.data.static

try:
    codecs.lookup('mbcs')
except LookupError:
    ascii = codecs.lookup('ascii')
    func = lambda name, enc=ascii: {True: enc}.get(name == 'mbcs')
    codecs.register(func)

_OPTIONAL = {
    'with_gui': ['PyQt5 >= 5.9.1'],
    'with_updater': ['urllib3'],
}
with_everything = [package for optional_list in _OPTIONAL.values() for package in optional_list]
_OPTIONAL['with_everything'] = with_everything
devel_pkg = _OPTIONAL['with_everything'] + [
    'prospector[with_everything]',
    'cov-core',
    'codecov',
    'coverage',
    'nose2',
    'Sphinx',
]
_OPTIONAL['dev'] = devel_pkg

setup(
    name=mp3monitoring.data.static.NAME,
    version=mp3monitoring.data.static.VERSION,
    description='Monitors a folder and copies mp3s to another folder.',
    author=mp3monitoring.data.static.AUTHOR,
    author_email=mp3monitoring.data.static.AUTHOR_EMAIL,
    license='GPLv3',
    classifiers=[
        'Programming Language :: Python :: 3.6',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Development Status :: 4 - Beta',
        'Operating System :: OS Independent',
        'Intended Audience :: End Users/Desktop',
        'Natural Language :: English',
        'Environment :: Console',
        'Environment :: X11 Applications :: Qt',
    ],
    packages=find_packages(),
    python_requires='>=3.6',
    install_requires=[
        'mutagen',
        'tqdm',
    ],
    extras_require=_OPTIONAL,
    package_data={
        "mp3monitoring": [
            'pkg_data/gui/icon_export.svg',
        ],
    },
    include_package_data=True,
    zip_safe=True,
    entry_points={
        'console_scripts': [
            'mp3-monitoring = mp3monitoring.core:start',
        ],
        'gui_scripts': [
            'mp3-monitoring-gui = mp3monitoring.core:gui_start',
        ],
    },
)
