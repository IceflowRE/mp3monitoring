#!/usr/bin/env python

from setuptools import find_packages, setup

# Work around mbcs bug in distutils.
# http://bugs.python.org/issue10945
import codecs
try:
    codecs.lookup('mbcs')
except LookupError:
    ascii = codecs.lookup('ascii')
    func = lambda name, enc=ascii: {True: enc}.get(name=='mbcs')
    codecs.register(func)

setup(
    name='MP3 Monitoring',
    version='1.0.0',
    description='Monitors a folder and copies mp3s to another folder.',
    author='Iceflower S',
    author_email='iceflower@gmx.de',
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
        'License': ['LICENSE'],
        'ReadMe': ['README.md'],
    },
    zip_safe=True,
    scripts=[
        'bin/mp3-monitoring'
    ],
)
