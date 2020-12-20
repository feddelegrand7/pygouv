import requests
import pandas as pd
import unicodedata
from urllib.parse import quote


def home():
    """Displays the most important information about the datasets 
    that are currently exhibited at the home page of 
    the data.gouv portal.

    Returns:
        DataFrame
    """

    try:
        request = requests.get(
            "https://www.data.gouv.fr/api/1/site/home/datasets/")

        data = request.json()
        data = pd.json_normalize(data)
        data_final = data[['id',
                           'title',
                           'frequency',
                           'created_at',
                           'last_modified',
                           'last_update',
                           'archived',
                           'deleted',
                           'page', ]]
        return data_final

    except requests.exceptions.HTTPError as errh:
        print("Http Error: ", errh)

    except requests.exceptions.ConnectionError as errc:
        print("Error Connecting: ", errc)

    except requests.exceptions.Timeout as errt:
        print("Timeout Error: ", errt)

    except requests.exceptions.RequestException as err:
        print("Undefined Error: ", err)


def search(query, n_pages=20):
    """ Searches for a specific data sets through the data.gouv API.

    Args:
        query (str): a character string defining the research.
        n_pages (int, optional): the desired number of results, default to 20.

    Returns:
        DataFrame
    """

    # removing French accents (é, ç, è ...)
    def remove_accents(input_str):
        nfkd_form = unicodedata.normalize('NFKD', input_str)
        return u"".join([c for c in nfkd_form if not unicodedata.combining(c)])

    base_url = "https://www.data.gouv.fr/api/1/datasets/?q="

    complement = "&page=0&page_size="

    search = remove_accents(query)

    # parsing the URL (replacing space with %20)
    search = quote(search)

    final_url = base_url + search + complement + str(n_pages)

    try:
        request = requests.get(final_url)

        data = request.json()

        # get the data key from the json response
        data = data['data']

        # transform raw json into a data frame
        data = pd.json_normalize(data)

        # selecting only the relevant column from the data

        data_final = data[['id',
                           'title',
                           'frequency',
                           'created_at',
                           'last_modified',
                           'last_update',
                           'archived',
                           'deleted',
                           'page', ]]

        return data_final

    except requests.exceptions.HTTPError as errh:
        print("Http Error: ", errh)

    except requests.exceptions.ConnectionError as errc:
        print("Error Connecting: ", errc)

    except requests.exceptions.Timeout as errt:
        print("Timeout Error: ", errt)

    except requests.exceptions.RequestException as err:
        print("Undefined Error: ", err)


def explain(dataset_id):
    """A description in French of the data set.

    Args:
        dataset_id (str): the unique id number of the data set

    Returns:
        str

    """

    basic_url = "https://www.data.gouv.fr/api/1/datasets/"

    final_url = basic_url + dataset_id + "/"

    try:
        request = requests.get(final_url)

        data = request.json()

        return(data['description'])

    except requests.exceptions.HTTPError as errh:
        print("Http Error: ", errh)

    except requests.exceptions.ConnectionError as errc:
        print("Error Connecting: ", errc)

    except requests.exceptions.Timeout as errt:
        print("Timeout Error: ", errt)

    except requests.exceptions.RequestException as err:
        print("Undefined Error: ", err)


def resources(dataset_id):
    """lists all the resources available within a specific data set

    Args:
        dataset_id (str): the unique id of the data set.


    Returns:
        DataFrame

    """

    basic_url = "https://www.data.gouv.fr/api/1/datasets/"

    final_url = basic_url + dataset_id + "/"

    try:
        request = requests.get(final_url)

        data = request.json()

        data = data['resources']

        data_final = pd.json_normalize(data)

        data_final = data_final[['id',
                                 'title',
                                 'format',
                                 'published',
                                 'url',
                                 'description']]
        return data_final

    except requests.exceptions.HTTPError as errh:
        print("Http Error: ", errh)

    except requests.exceptions.ConnectionError as errc:
        print("Error Connecting: ", errc)

    except requests.exceptions.Timeout as errt:
        print("Timeout Error: ", errt)

    except requests.exceptions.RequestException as err:
        print("Undefined Error: ", err)


def site_metrics():
    """List data.gouv.fr API metrics

    Returns:
        DataFrame

    """

    url = "https://www.data.gouv.fr/api/1/site/"

    try:
        request = requests.get(url)
        result = request.json()
        data = pd.json_normalize(result)
        return data
    except requests.exceptions.HTTPError as errh:
        print("Http Error: ", errh)

    except requests.exceptions.ConnectionError as errc:
        print("Error Connecting: ", errc)

    except requests.exceptions.Timeout as errt:
        print("Timeout Error: ", errt)

    except requests.exceptions.RequestException as err:
        print("Undefined Error: ", err)
