import requests
import xmltodict


def fetch_pubmed_articles(query, retmax=100):
    """
    Parameters:
    - query (str): The search term to use in PubMed.
    - retmax (int): The maximum number of articles to retrieve.
    Returns:
    - dict: A dictionary containing the articles' data.
    """
    base_url = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/"
    search_url = f"{base_url}esearch.fcgi"

    search_params = {
        "db": "pubmed",
        "term": query,
        "retmax": retmax,
        "retmode": "json"
    }

    search_response = requests.get(search_url, params=search_params)
    search_response.raise_for_status()
    article_ids = search_response.json()['esearchresult']['idlist']

    if not article_ids:
        return {"result": {"uids": []}}

    ids_str = ",".join(article_ids)
    fetch_url = f"{base_url}efetch.fcgi"

    fetch_params = {
        "db": "pubmed",
        "id": ids_str,
        "retmode": "xml",
        "rettype": "abstract"
    }

    fetch_response = requests.get(fetch_url, params=fetch_params)
    fetch_response.raise_for_status()
    articles_xml = fetch_response.content
    articles_dict = xmltodict.parse(articles_xml)

    return articles_dict