#!/usr/bin/env python

# Work around mbcs bug in distutils.
# http://bugs.python.org/issue10945
import codecs

from setuptools import find_packages, setup

from data import static

try:
    codecs.lookup('mbcs')
except LookupError:
    ascii = codecs.lookup('ascii')
    func = lambda name, enc=ascii: {True: enc}.get(name=='mbcs')
    codecs.register(func)

setup(
    name=static.NAME,
    version=static.VERSION,
    description='Monitors a folder and copies mp3s to another folder.',
    author=static.AUTHOR,
    author_email=static.AUTHOR_EMAIL,
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
    install_requires=[
        'mutagen',
        'tqdm',
        'PyQt5',
    ],
    package_data={
        'License': ['LICENSE.md'],
        'ReadMe': ['README.md'],
    },
    zip_safe=True,
    scripts=[
        'bin/mp3-monitoring'
    ],
)
