# Analyzing Podcast Reviews 

## Objectives
In this notebook, we will pursue the following objectives:

Load and explore the "Podcast Reviews" dataset.
Perform sentiment analysis on podcast reviews to gauge overall sentiment trends.
Perform AB test to determine whether Positive sentiment reviews are linked to podcasts with higher average rating than Negative sentiment reviews.

## Introduction:
Podcasts have gained immense popularity in recent years, providing a diverse platform for content creators to share their ideas, stories, and expertise. With the increasing number of podcasts available, understanding listener feedback and sentiments becomes crucial for podcasters and platforms alike.

In this notebook, we delve into the "Podcast Reviews" dataset, a comprehensive collection of 2 million podcast reviews covering 100,000 unique podcasts. Updated monthly, this dataset offers a treasure trove of text feedback and review data that we can use to gain insights into listener opinions, preferences, and sentiments.

## Dataset Overview:
This project is based on a dataset containing information about podcasts, reviews, and sentiment analysis. The dataset is organized into several tables:

- `podcasts`: Contains information about podcasts, including title, iTunes ID, and categories.
- `reviews`: Includes reviews of podcasts, along with author information, content, and ratings.
- `categories`: Lists the categories associated with each podcast.
- `runs`: Contains data related to the podcast data extraction process.

The data is collected over time, with podcast and review information spanning multiple years. Some of the data columns include podcast titles, review content, sentiment analysis, average ratings, and sentiment categories.

## Table of Contents:
- [Data Extraction](#data-extraction)
- [Sentiment Analysis](#sentiment-analysis)
- [General Summary](#general-summary)
- [Potential Improvements](#potential-improvements)
- [Getting Started](#getting-started)
- [Dependencies](#dependencies)
- [Usage](#usage)
- [License](#license)

## Data Extraction:
- The data is sourced from [Podcast Reviews](https://www.kaggle.com/datasets/anth7310/mental-health-in-the-tech-industry).
- It is organized into four tables: `podcasts`, `reviews`, `categories`, and `runs`.
- EDA is conducted to gain insights into the podcasts and the trends associated.

## Sentiment Analysis:
- Sentiment analysis is performed on the content of the reviews for podcasts.
- Positive, neutral and negative sentiments are categorized.
- An AB test on the sentiment analysis is performed to determine whether Positive sentiment reviews are linked to podcasts with higher average rating than Negative sentiment reviews.

## General Summary:
The analysis revealed the following key results:

- Significant differences in average ratings among podcasts with different sentiment categories.
- Effect sizes (Cohen's d) indicating the magnitude of these differences.
- Visualization of the results through box plots and bar charts.

The results suggest that sentiment plays a significant role in the average ratings of podcasts. Positive sentiment reviews tend to be associated with higher ratings, while negative sentiment reviews correlate with lower ratings. Neutral sentiment reviews show intermediate ratings.

## Potential Improvements:
Some aspects that could be improved on this analysis:

- Natural Language Processing (NLP): Incorporating NLP techniques, such as topic modeling, sentiment intensity analysis, and entity recognition, can offer deeper insights into the content of reviews and podcasts. This could help in identifying specific topics or themes that impact ratings.

- Time-Series Analysis: Analyzing the temporal aspect of reviews and ratings can reveal how sentiments and podcast popularity evolve over time. Time-series analysis can provide valuable information for podcast creators and marketers.

- Machine Learning Models: Implementing machine learning models for sentiment analysis and predicting podcast success can lead to more accurate predictions and recommendations. Models can help in identifying which podcasts are likely to receive high or low ratings based on content and user engagement.

## Getting Started:
To replicate this analysis, follow these steps:

### Dependencies:
- Python (3.x)
- Required libraries are shown in the `requirements.txt` file

### Usage:
1. Clone this repository.
2. Install the required dependencies through the `requirements.txt` file
3. Download the dataset from Kaggle and place it in the folder 'data/raw_data'
4. Run the provided Python scripts in the order specified.

## License
This project is licensed under the [MIT License](LICENSE).

For more information, feel free to [email me](mailto:alessionespoli.97@gmail.com).

