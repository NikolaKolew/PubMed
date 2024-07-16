def save_to_csv(df, filename):
    df.to_csv(filename, encoding='utf-8', index=False)
