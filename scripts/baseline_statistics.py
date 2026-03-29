import pandas as pd
from pathlib import Path

def generate_baseline_stats(file_path):
    path = Path(file_path)
    if not path.is_absolute():
        path = (Path(__file__).resolve().parent / path).resolve()

    print(f"Loading dataset from: {path}")
    df = pd.read_csv(path)
    df['income'] = df['income'].astype(str).str.strip()
    df['high_income'] = df['income'] == '>50K'

    # 1. Income by Sex
    sex_stats = df.groupby('sex')['high_income'].mean() * 100

    # 2. Income by Race
    race_stats = df.groupby('race')['high_income'].mean() * 100

    # 3. Income by Education (Top 5 by count)
    top_edu = df['education'].value_counts().head(5).index
    edu_stats = df[df['education'].isin(top_edu)].groupby('education')['high_income'].mean() * 100

    # 4. Income by Age Group (matching 10-year hierarchy bins)
    bins   = [0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
    labels = ['0-10','10-20','20-30','30-40','40-50',
              '50-60','60-70','70-80','80-90','90-100']
    df['age_group'] = pd.cut(df['age'], bins=bins, labels=labels, right=False)
    age_stats = df.groupby('age_group', observed=True)['high_income'].agg(['mean','count'])
    age_stats['pct_high_income'] = (age_stats['mean'] * 100).round(2)

    print("\n--- Income (>50K) Baseline Statistics ---")
    print("\nBy Sex (% >50K):")
    print(sex_stats.round(2))
    print("\nBy Race (% >50K):")
    print(race_stats.round(2))
    print("\nBy Education (Top 5) (% >50K):")
    print(edu_stats.round(2))
    print("\nBy Age Group (% >50K):")
    print(age_stats[['count', 'pct_high_income']].to_string())

if __name__ == "__main__":
    generate_baseline_stats('../data/processed/adult_clean.csv')