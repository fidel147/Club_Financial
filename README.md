# Club_Financial
# Club Financials Analysis

Data analysis project exploring football club financial data (2010–2026) using Python and pandas. The project covers descriptive statistics, correlation analysis, and a simple predictive model for club profitability.

## Overview

This project analyzes a dataset of club-level financial metrics across major European leagues to answer three questions:

- How fast is a given club's revenue growing over time?
- Which financial metrics are most correlated with a club's profitability?
- Can club profitability be predicted from wage spending and transfer activity?

## Dataset

The dataset (`club_financials.csv`) includes yearly financial records per club:

| Column | Description |
|---|---|
| `year` | Season year (2010–2026) |
| `club_name` | Club name |
| `league` | National league |
| `country` | Club's country code |
| `stadium_capacity` | Stadium capacity |
| `revenue_eur_m` | Total revenue (€M) |
| `wage_bill_eur_m` | Total wage bill (€M) |
| `wages_to_revenue_pct` | Wage-to-revenue ratio (%) |
| `net_transfer_spend_eur_m` | Net transfer spend (€M) |
| `operating_profit_eur_m` | Operating profit (€M) |

## Project Structure

```
├── Datasets/
│   └── club_financials.csv
├── First_Step/
│   ├── Financial/
│   │   ├── dataset.py          # ClubFinancials class (data access layer)
│   │   └── settings.py         # Config / constants
│   └── import_data.py
└── README.md
```

## Key Components

### `ClubFinancials` class

An object-oriented wrapper around the dataset that filters club data by dynamic criteria (club name, year, etc.) using an encapsulated `indexing` property with getter/setter, so filter criteria can be updated without exposing internal state directly.

### Analysis

- Descriptive statistics per club and per league (`.describe()`, `.groupby()`)
- Growth analysis (CAGR of revenue per club)
- Correlation analysis between wage spending, transfer spend, and operating profit
- League-level comparison (revenue, wage-to-revenue ratio, cumulative profit)


## Requirements

```
pandas
numpy
matplotlib
```

## Usage

```python
from dataset import ClubFinancials
import pandas as pd

data = pd.read_csv("Datasets/club_financials.csv")
cf = ClubFinancials({"club_financials": data}, club_name="Manchester City")

club_data = cf.get_club()
```

## Author

Fidèle Togbédji ZOGBE — [GitHub](https://github.com/zogbefidele)
Student in Génie Informatique et Télécommunications, EPAC (Université d'Abomey-Calavi)
