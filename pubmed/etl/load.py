def save_to_csv(df, filename):
    """
    Saves the DataFrame to a CSV file.

    Parameters:
    - df (DataFrame): The DataFrame to save.
    - filename (str): The name of the file to save the data to.
    """
    df.to_csv(filename, encoding='utf-8', index=False)
