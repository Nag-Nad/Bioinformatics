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
- [**SciPy**] (https://docs.scipy.org/doc/scipy/reference/stats.html) - normality test (shapiro)

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


- The initial compressed dataset is available as:
  `input/scdr_compresssed.h5ad`

---

## sc-RNA-seq data clustering and cell identification

Single-cell RNA-seq allows the profiling of gene expression at the level of individual cells, revealing heterogeneity within cell populations. In this project, we focus on T-cells and aim to identify distinct subpopulations, such as Naive (TN), Central Memory (TCM), Effector Memory (TEM), and Effector Memory re-expressing CD45RA (TEMRA).


## Workflow Overview

The analysis follows these main steps:

1. **Dimensionality reduction** – Principal Component Analysis (PCA) to summarize high-dimensional gene expression data.
2. **Neighborhood graph construction** – Identify each cell’s closest neighbors based on PCA components.
3. **Clustering** – Leiden algorithm is used to identify clusters of cells with similar expression profiles.
4. **Visualization** – UMAP is used to visualize clusters in 2D space.
5. **Marker gene identification** – Differentially expressed genes are identified for each cluster.
6. **Cell type annotation** – Clusters are assigned cell type labels based on known marker genes.


## Results

Clusters correspond to known T-cell subtypes:
_UMAP visualization shows clear separation between subtypes._

- **TN (Naive T-cells)** – clusters 0, 3, 5
- **TCM (Central Memory T-cells)** – clusters 1, 2
- **TEM (Effector Memory T-cells)** – cluster 4
- **TEMRA (Effector Memory re-expressing CD45RA)** – cluster 6

