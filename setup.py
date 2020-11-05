#!/usr/bin/env python
"""
Setup.py for mp3monitoring.
"""

from pathlib import Path

from setuptools import find_packages, setup

from mp3monitoring import static_data

# get long description
with Path('README.rst').open(mode='r', encoding='UTF-8') as reader:
    LONG_DESCRIPTION = reader.read()

setup(
    name=static_data.NAME,
    version=static_data.VERSION,
    description=static_data.DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    long_description_content_type='text/x-rst',
    author=static_data.AUTHOR,
    author_email=static_data.AUTHOR_EMAIL,
    license='GPLv3',
    url=static_data.PROJECT_URL,
    classifiers=[
        'Programming Language :: Python :: 3.8',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Development Status :: 5 - Production/Stable',
        'Operating System :: OS Independent',
        'Intended Audience :: End Users/Desktop',
        'Natural Language :: English',
        'Environment :: Console',
        'Environment :: X11 Applications :: Qt',
    ],
    keywords='mp3 monitoring',
    packages=find_packages(include=['mp3monitoring', 'mp3monitoring.*']),
    python_requires='>=3.8',
    install_requires=[
        'mutagen>=1.45.1',
        'packaging>=20.4',
    ],
    extras_require={
        'gui': [
            'pyqt5>=5.15.1',
            'urllib3[secure]>=1.25.10',
        ],
        'dev': [
            'flake8>=3.8.3',
            'pylint>=2.6.0',
            'pyroma>=2.6',
            'pytest>=6.0.1',
            'pytest-cov>=2.10.1',
            'setuptools>=50.3.0',
            'Sphinx>=3.2.1',
            'sphinx-autodoc-typehints>=1.11.0',
            'sphinx_rtd_theme>=0.5.0',
            'twine>=3.2.0',
            'wheel>=0.35.1',
        ],
    },
    include_package_data=True,
    package_data={
        "mp3monitoring": [
            'gui/pkg_data/icon.svg',
            'gui/pkg_data/symbols/*',
        ],
    },
    zip_safe=True,
    entry_points={
        'console_scripts': [
            'mp3monitoring = mp3monitoring.main:main',
        ],
        'gui_scripts': [
            'mp3monitoring-gui = mp3monitoring.main:main_gui',
        ],
    },
)
