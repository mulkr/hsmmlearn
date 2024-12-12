""" Hidden semi-Markov models with explicit durations in Python.
"""
import glob
import os

from setuptools import find_packages, setup, Extension


SOURCES = (
    ["hsmmlearn/base.pyx"] + glob.glob('hsmmlearn/_hsmm/src/*.cpp')
)


def get_extension_modules():
    # ReadTheDocs has trouble with C extension modules, so don't build the
    # Cython modules.
    on_rtd = os.environ.get('READTHEDOCS', None) == 'True'
    if on_rtd:
        return []
    else:
        from Cython.Build import cythonize
        extensions = [
            Extension("hsmmlearn.base", SOURCES, language="c++")
        ]
        return cythonize(extensions)


CLASSIFIERS = [
    "Development Status :: 3 - Alpha",
    "License :: OSI Approved",
    "Intended Audience :: Developers",
    "Intended Audience :: Science/Research",
    "Topic :: Software Development",
    "Topic :: Scientific/Engineering",
    "Programming Language :: Cython",
    "Programming Language :: Python",
    "Programming Language :: Python :: 3.10"
]

REQUIREMENTS = [
    "numpy>=1.25.2",
    "scipy>=1.9.3"
]

DESCRIPTION = __doc__
MAINTAINER = 'Kristóf Müller'
MAINTAINER_EMAIL = 'muller.kristof@itk.ppke.hu'
LICENSE = 'GPL v3'

with open('README.md', encoding="utf-8") as handle:
    LONG_DESCRIPTION = handle.read()

setup(
    name='hsmmlearn',
    ext_modules=get_extension_modules(),
    packages=find_packages(include=["hsmmlearn"]),
    include_package_data=True,
    install_requires=REQUIREMENTS,
    classifiers=CLASSIFIERS,
    version='0.1.1',
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    maintainer=MAINTAINER,
    maintainer_email=MAINTAINER_EMAIL,
    license=LICENSE,
    python_requires=">=3.10"
)
