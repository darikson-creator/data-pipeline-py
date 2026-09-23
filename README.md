# Python Data Engine: Automated Cleaning & Executive PDF Reporting

## Description
An automated end-to-end Python pipeline developed in VS Code to reconcile sales datasets, perform advanced text normalization using Fuzzy Logic, and dynamically compile executive visual reports in PDF format.

## Key Features
* **Dataset Reconciliation:** Automated merge and cross-referencing of master sales and rep data using `pandas`.
* **Fuzzy String Matching:** Row-by-row data cleaning pipeline implementing `thefuzz` (Token Sort Ratio) to resolve typos, inverted text, and naming inconsistencies.
* **Data Visualization:** Automated generation and export of custom high-resolution charts (`matplotlib`).
* **PDF Compilation:** Dynamic generation of executive reports (`FPDF`) featuring summary tables, metadata timestamps, and embedded visualizations.

## Tech Stack
* **Language:** Python
* **Data Processing:** Pandas, NumPy
* **Text Matching:** TheFuzz (FuzzyWuzzy), Levenshtein
* **Visualization & Reporting:** Matplotlib, FPDF
* **IDE:** Visual Studio Code

---

## 🛠️ Workflow (Images)

### Merge Tables (.py code)
 ![image alt](https://github.com/darikson-creator/data-pipeline-py/blob/088547c4aa9ac3b34df64121e8f4d586b2613b4e/1.%20Merge%20Tables.png)
 
### Fixed Mistakes
 ![image alt](https://github.com/darikson-creator/data-pipeline-py/blob/088547c4aa9ac3b34df64121e8f4d586b2613b4e/2.%20Fixed%20Mistakes.png)
 
### Create PNG Image (.py code)
 ![image alt](https://github.com/darikson-creator/data-pipeline-py/blob/088547c4aa9ac3b34df64121e8f4d586b2613b4e/3.%20Create%20PNG%20image.png)
 
### PNG Image Result
 ![image alt](https://github.com/darikson-creator/data-pipeline-py/blob/088547c4aa9ac3b34df64121e8f4d586b2613b4e/3.1.%20Venta_por_empresa.png)
 
### Create PDF File (.py code)
![image alt](https://github.com/darikson-creator/data-pipeline-py/blob/088547c4aa9ac3b34df64121e8f4d586b2613b4e/4.%20Create%20PDF%20file.png)

### PDF File Result
![image alt](https://github.com/darikson-creator/data-pipeline-py/blob/088547c4aa9ac3b34df64121e8f4d586b2613b4e/5.%20PDF%20Report.png)
