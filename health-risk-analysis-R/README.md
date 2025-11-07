**Health Data Analysis**

This folder has my analysis of a health dataset. I looked at patient features like age, BMI, glucose level, smoking, work type, and how they relate to stroke and other outcomes.

**Dataset**
- 5110 patients
  
- 12 features:
  
  1. id – patient ID
  2. gender – Male, Female, Other
  3. age – patient age
  4. hypertension – 0=no, 1=yes
  5. heart_disease – 0=no, 1=yes
  6. ever_married – No/Yes
  7. work_type – children, Govt_job, Never_worked, Private, Self-employed
  8. Residence_type – Rural/Urban
  9. avg_glucose_level – average blood glucose
  10. bmi – body mass index
  11. smoking_status – formerly smoked, never smoked, smokes, Unknown
  12. stroke – 0=no, 1=yes

**Workflow**

- Cleaned the data and fixed missing values
- Made plots to see distributions and relationships between features
- Checked correlations between age, BMI, glucose, etc.
- Ran PCA and clustering to see patterns in data
- Did statistical tests: normality, Mann–Whitney, Kruskal–Wallis, Chi-square
- Built a simple logistic model to see what affects stroke risk

**Key observations**

- Age, BMI, and glucose are weakly related
- Glucose has two peaks, BMI has some outliers
- Smoking status has small effects on BMI and stroke
- Work type and residence don’t change BMI or glucose much
- Hypertension is a strong risk factor for stroke
- PCA shows most variance is captured by the first two components

**Files**

- health_analysis.Rmd – R Markdown with full analysis and plots
- health_analysis.html – a format to easily scroll the results and plots

[🔗 View the full report (HTML)](https://nag-nad.github.io/Bioinformatics/health-risk-analysis-R/health_analysis.html)

- healthcare-dataset-stroke-data.csv – original dataset (if allowed)
  
**Packages used**

- tidyverse
- ggplot2
- pheatmap
- factoextra
- dunn.test
- car

**How to use**

- Clone this repo
- Open stroke_analysis.Rmd in RStudio
- Run the code or knit to HTML to see results
- Check plots and tables to explore data

