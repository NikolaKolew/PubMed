import pandas as pd


def extract_author_info(articles):
    """
    Extracts author information from articles.

    Parameters:
    - articles (dict): A dictionary containing articles' data.

    Returns:
    - list: A list of dictionaries, each containing author information.
    """
    author_list = []

    articles_result = articles.get('PubmedArticleSet', {}).get('PubmedArticle', [])
    for article in articles_result:
        article_data = article.get('MedlineCitation', {})
        article_authors = article_data.get('Article', {}).get('AuthorList', {}).get('Author', [])

        if isinstance(article_authors, dict):  # If there's only one author
            article_authors = [article_authors]

        for author in article_authors:
            first_name = author.get('ForeName', 'Unknown')
            last_name = author.get('LastName', 'Unknown')

            # Handle multiple affiliations
            affiliation_info = author.get('AffiliationInfo', [])
            if isinstance(affiliation_info, list):
                affiliations = []
                for affiliation in affiliation_info:
                    affiliation_text = affiliation.get('Affiliation', 'Unknown')
                    affiliations.append(affiliation_text)
                affiliation = ", ".join(affiliations)
            else:
                affiliation = affiliation_info.get('Affiliation', 'Unknown') if affiliation_info else 'Unknown'

            author_list.append({
                'firstName': first_name,
                'lastName': last_name,
                'affiliation': affiliation
            })

    return author_list


def clean_transform_data(author_info):
    df = pd.DataFrame(author_info)
    # Remove duplicates
    df = df.drop_duplicates()
    # Handle missing values (e.g., fill with 'Unknown')
    df = df.fillna('Unknown')

    return df
