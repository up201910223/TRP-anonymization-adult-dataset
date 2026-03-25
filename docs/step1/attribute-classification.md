# Attribute Classification

## Identifiers

**None present in the dataset**

The dataset does not contain direct identifiers such as names, social security numbers, or contact information. Therefore, no explicit identifier removal step is required. However, the absence of direct identifiers does not eliminate reidentification risk, as combinations of quasi-identifiers may still uniquely identify individuals.

---

## Sensitive Attributes

### income

The attribute `income` is considered sensitive because it represents private financial information about individuals. Disclosure of this attribute may lead to privacy violations, including financial profiling or discrimination.

Additionally, `income` is the target variable for analysis in this project. This creates an inherent trade-off: it must be preserved for utility, while being protected against inference attacks.

From a privacy perspective, it is crucial that the anonymization process prevents attackers from confidently inferring the income value of a specific individual within an equivalence class.

---

## Quasi-identifiers

Quasi-identifiers (QIs) are attributes that do not directly identify individuals but may enable reidentification when combined with external data sources.

### Selected quasi-identifiers:

- **age**  
  Age is a strong quasi-identifier, especially when represented as an exact value. Rare ages or combinations with other attributes significantly increase reidentification risk. It requires generalization into ranges.

- **sex**  
  Although low cardinality, it contributes to narrowing down equivalence classes when combined with other attributes.

- **race**  
  This attribute can increase identifiability, particularly for minority groups with lower representation in the dataset.

- **education**  
  Reflects socio-economic status and, when combined with other attributes, contributes to uniqueness.

- **marital.status**  
  Provides additional demographic segmentation, increasing linkage risk.

- **occupation**  
  High variability and presence of rare categories make this a strong quasi-identifier. Certain occupations may uniquely identify individuals in combination with other attributes.

- **native.country**  
  Particularly sensitive in terms of identifiability, as rare countries can significantly reduce anonymity. Requires grouping (e.g., by region).

- **relationship**  
  Often overlooked, but highly useful for reidentification. Categories such as “Husband” or “Own-child” add structural household information.

- **capital.gain**  
  Highly skewed attribute with many zero values and few extreme values. These extreme values may act as near-identifiers.

- **capital.loss**  
  Similar to `capital.gain`, it presents a skewed distribution and can significantly increase reidentification risk when combined with other attributes.

---

## Non-sensitive / Auxiliary Attributes

- **hours.per.week**  
  This attribute is not directly sensitive but may contribute moderately to reidentification. It is primarily useful for analytical purposes and can be retained with minimal generalization.

- **fnlwgt**  
  This is a sampling weight used by the Census Bureau and does not represent an intrinsic characteristic of an individual. It is therefore considered a technical attribute rather than a personal one.

  Due to its limited interpretability and relevance for the analysis objective, it may be excluded without significant loss of utility.

---

## Attributes to be Removed

- **education.num**

This attribute is a numerical encoding of the `education` attribute and does not provide additional information. Keeping both would introduce redundancy and potentially bias the anonymization process.

Therefore, `education.num` is removed to simplify the dataset and avoid duplicating information across attributes.

---

## Final Remarks

The classification of attributes was guided by both theoretical considerations from the literature on data anonymization and empirical characteristics of the dataset, such as attribute distributions, cardinality, and potential contribution to reidentification risk.

This classification serves as the foundation for the definition of generalization hierarchies and the application of privacy models in subsequent steps of the project.
