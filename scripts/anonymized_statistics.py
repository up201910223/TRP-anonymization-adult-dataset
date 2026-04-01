import pandas as pd
from pathlib import Path


def normalize_age_group(value):
    """Convert anonymized age values into consistent age-group labels."""
    if pd.isna(value):
        return "Unknown"

    value = str(value).strip()

    # Already generalized age ranges
    if "-" in value:
        return value

    # Fully suppressed or unknown values
    if value in {"*", "Unknown"}:
        return value

    # Original numeric value -> convert to 10-year buckets
    try:
        age = int(float(value))
        lower = (age // 10) * 10
        upper = lower + 10
        return f"{lower}-{upper}"
    except ValueError:
        return value


def generate_anonymized_stats(file_path):
    path = Path(file_path)
    if not path.is_absolute():
        path = (Path(__file__).resolve().parent / path).resolve()

    print(f"Loading dataset from: {path}")
    df = pd.read_csv(path)

    # Normalize target column
    df["income"] = df["income"].astype(str).str.strip()
    df["high_income"] = df["income"] == ">50K"

    # Normalize age groups
    if "age" in df.columns:
        df["age_group"] = df["age"].apply(normalize_age_group)

    # 1. Income by Sex
    if "sex" in df.columns:
        sex_stats = df.groupby("sex")["high_income"].mean() * 100
        print("\nBy Sex (% >50K):")
        print(sex_stats.round(2))

    # 2. Income by Race
    if "race" in df.columns:
        race_stats = df.groupby("race")["high_income"].mean() * 100
        print("\nBy Race (% >50K):")
        print(race_stats.round(2))

    # 3. Income by Education
    if "education" in df.columns:
        edu_stats = df.groupby("education")["high_income"].mean() * 100
        print("\nBy Education (% >50K):")
        print(edu_stats.round(2))

    # 4. Income by Age Group
    if "age_group" in df.columns:
        age_stats = df.groupby("age_group")["high_income"].mean() * 100
        age_counts = df["age_group"].value_counts().sort_index()

        print("\nBy Age Group (% >50K):")
        for group in sorted(age_stats.index):
            print(f"{group}: {age_stats[group]:.2f}% (n={age_counts[group]})")


if __name__ == "__main__":
    generate_anonymized_stats("../data/anonymized/others/adult_k10_l2_different_weights.csv")