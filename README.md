# pygouv

`pygouv` is a Python API wrapper for [data.gouv.fr](https://www.data.gouv.fr/fr/), the French Official Open Data Portal.

## Installation

```python
pip install pygouv
```

## Usage

```python
import pygouv as gv

```

### `gv.gouv_home()`

Displays the most important information about the datasets that are currently displayed within the home page of the data.gouv.fr portal.

```python
gv.gouv_home()
```

### `gv.gouv_search()`

Searches for specific data sets through the data.gouv API according to the pattern provided into the query argument.

```python
gv.gouv_search(query = 'paris', n_pages=20)
```

### `gv.gouv_explain()`

Provides in French a detailed description of a data set.

```python
# mind that we're using the pring function so that we get a well formatted text
print(gv.gouv_explain(dataset_id = '5f2bc22ff6bf657d74f48375'))

```

### `gv.gouv_resources()`

The data.gouv API provides access to several data sets in which one can find several individual data frames to exploit. The BARIS_resources lists all the data frames available within a specific data set along with the main information concerning the data frames.

```python
gv.gouv_resources(dataset_id = '5f2bc22ff6bf657d74f48375')
```

## Developing `pygouv`

To install `pygouv` along with the tools that you need to develop and run tests, run the following in your virtualenv:

```bash
$ pip install -e .[dev]
```

## Code of Conduct

Please note that the pygouv project is released with a [Contributor Code of Conduct](https://contributor-covenant.org/version/2/0/CODE_OF_CONDUCT.html). By contributing to this project, you agree to abide by its terms.
