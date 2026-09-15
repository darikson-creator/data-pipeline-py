#%%
# Loading the libraries 
import os
import pandas as pd
from thefuzz import fuzz, process


# Define the working directory
directorio = r"C:\Users\Darikson\Desktop\DEVELOPMENT (Data Engineer)\PYTHON\Project (IPS Datax)"
os.chdir(directorio) 

# Verify the directory
print("Directorio actual:", os.getcwd())

# Load the Data
df_ventas = pd.read_csv("Ventas.csv")
df_vendedores = pd.read_csv("Vendedores.csv")

# Convert company names to lowercase to avoid formatting issues.
df_ventas["empresa"] = df_ventas["empresa"].str.lower().str.strip()
df_vendedores["empresa"] = df_vendedores["empresa"].str.lower().str.strip()

# Create a function to find the best match.
# Provide a name, and it searches the list of names for the most similar one.
def encontrar_mejor_match(nombre, lista_empresas):
    mejor_match, score = process.extractOne(nombre, lista_empresas, scorer=fuzz.token_sort_ratio)
    # Returns the best match (best name from the list of names) and the score obtained.
    return mejor_match if score > 30 else None

# Create a new column named "empresa_corregida"
# 'apply' It applies the function to each row of the specified column. It evaluates row by row.
# x represents the company name in df_ventas["empresa"]
# x it takes on the value of each row within the df_ventas["empresa"] column
df_ventas["empresa_corregida"] = df_ventas["empresa"].apply(lambda x: encontrar_mejor_match(x, df_vendedores["empresa"].tolist()))

# Review the state of the data after creating the corrected column.
df_ventas.head()

# Merge the DataFrames using the new corrected column.
# 'Merge' in pandas is = to JOIN in SQL

df_final = df_ventas.merge(df_vendedores, left_on="empresa_corregida", right_on="empresa", how="left").drop(columns=["empresa_y"])

# Review the data after the merge.
df_final.head()
# There are several cases that do not cross the threshold; the threshold is lowered.
# Se ejecuta el codigo de nuevo, pero con un umbral menor
# The code is executed again, but with a lower threshold

# Rename the columns to review our progress so far.
df_final.rename(columns={"empresa_x": "empresa_original", "empresa_corregida": "empresa_correcta"}, inplace=True)

# Filter non-matching records
df_sin_match = df_final[df_final["empresa_correcta"].isna()]

# Save the results to a CSV file in the original folder.
df_final.to_csv("resultados_cruce.csv", index=False)
df_sin_match.to_csv("resultados_sin_cruce.csv", index=False)





"""
Parte 2) Data Reporting y Data Visualization

- Install the libraries (fpdf Mostly)
    - pip install fpdf 
"""

import matplotlib.pyplot as plt
from fpdf import FPDF
import pandas as pd
from datetime import datetime

# 1. Calculate the sales amount by company
ventas_por_empresa = df_final.groupby("empresa_correcta")["monto"].sum().reset_index()
ventas_por_empresa = ventas_por_empresa.dropna().sort_values(by="monto", ascending=False)

# 2. Calculate the sales amount by salesperson.
ventas_por_vendedor = df_final.groupby("vendedor")["monto"].sum().reset_index()
ventas_por_vendedor = ventas_por_vendedor.dropna().sort_values(by="monto", ascending=False)

# 3. Create PNG graphs and save (Sales amount by company)
plt.figure(figsize=(10, 5))
plt.barh(ventas_por_empresa["empresa_correcta"], ventas_por_empresa["monto"], color='skyblue')
plt.xlabel("Monto Vendido")
plt.ylabel("Empresa")
plt.title("Monto Vendido por Empresa")
plt.gca().invert_yaxis() # Reverse the order of the graph's values.
plt.savefig("ventas_por_empresa.png", bbox_inches='tight')  # Save image and remove whitespace
plt.close()

# (Sales amount by salesperson)
plt.figure(figsize=(10, 5))
plt.barh(ventas_por_vendedor["vendedor"], ventas_por_vendedor["monto"], color='orange')
plt.xlabel("Monto Vendido")
plt.ylabel("Vendedor")
plt.title("Monto Vendido por Vendedor")
plt.gca().invert_yaxis() 
plt.savefig("ventas_por_vendedor.png", bbox_inches='tight')
plt.close()






# 4. Create PDF
pdf = FPDF()
pdf.set_auto_page_break(auto=True, margin=15) #Add new pages if necessary, with a margin of 15.
pdf.add_page() #Add a new PDF page

# 5. Add a title to the PDF
pdf.set_font("Helvetica", style="B", size=16)
fecha_hora_actual = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
titulo = f"Reporte de Ventas - {fecha_hora_actual}"

pdf.cell(200, 10, titulo, ln=True, align="C") # Create a cell with the text
# Width, height, text, line break, centering
pdf.ln(10) # Add a blank space of 10

# 6. Add 'ventas por empresa' table
# Add a title to the table                                                           
pdf.set_font("Arial", size=12)
pdf.cell(200, 10, "Monto Vendido por Empresa", ln=True, align="C")
pdf.ln(5)
# Add values ​​cell by cell
for index, row in ventas_por_empresa.iterrows(): # .iterrows() Indicates that it will be traversed row by row.
    pdf.cell(100, 10, row["empresa_correcta"], border=1) # It creates a cell and does not insert a line break.
    # border=1 indicates that a border is added to the cell
    pdf.cell(50, 10, f"${row['monto']:.2f}", border=1, ln=True) # Creates a cell and inserts a line break.
pdf.ln(10)

# 7. Add 'ventas por vendedor' table
pdf.cell(200, 10, "Monto Vendido por Vendedor", ln=True, align="C")
pdf.ln(5)
for index, row in ventas_por_vendedor.iterrows():
    pdf.cell(100, 10, row["vendedor"], border=1)
    pdf.cell(50, 10, f"${row['monto']:.2f}", border=1, ln=True)
pdf.ln(10)

# 8. Insert graphics into the PDF
pdf.cell(200, 10, "Grafico: Monto Vendido por Empresa", ln=True, align="C")
pdf.image("ventas_por_empresa.png", x=10, w=180)
pdf.ln(10)
pdf.cell(200, 10, "Grafico: Monto Vendido por Vendedor", ln=True, align="C")
pdf.image("ventas_por_vendedor.png", x=10, w=180)
pdf.ln(10)

# 9. Save PDF
pdf.output("reporte_ventas.pdf")
print("✅ PDF successfully generated: reporte_ventas.pdf")



"""

- useful for an automation process


"""



# %%
