# DNA to RNA Converter

A Python tool for validating DNA sequences and converting them into RNA.

This program takes a DNA sequence as input, checks whether it contains valid DNA bases (`A`, `T`, `G`, `C`), and replaces thymine (`T`) with uracil (`U`) to generate the corresponding RNA sequence.

## Features

* Converts DNA sequences to uppercase.
* Checks for valid DNA bases (`A`, `T`, `G`, `C`).
* Handles empty input and invalid DNA sequences.
* Converts DNA to RNA by replacing `T` with `U`.
* Displays the resulting RNA sequence.

## Example

**Input:**

```text
ATGCTT
```

**Output:**

```text
Valid DNA sequence
RNA: AUGCUU
```
## How to Run

1. Make sure Python is installed.
2. Clone or download this repository.
3. Open a terminal in the project folder and run:

```bash
python dna_to_rna.py
```


