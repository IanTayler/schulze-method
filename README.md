# Schulze Method [![Build status][Build image]][Build] [![Updates][Dependency image]][PyUp] [![Python 3][Python3 image]][PyUp] [![Code coverage][Codecov image]][Codecov]

  [Build]: https://travis-ci.org/woctezuma/schulze-method
  [Build image]: https://travis-ci.org/woctezuma/schulze-method.svg?branch=travis

  [PyUp]: https://pyup.io/repos/github/woctezuma/schulze-method/
  [Dependency image]: https://pyup.io/repos/github/woctezuma/schulze-method/shield.svg
  [Python3 image]: https://pyup.io/repos/github/woctezuma/schulze-method/python-3-shield.svg

  [Codecov]: https://codecov.io/gh/woctezuma/schulze-method
  [Codecov image]: https://codecov.io/gh/woctezuma/schulze-method/branch/travis/graph/badge.svg

This repository provides a Python implementation of the [Schulze method](http://en.wikipedia.org/wiki/Schulze_method).

## Requirements

- Install the latest version of [Python 3.X](https://www.python.org/downloads/).

- Install the required packages:

```
pip install -r requirements.txt
```

## Usage

- To rank candidates, import and call the `compute_ranks()` function, with [given signature](schulze.py#L88).

```python
from schulze import compute_ranks

# Input parameters:
#
# candidate_names: a list which contains all the candidate names.
#
# weighted_ranking_orders: a list of pairs (ranking_order, weight), where:
# - ranking_order is a list of list, e.g. [[a, b], [c], [d, e]] represents a = b > c > d = e.
# - weight is a number, typically the number of voters who choose this ranking order.
#

schulze_ranking = compute_ranks(candidate_names, weighted_ranks)
```
This method has .

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
