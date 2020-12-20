# pygouv

`pygouv` is a Python API wrapper for [data.gouv.fr](https://www.data.gouv.fr/fr/), the French Official Open Data Portal.

## Installation

```python
pip install pygouv
```

## Usage

```python
from pygouv import *
```

### home()

Displays the datasets that are currently exhibited within the home page of the data.gouv.fr portal:

```python
home()
```

### site_metrics()

Provides global metrics related to the data.gouv.fr portal

```python
site_metrics()
```

### search()

---

Searches for specific data sets through the data.gouv API according to the pattern provided into the `query` parameter:

```python
search(query = 'paris', page=0, page_size=20)
```

### explain()

---

Provides in **French** a detailed description of a data set:

```python
# mind that we're using the print function so that we get a well formatted text
print(explain(dataset_id = '5f2bc22ff6bf657d74f48375'))

```

### resources()

---

`resources()` lists all the resources available within a specific data set:

```python
resources(dataset_id = '5f2bc22ff6bf657d74f48375')
```

### suggest_territory()

Returns suggested territory pages according to the query provided by the user:

```python

suggest_territory(query = 'paris', result_size=10):

```

## Developing `pygouv`

To install `pygouv` along with the tools that you need to develop and run tests, run the following in your virtualenv:

```bash
$ pip install -e .[dev]
```

## Code of Conduct

Please note that the `pygouv` project is released with a [Contributor Code of Conduct](https://contributor-covenant.org/version/2/0/CODE_OF_CONDUCT.html). By contributing to this project, you agree to abide by its terms.
