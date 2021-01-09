
# pygouv

`pygouv` is a __non official__ Python API wrapper for [data.gouv.fr](https://www.data.gouv.fr/fr/), the French Official Open Data Portal.

## Installation

You can install `pygouv` with:

`pip install pygouv`

## Usage

```python

import pygouv as gv

```

### gv.home( ) and gv.home_compact()

Displays the datasets that are currently exhibited within the home page of the data.gouv.fr portal.

`gv.home()` returns all the columns that are provided by the data.gouv API and can be overwhelming. In this context, there is the `gv.home_compact()` that as its name implies much more compact and contains only the most important columns: `id, title, last_update`

### gv.site_metrics( )

Provides global metrics related to the data.gouv.fr portal:

### gv.search( ) and gv.search_compact()

Searches for specific data sets through the data.gouv API according to the pattern provided into the `query` parameter. It takes three arguments `query`, `page` and `page_size`:

```python
gv.search(query='cafés à paris',
          page = 0, # look at page 0 (the default)
          page_size = 20) # pull 20 results
```

`gv.search()` returns all the columns provided by the API. `gv.search_compact()` returns only three columns: `id, description, last_update`

## gv.explain( )

Provides in **French** a detailed description of a data set. It takes one mandatory argument which is the `dataset_id` that you can get from output of the `search()` function.

```python
print(gv.explain('5f9b902d3784843c84d5f959'))
```

    **Ce jeu de données recense les déclarations de terrasse éphémère.**

    La Ville de Paris a pris la décision d'autoriser l'extension gratuite des terrasses pour les cafés, bars et restaurants.

    Habituellement soumises à une autorisation, les extensions provisoires sont exceptionnellement enregistrées à titre gratuit, et sont valables jusqu'en juin 2021.

    La déclaration est effectuée via un téléservice sur Paris.fr. Chaque commerçant doit signer et afficher une charte d'engagement.

    [Plus d'informations: sur Paris.fr](https://www.paris.fr/pages/reouverture-des-bars-et-restaurants-agrandir-ou-creer-sa-terrasse-7847)

    Description des données :

    · \- Reference Déclaration (Numéro de la déclaration)

    · \- Nom Commerce

    · \- Adresse Commerce et coordonnées géographiques (X ; Y)

### gv.resources( ) and gv.resources_compact():

`gv.resources()` lists all the available resources within a specific data set. `gv.resources_compact()` is its equivalent except that it returns only two columns: `format, url` 

```python
gv.resources('5f9b902d3784843c84d5f959')
```

### suggest_territory( )

Returns suggested territory pages according to the query provided by the user:

```python
gv.suggest_territory(query = 'paris', result_size=10)

```

## Code of Conduct

Please note that the `pygouv` project is released with a [Contributor Code of Conduct](https://contributor-covenant.org/version/2/0/CODE_OF_CONDUCT.html). By contributing to this project, you agree to abide by its terms.
