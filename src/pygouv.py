import requests
import pandas as pd


def home():
    """Displays the data sets that are currently exhibited at the home page of
    the data.gouv portal.

    Returns:
        DataFrame
    """

    try:
        request = requests.get(
            "https://www.data.gouv.fr/api/1/site/home/datasets/")

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


def search(query, page=0, page_size=20):
    """ Searches for a specific data sets through the data.gouv API.

    Args:
        query (str): a character string defining the research.
        page (int, optional): the page to display. Defaults to 0
        page_size (int, optional): the desired number of results per page, default to 20.

    Returns:
        DataFrame
    """

    url = "https://www.data.gouv.fr/api/1/datasets/"

    parameters = {"q": query, "page": page, "page_size": page_size}

    try:
        request = requests.get(url, params=parameters)

        result = request.json()

        # get the data key from the json response
        data = result['data']

        # transform raw json into a data frame
        data_final = pd.json_normalize(data)

        if data_final.empty:
            print("No Data available for your query, O_o', try something else !")
        else:
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
        dataset_id (str): the unique id number of the data set.

    Returns:
        str

    """

    basic_url = "https://www.data.gouv.fr/api/1/datasets/"

    final_url = basic_url + dataset_id + "/"

    try:
        request = requests.get(final_url)

        result = request.json()

        return(result['description'])

    except KeyError:
        print("Can't explain something that unavailable sorry :/ ")

    except requests.exceptions.HTTPError as errh:
        print("Http Error: ", errh)

    except requests.exceptions.ConnectionError as errc:
        print("Error Connecting: ", errc)

    except requests.exceptions.Timeout as errt:
        print("Timeout Error: ", errt)

    except requests.exceptions.RequestException as err:
        print("Undefined Error: ", err)


def resources(dataset_id):
    """lists all the resources available within a specific data set.

    Args:
        dataset_id (str): the unique id of the data set.


    Returns:
        DataFrame

    """

    basic_url = "https://www.data.gouv.fr/api/1/datasets/"

    final_url = basic_url + dataset_id + "/"

    try:
        request = requests.get(final_url)

        result = request.json()

        data = result['resources']

        data_final = pd.json_normalize(data)

        return data_final

    except KeyError:
        print('No resources found for this data frame ID o_o')
    except requests.exceptions.HTTPError as errh:
        print("Http Error: ", errh)

    except requests.exceptions.ConnectionError as errc:
        print("Error Connecting: ", errc)

    except requests.exceptions.Timeout as errt:
        print("Timeout Error: ", errt)

    except requests.exceptions.RequestException as err:
        print("Undefined Error: ", err)


def site_metrics():
    """List data.gouv.fr API metrics.

    Returns:
        DataFrame

    """

    url = "https://www.data.gouv.fr/api/1/site/"

    try:
        request = requests.get(url)
        result = request.json()['metrics']
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


def suggest_territory(query, result_size=10):
    """Returns suggested territory pages according to the query provided
    by the user.

    Args:
        query (str): a character string defining the query.
        result_size (int, optional): the maximum result size. Defaults to 10.

    Returns:
        DataFrame


    """

    url = "https://www.data.gouv.fr/api/1/territory/suggest/"
    parameters = {"q": query, "size": result_size}

    try:
        request = requests.get(url, params=parameters)

        result = request.json()

        data = pd.json_normalize(result)

        if data.empty:
            print("No suggestions found for this territory ~.~")
        else:
            return data

    except requests.exceptions.HTTPError as errh:
        print("Http Error: ", errh)

    except requests.exceptions.ConnectionError as errc:
        print("Error Connecting: ", errc)

    except requests.exceptions.Timeout as errt:
        print("Timeout Error: ", errt)

    except requests.exceptions.RequestException as err:
        print("Undefined Error: ", err)

###### Compact parts ##################


def home_compact():
    """Displays the data sets that are currently exhibited at the home page of
    data.gouv.fr in a compact manner. Only the columns 'id', 'title' and 'last_update'
    are kept

    Returns:
        DataFrame
    """
    try:
        if home() is None:
            print("Oops something went wrong D:")
        else:
            return(home()[['id', 'title', 'last_update']])

    except requests.exceptions.HTTPError as errh:
            print("Http Error: ", errh)

    except requests.exceptions.ConnectionError as errc:
            print("Error Connecting: ", errc)

    except requests.exceptions.Timeout as errt:
            print("Timeout Error: ", errt)

    except requests.exceptions.RequestException as err:
            print("Undefined Error: ", err)




