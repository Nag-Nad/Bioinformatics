# 🧪 Molecular Descriptor Calculation and Similarity Analysis

This project analyzes small molecules using **RDKit** and related Python libraries.  
It performs molecular data processing, descriptor calculation, filtering, fingerprint generation, similarity measurement, and visualization.

---

## 📦 Required Libraries

- `pandas`  
- `numpy`  
- `seaborn`  
- `matplotlib`  
- `scipy`  
- `rdkit`

---

Each CSV file contains:

- `zinc_id` — unique molecule identifier  
- `smiles` — SMILES representation of the molecule  

All CSV files are concatenated into one DataFrame using the **glob** library.

---

## ⚙️ Workflow

### 1. Data Preparation
- Combine all CSV files into a single DataFrame.  
- Add molecule names manually (e.g., *Ice*, *Dopamine*, *Eugenol*, *Caffeine*, *Pyruvate*).

### 2. Descriptor Calculation
Using **RDKit Descriptors**, compute the following physicochemical properties:
- Molecular Weight (MolWt)  
- Number of Heavy Atoms  
- Number of Rotatable Bonds  
- LogP (octanol-water partition coefficient)

### 3. Filtering Criteria
Filter molecules based on standard **drug-likeness** conditions:
- Molecular weight between **100–700 Da**  
- ≤ **60** heavy atoms  
- ≤ **15** rotatable bonds  
- **LogP ≤ 5**

### 4. Fingerprint and Similarity Analysis
- Generate **Morgan fingerprints** (radius = 3, 2048 bits).  
- Calculate **Tanimoto similarity** between all molecule pairs.  
- Store results in a similarity matrix.

### 5. Visualization
- **Heatmap:** shows pairwise similarity (darker blue = higher similarity).  
- **Cluster map:** hierarchical clustering of molecules by structural similarity.  
- **2D structure rendering:** generated using `Draw.MolsToGridImage` and `PandasTools`.

### 6. 3D Conformer Generation
- Add hydrogens to molecules.  
- Generate multiple 3D conformations using `AllChem.EmbedMultipleConfs`.  
- Export each structure to `.sdf` files and one combined `all_conformers.sdf`.

---

## 📊 Outputs

| Output Type | Description |
|--------------|-------------|
| `similarity_matrix` | Tanimoto similarity scores between molecules |
| **Heatmap / Cluster map** | Visualization of chemical similarity |
| `conformers*.sdf` | 3D conformations of each molecule |
| `all_conformers.sdf` | Combined 3D conformations of all molecules |

---

## 🧠 Key Concepts

- **Tanimoto Similarity:** Measures structural resemblance between molecules (0 = dissimilar, 1 = identical).  
- **Morgan Fingerprints:** Circular fingerprints capturing molecular substructure information.  
- **Descriptors:** Quantitative features used in QSAR, clustering, or machine-learning analyses.

---

## 🧬 Example Molecules

| Molecule | ZINC ID | Molecular Weight | LogP |
|-----------|----------|------------------|------|
| Ice | ZINC000000001084 | 194.19 | −1.03 |
| Dopamine | ZINC000000033882 | 153.18 | 0.60 |
| Eugenol | ZINC000000001411 | 164.20 | 2.13 |
| Caffeine | ZINC000001482164 | 156.27 | 2.44 |

---

## 🧩 Notes

This workflow demonstrates **molecular filtering and similarity exploration**, commonly used in:
- Virtual screening  
- Drug discovery  
- QSAR modeling  

The generated `.sdf` files can be visualized in tools such as **PyMOL**, **Chimera**, or **Avogadro**.

---


