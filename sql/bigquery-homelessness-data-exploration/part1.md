# BigQuery Homelessness Data Exploration – Part 1

## Project Overview
This project explores homelessness data from the BigQuery Public Dataset
`sdoh_hud_pit_homelessness.hud_pit_by_coc`. The goal of Part 1 is to understand
the structure of the dataset, interpret key columns and acronyms, and prepare
the data for further analysis.

---

## Step 1: Dataset Schema Review
The Schema tab in BigQuery was reviewed to understand the meaning and data types
of each column. This step helped establish context for how homelessness data is
captured across U.S. Continuums of Care (CoC).

---

## Step 2: Dataset Understanding Questions

### Acronyms Used in the Dataset
- **CoC**: Continuum of Care  
- **Sheltered_ES**: Emergency Shelter  
- **Sheltered_TH**: Transitional Housing  
- **Sheltered_SH**: Safe Haven Housing  

### Columns That Are Not Integer Type
The only three columns in the dataset that are not integers are:
- `CoC_Number`
- `CoC_Name`
- `CoC_Category`

### Determining the State for Each Record
Each `CoC_Number` begins with a two-letter state abbreviation, allowing the state
to be identified directly from the CoC code.

### Total Number of Rows
- **Total rows in the dataset:** 2,768

### Potential Use Cases for This Dataset
The `sdoh_hud_pit_homelessness` dataset may be used by government agencies,
public health organizations, and nonprofit groups to analyze homelessness trends
across regions. When combined with social determinants of health data, it can
support:
- Identifying communities with greater housing instability
- Understanding the relationship between homelessness and health outcomes
- Informing funding allocation and policy development
- Supporting data-driven social service planning

---

## Step 3: Creating a Working Table in BigQuery

A new table was created to streamline analysis and add a state-level identifier
derived from the Continuum of Care number.


SQL Function Explanation

The LEFT() function extracts a specified number of characters from the beginning
of a string. In this query:

LEFT(CoC_Number, 2) AS State


This creates a new column named State containing the first two characters of
the CoC_Number, which correspond to the state abbreviation.

Step 4: Data Validation

After creating the new table, the Preview tab was used to confirm that all
columns appeared correctly and the data was structured as expected.
