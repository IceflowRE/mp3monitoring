#!/usr/bin/env python
from pathlib import Path

from setuptools import find_packages, setup

import mp3monitoring.data.static as static_data

# get long description
with Path('README.rst').open(mode='r', encoding='UTF-8') as reader:
    long_description = reader.read()

_OPTIONAL = {
    'gui': ['pyqt5==5.11.3'],
    'updater': ['urllib3[secure]==1.24.1'],
}
_OPTIONAL['with_everything'] = _OPTIONAL['gui'] + _OPTIONAL['updater']
_OPTIONAL['dev'] = _OPTIONAL['with_everything'] + [
    'prospector[with_everything]==1.1.3',
    'nose2[coverage_plugin]==0.8.0',
    'twine==1.12.1',
    'setuptools==40.4.3',
    'wheel==0.32.1',
]

setup(
    name=static_data.NAME,
    version=static_data.VERSION,
    description=static_data.DESCRIPTION,
    long_description=long_description,
    author=static_data.AUTHOR,
    author_email=static_data.AUTHOR_EMAIL,
    license='GPLv3',
    url=static_data.PROJECT_URL,
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
    keywords='mp3 monitoring',
    packages=find_packages(include=['mp3monitoring', 'mp3monitoring.*']),
    python_requires='>=3.6',
    install_requires=[
        'mutagen==1.41.1',
        'tqdm==4.28.1',
        'packaging==18.0',
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
            'mp3monitoring = mp3monitoring.core:start',
        ],
        'gui_scripts': [
            'mp3monitoring-gui = mp3monitoring.core:gui_start',
        ],
    },
)
