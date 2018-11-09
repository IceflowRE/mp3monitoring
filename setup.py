#!/usr/bin/env python

from setuptools import find_packages, setup

import mp3monitoring.data.static as static_data

_OPTIONAL = {
    'gui': ['pyqt5==5.11.3'],
    'updater': ['urllib3==1.24.1'],
}
_OPTIONAL['with_everything'] = [package for optional_list in _OPTIONAL.values() for package in optional_list]
_OPTIONAL['dev'] = _OPTIONAL['with_everything'] + [
    'prospector[with_everything]',
    'cov-core',
    'codecov',
    'coverage',
    'nose2',
    'Sphinx',
]

setup(
    name=static_data.NAME,
    version=static_data.VERSION,
    description='Monitors a folder and copies mp3s to another folder.',
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
    packages=find_packages(exclude=['gui', 'installer', 'scripts', 'tests']),
    python_requires='>=3.6',
    install_requires=[
        'mutagen==1.41.1',
        'tqdm==4.28.1',
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
