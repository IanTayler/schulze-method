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

- To rank candidates, import and call the `compute_ranks()` function, with [given signature](schulze.py#L86).

```python
from schulze import compute_ranks

schulze_ranking = compute_ranks(candidate_names, weighted_ranking_orders)
```
