# Initial Inspection

## Dataset Overview

The dataset used in this project is the Adult (Census Income) dataset, after preprocessing.

- **Number of records:** 32,561 (excluding header)
- **Number of attributes:** 14 (after preprocessing)
- **Processed dataset location:** `data/processed/adult_clean.csv`

---

## Preprocessing Summary

The following preprocessing steps were applied:

- Removed quotation marks from the original dataset
- Replaced missing values (`?`) with `"Unknown"`
- Removed redundant attribute `education.num`
- Ensured consistent CSV formatting for compatibility with ARX

---

## Attribute Roles

### Sensitive Attribute
- `income`  
  Represents whether an individual earns more than 50K per year.

### Quasi-identifiers
- age  
- sex  
- race  
- education  
- marital.status  
- occupation  
- relationship  
- native.country  
- capital.gain  
- capital.loss  

These attributes may enable reidentification when combined.

### Non-sensitive / Auxiliary Attributes
- hours.per.week  
- fnlwgt  

---

## Baseline Analytical Observations

To understand the utility of the dataset before anonymization, baseline statistics were computed.

### Income Distribution by Sex

- Male: **30.57%** earn >50K  
- Female: **10.95%** earn >50K  

This shows a significant disparity in income distribution by sex.

---

### Income Distribution by Race

- Asian-Pac-Islander: **26.56%**
- White: **25.59%**
- Black: **12.39%**
- Amer-Indian-Eskimo: **11.58%**
- Other: **9.23%**

There are noticeable differences across racial groups, indicating that race is a relevant factor in income distribution.

---

### Income Distribution by Education (Top Categories)

- Masters: **55.66%**
- Bachelors: **41.48%**
- Assoc-voc: **26.12%**
- Some-college: **19.02%**
- HS-grad: **15.95%**

Education level appears to be strongly correlated with higher income.

---

## Key Observations

- Income distribution varies significantly across multiple attributes, especially **sex** and **education**
- Several quasi-identifiers (e.g., occupation, country, capital gain/loss) have high variability and may increase reidentification risk
- The dataset contains imbalanced distributions, which may affect both privacy and utility after anonymization

---

## Objective for Data Release

The goal is to anonymize the dataset while preserving its ability to support analysis of:

- The relationship between **education and income**
- Differences in income distribution across **sex and race**

These analytical goals will be used later to evaluate the utility of the anonymized dataset.

---

## Next Step

The next step is to import the dataset into ARX, define attribute types, and construct generalization hierarchies required for privacy models.