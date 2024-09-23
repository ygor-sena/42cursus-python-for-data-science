import pandas as pd


def load(path: str) -> pd.DataFrame:
    """Loads a CSV file into a pandas DataFrame.

    This function reads a CSV file from the specified file path and returns
    the data as a pandas DataFrame. It also prints the dimensions of the
    loaded dataset.

    Args:
        file_path (str): The path to the CSV file to be loaded.

    Returns:
        pd.DataFrame: The loaded data as a pandas DataFrame.
    """
    data = pd.read_csv(path)
    print(f"Loading dataset of dimensions ({data.shape[0]}, {data.shape[1]})")
    return data
