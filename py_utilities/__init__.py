print(f"Invoking __init__.py for {__name__}")

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy import stats
from typing import Dict


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


def shapiro_wilk_and_bartlett_tests(
    df: pd.DataFrame, target_column: str, group_column: str
) -> Dict[str, Dict[str, float]]:
    """
    Perform Shapiro-Wilk test for normality and Bartlett's test for homoscedasticity tests on a DataFrame after removing all nas for selected columns.

    Parameters:
        df (pd.DataFrame): The input DataFrame.
        target_column (str): The column containing the target variable.
        group_column (str): The column containing the group variable.

    Returns:
        dict: A dictionary containing the results of the Shapiro-Wilk test and Bartlett's test.

    Examples:
        >>> normality_and_homoscedasticity_tests(df, 'target', 'group')
    """

    valid_data = df[df[target_column].notna() & df[group_column].notna()]

    # Check for normality using Shapiro-Wilk test for each group
    shapiro_results = {}
    groups = valid_data[group_column].unique()

    # Create a single figure with subplots for the Q-Q plots
    fig, axes = plt.subplots(1, len(groups), figsize=(15, 4))

    for i, group in enumerate(groups):
        data = valid_data[valid_data[group_column] == group][target_column]
        shapiro_stat, shapiro_p = stats.shapiro(data)
        shapiro_results[group] = {
            "Shapiro Statistic": shapiro_stat,
            "p-value": shapiro_p,
        }

        # Create a Q-Q plot in the corresponding subplot
        stats.probplot(data, plot=axes[i])
        axes[i].set_title(
            f"Q-Q Plot for {group} Group in {group_column}\n" f" p-value: {shapiro_p}"
        )
        axes[i].set_xlabel("Theoretical Quantiles")
        axes[i].set_ylabel("Ordered Values")

    # Adjust spacing between subplots
    plt.tight_layout()

    # Perform Bartlett's test on the filtered data for homoscedasticity
    bartlett_results = {}
    group_data = [
        valid_data[valid_data[group_column] == group][target_column] for group in groups
    ]
    bartlett_stat, bartlett_p = stats.bartlett(*group_data)
    bartlett_results[group_column] = {  # Changed to use group_column as the key
        "Bartlett Statistic": bartlett_stat,
        "p-value": bartlett_p,
    }

    # Print the test results
    print("Shapiro-Wilk Test Results:")
    for group, result in shapiro_results.items():
        print(
            f"Group: {group}, Shapiro Statistic: {result['Shapiro Statistic']}, p-value: {result['p-value']}"
        )

    print("\nBartlett Test Results:")
    for group, result in bartlett_results.items():
        print(
            f"Group: {group}, Bartlett Statistic: {result['Bartlett Statistic']}, p-value: {result['p-value']}"
        )

    return shapiro_results, bartlett_results
