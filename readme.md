# 📊 CSV Plotter — Interactive CSV Data Visualizer

A command-line Python tool for **loading**, **exploring**, and **visualizing** CSV datasets with ease. Designed to support fast experimentation, lightweight data inspection, and quick visual interpretations — all in a single script.

---

## 🚀 Features          

- 🔄 Load CSVs from:
  - 📂 Local file paths
  - 🌐 Online URLs
  - 🧠 A default hardcoded dataset (Iris)

- 📌 Column-wise visualization:
  - Select 1 or 2 columns
  - Choose plot type: `scatter` or `line`
  - Supports single-series plots against index

- 📉 Auto-interprets plotted graphs:
  - Understand axis roles (independent/dependent)
  - Highlights what trends or patterns to look for

- 🔁 Repeatable plotting:
  - Explore multiple column combinations without restarting the script

---

## 🛠️ Dependencies

- Python 3.7+
- `pandas`
- `numpy`
- `matplotlib`
- `requests`

Install them with:

```bash
pip install pandas numpy matplotlib requests

---

##🧠 How to Use
▶️ Run the Script
bash
Copy
Edit
python main.py

---

## 📊 Example Output
Visualizing Sepal Length vs Petal Width (Iris dataset):
Column Headings:
['sepal_length', 'sepal_width', 'petal_length', 'petal_width', 'species']

First Two Rows:
   sepal_length  sepal_width  petal_length  petal_width species
0           5.1          3.5           1.4          0.2  setosa
1           4.9          3.0           1.4          0.2  setosa

Available columns: ['sepal_length', 'sepal_width', 'petal_length', 'petal_width', 'species']
Enter the column name for X-axis:
<sub>Sample visualization using default dataset</sub>

---

## ✅ Example Use Cases
-Exploratory Data Analysis (EDA)
-Teaching data science concepts
-Quick visual insights on unfamiliar CSVs
-Lightweight CLI-based graph generation

---

## 📌 Future Enhancements (PRs welcome!)
-Add CSV export of filtered/processed data
-Advanced plotting: histograms, box plots
-GUI version with Tkinter or Streamlit
-Data type inference and automatic plot suggestions
