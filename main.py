import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import requests
import io
import os

def load_csv():
    """Load CSV file from local upload, user-provided URL, or hardcoded URL."""
    print("Choose CSV loading method:")
    print("1. Upload local CSV file")
    print("2. Enter CSV URL")
    print("3. Use default URL (hardcoded)")
    choice = input("Enter choice (1-3): ")

    if choice == '1':
        file_path = input("Enter the path to your local CSV file: ")
        if os.path.exists(file_path):
            return pd.read_csv(file_path)
        else:
            print("File not found. Exiting.")
            exit()
    elif choice == '2':
        url = input("Enter the CSV URL: ")
        try:
            response = requests.get(url)
            response.raise_for_status()
            return pd.read_csv(io.StringIO(response.text))
        except Exception as e:
            print(f"Error loading URL: {e}. Exiting.")
            exit()
    elif choice == '3':
        # Hardcoded URL (example: Iris dataset)
        url = "https://raw.githubusercontent.com/mwaskom/seaborn-data/master/iris.csv"
        try:
            response = requests.get(url)
            response.raise_for_status()
            return pd.read_csv(io.StringIO(response.text))
        except Exception as e:
            print(f"Error loading default URL: {e}. Exiting.")
            exit()
    else:
        print("Invalid choice. Exiting.")
        exit()

def display_data(df):
    """Print column headings and first two rows."""
    print("\nColumn Headings:")
    print(df.columns.tolist())
    print("\nFirst Two Rows:")
    print(df.head(2))

def get_columns(df):
    """Return column names as a list."""
    return df.columns.tolist()

def select_columns(columns):
    """Prompt user to select one or two columns for plotting."""
    print("\nAvailable columns:", columns)
    x_col = input("Enter the column name for X-axis: ")
    if x_col not in columns:
        print("Invalid column name. Exiting.")
        exit()
    
    plot_type = input("Do you want a second column for Y-axis? (y/n): ").lower()
    if plot_type == 'y':
        y_col = input("Enter the column name for Y-axis: ")
        if y_col not in columns:
            print("Invalid column name. Exiting.")
            exit()
        return x_col, y_col
    return x_col, None

def convert_to_numpy(df, x_col, y_col=None):
    """Convert selected columns to NumPy arrays."""
    x_data = df[x_col].to_numpy()
    if y_col:
        y_data = df[y_col].to_numpy()
        return x_data, y_data
    return x_data, None

def plot_data(x_data, y_data, x_col, y_col=None):
    """Create a scatter or line plot based on user input."""
    plt.figure(figsize=(10, 6))
    if y_data is not None:
        plot_type = input("Enter plot type (scatter/line): ").lower()
        if plot_type == 'scatter':
            plt.scatter(x_data, y_data)
        elif plot_type == 'line':
            plt.plot(x_data, y_data)
        else:
            print("Invalid plot type. Defaulting to scatter.")
            plt.scatter(x_data, y_data)
        plt.xlabel(x_col)
        plt.ylabel(y_col)
        plt.title(f"{y_col} vs {x_col}")
    else:
        plt.plot(x_data)
        plt.xlabel("Index")
        plt.ylabel(x_col)
        plt.title(f"{x_col} vs Index")
    
    plt.grid(True)
    plt.show()

def interpret_graph(x_col, y_col=None):
    """Provide basic interpretation of the graph."""
    if y_col:
        print(f"\nInterpretation: This graph shows the relationship between {x_col} and {y_col}.")
        print(f"- X-axis ({x_col}): Represents the independent variable.")
        print(f"- Y-axis ({y_col}): Represents the dependent variable.")
        print("Look for patterns such as positive/negative trends, clusters, or outliers.")
    else:
        print(f"\nInterpretation: This graph shows {x_col} plotted against its index.")
        print(f"- X-axis: Represents the row index of the data.")
        print(f"- Y-axis ({x_col}): Shows the variation of {x_col} across the dataset.")
        print("Look for trends or fluctuations in the data over the sequence.")

def main():
    # Load CSV and create DataFrame
    df = load_csv()
    
    # Display headings and first two rows
    display_data(df)
    
    # Store column names
    columns = get_columns(df)
    
    while True:
        # Select columns for plotting
        x_col, y_col = select_columns(columns)
        
        # Convert to NumPy arrays
        x_data, y_data = convert_to_numpy(df, x_col, y_col)
        
        # Plot the data
        plot_data(x_data, y_data, x_col, y_col)
        
        # Provide interpretation
        interpret_graph(x_col, y_col)
        
        # Ask if user wants to plot another combination
        again = input("\nDo you want to plot another column combination? (y/n): ").lower()
        if again != 'y':
            break

if __name__ == "__main__":
    main()