import json
import pandas as pd


def clean_profiles(json_file):

    with open(json_file, 'r', encoding='utf-8') as file:
        profiles = json.load(file)

    cleaned_profiles = []
    for profile in profiles:
        cleaned_profile = {
            'firstName': profile.get('firstName', 'Unknown'),
            'lastName': profile.get('lastName', 'Unknown'),
            'affiliation': profile.get('affiliation', 'Unknown'),
            'formattedName': profile.get('formattedName', 'Unknown'),
        }
        cleaned_profiles.append(cleaned_profile)

    return pd.DataFrame(cleaned_profiles)


def save_to_csv(df, filename):
    df_profiles = pd.DataFrame(df)
    df_profiles = df_profiles.drop_duplicates()

    df_profiles.replace('', 'Unknown', inplace=True)

    df_profiles = df_profiles[(df_profiles['firstName'] != 'Unknown') &
                              (df_profiles['lastName'] != 'Unknown') &
                              (df_profiles['affiliation'] != 'Unknown')&
                              (df_profiles['formattedName'] != 'Unknown')]
    df_profiles.to_csv(filename, index=False, encoding='utf-8')


def main():
    json_file = './data_match/person_profiles.json'
    cleaned_profiles_df = clean_profiles(json_file)
    save_to_csv(cleaned_profiles_df, './data_match/cleaned_person_profiles.csv')
    result = pd.read_csv('./data_match/cleaned_person_profiles.csv', encoding='utf-8')
    print(result.head(40))


if __name__ == "__main__":
    main()
