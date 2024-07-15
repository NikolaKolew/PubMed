import pandas as pd

result = pd.read_csv('./result/matched_author_info.csv', encoding='utf-8')

filtered_result = result[result['match'] == False]


# print(result.head(50))

df = result.head(50)

tsv_file_path = './result/match_result.tsv'
df.to_csv(tsv_file_path, sep='\t', index=False)

df2 = pd.read_csv(tsv_file_path, sep='\t')

sample_data = df2[['firstName', 'lastName', 'match']].to_markdown(index=False)
print(sample_data)
