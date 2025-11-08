# CLI automation with Typer

This Python script provides a command-line interface (CLI) for analyzing molecular dynamics (MD) trajectories using mdtraj. It allows users to load trajectory and coordinate files, select specific atoms, and perform PCA (Principal Component Analysis) on the selected atoms to reduce dimensionality. The script standardizes the data, computes PCA, and visualizes the first two principal components as a scatter plot colored by simulation time.

Additionally, it performs K-Means clustering on the PCA-transformed data, evaluates cluster quality using the Elbow method, Silhouette score, and a distortion-based heuristic, and saves the optimal number of clusters. All results, including plots and a text file with the optimal cluster number, are saved to a user-specified output directory.
The script is fully CLI-driven using Typer, allowing users to specify trajectory file paths, selection rules, number of PCA components, and output path directly from the terminal. This design makes it modular, reusable, and easily automatable.

**Key features:**
- Flexible atom selection using MDTraj-style selection strings
- PCA analysis with explained variance reporting
- K-Means clustering with automated evaluation of optimal cluster number
- CLI interface for easy integration into workflows
