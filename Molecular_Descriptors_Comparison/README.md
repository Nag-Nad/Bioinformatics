# Chemical Properties Comparison of Random Molecules

## Overview
This mini-project analyzes and compares the **chemical properties** of ten randomly selected molecules using three different computational approaches:

1. **RDKit** – local cheminformatics analysis directly from molecular structures.
2. **PubChemPy** – property retrieval via the PubChem Python interface.
3. **PubChem API with BeautifulSoup** – data extraction from the PubChem website through web scraping.

The main goal is to evaluate the **consistency, accessibility, and scope** of chemical property information obtained through these three methods.

## Molecular Descriptors
The project focuses on the following molecular descriptors, which are crucial in drug design because they correlate with pharmacokinetics (ADME) and drug-likeness:

| Descriptor | Description | Importance |
|------------|-------------|------------|
| **LogP** | Lipophilicity (hydrophobic/hydrophilic balance) | Affects solubility, membrane permeability, and bioavailability |
| **Molecular Weight (MW)** | Total mass of the molecule | Influences absorption, transport, and oral bioavailability |
| **Number of Rotatable Bonds** | Molecular flexibility | Higher flexibility may reduce binding efficiency and oral bioavailability |
| **Number of Heavy Atoms** | Count of non-hydrogen atoms | Reflects molecular size and complexity |

These descriptors relate to **Lipinski’s Rule of Five**, commonly used for assessing drug-likeness:

- MW ≤ 500  
- LogP ≤ 5  
- ≤ 5 hydrogen bond donors  
- ≤ 10 hydrogen bond acceptors  
- ≤ 10 rotatable bonds

## Libraries Used
- `RDKit` – cheminformatics calculations  
- `PubChemPy` – access to PubChem compound properties  
- `BeautifulSoup` – web scraping PubChem API  
- `pandas`, `numpy`, `seaborn`, `matplotlib` – data processing and visualization  

## How It Works
1. **Random Compound Selection**  
   Ten random PubChem CIDs are selected programmatically.  

2. **Property Extraction**  
   - RDKit: Calculates descriptors from SMILES strings.  
   - PubChemPy: Retrieves molecular descriptors via the PubChem Python API.  
   - PubChem API: Scrapes SMILES from the PubChem website and calculates descriptors.  

3. **Comparison**  
   The calculated descriptors from all three methods are compared for consistency. Visualizations highlight any differences.

## Files
- `ten_random_chemicals.csv` – CSV file containing the randomly selected compounds and their properties  
- `ten_random_chemicals.html` – HTML version of the data for visualization  
- `Chemical_Properties_Analysis.ipynb` – Jupyter notebook implementing the analysis and comparison  

## Conclusion

This project demonstrates that molecular descriptors _(MW, LogP, rotatable bonds, heavy atoms)_ can be reliably calculated from both local and online sources. The comparison confirms the consistency of these descriptors across RDKit, PubChemPy, and PubChem API methods.**
