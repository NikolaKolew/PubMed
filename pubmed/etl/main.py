from pubmed.etl.extract_from_pubmed_api import fetch_pubmed_articles
from pubmed.etl.transform import extract_author_info
from pubmed.etl.transform import clean_transform_data
from pubmed.etl.load import save_to_csv
from pubmed.match import check_matches
import pandas as pd


def main():
    # Extract
    articles = fetch_pubmed_articles("Ulcerative Colitis")

    # Transform
    author_info = extract_author_info(articles)
    cleaned_data = clean_transform_data(author_info)
    # print(cleaned_data.head(40))

    save_to_csv(cleaned_data, '../result/pub_med.csv')

    profiles = pd.read_csv('../data_match/cleaned_person_profiles.csv', encoding='utf-8')

    matched_data = check_matches(cleaned_data, profiles)

    save_to_csv(matched_data, '../result/matched_author_info.csv')


if __name__ == "__main__":
    main()
