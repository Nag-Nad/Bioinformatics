import os
import mdtraj as md
import matplotlib.pyplot as plt
from sklearn import decomposition
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score
from scipy.spatial.distance import cdist
import numpy as np
import seaborn as sns
import pandas as pd
import typer
from typing import List


def app (
    traj: str = typer.Option(..., "--traj", "-t", help= "The path to the trajectory.xtc file"),
    coord: str = typer.Option(..., "--coord", "-c", help= "The path to the md.gro or npt.gro file"),
    selection: str = typer.Option(..., "--selection", "-s", help="selection rules: 1) must be a string (""), 2) subtact the resid (e.g., 102) from sequence start resid (e.g., 100). So, in this example the resid is 2!"),
    pca_components: int = typer.Option(..., "--pca_components", "-pcac", help="Number of PCA components to keep."),
    output_path: str = typer.Option(..., "--output_path", "-o", help="default = /home/naqme/md-pipeline/ML_files")
):
    """
    Selection Examples based on MDTraj Selection:
        backbone and side chain: "(resid 8 or resid 9 or resid 10 or ...) and not element H
        backbone: "(backbone and (resid 8 or resid 9 or resid 10 or ...))"
    """
    try:
        files = md.load_xtc(traj, coord)
    except Exception as e:
        print(f"Error loading files: {e}")
        raise typer.Exit(code=1)
    
    if selection:
        atom_indices = files.topology.select(selection)
        # Adjusting indices to match the original sequence
        adjusted_indices = [i + 1 for i in atom_indices]
        if atom_indices.size == 0:
            print("No atoms are selected! We will proceed with all atom for PCA.")
    else:
        adjusted_indices = np.arange(files.n_atoms)
    

    # Slice the trajectory for the selected atoms
    files_sliced = files.atom_slice(adjusted_indices)  
    # Reshape to (n_frames, n_coordinates)
    xyz = files_sliced.xyz.reshape((files_sliced.n_frames, files_sliced.n_atoms * 3))
    # Step 1: Standardize the data (scaling and centering)
    scaler = StandardScaler()
    xyz_scaled = scaler.fit_transform(xyz)
    # Step 2: Perform PCA
    pca = PCA(n_components=pca_components)
    pca.fit(xyz_scaled)
    # Step 3: Transform the data using the fitted PCA model
    xyz_transformed = pca.transform(xyz_scaled)
    variance = pca.explained_variance_ratio_
    print(f"Explained variance ratio: {variance}")
    print(f"sum. : {variance.sum()}")

    plt.figure()
    plt.scatter(xyz_transformed[:,0],xyz_transformed[:,1], marker='x', c=files.time)
    plt.xlabel('PC1')
    plt.ylabel('PC2')
    plt.title('PCA')
    cbar = plt.colorbar()
    cbar.set_label('Time [ps]')
    plt.savefig(f"{output_path}/PCA.png", format="png", dpi=300)
    n_samples = xyz_transformed.shape[0]  # Number of frames/samples
    max_clusters = min(n_samples - 1, 10)  # Ensure k < n_samples
    range_n_clusters = list(range(2, max_clusters + 1))
    elbow = []
    ss = []
    distortions =[]
    
    for k in range_n_clusters:  # iterating through cluster sizes
        clusterer = KMeans(n_clusters=k, random_state=42)
        cluster_labels = clusterer.fit_predict(xyz_transformed)
        
        # Finding the average silhouette score
        silhouette_avg = silhouette_score(xyz_transformed, cluster_labels)
        ss.append(silhouette_avg)
        # Finding the average SSE (inertia)
        # Inertia: Sum of squared distances to closest cluster center
        elbow.append(clusterer.inertia_)
        distortions.append(sum(np.min(cdist(xyz_transformed, clusterer.cluster_centers_, 'euclidean'), axis=1)) / xyz_transformed.shape[0])

        print(f"For n_clusters = {k}, the average silhouette score is: {silhouette_avg}")
        
        # Check if the output directory exists, if not, create it
    if not os.path.exists(output_path):
        os.makedirs(output_path)

    fig = plt.figure(figsize=(14, 7))
    # Plot SSE (Elbow method)
    fig.add_subplot(121)
    plt.plot(range_n_clusters, elbow, 'b-', label='Sum of squared error')
    plt.title('Elbow Method in K-Means Clustering')
    plt.xlabel("Number of clusters")
    plt.ylabel("SSE")
    plt.legend()

    # Plot Silhouette Score
    fig.add_subplot(122)
    plt.plot(range_n_clusters, ss, 'b-', label='Silhouette Score')
    plt.title("Silhouette Method in K-Means Clustering")
    plt.xlabel("Number of clusters")
    plt.ylabel("Silhouette Score")
    plt.legend()
    plt.savefig(f"{output_path}/n_clusters.png")
    plt.show()

    # Draw a linear function between the end points
    # (y2 - y1 / x2 - x1) * x + c
    linear = []
    ld = len(distortions)
    steep = (distortions[ld-1] - distortions[0]) / (ld - 1)
    c = distortions[ld-1] - steep * ld
    for x in range(0,ld):
        linear.append(steep * (x+1) + c)
    
    # And last we look for max distance between the points
    distances = np.array(linear)-np.array(distortions)
    max_index = str(distances.argmax(axis=0)+1)

    with open (f"{output_path}/optimal_K.txt", "w") as file:
        optimum = file.write(max_index)


if __name__ == "__main__":
    typer.run(app)
     