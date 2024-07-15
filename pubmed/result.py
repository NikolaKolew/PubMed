import pandas as pd

result = pd.read_csv('./result/matched_author_info.csv', encoding='utf-8')

filtered_result = result[result['match'] == False]

# Print the first 50 rows of the filtered DataFrame
print(filtered_result.head())