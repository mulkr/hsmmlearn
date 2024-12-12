hsmmlearn
=========

`hsmmlearn` is a library for **unsupervised** learning of hidden semi-Markov
models with explicit durations. It is a port of the
[hsmm package](https://cran.r-project.org/web/packages/hsmm/) for R, and in
fact wraps the same underlying C++ library.

Since the [original version](https://github.com/jvkersch/hsmmlearn) was abandoned. I decided to pick up the maintenance of the project.

I am not yet too familiar with the underlying C++ code. If you see inaccuracies in any of the algorithms please open an issue/pull request about it and we can figure out a way to correct it.

`hsmmlearn` borrows its name and the design of its api from
[hmmlearn](http://hmmlearn.readthedocs.org/en/latest/).

Install
-------

`hsmmlearn` supports Python 3.6 and up. After cloning the
repository, you can install the package by running 
```console
pip install .
```
(PyPi distribution is planned in the future)

**IMPORTANT!**

You will need a C++ compiler to build and install the package

Building the documentation
--------------------------

The documentation for `hsmmlearn` is a work in progress. To build the docs,
first install the doc requirements, then run Sphinx:
```console
cd docs
pip install -r doc_requirements.txt
make html
```
If everything goes well, the documentation should be in `docs/_build/html`.

Some of the documentation comes as jupyter notebooks, which can be found in the
`notebooks/` folder. Sphinx ingests these, and produces rst documents out of
them. If you end up modifying the notebooks, run `make notebooks` in the
documentation folder and check in the output.