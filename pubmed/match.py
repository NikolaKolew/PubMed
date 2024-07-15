import pandas as pd


def check_matches(cleaned_data, profiles):

    cleaned_data['fullName'] = cleaned_data['firstName'].fillna('') + ' ' + cleaned_data['lastName'].fillna('')

    profiles['fullName'] = profiles['formattedName']

    profile_names_set = set(profiles['fullName'])

    def check_match(cleaned_name, profile_names):
        if pd.isna(cleaned_name):
            return False
        for profile_name in profile_names:
            if pd.notna(profile_name) and profile_name in cleaned_name:
                return True
        return False

    cleaned_data['match'] = cleaned_data['fullName'].apply(lambda cleaned_name: check_match(cleaned_name, profile_names_set))

    return cleaned_data

