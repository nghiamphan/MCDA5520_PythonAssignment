import pandas as pd


def count_vowels(s: str) -> int:
    """
    Return the number of vowels in a string.
    """
    if not isinstance(s, str):
        s = str(s)

    vowels = ["a", "e", "i", "o", "u"]
    count = 0
    for c in s:
        if c in vowels:
            count += 1
    return count


def count_vowels_in_column(file_name: str, column_name: str) -> pd.DataFrame:
    """
    Arguments
    file_name: str
        file name of the csv file to be read
    column_name: str
        column from which to count the number of vowels

    Returns
    -------
    df: pd.DataFrame
        returned dataframe will contain column "vowels" which is the number of vowels
    """
    df = pd.read_csv(file_name)
    df["vowels"] = df[column_name].apply(lambda x: count_vowels(x))
    return df


def test():
    df = count_vowels_in_column("titles.csv", "title")
    print(df)


if __name__ == "__main__":
    test()
