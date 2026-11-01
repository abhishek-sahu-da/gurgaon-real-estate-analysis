# Gurgaon Real Estate Analysis

Cleaning and analysing 14,000+ Gurgaon property listings with Python and Pandas.

## Data
Source: "Gurgaon Real Estate Dataset of 2024" by NikhilMehrahr26 on Kaggle (https://www.kaggle.com/datasets/nikhilmehrahr26/gurgaon-real-estate-dataset). The raw file has 19,515 listings; after removing duplicates and fixing data types, 14,223 remain. The dataset is not included in this repository, so download it from Kaggle and save it as gurugram.csv in the same folder as the script.
## What I did
- Cleaned column names, prices, areas and categories
- Compared price and price per sq ft across localities, property status and RERA approval
- Measured how area relates to price (Spearman correlation about 0.8)
- Made bar charts, scatter plots and heatmaps with Seaborn

## Findings
- Sector 42 has the highest average price and price per sq ft
- [Add one more finding from your own output]

## Tools
Python, Pandas, NumPy, Matplotlib, Seaborn