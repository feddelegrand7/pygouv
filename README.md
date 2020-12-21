
# pygouv

`pygouv` is a __non official__ Python API wrapper for [data.gouv.fr](https://www.data.gouv.fr/fr/), the French Official Open Data Portal.

## Installation

You can install `pygouv` with: 

`pip install pygouv`

## Usage


```python
from pygouv import * 
```

### home( )

Displays the datasets that are currently exhibited within the home page of the data.gouv.fr portal:


```python
home()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>acronym</th>
      <th>archived</th>
      <th>badges</th>
      <th>created_at</th>
      <th>deleted</th>
      <th>description</th>
      <th>frequency</th>
      <th>frequency_date</th>
      <th>id</th>
      <th>last_modified</th>
      <th>...</th>
      <th>spatial.granularity</th>
      <th>spatial.zones</th>
      <th>spatial</th>
      <th>extras.recommendations</th>
      <th>extras.recommendations:sources</th>
      <th>extras.apigouvfr:apis</th>
      <th>extras.datafairDatasetId</th>
      <th>extras.datafairOrigin</th>
      <th>temporal_coverage.end</th>
      <th>temporal_coverage.start</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>SI-DEP</td>
      <td>None</td>
      <td>[]</td>
      <td>2020-10-21T09:20:09.639000</td>
      <td>None</td>
      <td>**Point d'attention : les difficultés de remon...</td>
      <td>daily</td>
      <td>2020-10-22T09:19:41</td>
      <td>5f8fe1290de5138270132602</td>
      <td>2020-12-20T19:27:08.779000</td>
      <td>...</td>
      <td>fr:iris</td>
      <td>[country:fr]</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>1</th>
      <td>SI-DEP</td>
      <td>None</td>
      <td>[]</td>
      <td>2020-09-29T15:32:39.020000</td>
      <td>None</td>
      <td>**Point d'attention: Les difficultés de remont...</td>
      <td>daily</td>
      <td>2020-10-15T14:19:14</td>
      <td>5f733777722fc12a413290eb</td>
      <td>2020-12-20T19:27:11.047000</td>
      <td>...</td>
      <td>fr:epci</td>
      <td>[country:fr]</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>2</th>
      <td>None</td>
      <td>None</td>
      <td>[]</td>
      <td>2020-06-17T11:16:00.320000</td>
      <td>None</td>
      <td>### Présentation des indicateurs de suivi\n\nL...</td>
      <td>daily</td>
      <td>2020-10-29T15:46:30</td>
      <td>5ee9df5003284f565d561278</td>
      <td>2020-12-20T16:24:05.918000</td>
      <td>...</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>[{'id': '5eaaf07f5abc47e306c5c258', 'score': 1...</td>
      <td>[matomo]</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>3</th>
      <td>None</td>
      <td>None</td>
      <td>[{'kind': 'covid-19'}]</td>
      <td>2020-03-27T15:40:10.048000</td>
      <td>None</td>
      <td>**Point d'information :** Un établissement hos...</td>
      <td>daily</td>
      <td>2020-03-28T15:39:51</td>
      <td>5e7e104ace2080d9162b61d8</td>
      <td>2020-12-20T19:06:25.164000</td>
      <td>...</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>[{'id': '5e74ecf52eb7514f2d3b8845', 'score': 4...</td>
      <td>[matomo]</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>4</th>
      <td>None</td>
      <td>None</td>
      <td>[]</td>
      <td>2020-06-11T16:00:55.511000</td>
      <td>None</td>
      <td>Le diagnostic de performance énergétique (DPE)...</td>
      <td>unknown</td>
      <td>None</td>
      <td>5ee2391763c79811ddfbc86a</td>
      <td>2020-10-28T09:53:44.306000</td>
      <td>...</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>[{'logo': '/images/api-logo/ademe.png', 'openn...</td>
      <td>dpe-france</td>
      <td>https://koumoul.com/s/data-fair</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>5</th>
      <td>None</td>
      <td>None</td>
      <td>[{'kind': 'covid-19'}]</td>
      <td>2020-04-20T17:20:30.636000</td>
      <td>None</td>
      <td>### Le fonds de solidarité \n\nDans le context...</td>
      <td>daily</td>
      <td>2020-04-21T17:49:37</td>
      <td>5e9dbdbe71589194c8f7b42f</td>
      <td>2020-12-07T17:59:34.038000</td>
      <td>...</td>
      <td>fr:departement</td>
      <td>[country:fr]</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>2020-12-31</td>
      <td>2020-03-01</td>
    </tr>
    <tr>
      <th>6</th>
      <td>SI-DEP</td>
      <td>None</td>
      <td>[]</td>
      <td>2020-05-29T16:10:35.407000</td>
      <td>None</td>
      <td>**Point d'attention : Les difficultés de remon...</td>
      <td>daily</td>
      <td>2020-10-22T09:53:26</td>
      <td>5ed117db6c161bd5baf070be</td>
      <td>2020-12-20T19:20:29.771000</td>
      <td>...</td>
      <td>other</td>
      <td>[country:fr]</td>
      <td>NaN</td>
      <td>[{'id': '5e7de8cf4663c08d4f74ba01', 'score': 8...</td>
      <td>[matomo]</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>7</th>
      <td>None</td>
      <td>None</td>
      <td>[]</td>
      <td>2020-09-28T16:44:09.669000</td>
      <td>None</td>
      <td>Version : AGRIBALYSE® v3.0.1\n\nAGRIBALYSE® es...</td>
      <td>unknown</td>
      <td>None</td>
      <td>5f71f6b9f23df7fcd508af57</td>
      <td>2020-11-24T17:19:10.789000</td>
      <td>...</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>[{'logo': '/images/api-logo/ademe.png', 'openn...</td>
      <td>agribalyse-synthese</td>
      <td>https://koumoul.com/s/data-fair</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>8</th>
      <td>None</td>
      <td>None</td>
      <td>[]</td>
      <td>2020-09-22T14:23:13.380000</td>
      <td>None</td>
      <td>**Point d'attention : Depuis le 17/10/2020, le...</td>
      <td>daily</td>
      <td>2020-09-23T14:20:21</td>
      <td>5f69ecb155c43420918410b8</td>
      <td>2020-12-21T00:30:59.566000</td>
      <td>...</td>
      <td>fr:departement</td>
      <td>[country:fr]</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
  </tbody>
</table>
<p>9 rows × 46 columns</p>
</div>



`home()` provides a `pandas` dataFrame with the following columns : 


```python
for col in home().columns:
    print(col)
```

    acronym
    archived
    badges
    created_at
    deleted
    description
    frequency
    frequency_date
    id
    last_modified
    last_update
    license
    owner
    page
    private
    resources
    slug
    tags
    temporal_coverage
    title
    uri
    metrics.discussions
    metrics.followers
    metrics.issues
    metrics.reuses
    metrics.views
    organization.acronym
    organization.class
    organization.id
    organization.logo
    organization.logo_thumbnail
    organization.name
    organization.page
    organization.slug
    organization.uri
    spatial.geom
    spatial.granularity
    spatial.zones
    spatial
    extras.recommendations
    extras.recommendations:sources
    extras.apigouvfr:apis
    extras.datafairDatasetId
    extras.datafairOrigin
    temporal_coverage.end
    temporal_coverage.start
    

### site_metrics( )

Provides global metrics related to the data.gouv.fr portal.


```python
site_metrics()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>datasets</th>
      <th>discussions</th>
      <th>followers</th>
      <th>max_dataset_followers</th>
      <th>max_dataset_reuses</th>
      <th>max_org_datasets</th>
      <th>max_org_followers</th>
      <th>max_org_reuses</th>
      <th>max_reuse_datasets</th>
      <th>max_reuse_followers</th>
      <th>organizations</th>
      <th>public-service</th>
      <th>resources</th>
      <th>reuses</th>
      <th>users</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>36046</td>
      <td>7628</td>
      <td>24129</td>
      <td>130</td>
      <td>133</td>
      <td>1017</td>
      <td>572</td>
      <td>114</td>
      <td>74</td>
      <td>324</td>
      <td>2659</td>
      <td>0</td>
      <td>195826</td>
      <td>2453</td>
      <td>65663</td>
    </tr>
  </tbody>
</table>
</div>



### search( )

Searches for specific data sets through the data.gouv API according to the pattern provided into the `query` parameter. It takes three arguments `query`, `page` and `page_size`:





```python
srch = search(query='cafés à paris', 
       page = 0, # look at page 0 (the default)
       page_size = 20) # pull 20 results

srch
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>acronym</th>
      <th>archived</th>
      <th>badges</th>
      <th>created_at</th>
      <th>deleted</th>
      <th>description</th>
      <th>frequency</th>
      <th>frequency_date</th>
      <th>id</th>
      <th>last_modified</th>
      <th>...</th>
      <th>organization.logo_thumbnail</th>
      <th>organization.name</th>
      <th>organization.page</th>
      <th>organization.slug</th>
      <th>organization.uri</th>
      <th>extras.datagouv_ckan_id</th>
      <th>extras.datagouv_ckan_last_sync</th>
      <th>spatial.geom</th>
      <th>spatial.granularity</th>
      <th>spatial.zones</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>None</td>
      <td>None</td>
      <td>[]</td>
      <td>2020-10-30T05:01:49.236000</td>
      <td>None</td>
      <td>**Ce jeu de données recense les déclarations d...</td>
      <td>unknown</td>
      <td>None</td>
      <td>5f9b902d3784843c84d5f959</td>
      <td>2020-10-29T18:36:54</td>
      <td>...</td>
      <td>https://static.data.gouv.fr/avatars/b2/0e83ec3...</td>
      <td>Mairie de Paris</td>
      <td>https://www.data.gouv.fr/fr/organizations/mair...</td>
      <td>mairie-de-paris</td>
      <td>https://www.data.gouv.fr/api/1/organizations/m...</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>1</th>
      <td>None</td>
      <td>None</td>
      <td>[]</td>
      <td>2014-04-23T10:10:02.419000</td>
      <td>None</td>
      <td>La liste des cafés à un euro de Paris.\n\nCe j...</td>
      <td>unknown</td>
      <td>None</td>
      <td>536998e0a3a729239d2050a4</td>
      <td>2016-03-16T08:35:42.023000</td>
      <td>...</td>
      <td>https://static.data.gouv.fr/avatars/b2/0e83ec3...</td>
      <td>Mairie de Paris</td>
      <td>https://www.data.gouv.fr/fr/organizations/mair...</td>
      <td>mairie-de-paris</td>
      <td>https://www.data.gouv.fr/api/1/organizations/m...</td>
      <td>29853df3-3493-43d9-82a3-4b6b49c44977</td>
      <td>2014-09-16T09:31:21.096000</td>
      <td>NaN</td>
      <td>other</td>
      <td>[]</td>
    </tr>
  </tbody>
</table>
<p>2 rows × 49 columns</p>
</div>



The `search()` function provides a `pandas` dataFrame with the following columns: 


```python
for col in srch.columns:
    print(col)
```

    acronym
    archived
    badges
    created_at
    deleted
    description
    frequency
    frequency_date
    id
    last_modified
    last_update
    license
    owner
    page
    private
    resources
    slug
    spatial
    tags
    temporal_coverage
    title
    uri
    extras.harvest:domain
    extras.harvest:last_update
    extras.harvest:remote_id
    extras.harvest:source_id
    extras.ods:geo
    extras.ods:has_records
    extras.ods:url
    extras.remote_url
    metrics.discussions
    metrics.followers
    metrics.issues
    metrics.reuses
    metrics.views
    organization.acronym
    organization.class
    organization.id
    organization.logo
    organization.logo_thumbnail
    organization.name
    organization.page
    organization.slug
    organization.uri
    extras.datagouv_ckan_id
    extras.datagouv_ckan_last_sync
    spatial.geom
    spatial.granularity
    spatial.zones
    

## explain( )

Provides in **French** a detailed description of a data set. It takes one mandatory argument which is the `dataset_id` that you can get from output of the `search()` function:


```python
srch[['id', 'title']]
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>id</th>
      <th>title</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>5f9b902d3784843c84d5f959</td>
      <td>Terrasses éphémères</td>
    </tr>
    <tr>
      <th>1</th>
      <td>536998e0a3a729239d2050a4</td>
      <td>Liste des cafés à un euro</td>
    </tr>
  </tbody>
</table>
</div>



We can grab an id and put it inside the `explain()` function:

In order to get a well formated text, we need to use the `print()` function: 


```python
print(explain('5f9b902d3784843c84d5f959'))
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
    

### resources( ) 

`resources()` lists all the available resources within a specific data set:


```python
res = resources('5f9b902d3784843c84d5f959')
res
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>checksum</th>
      <th>created_at</th>
      <th>description</th>
      <th>filesize</th>
      <th>filetype</th>
      <th>format</th>
      <th>id</th>
      <th>last_modified</th>
      <th>latest</th>
      <th>mime</th>
      <th>...</th>
      <th>url</th>
      <th>extras.check:available</th>
      <th>extras.check:count-availability</th>
      <th>extras.check:date</th>
      <th>extras.check:headers:charset</th>
      <th>extras.check:headers:content-disposition</th>
      <th>extras.check:headers:content-type</th>
      <th>extras.check:status</th>
      <th>extras.check:url</th>
      <th>extras.ods:type</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>None</td>
      <td>2020-10-30T05:01:49.244000</td>
      <td>- *Référence déclaration*: reference_declarati...</td>
      <td>None</td>
      <td>remote</td>
      <td>csv</td>
      <td>59952231-e65f-4e52-b99a-f18ab317d4cc</td>
      <td>2020-10-29T18:36:54</td>
      <td>https://www.data.gouv.fr/fr/datasets/r/5995223...</td>
      <td>text/csv</td>
      <td>...</td>
      <td>https://opendata.paris.fr/explore/dataset/terr...</td>
      <td>True</td>
      <td>27</td>
      <td>2020-12-16T10:06:11.943000</td>
      <td>utf-8</td>
      <td>attachment; filename="terrasses-ephemeres.csv"</td>
      <td>application/csv</td>
      <td>200</td>
      <td>https://opendata.paris.fr/explore/dataset/terr...</td>
      <td>api</td>
    </tr>
    <tr>
      <th>1</th>
      <td>None</td>
      <td>2020-10-30T05:01:49.244000</td>
      <td>- *Référence déclaration*: reference_declarati...</td>
      <td>None</td>
      <td>remote</td>
      <td>json</td>
      <td>f094f3da-9b57-4fc3-ac1c-3538ace77d44</td>
      <td>2020-10-29T18:36:54</td>
      <td>https://www.data.gouv.fr/fr/datasets/r/f094f3d...</td>
      <td>application/json</td>
      <td>...</td>
      <td>https://opendata.paris.fr/explore/dataset/terr...</td>
      <td>True</td>
      <td>27</td>
      <td>2020-12-16T10:06:11.963000</td>
      <td>utf-8</td>
      <td>attachment; filename="terrasses-ephemeres.json"</td>
      <td>application/json</td>
      <td>200</td>
      <td>https://opendata.paris.fr/explore/dataset/terr...</td>
      <td>api</td>
    </tr>
  </tbody>
</table>
<p>2 rows × 25 columns</p>
</div>



`resources()` outputs a `pandas` dataFrame with the following columns : 


```python
for col in res.columns:
    print(col)
```

    checksum
    created_at
    description
    filesize
    filetype
    format
    id
    last_modified
    latest
    mime
    preview_url
    published
    schema
    title
    type
    url
    extras.check:available
    extras.check:count-availability
    extras.check:date
    extras.check:headers:charset
    extras.check:headers:content-disposition
    extras.check:headers:content-type
    extras.check:status
    extras.check:url
    extras.ods:type
    

We can grab the URL, the format and the description of the resources: 


```python
res[['description', 'format', 'url']]
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>description</th>
      <th>format</th>
      <th>url</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>- *Référence déclaration*: reference_declarati...</td>
      <td>csv</td>
      <td>https://opendata.paris.fr/explore/dataset/terr...</td>
    </tr>
    <tr>
      <th>1</th>
      <td>- *Référence déclaration*: reference_declarati...</td>
      <td>json</td>
      <td>https://opendata.paris.fr/explore/dataset/terr...</td>
    </tr>
  </tbody>
</table>
</div>



Now we can just extract with `pandas` the required resource. In this example, we've chosen to work with a __csv__ file: 


```python
df = pd.read_csv(res['url'][0], sep=";")
```


```python
df
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>reference_declaration</th>
      <th>nom_commerce</th>
      <th>adresse_commerce</th>
      <th>coord_x</th>
      <th>coord_y</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>169</td>
      <td>Cafe au pere tranquille</td>
      <td>16 rue Pierre Lescot, 75001 PARIS</td>
      <td>652202.4778</td>
      <td>6.862661e+06</td>
    </tr>
    <tr>
      <th>1</th>
      <td>278</td>
      <td>Cafe le marignan</td>
      <td>18 rue de Marignan, 75008 PARIS</td>
      <td>649134.9044</td>
      <td>6.863454e+06</td>
    </tr>
    <tr>
      <th>2</th>
      <td>916</td>
      <td>CAFE PETITE</td>
      <td>52 rue René Boulanger, 75010 PARIS</td>
      <td>653031.4339</td>
      <td>6.863377e+06</td>
    </tr>
    <tr>
      <th>3</th>
      <td>177</td>
      <td>Chez Julien</td>
      <td>1 rue du Pont Louis-Philippe, 75004 PARIS</td>
      <td>652687.2630</td>
      <td>6.861829e+06</td>
    </tr>
    <tr>
      <th>4</th>
      <td>669</td>
      <td>Demain c'est loin</td>
      <td>9 rue Julien Lacroix, 75020 PARIS</td>
      <td>654960.0896</td>
      <td>6.863351e+06</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>9576</th>
      <td>22470</td>
      <td>Le 7 EME B’ART</td>
      <td>19 rue de Choiseul, 75002 PARIS</td>
      <td>651285.2949</td>
      <td>6.863569e+06</td>
    </tr>
    <tr>
      <th>9577</th>
      <td>22501</td>
      <td>BIBIMBAP</td>
      <td>32 Boulevard de l'Hôpital</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>9578</th>
      <td>22507</td>
      <td>Holiday Inn Paris Elysees</td>
      <td>24 rue de Miromesnil</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>9579</th>
      <td>22532</td>
      <td>Le mandarin de rambuteau</td>
      <td>11 rue Rambuteau, 75004 PARIS</td>
      <td>652741.2095</td>
      <td>6.862449e+06</td>
    </tr>
    <tr>
      <th>9580</th>
      <td>22522</td>
      <td>Secret de Paris</td>
      <td>61 rue de Clichy</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
  </tbody>
</table>
<p>9581 rows × 5 columns</p>
</div>



### suggest_territory( )

Returns suggested territory pages according to the query provided by the user:



```python
terr = suggest_territory(query = 'paris', result_size=10)
terr
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>id</th>
      <th>image_url</th>
      <th>page</th>
      <th>parent</th>
      <th>title</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>fr:commune:75056@1943-01-01</td>
      <td></td>
      <td>https://www.data.gouv.fr/fr/territories/commun...</td>
      <td>Paris</td>
      <td>Paris</td>
    </tr>
    <tr>
      <th>1</th>
      <td>fr:commune:75115@1943-01-01</td>
      <td></td>
      <td>https://www.data.gouv.fr/fr/territories/commun...</td>
      <td>Paris</td>
      <td>Paris 15e Arrondissement</td>
    </tr>
    <tr>
      <th>2</th>
      <td>fr:commune:75120@1943-01-01</td>
      <td></td>
      <td>https://www.data.gouv.fr/fr/territories/commun...</td>
      <td>Paris</td>
      <td>Paris 20e Arrondissement</td>
    </tr>
    <tr>
      <th>3</th>
      <td>fr:commune:75118@1943-01-01</td>
      <td></td>
      <td>https://www.data.gouv.fr/fr/territories/commun...</td>
      <td>Paris</td>
      <td>Paris 18e Arrondissement</td>
    </tr>
    <tr>
      <th>4</th>
      <td>fr:commune:75119@1943-01-01</td>
      <td></td>
      <td>https://www.data.gouv.fr/fr/territories/commun...</td>
      <td>Paris</td>
      <td>Paris 19e Arrondissement</td>
    </tr>
    <tr>
      <th>5</th>
      <td>fr:commune:75113@1943-01-01</td>
      <td></td>
      <td>https://www.data.gouv.fr/fr/territories/commun...</td>
      <td>Paris</td>
      <td>Paris 13e Arrondissement</td>
    </tr>
    <tr>
      <th>6</th>
      <td>fr:commune:75117@1943-01-01</td>
      <td></td>
      <td>https://www.data.gouv.fr/fr/territories/commun...</td>
      <td>Paris</td>
      <td>Paris 17e Arrondissement</td>
    </tr>
    <tr>
      <th>7</th>
      <td>fr:commune:75116@1943-01-01</td>
      <td></td>
      <td>https://www.data.gouv.fr/fr/territories/commun...</td>
      <td>Paris</td>
      <td>Paris 16e Arrondissement</td>
    </tr>
    <tr>
      <th>8</th>
      <td>fr:commune:75111@1943-01-01</td>
      <td></td>
      <td>https://www.data.gouv.fr/fr/territories/commun...</td>
      <td>Paris</td>
      <td>Paris 11e Arrondissement</td>
    </tr>
    <tr>
      <th>9</th>
      <td>fr:commune:75112@1943-01-01</td>
      <td></td>
      <td>https://www.data.gouv.fr/fr/territories/commun...</td>
      <td>Paris</td>
      <td>Paris 12e Arrondissement</td>
    </tr>
  </tbody>
</table>
</div>



`suggest_territory()` returns a `pandas` dataFrame with the following columns: 


```python
for col in terr.columns:
    print(col)
```

    id
    image_url
    page
    parent
    title
    

## Code of Conduct

Please note that the `pygouv` project is released with a [Contributor Code of Conduct](https://contributor-covenant.org/version/2/0/CODE_OF_CONDUCT.html). By contributing to this project, you agree to abide by its terms.
