# Melting Temperature and GC Content Calculator

This Python script calculates the **melting temperature (Tm)** and **GC content** of a DNA sequence provided by the user. It also evaluates whether the values fall within optimal ranges for primer design.

---

## 🔬 Functions

### 1. `Tm(seq)`
Calculates the melting temperature of a DNA sequence.

- **Formula (for sequences ≤ 14 bases):**
  \[
  Tm = (A + T) \times 2 + (G + C) \times 4
  \]

- **Formula (for sequences > 14 bases):**
  \[
  Tm = 64.9 + 41 \times \frac{(G + C - 16.4)}{A + T + G + C}
  \]

#### Parameters
- `seq`: DNA sequence (string)

#### Returns
- Melting temperature in °C (float)

---

### 2. `CG_content(seq)`
Calculates the percentage of GC bases in a DNA sequence.

#### Formula
\[
GC\% = \frac{G + C}{A + T + G + C} \times 100
\]

#### Parameters
- `seq`: DNA sequence (string)

#### Returns
- GC content as a percentage (float)

---

## ⚙️ Script Workflow

1. The user is prompted to enter a DNA sequence.  
2. The sequence is converted to uppercase.  
3. The program calculates and prints:
   - The **melting temperature (Tm)**
   - The **GC content (%)**
4. The program gives feedback:
   - If `Tm > 65°C`: The primer may form **secondary structures**.  
   - If `52°C < Tm < 58°C`: The Tm is **optimal**.  
   - If `40% < GC% < 60%`: The GC content is **optimal**.

## 🧠 Notes

Works for DNA sequences only (A, T, G, C).

Ensure that the input sequence does not contain invalid characters or spaces.
