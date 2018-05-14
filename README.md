schulze-method [![Build status][Build image]][Build] [![Updates][Dependency image]][PyUp] [![Python 3][Python3 image]][PyUp] [![Code coverage][Codecov image]][Codecov]
==============

  [Build]: https://travis-ci.org/woctezuma/schulze-method
  [Build image]: https://travis-ci.org/woctezuma/schulze-method.svg?branch=master

  [PyUp]: https://pyup.io/repos/github/woctezuma/schulze-method/
  [Dependency image]: https://pyup.io/repos/github/woctezuma/schulze-method/shield.svg
  [Python3 image]: https://pyup.io/repos/github/woctezuma/schulze-method/python-3-shield.svg

  [Codecov]: https://codecov.io/gh/woctezuma/schulze-method
  [Codecov image]: https://codecov.io/gh/woctezuma/schulze-method/branch/master/graph/badge.svg

A Python implementation of the [Schulze method](http://en.wikipedia.org/wiki/Schulze_method).

To rank candidates, call the `compute_ranks` method of the `schulze` module. This method has the following signature and Pydoc:

```python
def compute_ranks(candidate_names, weighted_ranks):
    """Returns the candidates ranked by the Schulze method.

    Parameter candidate_names is a sequence containing all the candidate names.

    Parameter weighted_ranks is a sequence of (ranks, weight) pairs.

    The first element, ranks, is a ranking of the candidates. It is an array of
    arrays so that we can express ties. For example, [[a, b], [c], [d, e]]
    represents a = b > c > d = e.

    The second element, weight, is typically the number of voters that chose
    this ranking.
    """
```

For example usage, refer to the `schulze_test` module. From the command line, you can run these tests like so:

```text
$ python -m unittest schulze_test
.....
----------------------------------------------------------------------
Ran 5 tests in 0.002s

OK
```

