print(f"Invoking __init__.py for {__name__}")

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


def print_corr_matrix(
    df,
    min_threshold: float = -1,
    max_threshold: float = 1,
    precision: int = 2,
    method: str = "pearson",
    hide_blanks_ones: bool = False,
):
    """
    Prints the correlation matrix of a DataFrame within a specified correlation range.

    Args:
        df (DataFrame): The input DataFrame.
        min_threshold (float, optional): The minimum correlation threshold (inclusive). Default is -1.
        max_threshold (float, optional): The maximum correlation threshold (inclusive). Default is 1.
        precision (int, optional): The number of decimal places to display. Default is 2.
        method (str, optional): The correlation method to use. Default is 'pearson', other values are 'spearman' and 'kendall'.

    Returns:
        pd.io.formats.style.Styler: The styled correlation matrix.

    Examples:
        >>> print_correlation_matrix(df)  # Prints the full correlation matrix from -1 to 1.
        >>> print_correlation_matrix(df, min_threshold=0.5)  # Prints correlations greater than or equal to 0.5.
        >>> print_correlation_matrix(df, max_threshold=-0.3)  # Prints correlations less than or equal to -0.3.
    """

    corr_matrix = df.corr(method=method, numeric_only=True)

    if hide_blanks_ones:
        # This code is to show only 1 side of the correlation matrix and remove the 1s from the diagonal

        mask = np.zeros_like(corr_matrix, dtype=bool)
        mask[np.triu_indices_from(mask)] = True
        corr_matrix[mask] = np.nan

    filtered_corr_matrix = corr_matrix[
        (corr_matrix >= min_threshold) & (corr_matrix <= max_threshold)
    ]

    styled_matrix = (
        filtered_corr_matrix.style.background_gradient(
            cmap="coolwarm", axis=None, vmin=-1, vmax=1
        )
        .highlight_null(color="#f1f1f1")
        .format(precision=precision)
    )

    return styled_matrix


# Customize the y-axis labels using FuncFormatter
def format_yticks(y, _):
    """
    Formats the y-tick labels for a plot.

    Parameters:
        y (int): The y-value of the tick label.
        _ (Any): Ignored parameter.

    Returns:
        str: The formatted y-tick label.
    """
    if y >= 1000:
        return f"{int(y / 1000)}K"
    return str(y)
