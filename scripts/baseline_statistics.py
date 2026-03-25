import pandas as pd
from pathlib import Path

def generate_baseline_stats(file_path):
    path = Path(file_path)
    if not path.is_absolute():
        path = (Path(__file__).resolve().parent / path).resolve()

    print(f"Loading dataset from: {path}")
    df = pd.read_csv(path)

    # Normalize the income column to avoid whitespace issues
    df['income'] = df['income'].astype(str).str.strip()

    # Create a boolean column for >50K to calculate percentages easily
    df['high_income'] = df['income'] == '>50K'

    # 1. Income by Sex
    sex_stats = df.groupby('sex')['high_income'].mean() * 100

    # 2. Income by Race
    race_stats = df.groupby('race')['high_income'].mean() * 100

    # 3. Income by Education (Top 5 education levels by count)
    top_edu = df['education'].value_counts().head(5).index
    edu_stats = df[df['education'].isin(top_edu)].groupby('education')['high_income'].mean() * 100

    print("\n--- Income (>50K) Baseline Statistics ---")
    print("\nBy Sex (% >50K):")
    print(sex_stats.round(2))

    print("\nBy Race (% >50K):")
    print(race_stats.round(2))

    print("\nBy Education (Top 5 categories) (% >50K):")
    print(edu_stats.round(2))

if __name__ == "__main__":
    generate_baseline_stats('../data/processed/adult_clean.csv')