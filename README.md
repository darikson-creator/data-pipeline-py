# Python Data Engine: Automated Cleaning & Executive PDF Reporting

## Description
An automated end-to-end Python pipeline developed in VS Code to reconcile sales datasets, perform advanced text normalization using Fuzzy Logic, and dynamically compile executive visual reports in PDF format.

## Key Features
* **Dataset Reconciliation:** Automated merge and cross-referencing of master sales and rep data using `pandas`.
* **Fuzzy String Matching:** Row-by-row data cleaning pipeline implementing `thefuzz` (Token Sort Ratio) to resolve typos, inverted text, and naming inconsistencies.
* **Data Visualization:** Automated generation and export of custom high-resolution charts (`matplotlib`).
* **PDF Compilation:** Dynamic generation of executive reports (`FPDF`) featuring summary tables, metadata timestamps, and embedded visualizations.

## Tech Stack
* **Language:** Python 3.x
* **Data Processing:** Pandas, NumPy
* **Text Matching:** TheFuzz (FuzzyWuzzy), Levenshtein
* **Visualization & Reporting:** Matplotlib, FPDF
* **IDE:** Visual Studio Code
