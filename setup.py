#!/usr/bin/env python

# Work around mbcs bug in distutils.
# http://bugs.python.org/issue10945
import codecs

from setuptools import find_packages, setup

from mp3monitoring import static_data

try:
    codecs.lookup('mbcs')
except LookupError:
    ascii = codecs.lookup('ascii')
    func = lambda name, enc=ascii: {True: enc}.get(name=='mbcs')
    codecs.register(func)

setup(
    name=static_data.NAME,
    version=static_data.VERSION,
    description='Monitors a folder and copies mp3s to another folder.',
    author=static_data.AUTHOR,
    author_email=static_data.AUTHOR_EMAIL,
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
