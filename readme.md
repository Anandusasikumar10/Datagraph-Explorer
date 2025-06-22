DataGraph Explorer

Overview

DataGraph Explorer is a Python application that allows users to load, visualize, and interpret data from CSV files. It supports loading CSVs from local files, user-provided URLs, or a default dataset (Iris dataset). Users can select columns to create scatter or line plots and receive basic interpretations of the visualized data.

Features





Flexible CSV Loading: Load CSV files from a local path, a user-specified URL, or a default URL (Iris dataset).



Data Display: View column headings and the first two rows of the dataset.



Customizable Plots: Select one or two columns to create scatter or line plots using Matplotlib.



Data Interpretation: Receive simple insights about the plotted data, including trends and patterns.



Interactive Workflow: Loop to plot multiple column combinations without restarting.

Requirements





Python 3.x



Required libraries:





pandas



numpy



matplotlib



requests

Installation





Clone the repository:

git clone https://github.com/Anandusasikumar10/Datagraph-Explorer.git
cd Datagraph-Explorer



Install dependencies:

pip install pandas numpy matplotlib requests

Usage





Run the script:

python datagraph_explorer.py



Choose a CSV loading method:





Option 1: Upload a local CSV file by providing its file path.



Option 2: Enter a URL to a CSV file hosted online.



Option 3: Use the default Iris dataset.



Follow the prompts to:





View column headings and the first two rows.



Select columns for the X-axis and optionally the Y-axis.



Choose a plot type (scatter or line) if plotting two columns.



Review the graph and its interpretation.



Decide whether to plot another combination or exit.

Example

Choose CSV loading method:
1. Upload local CSV file
2. Enter CSV URL
3. Use default URL (hardcoded)
Enter choice (1-3): 3

Column Headings:
['sepal_length', 'sepal_width', 'petal_length', 'petal_width', 'species']

First Two Rows:
   sepal_length  sepal_width  petal_length  petal_width species
0          5.1          3.5           1.4          0.2  setosa
1          4.9          3.0           1.4          0.2  setosa

Available columns: ['sepal_length', 'sepal_width', 'petal_length', 'petal_width', 'species']
Enter the column name for X-axis: sepal_length
Do you want a second column for Y-axis? (y/n): y
Enter the column name for Y-axis: petal_length
Enter plot type (scatter/line): scatter

Interpretation: This graph shows the relationship between sepal_length and petal_length.
- X-axis (sepal_length): Represents the independent variable.
- Y-axis (petal_length): Represents the dependent variable.
Look for patterns such as positive/negative trends, clusters, or outliers.

File Structure





datagraph_explorer.py: Main Python script for loading, visualizing, and interpreting CSV data.



README.md: This file, providing project details and instructions.

Notes





Ensure the CSV file has valid formatting when using local or URL-based loading.



The default dataset is the Iris dataset, accessible via a public URL.



Invalid inputs (e.g., non-existent columns or files) will prompt an error and exit the program.



Plots are displayed using Matplotlib's interactive viewer.

Contributing

Contributions are welcome! Please fork the repository, create a new branch, and submit a pull request with your changes.


Contact

For issues or questions, please open an issue on GitHub or contact Anandusasikumar10.