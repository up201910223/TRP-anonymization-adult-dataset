# Step 1: Dataset Goal and Privacy Requirements

## Goal of the Dataset Release
The objective for releasing this anonymized dataset is to allow researchers to analyze how key demographic factors—specifically sex, race, and education—affect an individual's likelihood of earning an income greater than $50K per year. The dataset must preserve enough utility to accurately reflect these demographic income trends while preventing the re-identification of any individual and the inference of their specific income bracket.

## Baseline Statistics (Raw Dataset)
To evaluate utility preservation, we calculated the following baseline statistics on the original dataset regarding the percentage of individuals earning >$50K:

* **By Sex:** Female (10.95%), Male (30.57%)
* **By Race:** Asian-Pac-Islander (26.56%), White (25.59%), Black (12.39%), Amer-Indian-Eskimo (11.58%), Other (9.23%)
* **By Education (Top 5):** Masters (55.66%), Bachelors (41.48%), Assoc-voc (26.12%), Some-college (19.02%), HS-grad (15.95%)

These baseline metrics will be compared against the anonymized dataset output to measure utility loss.

## Privacy Requirements
Based on the dataset analysis, we have defined the following acceptable intervals for the anonymization process:

* **Privacy Models:** * $k$-Anonymity: Baseline of $k=5$ (acceptable range $k=3$ to $k=10$).
  * $l$-Diversity: $l=2$ recursive diversity on the sensitive `income` attribute to prevent attribute disclosure.
* **Suppression Limit:** An acceptable interval of 2% to 5%. Exceeding 5% may skew the demographic representation and result in unacceptable utility loss.
* **Attribute Weights:** Higher utility weights will be assigned to `sex`, `race`, and `education` to preserve our analytical goal. Lower weights will be assigned to attributes like `native.country` or `marital.status`.