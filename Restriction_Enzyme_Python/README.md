# 🧬 Restriction Enzyme Simulation in Python

This project simulates the cutting action of two restriction enzymes (**AbcI** and **AbcII**) on a DNA sequence using **regular expressions** in Python.

---

## 📦 Requirements

- Python ≥ 3.6  
- Standard library modules only:
  - `re` (Regular Expressions)

---

## ⚙️ Overview

Restriction enzymes recognize specific DNA sequences and cut at defined positions.  
This script defines two custom enzymes with simplified recognition motifs and simulates their cutting process.

---

## 🧪 Restriction Enzymes Defined

| Enzyme | Recognition Sequence | Pattern Description |
|---------|----------------------|---------------------|
| **AbcI** | `A[TCG]TAAT` | Recognizes `A` followed by T/C/G, then `TAAT` |
| **AbcII** | `GC[AG][AT]TG` | Recognizes `GC`, followed by A/G, then A/T, then `TG` |

---

## 🧩 Functions

### `AbcI(dna)`
- Finds all occurrences of the **AbcI** restriction site in a DNA sequence.  
- Splits the sequence where the enzyme cuts (`+3` offset after `AAT`).  
- Returns the digested DNA fragment.

### `AbcII(dna)`
- Finds all occurrences of the **AbcII** restriction site.  
- Splits the sequence where the enzyme cuts (`−2` offset before `TG`).  
- Returns the digested DNA fragment.

### `restricted_fragment(restriction_start_AbcI, restriction_start_AbcII)`
- Calculates the **length of the DNA fragment** between two cut sites.  
- Returns a formatted string showing the distance between AbcI and AbcII cut points.

---

## 🧬 Example Usage

```python
import re

# Example DNA sequence
dna = 'CCATTAATCCGCGATGCC'

restriction1 = AbcI(dna)
print('The AbcI cuts at', restriction1)

restriction2 = AbcII(dna)
print('The AbcII cuts at', restriction2)

insert = restricted_fragment(restriction_start_AbcI, restriction_start_AbcII)
print(insert)
