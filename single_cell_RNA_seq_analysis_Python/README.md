# T-Cell Single-Cell RNA-seq Preprocessing

This repository contains the preprocessing workflow for a single-cell RNA-seq dataset of human T cells. The goal of this step is to produce a **high-quality, normalized, and scaled dataset** suitable for downstream analyses such as dimensionality reduction, clustering, and marker gene exploration.

## Dataset

- **Format:** `.h5ad` (AnnData)  
- **Original dimensions:** 5016 cells × 20953 genes  
- **Observations (`.obs`):** cell type, cytokine condition, donor ID, batch, QC metrics, cell cycle scores, cluster IDs, effectorness  
- **Variables (`.var`):** gene identifiers (Ensembl or gene symbols)

## Libraries Used

The preprocessing workflow relies on the following Python libraries:  

- [**Scanpy**](https://scanpy.readthedocs.io/) – main package for single-cell RNA-seq analysis  
- [**NumPy**](https://numpy.org/) – numerical operations and array handling  
- [**Pandas**](https://pandas.pydata.org/) – data manipulation and dataframe operations  
- [**Matplotlib**](https://matplotlib.org/) – plotting and visualization  

## Preprocessing Steps

1. **Quality Control (QC)**  
   - Removed cells with fewer than 200 detected genes.  
   - Filtered out genes expressed in fewer than 3 cells.  
   - Excluded predicted doublets and cells with high mitochondrial content.

2. **Normalization and Log Transformation**  
   - Scaled total counts per cell to 10,000 CPM.  
   - Applied `log1p` transformation to reduce skew and compress extreme values.  
   - Visualized histograms to inspect the distribution of expression values.

3. **Highly Variable Genes (HVGs) Selection**  
   - Identified genes with higher-than-expected variability across cells.  
   - Focused on HVGs to reduce noise and computational load in downstream analyses.

4. **Scaling (Z-score Normalization)**  
   - Standardized gene expression values to mean 0 and standard deviation 1.  
   - Ensured all genes are on a comparable scale for PCA, clustering, and UMAP.

5. **Sanity Checks**  
   - Verified that log normalization and scaling worked as expected for example genes.  
   - Checked global statistics to confirm dataset quality.


- The preprocessed dataset is available as:
  `output/scdr_preprocessed.h5ad`

